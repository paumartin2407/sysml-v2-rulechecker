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

Pendiente de completar por el grupo. Se añadirán las búsquedas, la comparación de trabajos y las referencias para su revisión en la siguiente sesión.

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
