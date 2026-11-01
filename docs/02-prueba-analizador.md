# Prueba exploratoria del analizador SysML v2

**Estado: parcial; no se ha validado todavía la lectura semántica completa ni seleccionado definitivamente un adaptador.** Fecha: 01/11/2026.

## Objetivo y preparación

Evaluar la implementación piloto con un dron mínimo y comparar un archivo, dos archivos, una referencia inválida y una dependencia ausente. Los ejemplos y el script están en `prototipo/`; sus resultados esperados son observaciones de la prueba, no una afirmación de validez del modelo.

Se ha usado la [implementación piloto 2026-08](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases/tag/2026-08), commit `692170b71867353b8f90341e61556f49a5beb0e5`, paquete oficial `jupyter-sysml-kernel-0.62.0.zip` (SHA-256 `5a015ed3f2b3d2dae14e9c3fb9602d9e1fef5f9ce33cf396c422329405cc3cb2`), con Temurin JDK 21.0.13+9 en Windows. Se invoca `org.omg.sysml.xtext.util.SysML2JSON` del JAR incluido. No se ha usado la API de servicios.

Descargar y descomprimir el ZIP oficial de esa versión. Desde la raíz del repositorio, ejecutar:

```powershell
python prototipo/explorar.py --jar "C:/ruta/sysml/jupyter-sysml-kernel-0.62.0-all.jar"
```

Si Java no está en el PATH de la sesión, añadir `--java "C:/ruta/al/jdk/bin/java.exe"`. La opción `--biblioteca "C:/ruta/sysml/sysml.library"` intenta cargar la biblioteca estándar. Se necesita Python 3. El script utiliza un directorio temporal, imprime la salida y elimina sus archivos temporales. Las identificaciones y el orden pueden variar. No se guardan los JAR ni bibliotecas en el repositorio.

## Resultados observados

| Caso | Esperado de la prueba | Observado sin biblioteca estándar |
|---|---|---|
| `valido` | Componente, requisito, satisfacción y verificación reconocibles. | Se exportan `PartUsage` dron, `RequirementUsage` autonomia, `VerificationCaseUsage` pruebaAutonomia, `SatisfyRequirementUsage` y `RequirementVerificationMembership`. No se ha demostrado la resolución correcta de todos los extremos. |
| `multifichero` | Cargar ambos archivos y resolver los vínculos entre ellos. | Se exportan el componente, el requisito, el caso y referencias, pero no aparece `SatisfyRequirementUsage` en el JSON. La resolución entre archivos queda sin demostrar. |
| `invalido` | Diagnóstico localizable para un destino inexistente. | La exportación termina con `NullPointerException`, sin JSON ni diagnóstico útil; el proceso no comunica necesariamente el fallo mediante su código de salida. |
| `dependencia-ausente` | Diagnóstico de dependencia ausente y no evaluable cuando corresponda. | Se exportan referencias y un caso, pero no se observa un diagnóstico que clasifique la ausencia. No se puede concluir que el destino sea inválido. |

El JSON incluye identificadores y algunos campos `source`/`target` en relaciones, pero no se ha demostrado que todos correspondan a los extremos semánticos requeridos por E01 y T02; tampoco se ha obtenido ubicación en el archivo. Los objetos y referencias obtenidos sin las bibliotecas estándar no prueban que los modelos sean semánticamente válidos. El texto observado de una ejecución está en `prototipo/salida-observada.txt`.

Al intentar cargar `sysml.library` mediante esta utilidad en Windows, se produjo `FileNotFoundException` con un segmento como `Domain%20Libraries` o `Kernel%20Libraries`, aunque los directorios originales contienen espacios. Es una observación de esta forma de ejecución, no una conclusión sobre todos los modos de uso de la implementación piloto.

## Decisión y límites

Mantener la implementación piloto como candidata, **sin adoptarla todavía como adaptador**. La exportación directa muestra que es posible recuperar tipos y nombres, pero no satisface aún las necesidades de resolución, diagnósticos, ubicación y análisis parcial. La salida JSON o la mera ausencia de una relación no autorizan un veredicto de regla.

El siguiente experimento debe cargar correctamente las bibliotecas y usar la API de Xtext/EMF para obtener diagnósticos y posiciones, comprobar enlaces semánticos de satisfacción y verificación y repetir los cuatro casos. Solo entonces se podrá decidir si E01 y T02 son evaluables; una dependencia sin resolver debe permanecer no evaluable salvo evidencia suficiente para otra clasificación.
