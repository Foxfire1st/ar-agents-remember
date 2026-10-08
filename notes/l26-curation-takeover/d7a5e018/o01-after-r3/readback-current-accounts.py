"""Read exact existing O01 populations; write evidence only in this memory root."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess

GROUP = Path(__file__).resolve().parents[5]
MEMORY = GROUP / "memory-260928-mik-l26"
CODE = GROUP / "260928-mik-l26"
OUT = Path(__file__).parent
FIX3 = OUT.parent / "fix3"
R3 = GROUP / "task-reports/role-launch/260928-MIK-L26-reviewer-c90c02de-94e9-45be-bd5a-dd61c880a014.memory-r3.evidence"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def load(path):
    return json.loads(path.read_text())

def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def index(repo):
    path = subprocess.check_output(["git", "rev-parse", "--git-path", "index"], cwd=repo, text=True).strip()
    path = Path(path) if Path(path).is_absolute() else repo / path
    return {"raw": digest(path.read_bytes()), "stageNul": digest(subprocess.check_output(["git", "ls-files", "--stage", "-z"], cwd=repo))}

indices_before = {"code": index(CODE), "memory": index(MEMORY)}
plan = load(OUT / "21-card-authored-plan.json")
by_source = {r["source"]: r for r in plan["rows"]}
readback = []
for row in plan["rows"]:
    source = CODE / row["source"]
    assert digest(source.read_bytes()) == row["sourceSha256"], row["source"]
    card = MEMORY / row["card"]
    body = card.read_text()
    assert row["authoredPurpose"] in body and row["authoredReconciliation"] in body
    side = load(MEMORY / (row["card"][:-3] + ".json"))
    declared = set(side["references"])
    cited = set(re.findall(r"\[(\d+)\]", body))
    assert cited == declared, (card, cited, declared)
    references = []
    for number, reference in side["references"].items():
        for target in reference["targets"]:
            anchor = target["anchor"]
            path = anchor.get("path", side["path"])
            data = (CODE / path).read_bytes()
            blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            assert blob == anchor["blob"], (path, number, "blob")
            lines = data.decode().splitlines(keepends=True)
            locator = anchor["locator"]
            if locator["kind"] == "symbol":
                nodes = [n for n in ast.walk(ast.parse(data)) if getattr(n, "name", None) == locator["name"]]
                assert nodes, (path, locator)
                ranges = [(min([n.lineno] + [d.lineno for d in getattr(n, "decorator_list", [])]), n.end_lineno) for n in nodes]
            else:
                assert locator["kind"] == "line_range", locator
                ranges = [(locator["start"], locator["end"])]
            assert all(1 <= start <= end <= len(lines) for start, end in ranges)
            excerpts = ["".join(lines[start - 1:end]) for start, end in ranges]
            hashes = [digest(s.encode()) for s in excerpts]
            assert anchor["content"] in ["sha256:" + h for h in hashes], (path, number, ranges, hashes, anchor["content"])
            references.append({"number": number, "note": reference["note"], "sourcePath": path, "locator": locator, "ranges": ranges, "sourceBlob": blob, "sourceSha256": digest(data), "excerpts": excerpts, "resolvedContentDigests": hashes})
    readback.append({"card": row["card"], "source": row["source"], "sealedR3Criterion": row["sealedR3Criterion"], "sourceSha256": digest(source.read_bytes()), "cardSha256": digest(card.read_bytes()), "sidecarSha256": digest((MEMORY / (row["card"][:-3] + ".json")).read_bytes()), "currentCard": body, "references": references, "curatorReconciliation": row["authoredReconciliation"], "independentAcceptance": False})

old_shared = load(FIX3 / "source87-coherence-shared74-evidence.json")
reviewed = load(R3 / "shared74-individual-applicability-adjudications.json")
review_by_path = {r["sourceFile"]: r for r in reviewed["rows"]}
catalog_reasons = {
    "mcp/tests/evidence-lifecycle.toml": "The actual incoming delta adds master-retirement and abandoned-row consumers to existing artifact lists. The current card retains contract/artifact ownership and consumer declarations and names those new consumers. The data declares ownership; it executes no contract, adds no knowledge identity, and supplies no lane table.",
    "mcp/tests/test-evidence-lanes.toml": "The actual incoming delta assigns abandoned-series and refusal-wording modules to unit-regression and master-retirement/readiness/state-machine/abandoned-row modules to integration. The current card describes one lane per current module and expressly separates lane registration from collection and execution. The parsed incoming lists, not an old source-tree assertion, carry that membership evidence.",
}
shared_rows = []
for ordinal, old in enumerate(old_shared["rows"], 1):
    path = old["sourceFile"]
    source = (CODE / path).read_text()
    card_path = MEMORY / "onboarding" / old["onboardingFile"]
    card = card_path.read_text()
    prior = review_by_path[path]
    source_same = digest(source.encode()) == old["sourceSHA256"]
    card_same = digest(card.encode()) == old["cardSHA256"]
    if path in by_source:
        authored = by_source[path]
        reason = authored["authoredPurpose"] + " " + authored["authoredReconciliation"]
        action = "existing-O01-current-account-corrected"
        assert not prior["reconciledDispositionSupported"]
    elif path in catalog_reasons:
        reason = catalog_reasons[path]
        action = "incoming-Source41-declarations-read-with-retained-card"
        assert prior["reconciledDispositionSupported"]
    else:
        assert source_same and card_same, path
        assert prior["reconciledDispositionSupported"], path
        reason = old["rationale"].replace("held Source87 source", "completed Source41 leaf source")
        action = "exact-paired-bytes-preserved-from-supported-R3-account"
    why = (f"Shared row {ordinal} contains the whole actual {path} source and its own {old['onboardingFile']} companion card, with their individually measured digests. "
           f"The row's reconciliation is about this source/card pair: {reason} "
           "This makes the shared file evidence for this individual judgment; a deletion hunk or a shared count alone is insufficient. Static definitions and fixture relationships do not establish execution or semantic acceptance.")
    shared_rows.append({"ordinal": ordinal, "classification": old["classification"], "onboardingFile": old["onboardingFile"], "sourceFile": path,
                        "card": card, "cardSHA256": digest(card.encode()), "source": source, "sourceSHA256": digest(source.encode()),
                        "rationale": reason, "whyEvidenceApplies": why, "action": action,
                        "sameSourceBytesAsR3": source_same, "sameCardBytesAsR3": card_same,
                        "sealedR3Account": {"adjudicationSupported": prior["reconciledDispositionSupported"], "reason": prior["reviewerReason"]}, "independentAcceptance": False})
assert len(shared_rows) == 74
save("source41-coherence-shared74-evidence.json", {"schema": "l26-per-judgment-shared-evidence/v1", "sourceHead": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=CODE, text=True).strip(), "codeTree": None,
     "codeTreeState": "awaiting-qualified-whole-Worker-envelope-and-Owner-production-binding", "original74Population": True,
     "predecessor": {"path": "notes/l26-curation-takeover/d7a5e018/fix3/source87-coherence-shared74-evidence.json", "sha256": digest((FIX3 / "source87-coherence-shared74-evidence.json").read_bytes())}, "rows": shared_rows})

original84 = load(R3 / "o01-original84-individual-adjudications.json")
prior84 = {r["sourcePath"]: r for r in load(FIX3 / "source87-O01-original84-current-dispositions.json")["rows"]}
rows84 = []
incoming = {
    "mcp/src/agents_remember/kernel/atomic_write.py": "The incoming source adds same-target abandoned-temp cleanup after direct os.replace and before directory fsync, with in-flight tracking, live/unknown/invalid-pid retention and Windows skip. The content-resolved current card explicitly states those boundaries and the separate atomic_replace failure window; it does not claim rollback or removal of every leftover.",
    "mcp/src/agents_remember/worktrees/reopen.py": "The incoming implementation delegates its exact master-row admission to require_reopenable_row; the surviving _plan_master_index_reset still plans that exact row reset under admission. The retained card does not name the removed local _validate_reopen_row_path helper or grant task edits. Its planning/publication/recovery ownership account remains applicable; source citations require current refresh.",
}
for sealed in original84["rows"]:
    path = sealed["sourcePath"]
    data = (CODE / path).read_bytes()
    card = (MEMORY / sealed["card"]).read_text()
    same_source = digest(data) == sealed["sourceSHA256"]
    same_card = digest(card.encode()) == sealed["cardSHA256"]
    if path in by_source:
        reason = by_source[path]["authoredReconciliation"]
        action = "existing-O01-current-account-corrected"
    elif path in incoming:
        reason = incoming[path]
        action = "incoming-Source41-owner-change-read-with-current-card"
    else:
        assert same_source and same_card and sealed["adjudication"] == "accepted", path
        reason = "The exact source and current-card bytes remain the individually supported R3 account. " + prior84[path]["basis"]
        action = "exact-paired-bytes-preserved-from-accepted-R3-account"
    rows84.append({"ordinal": sealed["ordinal"], "sourcePath": path, "card": sealed["card"], "sourceSha256": digest(data), "cardSha256": digest(card.encode()),
                  "currentSource": data.decode(), "currentCard": card, "rationale": reason, "action": action,
                  "sealedR3Disposition": sealed["adjudication"], "sameSourceBytesAsR3": same_source, "sameCardBytesAsR3": same_card, "independentAcceptance": False})
assert len(rows84) == 84
indices_after = {"code": index(CODE), "memory": index(MEMORY)}
assert indices_after == indices_before
save("source41-O01-original84-current-dispositions.json", {"schema": "l26-sealed-o01-population-readback/v1", "population": 84, "rows": rows84, "acceptedByReviewer": None})
save("21-citation-and-current-account-readback.json", {"state": "all21-card-bodies-and-citations-read-back", "originalFinding": "L26-MR1-O01", "rows": readback, "indexesBefore": indices_before, "indexesAfter": indices_after, "sourceIndexStageMutation": False, "independentAcceptance": False})
print(json.dumps({"cards": len(readback), "verifiedCitationTargets": sum(len(r["references"]) for r in readback), "sharedEntries": len(shared_rows), "original84": len(rows84), "indexesUnchanged": True, "independentAcceptance": False}))
