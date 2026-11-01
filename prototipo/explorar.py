import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

parser = argparse.ArgumentParser(description="Explora la exportación JSON del piloto; no valida SysML.")
parser.add_argument("--jar", required=True, help="Ruta al JAR oficial 0.62.0-all")
parser.add_argument("--java", default="java", help="Ruta de java.exe")
parser.add_argument("--biblioteca", help="Ruta opcional a sysml.library")
args = parser.parse_args()
jar = str(Path(args.jar).resolve(strict=True))
java = args.java
if Path(java).exists(): java = str(Path(java).resolve())
cases = Path(__file__).resolve().parent / "casos"
with tempfile.TemporaryDirectory(prefix="sysmlprobe_", dir=".") as work:
    work = Path(work)
    for case in sorted(cases.iterdir()):
        if not case.is_dir(): continue
        source = work / case.name
        shutil.copytree(case, source)
        cmd = [java, "-cp", jar, "org.omg.sysml.xtext.util.SysML2JSON", str(source)]
        if args.biblioteca: cmd.append(str(Path(args.biblioteca).resolve()))
        run = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print("\n===", case.name, "===")
        print((run.stdout + run.stderr).strip())
        output = Path(str(source) + ".json")
        if not output.exists():
            print("No se produjo JSON; el código de salida no garantiza éxito.")
            continue
        try:
            payloads = [x["payload"] for x in json.loads(output.read_text(encoding="utf-8"))]
        except (ValueError, KeyError) as e:
            print("JSON no interpretable:", e); continue
        for x in payloads:
            t, n = x.get("@type"), x.get("declaredName")
            if t in ("SatisfyRequirementUsage", "RequirementVerificationMembership", "VerificationCaseUsage", "PartUsage") or n in ("autonomia", "dron", "pruebaAutonomia"):
                print("elemento", t, repr(n), "extremos", {k:x[k] for k in ("source","target") if k in x})
        print("Total:",len(payloads),"objetos; los identificadores pueden variar entre ejecuciones.")
