"""Apply Curator-checked Markdown proposals; citation_fix owns all sidecar writes."""
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = HERE.parents[2]
CODE = MEM.parent / "260928-mik-l26"

def symbol_span(path, name):
    data = (CODE / path).read_text()
    if path.endswith(".py"):
        tree = ast.parse(data)
        matches = []
        def visit(nodes, prefix=""):
            for node in nodes:
                if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    qualified = prefix + node.name
                    if qualified == name:
                        matches.append((node.lineno, node.end_lineno))
                    visit(node.body, qualified + ".")
                elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.TypeAlias)):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else [node.name]
                    if any(isinstance(t, ast.Name) and prefix + t.id == name for t in targets):
                        matches.append((node.lineno, node.end_lineno))
        visit(tree.body)
        if len(matches) != 1:
            raise ValueError(f"{path}::{name} binds {len(matches)} definitions")
        return matches[0]
    # Non-Python targets must retain their inspected explicit source range.
    raise ValueError(f"No Python symbol span for {path}::{name}; author an inspected line range")

def card_path(row):
    if row.get("markdownPath"):
        return Path(row["markdownPath"]).resolve()
    path = row["card"]
    return MEM / (path if path.startswith("onboarding/") else "onboarding/" + path)

def evidence_table(update):
    anchors, sources = [], []
    for target in update["targets"]:
        path, symbol = target["path"], target.get("symbol")
        if symbol and path.endswith(".py"):
            start, end = symbol_span(path, symbol)
            anchors.append("`" + symbol + "`")
            sources.append(f"{path}:{start}-{end}")
        elif symbol:
            line = target.get("line")
            if not line or symbol not in (CODE / path).read_text().splitlines()[line - 1]:
                raise ValueError(f"Unverified non-Python target {target}")
            anchors.append("`" + symbol + "`")
            sources.append(f"{path}:{line}-{target.get('endLine', line)}")
        elif target.get("startLine"):
            start, end = target["startLine"], target.get("endLine", target["startLine"])
            sources.append(f"{path}:{start}-{end}")
        else:
            if not (CODE / path).is_file():
                raise ValueError(f"Missing target {path}")
            sources.append(path)
    note = update["note"].replace("|", "\\|")
    return "\n| Finding | Anchor | Source |\n| --- | --- | --- |\n| " + note + " [" + str(update["number"]) + "] | " + "; ".join(anchors) + " | " + "; ".join(sources) + " |\n"

def prepare(row):
    path = card_path(row)
    before = path.read_text()
    text = before
    for item in row.get("replacements", []):
        expected = item.get("expectedOccurrences", 1)
        if text.count(item["old"]) != expected:
            raise ValueError(f"{path}: old paragraph matches {text.count(item['old'])}, expected {expected}")
        text = text.replace(item["old"], item["new"])
    updates = {str(r["number"]): r for r in row.get("referenceUpdates", [])}
    retired = {str(n) for n in row.get("retiredReferenceNumbers", [])}
    if set(updates) & retired:
        raise ValueError(f"{path}: reference both updated and retired")
    found = set()
    output = []
    for line in text.splitlines(keepends=True):
        m = re.match(r"^\s*[-*+]\s+.*?\[(\d+)\]\s*$", line.rstrip("\n"))
        number = m.group(1) if m else None
        if number in updates:
            if number in found:
                output.append(re.sub(r"\s*\[" + number + r"\]\s*$", "", line.rstrip("\n")) + "\n")
            else:
                found.add(number)
                output.append(evidence_table(updates[number]) + "\n")
        elif number in retired:
            found.add(number)
        else:
            output.append(line)
    missing = set(updates) - found
    if missing:
        # Overview claims may cite a number inline. Author one explicit evidence row,
        # preserving those current inline claims rather than silently repointing them.
        for number in sorted(missing, key=int):
            if not re.search(r"\[" + re.escape(number) + r"\]", text):
                raise ValueError(f"{path}: no body citation for reference [{number}]")
        output.append("\n" + ("## Evidence\n\n" if "## Evidence" not in text else ""))
        output.extend(evidence_table(updates[number]) + "\n" for number in sorted(missing, key=int))
    text = "".join(output)
    for number in retired:
        if re.search(r"\[" + re.escape(number) + r"\]", text):
            raise ValueError(f"{path}: retired reference [{number}] still cited in body")
    return path, before, text

document = json.loads(Path(sys.argv[1]).read_text())
rows = document.get("rows", document.get("proposals"))
prepared, errors = [], []
for row in rows:
    try:
        prepared.append((*prepare(row), row))
    except (ValueError, KeyError, SyntaxError, OSError) as error:
        errors.append(str(error))
report = {"source": sys.argv[1], "errors": errors, "cards": []}
for path, before, after, row in prepared:
    report["cards"].append({"card": str(path.relative_to(MEM)), "changed": before != after,
        "beforeSha256": hashlib.sha256(before.encode()).hexdigest(),
        "afterSha256": hashlib.sha256(after.encode()).hexdigest(),
        "bodyReplacements": len(row.get("replacements", [])), "updatedReferences": len(row.get("referenceUpdates", [])),
        "retiredReferences": row.get("retiredReferenceNumbers", [])})
if "--apply" in sys.argv:
    if errors:
        raise SystemExit(json.dumps(report, indent=2))
    for path, before, after, row in prepared:
        if before != after:
            path.write_text(after)
report["applied"] = "--apply" in sys.argv and not errors
(HERE / (Path(sys.argv[1]).stem + ".apply-result.json")).write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"errors": errors, "cards": len(prepared), "changed": sum(before != after for _, before, after, _ in prepared), "applied": report["applied"]}, indent=2))
