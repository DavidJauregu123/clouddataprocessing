from flask import Flask, request, jsonify, render_template
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

WORKER_COUNT = 4

def fetch_words(url):
    r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    text = soup.get_text()
    return re.findall(r'\b[a-záéíóúña-záéíóúñ]{4,}\b', text.lower())

def mapreduce(words):
    # Dividir palabras en chunks por worker
    size = max(1, len(words) // WORKER_COUNT)
    chunks = [words[i:i+size] for i in range(0, len(words), size)]

    # MAP: cada worker etiqueta sus palabras
    map_results = []
    for i, chunk in enumerate(chunks[:WORKER_COUNT]):
        pairs = [(w, 1) for w in chunk]
        map_results.append({"worker": i + 1, "pairs": pairs, "total": len(pairs)})

    # SHUFFLE: agrupar por palabra
    shuffled = defaultdict(list)
    for result in map_results:
        for word, count in result["pairs"]:
            shuffled[word].append(count)

    # REDUCE: sumar
    reduced = {k: sum(v) for k, v in shuffled.items()}
    top20 = dict(sorted(reduced.items(), key=lambda x: -x[1])[:20])

    # Muestra solo muestra del shuffle para no saturar la UI
    shuffle_sample = {k: v for k, v in list(shuffled.items())[:8] if k in top20}

    return {
        "word_count": len(words),
        "unique_words": len(shuffled),
        "map": [{"worker": r["worker"], "total": r["total"], "sample": r["pairs"][:6]} for r in map_results],
        "shuffle": shuffle_sample,
        "reduce": top20,
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.json.get("url", "").strip()
    if not url.startswith("http"):
        return jsonify({"error": "URL inválida"}), 400
    try:
        words = fetch_words(url)
        if not words:
            return jsonify({"error": "No se encontró texto en la página"}), 400
        return jsonify(mapreduce(words))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
