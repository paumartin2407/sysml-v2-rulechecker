import argparse
from pathlib import Path
import os
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description="Prueba Xtext/EMF de la implementación piloto 2026-08")
p.add_argument("--jar", required=True, help="JAR oficial 0.62.0-all")
p.add_argument("--biblioteca", required=True, help="Directorio sysml.library de la distribución 0.62.0")
p.add_argument("--java", default="java")
p.add_argument("--javac", default="javac")
p.add_argument("--salida", help="Guardar el informe en UTF-8")
a = p.parse_args()
jar, biblioteca = Path(a.jar).resolve(strict=True), Path(a.biblioteca).resolve(strict=True)
if not biblioteca.is_dir(): p.error("La biblioteca debe ser un directorio")
report = []
def log(line=""):
    print(line)
    report.append(line)
def run(cmd):
    return subprocess.run(cmd, text=True, encoding="utf-8", errors="replace", capture_output=True)
with tempfile.TemporaryDirectory(prefix="sysml-xtext-", dir=".") as temp:
    compile_result = run([a.javac, "-encoding", "UTF-8", "-cp", str(jar), "-d", temp, str(HERE / "Probe.java")])
    if compile_result.returncode:
        print(compile_result.stderr, file=sys.stderr); sys.exit(2)
    failed = False
    for case in ("valido", "multifichero", "invalido", "dependencia-ausente", "sin-verificacion"):
        cmd = [a.java, "-Xmx2g", "-cp", temp + os.pathsep + str(jar), "Probe", str(biblioteca), str(HERE / "casos" / case)]
        r = run(cmd)
        out = r.stdout
        log("=== " + case + " ===")
        log(out.rstrip())
        if r.stderr: log("STDERR: " + r.stderr.strip())
        checks = [r.returncode == 0, "LIBRARY=94" in out]
        if case == "valido":
            checks += ["ISSUE=ERROR|" not in out, "SAT=RequirementUsage:Dron::autonomia|PartUsage:Dron::dron" in out,
                       "VERIFY=RequirementUsage:Dron::autonomia|case=VerificationCaseUsage:Dron::pruebaAutonomia" in out]
        elif case == "multifichero":
            checks += ["ISSUE=ERROR|" not in out, "SAT=RequirementUsage:ModeloDron::autonomia|PartUsage:ModeloDron::dron" in out,
                       "VERIFY=RequirementUsage:ModeloDron::autonomia|case=VerificationCaseUsage:EnsayoDron::pruebaAutonomia" in out]
        elif case == "invalido":
            checks += ["Diagnostic.Linking|4:26|" in out, "dronInexistente" in out, "|PROXY|" in out,
                       "VERIFY=RequirementUsage:Dron::autonomia|case=VerificationCaseUsage:Dron::pruebaAutonomia" in out]
        elif case == "dependencia-ausente":
            checks += ["Diagnostic.Linking|2:20|" in out, "Namespace 'ModeloDron'" in out,
                       "Diagnostic.Linking|4:55|" in out, "VERIFY=RequirementUsage:null|" in out]
        else:
            checks += ["ISSUE=ERROR|" not in out, "ELEMENT=RequirementUsage|autonomia" in out, "VERIFY=" not in out]
        ok = all(checks)
        log("COMPROBACION=" + ("OK" if ok else "FALLO"))
        if not ok: failed = True
    if a.salida: Path(a.salida).write_text("\n".join(report) + "\n", encoding="utf-8")
    sys.exit(1 if failed else 0)

