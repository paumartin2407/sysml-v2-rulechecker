# sysml-v2-rulechecker

Propuesta de una herramienta para revisar modelos SysML v2 mediante reglas de estructura y trazabilidad. El proyecto combina resultados reproducibles y localizables con explicaciones basadas en la evidencia, asistidas por inteligencia artificial.

Proyecto de **Digitalización de Ingeniería de Sistemas Complejos · UC3M**, centrado en la verificación y validación inteligente de modelos SysML v2.

> **Estado:** propuesta y requisitos iniciales. El diseño, la implementación y la evaluación de la herramienta están pendientes.

## Qué se pretende hacer

La primera entrega se plantea como una aplicación local, accesible desde el navegador, que permita:

- Cargar archivos `.sysml` y analizar un subconjunto declarado de SysML v2.
- Aplicar diez reglas configurables de estructura, trazabilidad y propiedades.
- Consultar hallazgos con su regla, elemento afectado, evidencia y ubicación cuando esté disponible, así como las limitaciones del análisis.
- Solicitar explicaciones y sugerencias de revisión asistidas por IA.
- Comparar ejecuciones y exportar los resultados en HTML y JSON.

El motor de reglas determinará los resultados; la IA ayudará a interpretarlos. Las reglas de calidad del proyecto se distinguirán de las obligaciones del lenguaje. La aplicación no incluirá un editor completo, corrección automática ni simulación física, y no demostrará por sí sola que el sistema satisfaga las necesidades reales.

## Objetivo e hipótesis

El objetivo general es desarrollar y evaluar una herramienta que detecte problemas de estructura y trazabilidad en modelos SysML v2 mediante reglas reproducibles y facilite su revisión con explicaciones basadas en evidencias.

La hipótesis propone que, frente a la revisión manual, la herramienta permita localizar los defectos conocidos al menos un **30 % más rápido**, con una **sensibilidad mínima del 85 %** y un **máximo del 10 % de avisos falsos** entre los emitidos. Estos son objetivos de evaluación, no resultados obtenidos.

Para ponerla a prueba se plantea un caso de estudio de un dron pequeño, con modelos que contienen defectos conocidos, y una comparación entre revisión manual y asistida. Las conclusiones se limitarán a los modelos y participantes estudiados.

## Documentación

- [Planteamiento de la investigación](docs/00-planteamiento.md): contexto, objetivos, antecedentes y propuesta de evaluación.
- [Requisitos de la aplicación](docs/01-requisitos.md): alcance, funciones, catálogo inicial de reglas y criterios de verificación.
- [Página web de la entrega](https://paumartin2407.github.io/sysml-v2-rulechecker/).
