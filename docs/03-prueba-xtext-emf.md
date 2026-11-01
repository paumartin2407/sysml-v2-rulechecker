# Prueba de lectura y resolución con Xtext/EMF

**Fecha:** 01/11/2026. **Resultado:** capacidades demostradas para los ejemplos; decisión condicionada para E01 y T02. Esta prueba continúa la [exploración anterior](02-prueba-analizador.md).

## Configuración reproducible

Se ha usado el mismo JDK Temurin 21.0.13+9 y la implementación piloto 2026-08, commit `692170b71867353b8f90341e61556f49a5beb0e5`. El ZIP oficial `jupyter-sysml-kernel-0.62.0.zip` tiene SHA-256 `5a015ed3f2b3d2dae14e9c3fb9602d9e1fef5f9ce33cf396c422329405cc3cb2`. Contiene el JAR y las bibliotecas. Hay que [descargarlo de la versión oficial](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases/tag/2026-08) y descomprimirlo; no se incluyen sus binarios en este repositorio.

Con Python 3 y JDK 21, desde la raíz del repositorio:

```powershell
python prototipo/xtext-emf/ejecutar.py --jar "C:/ruta/sysml/jupyter-sysml-kernel-0.62.0-all.jar" --biblioteca "C:/ruta/sysml/sysml.library" --salida resultado-xtext.txt
```

Si el JDK no está en el PATH, añadir `--java "C:/ruta/jdk/bin/java.exe" --javac "C:/ruta/jdk/bin/javac.exe"`. El script compila `Probe.java` en un directorio temporal dentro del directorio actual, ejecuta cinco casos y devuelve código 0 solo si se cumplen las comprobaciones fijadas; 1 indica que alguna ha fallado y 2 que no se ha podido compilar. `--salida` es opcional y escribe el informe de la ejecución. La ejecución observada se conserva en `prototipo/xtext-emf/salida-observada.txt`.

La prueba carga e indexa 94 archivos `.kerml` y `.sysml` de la biblioteca distribuida. Se construyen URI con `Path.toUri()` y `URI.createURI()`, evitando la doble codificación de espacios observada en la utilidad anterior. Se cargan todos los archivos de cada caso en el mismo conjunto de recursos y se indexan antes de validar. Los diagnósticos de entrada usan `IResourceValidator` con `CheckMode.ALL`; los elementos y las relaciones se recorren mediante EMF y las posiciones se obtienen de Xtext. No se ha validado individualmente la corrección de todos los archivos de biblioteca.

## Casos y observaciones

| Caso | Observación de esta ejecución |
|---|---|
| `valido` | Sin errores de validación en el archivo. Se reconocen `dron`, `autonomia` y `pruebaAutonomia`. `SatisfyRequirementUsage` resuelve `Dron::autonomia` y `Dron::dron`; `RequirementVerificationMembership` resuelve el mismo requisito y su caso contenedor. |
| `multifichero` | Sin errores en los dos archivos. Satisfacción y verificación resuelven `ModeloDron::autonomia`; satisfacción resuelve también `ModeloDron::dron`. El caso de verificación está en el segundo archivo. |
| `invalido` | Diagnóstico de enlace en `dron.sysml`, línea 4, columna 26, para `dronInexistente`; el extremo es un proxy no resuelto. Hay además una advertencia de conformidad de tipos. El vínculo de verificación independiente sí se resuelve. |
| `dependencia-ausente` | En `ensayo.sysml`, Xtext comunica en 2:20 que no resuelve el espacio de nombres `ModeloDron` y señala las tres referencias afectadas; aparecen además diagnósticos derivados. El destino de verificación queda sin resolver. |
| `sin-verificacion` | Control adicional: el requisito y el caso se reconocen sin errores, pero no hay ninguna relación de verificación en el recurso. |

**Corrección de la prueba anterior:** el caso multifichero previo usaba `import` sin `private` o `public`; el parser lo rechazaba. Los ejemplos de esta segunda prueba usan `private import ModeloDron::*;` en ambos escenarios y se han validado. Por tanto, la falta del objeto de satisfacción en la exportación anterior no demuestra una limitación del piloto para relaciones entre archivos.

En los diagnósticos se registran archivo, severidad, código, línea, columna y mensaje. Para elementos y relaciones, la prueba registra el archivo, la línea inicial y el desplazamiento Xtext; la posición no debe inventarse si falta el nodo. Los extremos semánticos se consultan mediante `getSatisfiedRequirement()`, `getSatisfyingFeature()` y `getVerifiedRequirement()`; el caso se obtiene buscando el `VerificationCaseUsage` contenedor. `null` y los proxies no resueltos no se tratan como destinos válidos. El aviso de Log4j se debe a la ausencia de configuración de logging en esta ejecución; no es un diagnóstico del modelo.

## Decisión sobre E01 y T02

- **E01: evaluable de forma condicionada.** El analizador resuelve los ejemplos correctos y produce diagnósticos localizados de referencias sin resolver. El adaptador aún debe relacionar cada diagnóstico con su comprobación y demostrar que el conjunto de archivos y dependencias del ámbito está completo antes de afirmar que el destino es inválido. El analizador no distingue automáticamente una dependencia ausente de un nombre erróneo: sin evidencia suficiente, corresponde **no evaluable**, no incumple. Las distintas categorías de referencia de E01 todavía no se han probado.
- **T02: evaluable de forma condicionada** para el vínculo explícito `objective { verify ...; }` de estos ejemplos. Se obtiene el requisito referido y el caso de verificación contenedor, incluso entre dos archivos; el control sin vínculo muestra que se puede detectar la ausencia en este conjunto completo y sin errores. Una referencia sin resolver o un ámbito incompleto impide concluir ausencia y debe dar **no evaluable**. Faltan la política que decide qué requisitos están sujetos a T02, otras formas de vínculo y pruebas de cobertura del ámbito.

Se recomienda continuar con un adaptador experimental sobre Xtext/EMF y esta versión fijada. Estos resultados prueban capacidades sobre un subconjunto pequeño; **no implementan aún E01 ni T02** y no garantizan cobertura general de SysML v2, estabilidad de identificadores o ejecución parcial segura ante todos los errores. El siguiente paso es definir el contrato del adaptador, la identidad de los elementos y la política de completitud, y añadir casos positivos, negativos y no evaluables a las fichas de ambas reglas.
