# ☁️ Cloud Data Processing — Portafolio de Tareas

> **Materia:** Procesamiento de Datos en la Nube  
> **Repositorio:** [clouddataprocessing](https://github.com/DavidJauregu123/clouddataprocessing)

---

## 📓 Bitácoras de Clase

---

### 📅 Clase 1 — 01/06/2026

#### Temas Vistos

**Introducción al curso**  
El profesor presentó la materia y sus objetivos generales. También hubo un momento de reconocimiento entre quienes ya habían cursado materias previas con él.

---

**Infraestructura como Código (IaC)**  
En lugar de configurar servidores y recursos manualmente, IaC permite hacerlo a través de archivos de texto o scripts. Esto hace el proceso más reproducible, automatizable y fácil de mantener.

| Herramienta | Descripción |
|---|---|
| **Terraform** | Una de las opciones más populares; funciona con casi cualquier proveedor de nube. |
| **Pulumi** | Interesante porque te deja escribir la infraestructura en lenguajes que ya conoces, como Python o JavaScript. |
| **CloudFormation** | La opción nativa de AWS; ideal si vas a trabajar exclusivamente dentro de ese ecosistema. |

---

**Servicios en la nube y máquinas virtuales**  
- **Servicio en la nube:** en lugar de tener el hardware físico, accedes a recursos de cómputo por internet cuando los necesitas.  
- **Máquina virtual:** es básicamente una computadora simulada dentro de otra; corre su propio sistema operativo y sus propias apps sin interferir con el resto.

---

**Cloud Agnostic**  
Se refiere a diseñar software de forma que no dependa de un solo proveedor de nube. Si en algún momento quieres cambiar de AWS a Azure, por ejemplo, el sistema debería poder adaptarse sin reescribirse desde cero.

---

**CI/CD y DevOps**  
Se vio cómo la integración y entrega continua (CI/CD) busca automatizar todo el ciclo: desde que un desarrollador sube código hasta que ese código llega a producción, pasando por pruebas automáticas y validaciones.

**Branching Strategy**  
Tener una estrategia de ramas bien definida es clave para que varios desarrolladores puedan trabajar en paralelo sin pisarse unos a otros.

**Herramientas de automatización y despliegue:**

| Herramienta | Descripción |
|---|---|
| **FluxCD** | Se usa en entornos Kubernetes para que los despliegues se disparen automáticamente cuando hay cambios en el repositorio. |
| **GitHub Actions** | Permite crear flujos de trabajo directamente en GitHub, sin necesidad de herramientas externas. |
| **Jenkins** | Una solución clásica y muy extendida para pipelines de CI/CD en todo tipo de proyectos. |

#### ✅ Conclusiones

La clase sentó las bases del curso: computación en la nube, infraestructura como código y cultura DevOps. Lo más valioso fue ver cómo estas herramientas no son independientes, sino que se complementan para automatizar y escalar el desarrollo de software.

---

### 📅 Clase 2 — 02/06/2026

#### Temas Vistos

**Sistemas de Control de Versiones (VCS)**  
Un VCS lleva un registro histórico de todos los cambios en un proyecto, permitiendo volver a versiones anteriores y trabajar en equipo sin conflictos.

**Comandos básicos de Git:**

```bash
git init       # Inicializar repositorio
git status     # Ver estado del repositorio
git add        # Agregar cambios al staging
git commit     # Confirmar cambios
git push       # Enviar cambios al remoto
git pull       # Obtener y fusionar cambios del remoto
git fetch      # Obtener cambios sin fusionar
git clone      # Clonar repositorio remoto
```

---

**Plataformas de alojamiento de repositorios**

Las más usadas para guardar y compartir repositorios Git:

- **GitHub** — la más popular a nivel mundial
- **GitLab** — fuerte en entornos empresariales con CI/CD integrado
- **Gitea** — opción ligera y autoalojable

---

**Estrategias de ramas (Branching Strategy)**

Organizar el trabajo en ramas especializadas evita mezclar código en desarrollo con el que ya está en producción.

| Rama | Propósito |
|---|---|
| `main` | Código estable listo para producción |
| `develop` | Punto de integración de las nuevas funciones antes de liberar |
| `feature` | Desarrollo aislado de una funcionalidad nueva |
| `release` | Preparativos finales antes de lanzar una versión |
| `hotfix` | Parches urgentes directamente sobre producción |

---

**DevOps y CI/CD**

Aplicar CI/CD en el flujo de trabajo trae varias ventajas concretas:

- Los despliegues se vuelven predecibles y automáticos
- Se detectan errores mucho antes, cuando son más fáciles de corregir
- El tiempo entre que se termina una función y que llega al usuario se acorta considerablemente
- Los equipos de desarrollo y operaciones trabajan con más sincronía

---

**Git Flow — Flujo básico**

1. Crear una rama para la tarea:

```bash
git branch 998
git checkout 998
```

2. Realizar cambios y agregarlos al repositorio:

```bash
git add .
git commit -m "Added evidence for 998"
```

3. Integrar cambios a la rama principal:

```bash
git checkout main
git merge 998
git push
```

#### ✅ Conclusiones

Git es la base del trabajo colaborativo moderno en software. Conocer sus comandos esenciales, combinado con una buena estrategia de ramas y un pipeline de CI/CD, permite que equipos completos desarrollen en paralelo con orden y confianza.

---

### 📅 Clase 3 — 03/06/2026

#### Temas Vistos

**¿Qué es la informática en la nube?**

> En esencia, la nube te da acceso a recursos de cómputo —servidores, bases de datos, almacenamiento— a través de internet, y solo pagas por lo que realmente usas, sin necesidad de comprar ni mantener hardware propio.

---

**Infraestructura Informática Tradicional**

El modelo clásico tiene limitaciones importantes que la nube viene a resolver:

- Comprar y mantener servidores físicos requiere inversión inicial alta, espacio y personal dedicado
- Adquirir nuevo hardware puede tomar semanas o meses
- La capacidad hay que planificarla con anticipación, lo que lleva a tener recursos ociosos o insuficientes según la demanda

---

**Modelos de Servicio en la Nube**

Dependiendo de cuánto quieras gestionar tú mismo, existen tres niveles:

| Modelo | Nombre completo | ¿Qué te da? |
|---|---|---|
| **IaaS** | Infraestructura como Servicio | Acceso a servidores virtuales y redes; tú instalas y configuras todo encima |
| **PaaS** | Plataforma como Servicio | Un entorno ya listo para desplegar tu app sin preocuparte por el sistema operativo |
| **SaaS** | Software como Servicio | Una aplicación completa lista para usar desde el navegador |

---

**Tipos de Nube**

- ☁️ **Pública** — La gestiona un proveedor externo (AWS, Azure, GCP) y la comparten muchos clientes
- 🔒 **Privada** — Infraestructura dedicada exclusivamente a una organización, con mayor control
- 🤝 **Comunitaria** — Varias organizaciones con necesidades similares comparten la misma infraestructura
- 🔀 **Híbrida** — Mezcla lo mejor de la nube pública y privada según las necesidades de cada carga de trabajo

---

**Economías de Escala Masiva**  
Al operar a escala global, los grandes proveedores de nube reducen sus costos por unidad y parte de ese ahorro se traslada a los clientes. Es una de las razones por las que usar la nube suele ser más barato que montar infraestructura propia.

---

## 📝 Tareas

---

### Tarea #999 — NightPass: Plataforma de Eventos Nocturnos en Cancún

> Aplicación web y móvil para descubrir, reservar y acceder a fiestas caseras y antros en Cancún, con venta de boletos digitales y control de acceso por QR.

#### Descripción del Proyecto

**NightPass** es una plataforma digital diseñada para conectar a los asistentes con los mejores eventos nocturnos de Cancún: desde fiestas privadas en casas hasta los antros más reconocidos de la zona hotelera. La app permite comprar entradas con antelación, reservar mesas VIP y acceder al evento mediante un código QR único, eliminando filas y facilitando el control de aforo para los organizadores.

El proyecto nace de la necesidad de digitalizar la experiencia nocturna en una de las ciudades turísticas más importantes de México.

#### Objetivo

Desarrollar una aplicación de **3 capas** desplegada en **AWS** que permita:

- 🔍 **Descubrir** eventos nocturnos cercanos en tiempo real
- 🎟️ **Comprar** boletos de forma segura (tarjeta, OXXO, transferencia)
- 🥂 **Reservar** mesas VIP con servicio de botella
- 📱 **Acceder** al evento mediante QR digital validado en puerta
- 📊 **Gestionar** aforo, ingresos y asistentes desde panel de administración

#### Diagrama de Arquitectura

![Diagrama de arquitectura NightPass](https://github.com/DavidJauregu123/clouddataprocessing/blob/f694026af54fc7ba25f73866f418f8510a5af955/Diagrama%20de%20arquitectura.png)

---

### Tarea #997 — Pizza as a Service 2.0

> Investigación sobre Pizza as a Service 2.0 y los diferentes modelos de servicio en la nube.

🔗 [Ver presentación](https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/)

---

### Tarea #996 — Solución Estratificada de Problemas en TIC

> Investigación sobre la solución estratificada de problemas en Tecnologías de la Información y Comunicación.

🔗 [Ver presentación](https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/)
