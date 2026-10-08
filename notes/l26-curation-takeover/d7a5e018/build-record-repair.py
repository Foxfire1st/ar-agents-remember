"""Author the remaining original MR1 meaning repairs; never write product records directly."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = HERE.parents[2]
records = {json.loads(p.read_text())["id"]: json.loads(p.read_text())
           for p in (MEM / "knowledge").glob("*/*.json")
           if isinstance(json.loads(p.read_text()), dict) and "id" in json.loads(p.read_text())}
history = json.loads((MEM / "knowledge/history/260928-MIK-L26.json").read_text())
old_rows = {r["subject"]: r for r in history["rows"]}
attachments = {}
for p in (MEM / "onboarding").rglob("*.json"):
    if p.name.endswith(".index.json"):
        continue
    d = json.loads(p.read_text())
    path = d.get("path")
    if not path:
        continue
    for field in ["realizes", "proves"]:
        for e in d.get(field, []):
            attachments.setdefault(e["invariant"], []).append((path, field, e))

batch = {"entries": [], "records": [], "history": []}
reasons = {}
retired = {}
def update(kind, ident, fields, reason):
    existing = next((r for r in batch["records"] if r["id"] == ident), None)
    if existing is None:
        batch["records"].append({"key": "mr1-current-" + ident, "kind": kind, "id": ident, "fields": fields})
    else:
        existing["fields"].update(fields)
    reasons[ident] = (reasons[ident] + " " if ident in reasons else "") + reason
def retire(ident, reason):
    update("invariant", ident, {"status": "retired"}, reason)
    retired[ident] = reason

update("invariant", "INV-753SKJFF", {
    "statement": "Published intent is selected from the one resolved converted memory root: the official external memory root outside an enclosure and the leaf's memory worktree inside it. Its text records are canonical; reads select the derived index of that exact tree. An unconverted root is refused as legacy-format, and no canonical knowledge database publication destination is selected.",
    "applicability": "Ordinary published-intent selection for the resolved repository or canonical leaf.",
    "conditions": ["The resolved memory root holds knowledge/layout.json.", "The derived index can be built or read for the selected memory tree; failure remains an explicit unusable selection."],
    "exclusions": ["Historical canonical database publication and its former not-recorded converted result.", "A sibling memory layer or derived index cache as an alternative source of truth."]
}, "MIK-R26 deliberately supersedes dataset selection: resolve_published_intent selects the converted tree's index and refuses legacy roots. The original dataset and not-recorded promises are preserved only in prior Git history.")

retire("INV-VVMNM9B6", "The retired batch writer's allocation-content digest and journal replay are gone. TargetRealization describes authored values but does not enforce allocation_content_conflict, so retaining that realization would assert a mechanism the converted writer lacks.")
update("invariant", "INV-E8655Z54", {
    "conditions": ["A converted file-writer handoff supplies realization targets; _targets runs the shared value/route refusal before planning those targets."],
    "exclusions": ["Omitted or null governing_route, which remains ungoverned.", "Stored historical realization rows, which this admission check does not retrospectively rewrite."]
}, "The route-value refusal survives in handoff._targets via realization_refusal; allocation-journal replay exemptions do not survive the database retirement.")
update("invariant", "INV-J7179RG5", {
    "conditions": ["A converted file-writer handoff is parsed for realization targets before authoring its record and sidecar edits."],
    "exclusions": ["Target shapes that are not JSON objects, which the target-shape check refuses separately.", "Stored historical claims; this parser judges supplied targets rather than re-admitting every stored row."]
}, "The same role/rationale value and length checks survive at handoff._targets. The old committed-allocation bypass is retired and cannot scope the current file parser.")
update("invariant", "INV-H6A6JS63", {
    "statement": "A converted file-writer handoff target with neither its own nonblank rationale nor a nonblank entry default refuses the entry as realization_rationale_absent, naming the entry and offending targets before record or sidecar writes. The writer never invents the explanation.",
    "applicability": "Realization targets supplied to the converted curator file writer through knowledge-ingest or knowledge-bootstrap.",
    "conditions": ["At least one supplied realization target lacks a rationale at both levels."],
    "exclusions": ["Targetless task rulings, which create no realization.", "Stored historical claims; this admission check does not rewrite them."]
}, "The live _targets parser enforces the authored explanation. Database allocation journals and their replay exemptions are no longer an applicable condition.")
update("invariant", "INV-7W11WKKN", {
    "statement": "The review evidence collector reads owner records for the exact resolved comparison it is rendering, preserving explicit collection availability and immutable curator-generation provenance. Retired canonical detection, verification and evidence collections remain unavailable; an unread or uncaptured collection never becomes a favorable empty result.",
    "applicability": "review_records_for_resolution and its exact candidate-bound owner collections.",
    "conditions": ["The comparison is resolved once and supplied to the collector.", "Each collection reports its own availability; curator assessments are read through their generation integrity owner."],
    "exclusions": ["The retired dataset comparison publication producer and its explicit-positive-input admission protocol.", "A mutable current pointer, generic evidence citation or invented empty collection as replacement for an unread owner input."]
}, "Collection ownership and honest availability survive in review_evidence_records; the retired freeze publisher and reserved-positive-input checks do not. This revision preserves that live meaning and drops the unsupported publication claim.")
update("invariant", "INV-9NCBGQSY", {
    "statement": "A historical review reopens a recorded tree comparison from its recorded tree ids. A closed leaf that recorded only a canonical dataset comparison preserves its exact source sides and reports its retired knowledge operands as legacy-unavailable without opening their databases.",
    "applicability": "Historical review resolution after canonical knowledge database retirement.",
    "conditions": ["The retained record identifies its comparison format and exact source endpoints."],
    "exclusions": ["Reopening an unconverted canonical dataset or borrowing today's knowledge to stand for an unavailable operand."]
}, "MIK-R26 retires even the unconverted dataset read route. Historical source and tree comparisons remain readable; the old alternative that still opened the canonical dataset is deliberately superseded.")
update("invariant", "INV-FYZQK0", {
    "conditions": ["Publication raised after creating a reachable commit, HEAD switched, and expected-old take-back did not remove that commit."],
    "exclusions": ["Ordinary unpublished refusal and validation after a successful publication return; their restoration boundaries are separate."]
}, "Preserve the observed partial-publication guarantee while removing the exclusion's false assertion that ordinary unpublished refusals restore nothing.")
update("invariant", "INV-JZD1F5", {
    "applicability": "The ordinary closeout's documentation of its publication and preparation-restoration boundary.",
    "conditions": ["The documentation distinguishes publication raising after partial ref movement from proof validation after a successful publication return."],
    "exclusions": ["A claim that documentation repairs the retained runtime race or publication policy."]
}, "The documentation obligation remains current independently of any named final freeze; the authoring removes its temporary delivery-snapshot scope.")
update("invariant", "INV-PPGGTW", {
    "conditions": ["A converted memory repository is selected, optionally narrowed by a path or record id.", "The complete response is measured against the shared knowledge-read token threshold."],
    "exclusions": ["Inferring a semantic verdict from the mechanical diff.", "Canonical database-path comparison, which MIK-R26 retires."]
}, "The path-less request compares the full selected tree; an explicitly absent selector is refused. Scope must cover both omission disclosure and selector refusal rather than exclude the behavior its statement promises.")

admissions = {
    "INV-1BBPF3": "Foundation examples must name supported read views; otherwise a new project's first inspection is routed to an operation that cannot demonstrate its recorded knowledge.",
    "INV-K69R3M": "Calling converted foundations universally not-recorded hides an actually authored or partially authored foundation and can cause an operator to duplicate or omit its authoring work.",
    "INV-J6PAD2": "Negative controls expose loss of expected-old take-back, replacement narrowing and cleanup protection, which could otherwise overwrite concurrent commits or remove protected content while ordinary successful tests stay green.",
    "INV-PPGGTW": "A diff displayed as complete after silently dropping files can hide changed intent from its reviewer; explicit omissions and the shared read threshold prevent that error.",
    "INV-JM868W": "A bounded diff must disclose omitted content and its temporary Git-object capture: hiding either can make a partial review look complete or conceal the operation's storage side effect."
}
for ident, basis in admissions.items():
    update("invariant", ident, {"admission": {"criteria": ["prevents_costly_mistake"], "justification": basis}}, "The retained statement names a stable protected behavior; replace the generic admission with this specific failure and boundary.")

update("family", "FAM-7B6N3Y4Q", {
    "guarantee": "Authored knowledge writes use the admitted leaf knowledge-ingest or taskless knowledge-bootstrap command and the single converted file writer. Writer admission and ordinary readers resolve the same repository or leaf memory root, whose text files are canonical. An unconverted root is refused and no canonical dataset is published. Mechanical conversion, crossing merge, formatting and closeout flags are outside this authoring guarantee."
}, "The three members were examined together: writer reachability, one resolved read location and real taskless setup authority still give one authoring/read-location guarantee. The unconverted batch writer is deliberately removed by MIK-R26.")
update("family", "FAM-KQQE74ZT", {
    "members": [x for x in records["FAM-KQQE74ZT"]["members"] if x not in {"INV-4N43MNN2", "INV-VVMNM9B6"}],
    "guarantee": "Every realization target the converted file writer admits carries its author's nonblank explanation and a role from the stated target or explicit entry default; role absence is unclassified. The parser refuses malformed text, unknown roles, absent-literal routes and missing or overlong rationales before writes, naming the offending target. Stored historical claims are not retroactively reauthored; this guarantee asserts no database allocation-journal replay."
}, "Keep the five live explanation/target-validation obligations and remove the two retired allocation-replay obligations. Their distinct scope and exact current revisions were examined; _targets delegates to the retained value checker rather than the retired batch writer.")
update("family", "FAM-SK1BFPE2", {"status": "retired", "routes": []},
       "The former joint guarantee combined semantic-scope admission with the allocated-scope conflict protocol. The latter is retired; preserve INV-KBCKV7N1 as a standalone scoped obligation rather than claim its old partner still implements a joint promise.")
update("family", "FAM-XZ5BR65G", {
    "guarantee": "Historical review uses the exact retained comparison and explicitly names what it can reproduce: recorded tree comparisons retain their code and memory tree ids, while canonical-dataset history preserves exact source sides and marks knowledge legacy-unavailable. Comparison-bound curator generations preserve authored judgments and availability, and reconstruction is labelled. No current dataset, mutable pointer or favorable empty channel replaces unavailable history."
}, "All current and retired siblings were examined. Tree comparison and curator custody survive; canonical dataset operands and the comparison-publishing producer do not. The guarantee is narrowed to the actual retained historical read paths.")
update("family", "FAM-61DY2V", {
    "members": sorted(set(records["FAM-61DY2V"]["members"]) | {"INV-FYZQK0", "INV-GSEMMW"}),
    "guarantee": "A converted leaf's closeout and direct landing judge their prepared memory tree through the validator and invariant gate and publish only that admitted tree on the intended branch and observed parent. The source index, message and hook policy remain faithful, and moved inputs or unfinished native actions refuse. Unpublished refusals restore owned preparations and preserve concurrent content; expected-old take-back never overwrites a foreign commit. Partial publication whose take-back fails may leave a reachable commit while preparations restore, and a proof failure after successful publication return keeps the published preparation. Gate-input reuse and frozen history remain exact. Recorded landing has only its separately declared validator and closed-history checks."
}, "The current shared publication and both leaf routes implement admitted-tree/parent/index binding; direct landing is no longer an admission-snapshot exception. Preserve the Owner's R4-O2 partial-publication limit rather than inventing universal rollback. All unchanged base members and added members are retained and examined.")
update("family", "FAM-SDS92V", {
    "guarantee": "The repository's retirement guard and static source check expose canonical-database access in their declared test/source scopes, and test teardown restores the guard when a test removes it. The reviewed copy-cleanup owner removes only eligible copies and preserves tracked or symlinked companions. Together these protect the database retirement's executable paths and cleanup boundary; they do not certify unrun tests, derived-index deletion, or elimination of every workspace copy."
}, "The six members jointly cover retirement detection, continued guard enforcement and protected cleanup, each in its actual scope. The earlier universal production/refusal sentence overstated what test instrumentation and one reviewed cleanup can measure.")

# Every overwritten invariant row keeps its earlier cover set and adds current entries.
for ident, reason in reasons.items():
    if records[ident]["schema"] != "ar-invariant/v1":
        continue
    old = old_rows.get(ident, {})
    covers = {c["id"]: {"id": c["id"], **({"remove": True} if c.get("after") == "absent" else {})}
              for c in old.get("covers", [])}
    for path, field, e in attachments.get(ident, []):
        cover = {"id": e["id"]}
        if ident in retired:
            cover["remove"] = True
        elif ident == "INV-1XKX9ERN" and field == "realizes":
            cover["rationale"] = "The admitted command resolves the leaf or taskless setup and calls the converted file writer; it selects no canonical database destination."
        covers[e["id"]] = cover
    batch["history"].append({"subject": ident, "disposition": "deleted" if ident in retired else "changed",
                             "effect": "retire" if ident in retired else "clarify", "reason": reason,
                             "covers": list(covers.values())})
for ident, reason in reasons.items():
    if records[ident]["schema"] != "ar-family/v1":
        continue
    current = records[ident]
    fields = next(r["fields"] for r in batch["records"] if r["id"] == ident)
    members = set(current["members"]) | set(fields.get("members", []))
    batch["history"].append({"subject": ident, "disposition": "retired" if fields.get("status") == "retired" else "changed",
                             "reason": reason, "examined": sorted(members)})

(HERE / "remaining-record-repair.handoff.json").write_text(json.dumps(batch, indent=2) + "\n")
(HERE / "remaining-record-repair.meaning.json").write_text(json.dumps(reasons, indent=2) + "\n")
print(json.dumps({"records": len(batch["records"]), "history": len(batch["history"]), "retirements": retired}, indent=2))
