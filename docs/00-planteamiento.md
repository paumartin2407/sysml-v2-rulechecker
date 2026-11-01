# sysml-v2-rulechecker

**Digitalización de Ingeniería de Sistemas Complejos · UC3M**  
**Proyecto 7:** verificación y validación inteligente de modelos SysML v2  

## Ficha del planteamiento

| Campo | Nuestra propuesta |
|---|---|
| Títulos candidatos | `sysml-v2-rulechecker`; `sysml-v2-quality-checker`; `sysml-v2-tracecheck` |
| Nombre elegido | `sysml-v2-rulechecker`: indica que la herramienta comprueba reglas concretas. |
| Área | Ingeniería de sistemas basada en modelos (MBSE). |
| Tema | Herramienta para revisar modelos SysML v2 con reglas y explicar los problemas detectados con ayuda de IA. |
| Síntoma | Al revisar un modelo pueden pasar desapercibidas referencias incorrectas o relaciones que faltan entre requisitos, componentes y pruebas. |
| Causa | Las comprobaciones que queremos hacer no están reunidas en un proceso automático que indique qué regla falla y dónde. |
| Interés | Facilitar una revisión temprana y mostrar al modelador por qué se ha señalado cada problema. |
| Consecuencias de no resolverlo | Habrá que repetir revisiones manuales y algunos problemas podrían descubrirse tarde, cuando corregirlos cueste más. Son riesgos que todavía no hemos medido. |
| Beneficios de resolverlo | Localizar antes los defectos del caso de estudio y obtener resultados que se puedan comprobar y repetir. |
| Trabajos existentes | Hay propuestas de validación con reglas, patrones e IA. Su búsqueda y comparación están pendientes de completar por el grupo. |
| Solución propuesta | Leer un conjunto acotado de modelos SysML v2, aplicar reglas, mostrar cada problema con su evidencia y usar IA para explicarlo. Después se podrá analizar de nuevo el modelo corregido. |
| Hipótesis | Frente a una revisión manual, la herramienta permitirá localizar los defectos del caso de estudio al menos un 30 % más rápido, con una sensibilidad mínima del 85 % y un máximo del 10 % de avisos falsos. |
| Parámetros para corroborarla | Tiempo de localización, defectos encontrados y avisos falsos, medidos sobre modelos con defectos conocidos. |
| Estándares implicados | SysML v2 y KerML. La Systems Modeling API se usaría si resulta útil para leer los modelos. |

## Resumen

Revisar a mano un modelo SysML v2 puede llevar tiempo y dejar problemas sin detectar.  
Queremos crear una herramienta que compruebe reglas concretas de estructura y trazabilidad.  
Cada aviso mostrará qué se ha encontrado y en qué parte del modelo.  
La IA ayudará a explicar los avisos, pero no decidirá si una regla se cumple.  
Empezaremos por las partes de SysML v2 que podamos leer con fiabilidad.  
Compararemos el uso de la herramienta con una revisión manual.  
Mediremos el tiempo necesario, los defectos encontrados y los avisos falsos.

## Introducción

Nuestro trabajo se sitúa en el (ÁREA) de la ingeniería de sistemas basada en modelos. Al revisar modelos SysML v2, el (SÍNTOMA) es que algunas referencias incorrectas o relaciones ausentes pueden pasar desapercibidas. La (CAUSA) que abordamos es que las comprobaciones elegidas para este proyecto no se aplican juntas y de forma automática, con resultados fáciles de localizar. El (OBJETIVO) es crear una herramienta que haga esas comprobaciones y ayude a revisar sus resultados. Nuestra (HIPÓTESIS) es que permitirá encontrar los defectos del caso de estudio al menos un 30 % más rápido que una revisión manual, con una sensibilidad mínima del 85 % y un máximo del 10 % de avisos falsos.

La (IMPORTANCIA DE RESOLVER EL PROBLEMA) está en detectar y entender los problemas antes. Las (CONSECUENCIAS DE NO RESOLVER EL PROBLEMA) son repetir revisiones y correr el riesgo de descubrir errores más tarde. Los (BENEFICIOS DE RESOLVER EL PROBLEMA) serían ahorrar tiempo en el caso estudiado y obtener avisos que se puedan comprobar. Los (TRABAJOS EXISTENTES…) sobre validación de modelos y uso de IA se buscarán y compararán en el estado de la cuestión. Nuestra (SOLUCIÓN PROPUESTA) aplicará reglas para detectar problemas y usará IA para explicarlos a partir de la evidencia encontrada. Los (PARÁMETROS PARA CORROBORAR LA HIPÓTESIS) serán el tiempo de localización, la sensibilidad y la proporción de avisos falsos, comparados con una revisión manual.

## Hipótesis

**Si** usamos una herramienta que aplica reglas y señala dónde está cada problema en los modelos SysML v2 elegidos, **entonces** los revisores encontrarán los defectos conocidos al menos un **30 % más rápido** que al revisar a mano, con una **sensibilidad mínima del 85 %** y **como máximo un 10 % de avisos falsos**.

Estos umbrales son una propuesta para debatir con el profesor. Si no se alcanza cualquiera de ellos, consideraremos que el ensayo no confirma la hipótesis. Los resultados solo se referirán a los modelos estudiados.

## Objetivos

**Objetivo general.** Desarrollar y evaluar una herramienta que detecte problemas de estructura y trazabilidad en modelos SysML v2 mediante reglas y ayude a revisarlos con explicaciones basadas en los resultados obtenidos.

| ID | Objetivo específico | Resultado observable en el repositorio | Criterio de aceptación | Traza a |
|---|---|---|---|---|
| OE1 | Analizar trabajos sobre validación de SysML y uso de IA. | Búsquedas y comparación de trabajos. | Se documentan seis trabajos, incluidos tres artículos y una herramienta, consultando dos bases bibliográficas y comprobando sus DOI o URL. | Causa y trabajos existentes. |
| OE2 | Diseñar las reglas, el alcance y la estructura de la herramienta. | Descripción de las reglas y diseño de la herramienta. | Cada regla indica cuándo se aplica, qué detecta y qué ejemplos la cumplen o incumplen. | Causa y solución. |
| OE3 | Implementar la lectura de modelos, las reglas y las explicaciones. | Código, modelos de ejemplo y pruebas. | La herramienta lee un modelo SysML v2 del alcance elegido, produce resultados repetibles y explica avisos que realmente ha generado. | Solución. |
| OE4 | Evaluar la herramienta frente a la revisión manual. | Modelos etiquetados, procedimiento y resultados. | Se miden los tres indicadores y se concluye si la hipótesis se cumple o no. | Hipótesis y parámetros. |

Usaremos OE1–OE4 también en los hitos o épicas de GitHub y, más adelante, en requisitos y pruebas. **Estos objetivos aún deben validarse con el profesor.**

## Estado de la cuestión preliminar

**Cómo buscamos (22/10/2026).** Empezamos por validación de SysML v2 y después buscamos trabajos sobre IA y herramientas disponibles. Consultamos registros de IEEE Xplore y Wiley/INCOSE mediante búsquedas web limitadas a sus dominios; no usamos la búsqueda avanzada de esas bases. Elegimos cuatro artículos y dos herramientas relacionados con el problema. Cada código B1–B6 conecta una búsqueda con una fila de la comparación.

| ID | Fuente y consulta realizada | Trabajo obtenido |
|---|---|---|
| B1 | IEEE Xplore: `site:ieeexplore.ieee.org "SysML v2" validation metamodel`; [registro editorial](https://ieeexplore.ieee.org/document/11077130/). | Cibrián et al. (2025). |
| B2 | Búsqueda por título: `"Automated Semantic Fault Localization in SysML v2" Al-Shami`; [portal de Aalto](https://research.aalto.fi/en/publications/automated-semantic-fault-localization-in-sysml-v2-a-human-in-the-/) y [registro en Wiley/INCOSE](https://incose.onlinelibrary.wiley.com/doi/10.1002/iis2.70189). | Al-Shami et al. (2026). |
| B3 | Búsqueda por título: `"AI-Driven Consistency of SysML Diagrams" Sultan Apvrille MODELS 2024`; [texto de los autores](https://perso.telecom-paristech.fr/apvrille/docs/models2024_sultan.pdf), con referencia a la publicación en ACM. | Sultan y Apvrille (2024). |
| B4 | Wiley/INCOSE: `site:incose.onlinelibrary.wiley.com "Verification and Validation of SysML Models" Hecht Chen`; [registro editorial](https://incose.onlinelibrary.wiley.com/doi/full/10.1002/j.2334-5837.2021.00857.x). | Hecht y Chen (2021). |
| B5 | GitHub: `site:github.com/Systems-Modeling/SysML-v2-Pilot-Implementation SysML v2 pilot`; [repositorio](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation). | Implementación piloto de SysML v2. |
| B6 | Zenodo: `site:zenodo.org/records "Pattern-Based Validation of SysML v2 Models with Refinery"`; [artefacto, versión 2](https://zenodo.org/records/19297800). | Bajczi y Tóth (2026). |

**Comparación de trabajos.**

La tabla resume qué aporta cada trabajo y qué queda por explorar en nuestra propuesta.

| Trabajo | Enfoque | Estándares o lenguaje | Relación con nuestro problema | DOI o URL |
|---|---|---|---|---|
| **B1** Cibrián et al. (2025), *Ensuring Semantic Consistency in SysML v2 Models Through Metamodel-Driven Validation* | Comprueba modelos con reglas derivadas del metamodelo y sugiere correcciones de erratas en atributos. | SysML v2. | Ya detecta errores de modelo. Queremos estudiar avisos de trazabilidad, explicarlos con evidencia y medir si ayudan a revisar más rápido. | [10.1109/ACCESS.2025.3587786](https://doi.org/10.1109/ACCESS.2025.3587786) |
| **B2** Al-Shami et al. (2026), *Automated Semantic Fault Localization in SysML v2* | Entrena un modelo de lenguaje para localizar fallos y proponer cambios. | SysML v2. | Estudia sobre todo fallos de interfaces creados para la evaluación. Nosotros partimos de reglas explícitas y no entrenaremos un modelo de reparación. | [10.1002/iis2.70189](https://doi.org/10.1002/iis2.70189) |
| **B3** Sultan y Apvrille (2024), *AI-Driven Consistency of SysML Diagrams* | Combina reglas e IA para detectar y corregir diferencias entre diagramas. | SysML, diagramas de casos de uso y bloques. | Trabaja con diagramas gráficos; nuestra propuesta se centra en modelos textuales SysML v2 y en explicar avisos producidos por reglas. | [10.1145/3640310.3674079](https://doi.org/10.1145/3640310.3674079) |
| **B4** Hecht y Chen (2021), *Verification and Validation of SysML Models* | Propone adaptar a cada proyecto una lista de comprobaciones manuales y automáticas. | SysML. | Nos sirve como antecedente para elegir reglas; evaluaremos una herramienta concreta sobre SysML v2. | [10.1002/j.2334-5837.2021.00857.x](https://doi.org/10.1002/j.2334-5837.2021.00857.x) |
| **B5** Implementación piloto de SysML v2, OMG Systems Modeling Community | Ofrece herramientas del lenguaje y modelos de ejemplo. | SysML v2 y KerML. | Debemos comprobar qué errores detecta ya y si podemos aprovechar su lectura de modelos. | [Repositorio](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) |
| **B6** Bajczi y Tóth (2026), *Pattern-Based Validation of SysML v2 Models with Refinery* | Aplica patrones de validación a modelos obtenidos mediante la API. | SysML v2 API. | Es la herramienta más cercana para comparar nuestras reglas. Debemos revisar también cómo muestra la evidencia y si evalúa su utilidad para usuarios. | [10.5281/zenodo.19297800](https://doi.org/10.5281/zenodo.19297800) |

**Diferencia que queremos comprobar.** Proponemos unir reglas claras, avisos con evidencia y explicaciones de IA, y comprobar con personas si eso ayuda frente a una revisión manual. Afinaremos esta idea cuando el grupo lea los trabajos más próximos.

## Propuesta técnica inicial

Empezaremos por componentes, atributos, requisitos y algunas relaciones de satisfacción o verificación. Primero comprobaremos que podemos leer un modelo SysML v2 real y conservar sus elementos y relaciones. A partir de ahí decidiremos qué reglas podemos implementar con fiabilidad.

Cada aviso mostrará la regla aplicada, el elemento afectado, dónde está y qué evidencia lo respalda. Una relación de verificación ausente se señalará como posible problema de trazabilidad según las reglas acordadas; no significa necesariamente que el modelo incumpla SysML v2. La IA explicará los avisos a partir de estos datos y podrá sugerir qué revisar.

## Validación de la propuesta

**Caso de estudio:** un dron pequeño descrito con componentes, requisitos y casos de verificación en SysML v2. Prepararemos dos versiones comparables del modelo, con defectos conocidos y ejemplos correctos. Antes de la prueba anotaremos dónde está cada defecto y qué regla debería detectarlo.

**Procedimiento:** al menos cuatro personas revisarán una versión con la herramienta y otra a mano. Todos recibirán las mismas instrucciones. Alternaremos el orden y la versión asignada para que la comparación sea lo más justa posible. Anotaremos los tiempos y los problemas encontrados por cada persona.

| Métrica | Cálculo y criterio propuesto |
|---|---|
| Tiempo de localización | Compararemos la mediana de los tiempos. Con la herramienta deberá ser, como máximo, el 70 % de la mediana manual. Los defectos no encontrados se registrarán como tales. |
| Sensibilidad | Defectos conocidos encontrados / defectos conocidos que podían detectarse. Deberá ser al menos el 85 %. |
| Proporción de avisos falsos | Avisos sin defecto correspondiente / total de avisos. Deberá ser como máximo el 10 %. |

Guardaremos el tamaño del conjunto de modelos, los resultados sin nombres personales y las limitaciones de la prueba. Si cambiamos las reglas o los modelos, lo anotaremos antes de la evaluación final. Revisaremos aparte si las explicaciones de IA son fieles a la evidencia, claras y útiles.

## Estándares implicados

- **SysML v2:** lenguaje de los modelos que vamos a analizar. Indicaremos qué partes admite la herramienta.
- **KerML:** base de SysML v2 que consultaremos para interpretar los elementos utilizados.
- **Systems Modeling API:** posible forma de acceder a los modelos, si elegimos una herramienta que la utilice.

Distinguiremos las reglas del lenguaje de las reglas de calidad que definamos para el caso de estudio.

## Declaración de uso de IA

Durante la preparación de este documento se ha utilizado inteligencia artificial generativa como herramienta de apoyo, para organizar y redactar. El grupo revisará y asumirá la responsabilidad del contenido antes de la entrega.
