# Requisitos de sysml-v2-rulechecker

**Versión:** 1.1  
**Fecha:** 23/10/2026

## 1. Propósito y usuarios

La aplicación ayudará a revisar modelos SysML v2. Aplicará reglas de estructura y trazabilidad, mostrará los problemas encontrados y permitirá consultar sus evidencias. La inteligencia artificial explicará los hallazgos y sugerirá qué revisar. Los resultados de las reglas procederán del motor determinista.

La utilizarán las personas que preparan el modelo y las que lo revisan. Una misma persona puede desempeñar ambos papeles. Los modelos se modificarán fuera de la aplicación.

El caso de estudio será un dron pequeño. Los objetivos y las metas de evaluación indicados en este documento se consideran acordados para el proyecto.

## 2. Alcance

La primera entrega tendrá una interfaz visual local, abierta desde el navegador del equipo. Permitirá cargar archivos `.sysml`, configurar un único perfil, ejecutar las diez reglas del apartado 6, consultar resultados, pedir ayuda de IA, comparar ejecuciones y exportar HTML y JSON.

Se utilizará un analizador existente. El subconjunto cubrirá los requisitos, componentes, atributos, tipos, relaciones de contención, satisfacción y verificación, casos de verificación y extremos de relaciones que necesiten las reglas. Las conexiones se utilizarán para comprobar extremos y aislamiento; la compatibilidad de puertos, sus direcciones y las restricciones numéricas quedan fuera de esta entrega.

No se incluyen un editor completo, modificación automática, simulación física, ejecución de ensayos ni interpretación de todo SysML v2. La aplicación no demuestra por sí sola que el sistema modelado cumpla las necesidades reales.

## 3. Glosario

| Término | Significado |
|---|---|
| Revisión | Conjunto concreto de archivos del modelo y dependencias, identificado por sus nombres dentro del conjunto y su contenido. Una etiqueta escrita por el usuario no sustituye esa identidad. |
| Ejecución | Análisis de una revisión con versiones de herramientas, reglas y parámetros determinados. |
| Perfil | Configuración de trabajo que indica reglas activas y valores de sus parámetros. Esta entrega maneja un único perfil editable. |
| Elemento | Objeto del modelo que el analizador ha reconocido y que el adaptador puede identificar. |
| Ámbito | Conjunto de elementos y dependencias sobre el que una regla busca información. |
| Ámbito evaluable | Ámbito en el que están resueltas las dependencias y construcciones necesarias para decidir la condición concreta de la regla. No exige que todo el modelo sea interpretable. |
| Contenido utilizable | Elementos entregados por el analizador que el adaptador puede representar sin errores que invaliden sus datos. |
| Comprobación | Evaluación de una regla sobre un elemento o contexto identificado. |
| Resultado | Registro de una comprobación con su estado. |
| Hallazgo | Aviso asociado a un incumplimiento o a una limitación de análisis. Los resultados favorables también se conservan, aunque no produzcan avisos. |
| Diagnóstico de entrada | Problema comunicado durante la lectura o resolución del modelo, con identificación del analizador o adaptador que lo origina. |
| Política | Convención de revisión elegida en el perfil. No se presenta como una obligación universal del lenguaje. |
| Referencia contrastada | Referencia de una sugerencia que la aplicación ha podido asociar a un elemento de la revisión analizada. |

### Estados de una comprobación

| Estado | Significado |
|---|---|
| Cumple | La condición se ha evaluado y se satisface. |
| Incumple | La condición se ha evaluado y existe evidencia de que no se satisface. |
| No evaluable | La regla es pertinente, pero faltan datos o capacidades para decidir. |
| No aplicable | El elemento o contexto no está sujeto a la regla. |

Una regla desactivada se registra como **no seleccionada**. Un fallo interno se registra como **fallo de ejecución**. Ninguna de esas dos situaciones equivale a un resultado favorable.

### Severidad de los hallazgos

| Severidad | Uso |
|---|---|
| Error | Incumplimiento demostrado de una condición obligatoria dentro del alcance admitido. |
| Advertencia | Ausencia o problema respecto a una política de revisión que necesita valoración humana. |
| Información | Limitación de cobertura u observación que conviene comunicar. |

La ausencia de un vínculo en el modelo no demuestra que no exista satisfacción o verificación fuera de él. La presencia del vínculo tampoco demuestra cumplimiento físico ni ejecución de un ensayo.

## 4. Requisitos funcionales

Las descripciones explican el contexto. Los contratos del apartado 5 definen los datos y condiciones que se citan en los requisitos. Cada criterio de verificación se aplica al requisito de su fila.

### 4.1. Entrada

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RF-01 | La aplicación deberá importar los archivos `.sysml` y las dependencias seleccionadas por el usuario conforme al contrato C-ENT. | Los archivos se tratarán como una revisión. | Entrada | Cargar un modelo de un archivo y otro repartido en dos archivos relacionados; comprobar sus elementos y vínculos. |
| RF-02 | La aplicación deberá mostrar cada diagnóstico de entrada con origen, tipo y mensaje. | El contrato C-ENT define cuándo se dispone de archivo y posición. | Entrada | Probar diagnósticos con y sin posición y comprobar los campos mostrados. |
| RF-03 | La aplicación deberá clasificar las referencias no resueltas como dependencia ausente, destino inválido demostrado o causa indeterminada. | La clasificación se apoya en la evidencia descrita en C-ENT. | Entrada | Probar las tres causas y comprobar que un contexto incompleto no se presenta como destino inválido demostrado. |
| RF-04 | La aplicación deberá presentar el informe de importación definido en C-ENT. | Distingue contenido utilizable, contenido reconocido fuera del alcance y fallos de interpretación. | Entrada | Importar un ejemplo de cada situación y comprobar su clasificación y localización disponible. |
| RF-05 | Ante una entrada parcial, la aplicación deberá ejecutar únicamente las comprobaciones que no dependan del contenido invalidado. | Las comprobaciones pertinentes afectadas por la información ausente quedan no evaluables. | Entrada / motor | Omitir una dependencia y comprobar que una regla independiente se evalúa y una dependiente queda no evaluable. |
| RF-06 | La aplicación deberá detener las comprobaciones cuando el analizador y el adaptador no entreguen contenido utilizable. | El diagnóstico de entrada seguirá disponible. | Entrada / motor | Cargar un archivo que impida obtener elementos utilizables y comprobar que no se emiten veredictos sobre el modelo. |

### 4.2. Configuración y ejecución

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RF-07 | La aplicación deberá permitir activar o desactivar cada regla del catálogo desde el perfil de trabajo. | Solo se mantiene un perfil editable. | Configuración | Desactivar una regla y comprobar que queda no seleccionada en la siguiente ejecución. |
| RF-08 | La aplicación deberá aceptar para cada parámetro editable únicamente valores de su dominio declarado. | El editor conserva el último valor válido si rechaza uno nuevo. | Configuración | Introducir un valor admitido y otro fuera del dominio; comprobar aceptación, rechazo y mensaje. |
| RF-09 | La aplicación deberá conservar una copia de la configuración efectiva con cada ejecución. | Un cambio posterior del perfil no altera los análisis ya registrados. | Configuración | Ejecutar, cambiar un parámetro y comprobar que la ejecución anterior conserva su valor original. |
| RF-10 | La aplicación deberá iniciar la evaluación de las reglas activas cuando el usuario solicite el análisis. | Se aplica el catálogo del apartado 6 sobre el ámbito de cada regla. | Motor | Activar reglas, solicitar el análisis y comprobar las evaluaciones generadas y las reglas no seleccionadas. |
| RF-11 | La aplicación deberá mostrar la ficha de la regla seleccionada conforme a C-REG. | La ficha permite conocer qué se comprueba y con qué límites. | Catálogo | Consultar las diez reglas y comprobar los campos del contrato. |
| RF-12 | La aplicación deberá evaluar cada regla activa del apartado 6 sobre los elementos y contextos que correspondan a su definición. | Las diez reglas tienen precondiciones, resultados y ejemplos propios. | Motor de reglas | Para cada regla, probar un caso favorable, un defecto y una limitación de datos cuando corresponda; comprobar el resultado y la evidencia. |
| RF-13 | La aplicación deberá asignar a cada comprobación completada uno de los cuatro estados del apartado 3. | La comprobación identifica regla, versión y elemento o contexto. | Motor | Obtener los cuatro estados y comprobar que se conservan en los resultados. |
| RF-14 | La aplicación deberá registrar el motivo de cada resultado no evaluable o no aplicable. | El motivo identifica el dato ausente o la condición que no corresponde al contexto. | Motor | Comprobar motivos en una dependencia ausente y en un tipo de elemento no sujeto a una regla. |
| RF-15 | La aplicación deberá registrar los fallos internos como fallos de ejecución separados de los resultados del modelo. | Una evaluación fallida no recibe un estado cumple o incumple. | Motor | Provocar un fallo controlado y comprobar el registro de la regla afectada y la ausencia de veredicto para esa evaluación. |

### 4.3. Consulta de resultados

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RF-16 | La aplicación deberá mostrar cada hallazgo con los campos definidos en C-RES. | La evidencia registrada debe respaldar la afirmación del mensaje. | Resultados | Revisar un incumplimiento y una limitación de cobertura; comprobar campos, procedencia y evidencia. |
| RF-17 | La aplicación deberá mostrar los hallazgos que satisfagan los filtros seleccionados por el usuario. | Se filtra por severidad, categoría, regla y elemento, con la combinación definida en C-RES. | Resultados | Probar cada filtro y dos filtros combinados sobre un conjunto con resultados esperados. |
| RF-18 | La aplicación deberá mostrar el contexto del elemento seleccionado desde un hallazgo. | C-RES define los datos de contexto y la condición para señalar la fuente. | Resultados | Seleccionar un elemento con posición y otro sin ella; comprobar identidad, tipo y relaciones representadas. |
| RF-19 | La aplicación deberá presentar el resumen de ejecución definido en C-RES cuando el análisis finalice o se interrumpa por un fallo. | El resumen distingue estados, reglas no seleccionadas, fallos y cobertura. | Resultados | Analizar un caso con todas esas situaciones y comprobar los recuentos y el estado final de la ejecución. |

### 4.4. Explicaciones y sugerencias

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RF-20 | La aplicación deberá generar una explicación del hallazgo cuando el usuario la solicite. | Se vincula al hallazgo y revisión de origen y utiliza la pauta C-IA. | IA | Revisar explicaciones de estructura, trazabilidad y no evaluación mediante la pauta de cuatro preguntas. |
| RF-21 | La aplicación deberá generar una sugerencia de revisión del hallazgo cuando el usuario la solicite. | La sugerencia utiliza la regla, la evidencia y el contexto del modelo. | IA | Pedir sugerencias sobre un vínculo ausente y una referencia no resuelta; comprobar su relación con los hallazgos. |
| RF-22 | La aplicación deberá contrastar las referencias a elementos existentes antes de mostrarlas como hechos del modelo en una respuesta de IA. | Si una referencia no se resuelve, la respuesta se marca como no contrastada en ese punto. | IA | Usar respuestas controladas con ID válido, nombre parecido incorrecto y elemento inexistente; comprobar la clasificación. |
| RF-23 | La aplicación deberá presentar las respuestas de IA con las categorías de C-IA. | Se distinguen hechos contrastados, hipótesis, elementos nuevos propuestos, decisiones del usuario e información insuficiente. | IA / interfaz | Revisar una respuesta con cada categoría y comprobar que una propuesta no aparece como elemento existente. |
| RF-24 | La aplicación deberá ejecutar las reglas deterministas solicitadas cuando la IA esté indisponible. | El servicio generativo no determina los estados de las reglas. | Motor | Desactivar la IA antes de iniciar un análisis y comprobar los mismos resultados deterministas. |
| RF-25 | La aplicación deberá mostrar los resultados deterministas registrados cuando la IA esté indisponible. | Incluye mensajes y evidencias. | Resultados | Interrumpir la IA después de un análisis y comprobar que los resultados siguen accesibles. |
| RF-26 | La aplicación deberá informar de la indisponibilidad de la IA cuando una solicitud de ayuda falle por esa causa. | La notificación se vincula a la solicitud fallida. | IA / interfaz | Simular un fallo de conexión durante una explicación y comprobar el aviso. |

### 4.5. Revisiones, exportación e interfaz

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RF-27 | La aplicación deberá identificar como otra revisión un conjunto de archivos cuyo contenido o nombres difieran del conjunto cargado anteriormente. | Cada ejecución conserva su revisión de origen. | Revisiones | Modificar un archivo, volver a cargarlo y comprobar que los resultados anteriores siguen asociados al contenido original. |
| RF-28 | La aplicación deberá comparar los hallazgos de dos ejecuciones conforme a C-COMP. | La comparación distingue persistente, resuelto, nuevo y correspondencia indeterminada. | Revisiones | Probar las cuatro clases, incluido un renombrado sin ID estable y una regla desactivada. |
| RF-29 | La aplicación deberá mostrar un aviso cuando la revisión cargada difiera de la revisión de los resultados visibles. | La diferencia se basa en identidad de contenido, no en la fecha o el nombre de una etiqueta. | Revisiones | Cargar un cambio sin analizarlo y comprobar el aviso; volver al contenido original y comprobar la correspondencia. |
| RF-30 | La aplicación deberá exportar un informe HTML de la ejecución seleccionada conforme a C-SAL. | El informe puede abrirse en el navegador local. | Exportación | Abrir un informe con hallazgos y otro sin ellos pero con cobertura parcial; comprobar sus secciones y legibilidad. |
| RF-31 | La aplicación deberá exportar los resultados de la ejecución seleccionada en JSON conforme a C-SAL. | El documento incluye una versión de esquema. | Exportación | Validar contra el esquema una ejecución con hallazgos y otra con lista de hallazgos vacía y resultados no evaluables. |
| RF-32 | La aplicación deberá ofrecer las funciones de usuario de este documento mediante una interfaz visual local accesible desde el navegador. | Se utiliza sin publicar la aplicación en Internet. La IA puede ser un servicio externo. | Interfaz | Completar carga, configuración, análisis, consulta, comparación y exportación en una instalación local. |

## 5. Contratos comunes

### C-ENT. Entrada y cobertura

La documentación de entrada identificará la versión de SysML v2 admitida, las construcciones interpretadas, los formatos de dependencias y la versión del analizador. Las listas concretas se publicarán con el adaptador antes de aceptar sus pruebas de integración.

Cada diagnóstico contendrá origen, tipo o código y mensaje. Incluirá archivo y posición si el analizador los entrega; su ausencia se indicará sin inventar una localización.

El adaptador mantendrá una relación entre diagnósticos, elementos afectados y dependencias de las comprobaciones. Un elemento es utilizable cuando el analizador lo ha entregado y el adaptador puede representar los datos que necesita la regla sin un diagnóstico que los invalide. Una comprobación depende de contenido invalidado si necesita ese elemento o una referencia cuya resolución resulte afectada. Si el alcance del error no puede delimitarse, se consideran no evaluables las comprobaciones que puedan depender de él. Si no puede obtenerse ningún elemento utilizable, se detiene la evaluación.

La falta de destino solo se clasifica como inválida demostrada cuando se han resuelto los ámbitos, importaciones y construcciones necesarios para esa referencia. Si existe una dependencia identificada que no se ha cargado, se clasifica como dependencia ausente. En otro caso, la causa queda indeterminada.

El informe de importación enumera el contenido utilizable, el reconocido fuera del alcance y los fallos de interpretación. Cuando un fragmento no pueda interpretarse, se comunica esa limitación sin inventariar elementos que el analizador no haya reconocido.

### C-REG. Reglas y perfil

Cada ficha contiene ID, versión, descripción, categoría, origen de la obligación, tipos de elementos admitidos, ámbito, precondiciones, condición, parámetros con sus dominios, severidad, evidencia y motivos de no evaluación.

El perfil permite activar las diez reglas y ajustar las políticas de T01–T03, las propiedades requeridas por tipo de P01 y los tipos de componente sujetos a P02. Una lista de política vacía no introduce una obligación implícita. La configuración efectiva se copia al iniciar la ejecución.

Antes de implementar las reglas se adjuntarán al catálogo las tablas concretas de categorías de relación y extremos permitidos, los ámbitos de unicidad y los vínculos explícitos admitidos. El adaptador deberá demostrar que conserva los datos necesarios con ejemplos del dron. Un resultado no evaluable por una limitación no sustituye la prueba de una capacidad comprometida.

### C-RES. Registros y presentación

| Registro | Datos mínimos |
|---|---|
| Resultado | Ejecución, regla y versión, elemento o contexto, estado, evidencia y motivo cuando el estado sea no evaluable o no aplicable. |
| Hallazgo | ID, resultado o diagnóstico de origen, regla y versión cuando procedan, categoría, elementos o contexto, mensaje, severidad, evidencia, condiciones de aplicación y posición disponible. |
| Contexto de elemento | ID interno, nombre si existe, tipo, relaciones interpretadas y referencia a la fuente disponible. |
| Fallo interno | Ejecución, regla o etapa afectada, código y mensaje. |

Cada incumplimiento genera un hallazgo. Una limitación no evaluable genera un hallazgo informativo con su motivo. Las comprobaciones que cumplen o no son aplicables siguen accesibles como resultados. Los diagnósticos de entrada conservan su origen; si también se reflejan en una regla, se vinculan para reconocer que proceden del mismo problema.

Dentro de un filtro, varios valores seleccionados se combinan mediante «o». Entre filtros distintos se usa «y». Sin filtros se muestran todos los hallazgos de la ejecución seleccionada.

El resumen cuenta comprobaciones por estado y fallos por separado; identifica las reglas no seleccionadas y los elementos fuera de cobertura. También presenta los resultados agrupados por regla. Cada comprobación se identifica por regla y elemento o contexto, evitando confundir número de reglas con número de evaluaciones.

### C-IA. Respuestas generadas

El contexto enviado a la IA contiene hallazgo, regla, evidencia y fragmento o representación del modelo que interviene en la explicación. La respuesta conserva la revisión de origen.

La explicación responde a cuatro preguntas: qué se detectó, qué evidencia lo respalda, por qué puede importar y qué información o actuación permitiría abordarlo.

Las categorías de presentación son hecho contrastado, hipótesis, elemento nuevo propuesto, decisión pendiente del usuario e información insuficiente. La respuesta se identifica como contenido generado. Una referencia que la aplicación no pueda asociar a un elemento se marca como no contrastada; no se presenta como hecho verificado. El mismo nombre en dos ámbitos no basta para identificar un elemento.

La revisión de calidad comprueba que no se inventen ensayos o resultados, que un vínculo no se use como prueba de cumplimiento físico y que una sospecha en texto libre no se convierta en infracción determinista. Estas comprobaciones no se presuponen garantizadas por el modelo generativo: se registran en la evaluación humana y, en el caso de referencias a elementos, en la validación de la aplicación.

### C-COMP. Correspondencia entre ejecuciones

La clave de un hallazgo incluye regla y versión, elemento identificado y contexto de aplicación. Se utiliza el ID persistente del elemento si está disponible. Si no lo está, se utiliza tipo y nombre cualificado dentro del modelo. Un cambio de nombre sin ID persistente no se empareja por parecido textual.

| Clasificación | Condición |
|---|---|
| Persistente | La misma clave tiene un hallazgo en ambas ejecuciones. La variación de evidencia se muestra como detalle. |
| Resuelto | La comprobación correspondiente se puede emparejar y pasa de incumple a cumple con la misma versión de regla y las mismas políticas relevantes. |
| Nuevo | Existe un incumplimiento actual sin incumplimiento previo y hay evidencia de que antes cumplía o de que el elemento es una incorporación nueva identificable. |
| Correspondencia indeterminada | No puede emparejarse el elemento, cambia la regla o política relevante, falta cobertura, la regla está desactivada, desaparece el elemento o no se demuestra una de las condiciones anteriores. |

Una ausencia en la lista de avisos no demuestra que el defecto esté corregido. Las limitaciones informativas se comparan por su clave y motivo; su desaparición se marca como cobertura recuperada únicamente si la nueva ejecución permite comprobarlo.

### C-SAL. Exportaciones

El informe HTML incluye identidad de revisión y ejecución, configuración, resumen, hallazgos, evidencias, motivos de no evaluación, fallos y límites de cobertura. Se comprueba en el navegador de referencia indicado en el manual de la entrega. La inspección visual comprueba que el texto se puede leer completo y que las tablas no superponen ni ocultan sus datos.

El JSON contiene una versión de esquema y bloques de metadatos de ejecución, resultados, hallazgos, fallos y cobertura. Una lista de hallazgos vacía no elimina los demás bloques. Los campos mínimos son los de C-RES y las entradas y versiones descritas en RNF-01. El esquema JSON formal y un ejemplo de cada estado se entregarán con la implementación y se usarán en sus pruebas de aceptación.

### C-REP. Comparación de resultados repetidos

Para comparar dos ejecuciones se excluyen sus ID particulares y marcas de fecha y hora. Se comparan regla y versión, identidad de origen de elementos, estado, motivos, parámetros y valores de evidencia. Los mapas se comparan sin considerar el orden de sus claves. Las colecciones que representan conjuntos se ordenan por identidad; las secuencias cuyo orden tenga significado lo conservan. El esquema de resultados declara cuáles son conjuntos y cuáles secuencias. Los ID internos generados se sustituyen por sus referencias de origen para esta comparación.

## 6. Catálogo inicial

Las fichas de estas reglas cumplen C-REG. «Ámbito evaluable» tiene el significado del apartado 3 y C-ENT. Fuera del tipo o contexto sujeto a una regla, el resultado es no aplicable. Si la regla es pertinente y falta un dato necesario, es no evaluable con motivo.

| ID | Condición comprobada | Resultado desfavorable y evidencia | Ejemplos de verificación |
|---|---|---|---|
| E01 | Cada referencia admitida apunta a un destino resoluble. | Destino inválido demostrado: incumple y error, con referencia y ámbito. Dependencia ausente o causa indeterminada: no evaluable. | Destino válido, inexistente y dependencia ausente. |
| E02 | Cada relación interpretada tiene los extremos obligatorios de su categoría. | Incumple y error, con relación, categoría y extremo ausente. Si el analizador no entrega la relación, se registra diagnóstico de entrada. | Relación completa, incompleta representable y rechazada en lectura. |
| E03 | Cada extremo interpretado pertenece a una categoría permitida por la tabla del catálogo. | Incumple y error, con categorías observada y esperada. Destino no resuelto: no evaluable. | Categoría permitida, prohibida y extremo no resuelto. |
| E04 | Cada identificador sujeto a unicidad es único en el ámbito declarado. | Incumple y error, con identificador, ámbito y elementos. Un nombre repetido permitido no es una colisión. | Duplicación prohibida y nombres iguales permitidos en ámbitos distintos. |
| E05 | Cada tipo necesario para una operación admitida puede resolverse. | Tipo inválido demostrado: incumple y error. Dependencia ausente o causa desconocida: no evaluable. | Tipo válido, inexistente y dependencia ausente. |
| T01 | Cada requisito sujeto a la política tiene al menos un vínculo explícito de satisfacción. | Incumple y advertencia, con requisito, política y recuento cero en ámbito evaluable. | Con vínculo, sin vínculo y ámbito incompleto. |
| T02 | Cada requisito sujeto a la política tiene al menos un vínculo explícito con un caso de verificación. | Incumple y advertencia, con requisito, política y recuento cero. Un vínculo no resuelto impide afirmar ausencia. | Caso vinculado, ausencia y destino no resuelto. |
| T03 | Cada caso de verificación sujeto a la política tiene al menos un requisito vinculado. | Incumple y advertencia, con caso, política y recuento cero. Ámbito incompleto: no evaluable. | Caso vinculado, huérfano y destino no resuelto. |
| P01 | Cada elemento sujeto a una política de propiedades contiene las propiedades requeridas para su tipo. | Incumple y advertencia, con elemento, política y propiedades ausentes. Se comprueba presencia, no valor numérico. | Propiedad presente, ausente y tipo sin política. |
| P02 | Cada componente sujeto a la política tiene al menos una conexión representada. | Incumple y advertencia, con componente, política y recuento cero en ámbito evaluable. | Conectado, aislado sujeto a política y tipo sin política. |

E05 es una comprobación especializada de tipos; si coincide con E01 en una misma referencia, sus hallazgos compartirán la identificación del defecto de origen. No se contarán como dos defectos distintos en el estudio. En P02 se cuentan las conexiones interpretadas que incluyen al componente o a uno de sus extremos reconocidos, según la tabla de relaciones del catálogo; no se exige conexión a cualquier componente por defecto.

## 7. Requisitos no funcionales

| ID | Requisito | Descripción | Módulo | Criterio de verificación |
|---|---|---|---|---|
| RNF-01 | Con las mismas entradas y configuración, el motor deberá producir los mismos estados y evidencias conforme a C-REP. | Las entradas incluyen archivos, dependencias, versiones de analizador, adaptador, motor y catálogo, perfil y parámetros. Se excluye el texto generado por IA. | Motor | Repetir una ejecución y comparar según C-REP; cambiar un parámetro y comprobar que la configuración se distingue. |
| RNF-02 | La aplicación deberá conservar en cada resultado las identidades de ejecución, regla y elemento o contexto de origen. | Se conservan también archivo y posición cuando procedan del analizador. | Resultados | Seguir resultados de dos revisiones hasta sus entradas y elementos; comprobar que las referencias no se mezclan. |
| RNF-03 | La aplicación deberá conservar los mismos estados, motivos y datos de cobertura de una ejecución en pantalla, HTML y JSON. | La redacción de presentación puede variar sin alterar los datos ni convertir limitaciones en cumplimiento. | Resultados | Comparar las tres salidas para una ejecución parcial con un fallo y una regla no evaluable. |

## 8. Evaluación del proyecto

Estos criterios corresponden al estudio y a la documentación del proyecto. No obligan a incorporar funciones para gestionar participantes dentro de la aplicación.

| ID | Criterio | Verificación |
|---|---|---|
| EV-01 | El equipo documentará seis trabajos, incluidos tres artículos y una herramienta, consultando dos bases bibliográficas y comprobando sus DOI o URL. | Revisar búsquedas, referencias y comparación. |
| EV-02 | El equipo preparará ejemplos correctos y defectuosos de cada regla, más los casos de no evaluación y no aplicación indicados en el catálogo. | Comprobar el conjunto etiquetado y ejecutar las pruebas de cada regla. |
| EV-03 | El equipo comparará revisión manual y asistida con al menos cuatro personas y dos versiones comparables del dron. | Mantener instrucciones comunes y alternar orden y versión asignada. |
| EV-04 | La mediana del tiempo con la herramienta será como máximo el 70 % de la mediana manual. | Registrar los tiempos y las tareas incompletas con el protocolo previo al ensayo. |
| EV-05 | La sensibilidad será al menos del 85 % sobre los defectos conocidos detectables por el catálogo fijado para el ensayo. | Dividir defectos correctamente detectados entre defectos conocidos detectables. Publicar el denominador y las exclusiones. |
| EV-06 | La proporción de avisos falsos será como máximo del 10 %. | Dividir avisos sin defecto correspondiente entre el total de avisos, siguiendo el criterio de duplicados del protocolo. Sin avisos, la proporción queda no definida. |
| EV-07 | El equipo evaluará cada explicación de la muestra por fidelidad, claridad y utilidad. | Registrar por dimensión «satisface», «necesita revisión» o «no valorable», con una justificación. |

Para EV-07, fidelidad significa que las afirmaciones se apoyan en la evidencia o se identifican como hipótesis. Claridad significa que se reconocen problema, elemento y motivo sin ambigüedad detectada por el revisor. Utilidad significa que se identifica una actuación posible o el dato que falta, sin inventar información. Se registran estas dimensiones por separado, junto con las cuatro preguntas de C-IA; no se deduce la calidad de las explicaciones a partir de la rapidez del usuario.

Antes del ensayo se publicará un protocolo con estos datos:

- Versiones de modelos, reglas y configuración congeladas para la prueba.
- Defectos conocidos, ubicación y regla esperada, fijados antes de ejecutar la herramienta.
- Distribución de tipos y número de defectos en ambas versiones del dron y criterio de dificultad utilizado para hacerlas comparables.
- Unidad de tarea, evento de inicio, evento de finalización y límite de tiempo si se utiliza.
- Tratamiento de abandonos, defectos no encontrados y tareas incompletas; una terminación rápida sin localizar correctamente no cuenta como éxito.
- Correspondencia entre aviso y defecto y tratamiento de avisos duplicados.
- Revisores, instrucciones, asignación de versiones y orden, sin publicar nombres personales en los resultados.

La sensibilidad del detector se calculará sobre la verdad de referencia; las detecciones correctas realizadas por las personas se registrarán además para interpretar la comparación de tiempos. Las reglas o dependencias no evaluables se comunicarán como limitaciones y no se excluirán del conjunto de defectos fijado a posteriori para mejorar las métricas.

Si no se alcanza cualquiera de EV-04, EV-05 o EV-06, la hipótesis no queda confirmada. Si faltan datos para calcular una métrica, se comunica que no puede evaluarse. Las conclusiones se limitan a los modelos y participantes estudiados.

## 9. Documentos de diseño y aceptación

El diseño seleccionará el analizador, las bibliotecas de interfaz y el servicio de IA. Antes de aceptar la implementación se entregarán la declaración de entrada de C-ENT, las fichas y tablas de C-REG, el esquema JSON de C-SAL, el manual con navegador de referencia y el protocolo de evaluación del apartado 8.

Estos documentos concretan la implementación y sus pruebas sin ampliar el alcance descrito aquí. Si una dependencia no permite cumplir una capacidad exigida, se resolverá su integración o se revisará explícitamente el alcance antes de declarar el requisito satisfecho.
