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

#### ✅ Conclusiones

La nube elimina las limitaciones del hardware físico: pagas solo lo que usas y eliges el modelo de servicio (IaaS, PaaS o SaaS) según cuánto quieres gestionar tú mismo.

---

### 📅 Clase 4 — 04/06/2026

#### Temas Vistos

**3 Formas de interactuar con AWS**

1. **Consola de administración de AWS**
2. **Interfaz de línea de comandos (AWS CLI)**
3. **Kits de desarrollo de software (SDK)**

---

**Infraestructura Global de AWS**

Se diseñó y creó para ofrecer un entorno de cómputo en la nube **fiable, confiable, escalable y seguro**, con un rendimiento de red global de alta calidad.

**Regiones de AWS**

- Una región de AWS es una **zona geográfica**.
- La comunicación entre regiones utiliza la **infraestructura de red troncal de AWS**.
- Cada región proporciona a la red **niveles planos**.

**Centros de Datos de AWS**

- Cada centro de datos suele tener más de **50,000 a 80,000 servidores físicos**.

**Funciones de la Infraestructura de AWS**

| Función | Descripción |
|---|---|
| ⚡ Elasticidad y escalabilidad | Se adapta para crecer según la demanda |
| 🛡️ Tolerancia a errores | Continúa funcionando en presencia de un error |
| ✅ Alta disponibilidad | Minimiza el tiempo de inactividad sin intervención humana |

#### ✅ Conclusiones

AWS estructura su infraestructura global en regiones y centros de datos para garantizar escalabilidad, tolerancia a errores y alta disponibilidad. Interactuar con ella —ya sea por consola, CLI o SDK— da acceso a esa potencia sin gestionar hardware físico.

---

### 📅 Clase 5 — 08/06/2026

#### Temas Vistos

#### 🐳 Docker

**Conceptos Clave**

- **Efímero** — Los contenedores son temporales por naturaleza.
- **Contenedores** — Unidades de software aisladas que empaquetan código y dependencias.
- **Dockerfile** — Archivo de configuración para construir imágenes Docker.
- **docker-compose.yml** — Archivo para definir y orquestar múltiples contenedores.

---

**Imágenes Base Comunes**

- `alpine Linux` — Imagen minimalista y ligera.
- `debian python` — Imagen Debian con Python incluido.

---

**Estructura de un Dockerfile (ejemplo: servidor MariaDB)**

```dockerfile
FROM imagen_base
RUN apt install mariadb-server
CMD ./mysql_start
```

---

**Script de ejemplo: Hola Mundo**

```bash
#!/bin/bash
echo "Hola mundo"
```

> Editado con: `vi hola.sh`

---

**Comandos Docker Esenciales**

```bash
docker build . -t hola     # Construir imagen con tag
docker images              # Listar imágenes disponibles
docker run hola            # Ejecutar un contenedor
docker ps                  # Ver contenedores en ejecución
```

---

**Docker Compose — Estructura básica**

```yaml
services:
  container:
    image:
    name: front
    network:
    volumes:
  container:
    name: back
  container:
    name: bd
```

---

**Ecosistema y Herramientas Relacionadas**

| Herramienta | Descripción |
|---|---|
| **Docker Hub** | Registro público de imágenes |
| **Docker Playground** | Entorno online para practicar |
| **awesome-docker** | Colección de recursos Docker |
| **Kubernetes** | Orquestación de contenedores a escala |
| **Vagrant** | Gestión de entornos de desarrollo virtuales |
| **VirtualBox** | Virtualizador para correr boxes/VMs |
| **asciinema** | Grabación de sesiones de terminal |

---

**Patrón: Rebuild continuo**

```python
while True:
    docker build . -t hola
```

> Útil para desarrollo con reconstrucción automática de la imagen.

#### ✅ Conclusiones

Docker simplifica el despliegue al empaquetar código y dependencias en contenedores portables y efímeros. Un Dockerfile genera una imagen; esa imagen genera un contenedor. Docker Compose coordina múltiples contenedores con un solo archivo.

---

### 📅 Clase 6 — 09/06/2026


---

### 📅 Clase 7 — 10/06/2026

#### Temas Vistos

**Contenedores**

Los contenedores son entornos ligeros y aislados que permiten ejecutar aplicaciones junto con todas sus dependencias. Son más rápidos y consumen menos recursos que una máquina virtual.

**Efímero**

Un contenedor es considerado efímero porque puede crearse, ejecutarse y eliminarse fácilmente. Si no se utilizan volúmenes, los datos almacenados dentro del contenedor se pierden al eliminarlo.

---

**Dockerfile**

Archivo de texto que contiene las instrucciones para construir una imagen Docker.

Ejemplo básico:

```dockerfile
FROM ubuntu
RUN apt install -y apache2
CMD ["apache2ctl", "-D", "FOREGROUND"]
```

Instrucciones principales:

- **FROM**: Define la imagen base.
- **RUN**: Ejecuta comandos durante la construcción de la imagen.
- **CMD**: Define el comando que se ejecutará al iniciar el contenedor.

---

**Imágenes**

Plantillas de solo lectura con todo lo necesario para ejecutar una aplicación. Ejemplos de imágenes base: Alpine Linux, Debian, Python.

**Docker Hub**

Repositorio en línea donde se almacenan y comparten imágenes Docker públicas y privadas.

---

**docker-compose.yml**

Archivo YAML para definir y ejecutar múltiples contenedores y servicios con una sola configuración.

Elementos comunes de un servicio:

- **container_name**: Nombre del contenedor.
- **image**: Imagen utilizada.
- **networks**: Redes a las que pertenece.
- **volumes**: Volúmenes para persistencia de datos.

---

**Script Bash (hola.sh)**

```bash
#!/bin/bash
echo "Hola mundo"
```

**Comandos básicos de Docker**

```bash
docker build -t hola .    # Construir imagen
docker images             # Ver imágenes disponibles
docker run hola           # Ejecutar contenedor
docker ps                 # Ver contenedores en ejecución
```

---

**Herramientas relacionadas**

| Herramienta | Descripción |
|---|---|
| **Docker Playground** | Entorno online para practicar Docker |
| **Kubernetes** | Orquestación de contenedores a escala |
| **VirtualBox** | Virtualización de máquinas |
| **Vagrant** | Gestión de entornos de desarrollo virtualizados |

---

**Volúmenes y Redes**

- **Volúmenes:** almacenan datos fuera del contenedor para que persistan al eliminarlo.
- **Redes (Networks):** permiten la comunicación entre contenedores dentro del mismo entorno.

---

**Relación entre Dockerfile, Imagen y Contenedor**

```text
Dockerfile → Imagen → Contenedor
```

- El Dockerfile genera una imagen.
- La imagen es la plantilla.
- El contenedor es la instancia en ejecución.

#### ✅ Conclusiones

Docker profundiza en el ecosistema de contenedores: el Dockerfile construye la imagen, docker-compose orquesta múltiples servicios, y los volúmenes y redes resuelven persistencia y comunicación. Kubernetes extiende esto a escala de producción.

---

### 📅 Clase 8 — 11/06/2026

#### Temas Vistos

---

### 📅 Clase 9 — 15/06/2026

#### Temas Vistos

**Actividad #995 — Desarrollar un proyecto pequeño**

- El día de hoy subí el primer avance del proyecto.

---

### 📅 Clase 10 — 16/06/2026

#### Temas Vistos

En esta clase abordamos los fundamentos de redes en la nube mediante Amazon Virtual Private Cloud (AWS VPC), centrándonos en su configuración, el direccionamiento IP, la segmentación mediante subredes y las mejores prácticas para evitar el agotamiento de direcciones en entornos empresariales.

---

#### Amazon Virtual Private Cloud (VPC)

Es el entorno de red virtual aislado dentro de la infraestructura global de AWS donde viven y se despliegan las máquinas virtuales (instancias) y las aplicaciones.

**Configuración Inicial**

Al desplegar una VPC, se deben definir parámetros fundamentales para su enrutamiento:

| Parámetro | Descripción |
|---|---|
| **Región** | La ubicación geográfica de la red en la nube |
| **Nombre** | Identificador lógico del recurso para su administración |
| **Network Block** | Define el espacio de direccionamiento IP disponible |

**Direccionamiento IP y Redes Privadas**

Bloques de direcciones IPv4 reservados para redes privadas:

| Clase | Bloque |
|---|---|
| Clase A | `10.0.0.0/8` |
| Clase B | `172.16.0.0/12` |
| Clase C | `192.168.0.0/16` |

> En redes domésticas se usa comúnmente una máscara `/24` (ej. `192.168.1.0/24`), que otorga un máximo de 256 IPs.

**Agotamiento de IPs (IP Exhaustion)**

Ocurre cuando la red agota el número de direcciones IP disponibles para asignar a nuevos recursos.

- **On-Premises:** se cambia la máscara de subred o se usa un bloque contiguo con un router adicional.
- **En AWS (VPC):** es significativamente más complicado. Los servicios ya están configurados de fondo y no se pueden aplicar soluciones de infraestructura física directamente.
- **Solución:** planificar con exactitud las IPs necesarias **antes** de desplegar la VPC.

**Gestión de Entornos y Asignación Empresarial**

- Se recomienda una VPC dedicada por entorno: Producción, Stage, QA y Dev.
- Cada proyecto debe tener su propio bloque de red, solicitado y aprobado por el área de redes.
- ⚠️ **Concepto crítico:** AWS **reserva 5 IPs automáticamente** por subred (para conectividad, DNS y enrutamiento interno). Esas IPs no pueden asignarse a instancias.

---

#### Segmentación de Red: Subredes y Modelo CIDR

Para desplegar recursos de forma organizada, el bloque principal de la VPC se divide en segmentos más pequeños.

**Conceptos clave**

| Concepto | Descripción |
|---|---|
| **Subredes (Subnets)** | Particiones lógicas de la VPC que agrupan recursos por acceso y seguridad |
| **CIDR** | Estándar de enrutamiento que permite asignación flexible con formato de sufijo (ej. `/24`) |
| **División Base 2** | Los bloques solo pueden fragmentarse en potencias de 2 |

> Herramienta recomendada: [ipcalc.info](https://ipcalc.info/) para calcular y evitar solapamiento de redes.

**Ejemplo de División — Bloque `10.0.0.0/22` (1,024 IPs)**

| Subred | Bloque | IPs |
|---|---|---|
| Subnet A | `10.0.0.0/24` | 256 |
| Subnet B | `10.0.1.0/24` | 256 |
| Subnet C | `10.0.2.0/24` | 256 |
| Subnet D (Reserva) | `10.0.3.0/24` | 256 |

---

#### Mejores Prácticas

- **Zonas de Disponibilidad:** una subred vive en una sola AZ. Para alta disponibilidad, replicar subredes en múltiples AZs.
- **Subred pública:** tiene ruta a Internet mediante un Internet Gateway (IGW). Usada para balanceadores de carga y servidores web.
- **Subred privada:** sin ruta a Internet. Obligatoria para bases de datos (RDS) y backends por seguridad.

#### ✅ Conclusiones

Diseñar correctamente una VPC desde el inicio es crítico: el espacio de IPs no se puede ampliar fácilmente en la nube. Planificar subredes, zonas de disponibilidad y separación pública/privada desde el principio evita problemas costosos en producción.

---

### 📅 Clase 11 — 17/06/2026

#### Temas Vistos

La seguridad en AWS se basa en la protección de los recursos, datos y aplicaciones mediante controles de acceso, monitoreo y servicios de seguridad administrados.

---

**Modelo de Responsabilidad Compartida**

AWS utiliza un modelo donde tanto AWS como el cliente tienen responsabilidades específicas.

- **AWS** es responsable de la seguridad **de la nube**: infraestructura física, hardware, software de la plataforma, redes y virtualización.
- **El cliente** es responsable de la seguridad **en la nube**: configuración de servicios, gestión de usuarios y permisos, protección de datos, configuración de redes y aplicaciones.

---

**Servicios de AWS — Modelos de Servicio**

| Modelo | Ejemplos | Ventajas |
|---|---|---|
| **IaaS** | EC2, VPC, Elastic Load Balancer | Mayor control, escalabilidad flexible, pago por uso |
| **PaaS** | Elastic Beanstalk, Lambda, RDS | Menor administración, desarrollo más rápido, escalabilidad automática |

---

**Direcciones IP**

Las direcciones IPv4 se representan con cuatro octetos decimales separados por puntos (ej. `192.168.1.10`). Cada octeto va de 0 a 255.

- **IPv4:** 32 bits
- **IPv6:** 128 bits — mayor espacio de direccionamiento

---

**Grupos de Seguridad (Security Groups)**

- Actúan como firewall virtual a nivel de **instancia**.
- Controlan tráfico entrante y saliente.
- Son **stateful** — mantienen el estado de las conexiones.

**ACL de Red (Network ACL)**

- Operan a nivel de **subred**.
- Son **stateless** — no mantienen el estado de las conexiones.
- Permiten reglas de permiso y denegación.

| Característica | Security Group | Network ACL |
|---|---|---|
| Nivel | Instancia | Subred |
| Stateful | Sí | No |
| Reglas de denegación | No | Sí |

#### ✅ Conclusiones

La seguridad en AWS es responsabilidad compartida: AWS protege la infraestructura, el cliente protege sus datos y configuraciones. Security Groups y Network ACLs son las dos capas de control de tráfico en una VPC — complementarias, no excluyentes.

---

### 📅 Clase 12 — 18/06/2026

#### Temas Vistos

Se realizó la tarea 993.

---

### 📅 Clase 13 — 22/06/2026

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

![Diagrama de arquitectura NightPass](https://github.com/DavidJauregu123/clouddataprocessing/blob/7372038972c152aa5fae9cce9d695748b7e80bda/Tarea%20%23998_Diagrama%20de%20arquitectura.jpeg)

---

### Tarea #997 — Pizza as a Service 2.0

> Investigación sobre Pizza as a Service 2.0 y los diferentes modelos de servicio en la nube.

🔗 [Ver presentación](https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/)

---

### Tarea #996 — Solución Estratificada de Problemas en TIC

> Investigación sobre la solución estratificada de problemas en Tecnologías de la Información y Comunicación.

🔗 [Ver presentación](https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/)

---

### Tarea #994 — Hola mundo en docker

> grabar asciinema donde crean el contenedor usando la imagen que crearon. Se debe ver el mensaje de hola mundo.

🔗 [Ver archivo](https://github.com/DavidJauregu123/clouddataprocessing/blob/2dde56eec2ecb7a6476767639b6340946b2f218d/Tarea%20%23994-demo.cast)

---

### Tarea #992 Elegir una herramienta de la unidad 3 y realizar diapositivas usando Markdown y WebJeda.

🔗 [Ver presentación](https://tuxtter.github.io/diapositivas/map-reduce/#/)

---
