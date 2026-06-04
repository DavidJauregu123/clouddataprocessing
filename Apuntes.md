# clouddataprocessing
Portafolio de Tareas de la Materia de Procesamiento de Datos en la Nube

# Bitácora de Clase

## Fecha
01/06/2026

## Temas vistos

### Introducción al curso
Se presentó la materia, los objetivos del curso y se identificó a los alumnos que previamente habían tomado clases con el profesor.

### Infraestructura como Código (IaC)
Se explicó el concepto de Infraestructura como Código, una metodología que permite administrar y aprovisionar recursos tecnológicos mediante archivos de configuración en lugar de procesos manuales.

### Servicios en la nube y máquinas virtuales
Se revisó qué es un servicio en la nube y cómo permite acceder a recursos informáticos a través de internet. También se explicó el concepto de máquina virtual como una simulación de un equipo físico que puede ejecutar sistemas operativos y aplicaciones de manera independiente.

### Cloud Agnostic
Se abordó el concepto de *Cloud Agnostic*, que consiste en desarrollar soluciones que puedan ejecutarse en diferentes proveedores de nube sin depender de uno en particular.

### Herramientas de Infraestructura como Código
Se compararon las principales herramientas utilizadas para IaC:

- **Terraform:** Herramienta ampliamente utilizada y compatible con múltiples proveedores de nube.
- **Pulumi:** Permite definir infraestructura utilizando lenguajes de programación tradicionales.
- **CloudFormation:** Servicio de Amazon Web Services (AWS) para gestionar infraestructura dentro de su ecosistema.

### CI/CD y DevOps
Se introdujeron conceptos relacionados con la integración y entrega continua (CI/CD), destacando la automatización de procesos de desarrollo, pruebas y despliegue.

### Branching Strategy
Se explicó la importancia de definir estrategias de ramificación en Git para organizar el trabajo colaborativo y el control de versiones.

### Herramientas de automatización y despliegue
Se revisaron algunas herramientas utilizadas en entornos DevOps:

- **FluxCD:** Herramienta de GitOps para automatizar despliegues en Kubernetes.
- **GitHub Actions:** Plataforma integrada en GitHub para crear flujos de trabajo automatizados.
- **Jenkins:** Servidor de automatización de código abierto ampliamente utilizado para CI/CD.

## Conclusiones
Durante la clase se introdujeron conceptos fundamentales de computación en la nube, infraestructura como código y prácticas DevOps. Además, se analizaron diferentes herramientas utilizadas para automatizar la gestión de infraestructura y los procesos de integración y despliegue continuo.


Tarea #999
#  NightPass — Plataforma de Eventos Nocturnos en Cancún

> Aplicación web y móvil para descubrir, reservar y acceder a fiestas caseras y antros en Cancún, con venta de boletos digitales y control de acceso por QR.

---

##  Descripción del Proyecto

**NightPass** es una plataforma digital diseñada para conectar a los asistentes con los mejores eventos nocturnos de Cancún: desde fiestas privadas en casas hasta los antros más reconocidos de la zona hotelera. La app permite comprar entradas con antelación, reservar mesas VIP y acceder al evento mediante un código QR único, eliminando filas y facilitando el control de aforo para los organizadores.

El proyecto nace de la necesidad de digitalizar la experiencia nocturna en una de las ciudades turísticas más importantes de México, ofreciendo una solución sencilla tanto para los asistentes como para los organizadores de eventos.

---

##  Objetivo

Desarrollar una aplicación de 3 capas desplegada en la nube (AWS) que permita:

- **Descubrir** eventos nocturnos cercanos en tiempo real.
- **Comprar** boletos de entrada de forma segura (tarjeta, OXXO, transferencia).
- **Reservar** mesas VIP con servicio de botella.
- **Acceder** al evento mediante un QR digital validado en puerta.
- **Gestionar** aforo, ingresos y asistentes desde un panel de administración.

### Diagrama de Arquitectura

![Diagrama de arquitectura NightPass](https://github.com/DavidJauregu123/clouddataprocessing/blob/f694026af54fc7ba25f73866f418f8510a5af955/Diagrama%20de%20arquitectura.png)


# Bitácora de Clase

## Fecha
02/06/2026

## Temas vistos

### Sistemas de Control de Versiones (VCS)

Se introdujo el concepto de VCS (Version Control System), herramientas que permiten administrar cambios en archivos y proyectos de software.

#### Comandos básicos de Git

```bash
git init
git status
git add
git commit
git push
git pull
git fetch
git clone
```

### Plataformas de alojamiento de repositorios

Se revisaron diferentes plataformas utilizadas para almacenar y gestionar repositorios Git:

- GitHub
- GitLab
- Gitea

### Estrategias de ramas (Branching Strategy)

Se explicó la importancia de organizar el desarrollo mediante ramas especializadas.

#### Tipos de ramas

- **main**: versión estable del proyecto.
- **develop**: integración de nuevas funcionalidades.
- **feature**: desarrollo de nuevas características.
- **release**: preparación de versiones.
- **hotfix**: corrección urgente de errores.

### DevOps y CI/CD

Se introdujo el concepto de DevOps y la automatización mediante procesos de Integración Continua y Entrega Continua (CI/CD).

#### Beneficios

- Automatización de despliegues.
- Reducción de errores.
- Entregas más rápidas.
- Mejor colaboración entre equipos.

### GitHub y flujo de trabajo colaborativo

Se revisó la estructura de un repositorio remoto en GitHub y la interacción entre repositorios locales y remotos.

#### Conceptos vistos

- Repositorio local.
- Repositorio remoto.
- Sincronización mediante push y pull.
- Trabajo colaborativo.

### Git Flow

Se explicó el modelo Git Flow para administrar el ciclo de desarrollo mediante diferentes ramas.

#### Flujo básico

1. Crear una rama para una tarea.

```bash
git branch 998
git checkout 998
```

2. Realizar cambios y agregarlos al repositorio.

```bash
git add .
git commit -m "Added evidence for 998"
```

3. Integrar cambios a la rama principal.

```bash
git checkout main
git merge 998
git push
```

## Conclusiones

Durante la clase se estudiaron los fundamentos del control de versiones con Git, el uso de plataformas como GitHub, GitLab y Gitea, así como estrategias de ramificación y flujos de trabajo colaborativos. También se introdujeron conceptos de DevOps y CI/CD para automatizar procesos de integración y despliegue de software.



--Tarea #996 Investigacion de la Solución estratificada de problemas en TIC
Link: https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/


# Bitácora de Clase

## Fecha
03/06/2026

## Temas vistos

que es la informática en la nube?

----------------definición de informática en la nube:

la información en la nube es la entrega bajo demanda de potencia de computo, bases de datos, almacenamiento, aplicaciones y otros recurso de TI, a través de internet con un sistema de precios de pago por uso.


----------------INFRAESTRUCTURA INFORMATICA TRADICIONAL:

infraestructura como hardware 
soluciones de hardware

requieren de espacio personal, seguridad física, planificación e inversión de capital
tienen un ciclo largo de adquisición de hardware
le exigen aprovisionar capacidad mediante la predicción de los picos máximos teóricos

-----------------INFRAESTRUCTURA COMO SOFTWARE

-----------------MODELO DE SERVICIO EN LA NUBE

IaaS


INFRAESTRUCTURA COMO SERVICIO

PaaS

Plataforma como Servicio

SaaS

Sistema Como Servicio

--------------------Modelo de implementación Informatica

-------------------tipos de nubes

publica
privada
comunitaria
hibrida

Sobre el sprint Plannig

ECONIMIAS DE ESCALA MASIVA


--Tarea #997 Investigar sobre Pizza as a service 2.0 y los diferentes modelos de servicio en la nube que presenta.
Link: https://davidjauregu123.github.io/Presentaciones_web_Jeda_Tarea-996_y_Tarea-997/






