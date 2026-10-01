# mcp/src/agents_remember/application/knowledge_family_integrity.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one operation `KS-R16@v1`'s Normative Requirement asks for, plus the retention pair that proves a
finding survived cleanup.** `family_integrity_report` composes the family-integrity pipeline over one
dataset: it constructs the registered review scope, reads the recorded detection run back, groups that
run's facts, composes the five separated owner statuses, measures each authored record's currentness and
routes the groups into the existing curator worklist. `publish_review_evidence` publishes a finding and
its manifest through `KS-R18@v1`'s durable route and reads both back from the resolved destination, and
`worklist_row_disposable` is the single predicate that decides whether a worklist row may be discarded.

The module decides nothing of its own. Every act belongs to the module that owns it, and this file is the
seam that puts the acts in the packet's order. It deliberately does **not** own two of the five statuses:
the structural validator's and the verification runner's arrive verbatim on the request, and a request
that omits one is refused rather than completed with a plausible value. It also is not a gate: the report
carries the shipped actionability formula's three terms and the family-review row count beside them, and
has no field that could refuse a merge, block a closeout or add a fourth term.

## Code Commentary

### Logic

The module opens with fifty-seven lines of import and declaration, and the shape of that opening is the
argument: the standard library contributes `Mapping`, `Sequence`, `dataclass`, `field`, `Path` and
`Literal`; everything else is imported from the routes below this one — `application.knowledge_composition`,
`memory.knowledge.detection`, `memory.knowledge.durable_evidence`, `memory.knowledge.refusals`,
`memory.knowledge.registered_scope`, `memory_quality.family_review`, `memory_quality.knowledge_review`,
`models.knowledge.*` and `models.lifecycles.review_assessment`. The types this file *builds* are its own;
the facts it reports are all other owners' types.

`__all__` publishes six names — `FamilyIntegrityReport`, `FamilyIntegrityRequest`,
`ReviewEvidenceRetention`, `family_integrity_report`, `publish_review_evidence` and
`worklist_row_disposable` — so the two private composition helpers stay internal. **Two module constants
carry the leaf's decisions as values.** `CALLER_REPORTED_STATUS_OWNERS` names
`("structural-validator", "verification-runner")`, the two owners whose status this pipeline does not
derive, and the comment above it states why it is a value rather than a comment: a request that omits one
is refused **by name**. `COMPOSE_REPORT_OPERATION` is `"compose_family_integrity_report"`, and it is the
operation name the composition's own refusal carries — a member of the shipped operation vocabulary rather
than a new refusal *code*, because every code this leaf reuses is shipped.

`FamilyIntegrityRequest` is what one run reads, stated as identities and measurements rather than
descriptions. It carries `repository_id`, `run_id`, the `RegisteredScopeRequest`, the declared
`ScopeSnapshotSource` tuple, the caller's `owner_reported_statuses` mapping, the authored `assessments`,
and `current` — the caller's measurement of the world, keyed by record identity and then by
`(kind, name)`. Its three counts (`repair_count`, `missing_count`, `stale_count`) and its two scan flags
(`unresolved_inputs`, `incomplete_scan`) are carried so the report can state a value it did not compute.
Its one property, `missing_owner_statuses`, returns the owners of `CALLER_REPORTED_STATUS_OWNERS` absent
from the mapping.

`FamilyIntegrityReport` is the composed output: one field per act (`scope`, `run`, `groups`, `statuses`,
`currentness`, `routing`, `review_rows`, `currentness_status`) and **no merged verdict anywhere**. Its
`state` is `Literal["composed", "refused"]`; on a refusal the fields default to empty and
`refusal: KnowledgeRefusal | None` carries what stopped the pipeline. Two small accessors exist for
assertions rather than for logic: `report_only_rows()` reads `routing.review_row_count` (and answers `0`
when there is no routing), and `section_lines()` renders `knowledge_review_section(self.review_rows).lines`
so a caller can assert a row is present in the section.

`family_integrity_report(database_path, request)` is the operation, and its order is the packet's own.
**A request missing an owner's status is refused before the store is opened**, and it is refused *with a
constructed scope*, because everything downstream is a claim about the scope the run examined. A scope
that did not construct is refused with the scope's own refusal, or with `None` if the construction
returned neither. Only then does it open the dataset through `open_read_only_store`, read the recorded run
with `read_detection_run`, and close the handle in a `finally`. A run that came back `refused` returns
`_refused(scope, run.refusal)`; otherwise `_compose` builds the report.

`_refused` is three lines and one sentence of contract: it short-circuits the pipeline while **keeping
whatever was resolved and the refusal that stopped it**, so a reader of a refused report can still see
which scope the attempt was made over. `_compose` is the five-act body: `group_detection_facts(run.signals)`
for the groups, `compose_currentness(request.assessments, request.current)` for the per-record
measurements, then one construction call whose keyword arguments are
`compose_status_report(_owner_statuses(run, request, currentness))`, `route_family_review(groups,
review_ids_by_subject=_review_ids_by_subject(request.assessments), repair_count=…, missing_count=…,
stale_count=…)`, `family_review_summaries(request.assessments, request.current)` and
`curator_currentness_status(currentness)`.

`_owner_statuses` is where the five-owner split is executed. It copies the caller's mapping and then
**adds exactly three derived entries**: `detector` from `detector_status(run.signals,
unresolved_inputs=…, incomplete_scan=…)`, `curator-reviewer` from `curator_review_status([record.disposition
for record in request.assessments])`, and `authority-currentness` as `"stale"` when any
`binding.binding_state == "stale"` and `"dependencies-match"` otherwise. The two caller-reported owners
are never recomputed here — they are passed through into the report that validates them.
`_owner_status_refusal` builds the refusal for a missing owner: the shipped `invalid_payload` code, the
`COMPOSE_REPORT_OPERATION` name, a detail that names the absent owners and states that a default "would be
this leaf reporting a validator's or a runner's result it never measured", an explicit `next_action`, and
`RefusalFacts` carrying the expected and observed sides. `_review_ids_by_subject` is the last private
helper: it groups stored record identities by `assessment_subject_id(record)` — the spelling the routing
rows use — and sorts each group, so routing addresses the subject the existing collection already holds.

The second half of the file is the retention record and its two functions. `ReviewEvidenceRetention` holds
four values — the `DurableEvidencePublication` of the finding and of the manifest, and an
`EvidenceReadBack` for each — and its `destination` property returns `finding.destination.parent`, so the
directory is derived from the publication rather than restated. **`matched()` and `readable_together()` are
different claims and the difference is the point.** `matched()` asks whether both artifacts read back as
the bytes that were published; `readable_together()` additionally requires
`finding.destination.parent == manifest.destination.parent`, which is the property §6.3 asks this leaf to
prove. `blocked_reason()` answers `""` when the pair matched and otherwise renders the resolved
destination, each artifact's observed state, and the sentence that "Retention that rests on a path nobody
read back is not evidence."

`publish_review_evidence(task_root, *, finding_name, finding_content, manifest_name, manifest_content)`
publishes both artifacts through `publish_durable_evidence` and immediately calls `read_back_evidence` on
each. **The destination is resolved by the shipped publication function rather than by this one**, so the
set of destinations a retention claim may rest on keeps its single definition — the docstring states the
destination as `<task_root>/notes/reports/` and notes that the read-back is repeated by whoever holds the
publication record *after* cleanup, because that is the moment the claim becomes a measurement.
`worklist_row_disposable(*, durable_reference_count)` is one expression, `return durable_reference_count >
0`, and it is keyword-only so a caller cannot pass a count positionally into the wrong predicate.

### Conventions

Two frozen dataclasses, a keyword-only predicate, and private helpers below their public entry points —
the same shape the route's other knowledge seams use. The module reuses shipped vocabulary rather than
declaring new codes: the refusal code is `invalid_payload`, the operation name is a member of the shipped
operation vocabulary, and the statuses are the owners' own. Explanatory comments sit above the two
constants that encode a decision (why the caller-reported set is a value, and why the operation name is a
code-free refusal), and every function carries a docstring that states what it does *not* establish.

### Invariants And Boundaries

- **The pipeline owns three of the five statuses and no more.** `detector`, `curator-reviewer` and
  `authority-currentness` are derived from the run, the records and the currentness measurement;
  `structural-validator` and `verification-runner` are read off the request. `compose_status_report` itself
  raises when an owner reports nothing, so an omission that reached it would be an exception rather than a
  four-row report — the seam refuses first, by name, so the failure leaves as a typed
  `KnowledgeRefusal` instead.
- **A short-circuit keeps the scope and drops the rest.** `_refused` sets `state="refused"` and carries
  the resolved `scope` plus the refusal; `run`, `groups`, `statuses`, `currentness`, `routing` and
  `review_rows` stay at their empty defaults, because reporting a partial pipeline over a scope or a run
  that was not read is the silent partial state the packet's failure behaviour refuses.
- **Nothing here is a gate.** The report carries `actionable_count` produced by the routing module from the
  caller's three counts, `review_row_count` beside it, and `currentness_status` as a separate field. There
  is no field on `FamilyIntegrityReport` that could refuse a merge, block a closeout or add a fourth
  actionability term.
- **The read handle is opened once and closed in a `finally`**, and the operation opens no write path at
  all: the only durable write this module performs is the delegation to `publish_durable_evidence` inside
  `publish_review_evidence`, and it writes where that shipped function decides.
- **`readable_together()` is strictly stronger than `matched()`**, and the code states the difference in
  one expression: the pair must have matched *and* share a destination directory. A record whose two
  artifacts landed in different directories is not a record §6.3 has proven, even when both read back.
- **A retention failure answers with facts, never with "published".** `blocked_reason()` renders the
  destination and both observed states and returns `""` only on a match, so there is no branch that reports
  a non-matching read-back as a success.
- **The two caller-reported owners are carried, not recomputed.** `_owner_statuses` copies
  `request.owner_reported_statuses` and assigns only the three derived keys, so a status this leaf did not
  measure cannot be produced by this leaf — from either direction.
- **`CALLER_REPORTED_STATUS_OWNERS` is written out rather than derived from the model's
  `PIPELINE_STATUS_OWNERS`**, so the two vocabularies agree today by inspection and not by construction: a
  sixth owner registered in `models/knowledge/family_review.py` would not widen what this seam refuses
  before the store is opened.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module docstring states the whole contract: the one operation, the two owners this leaf does not report, the retention read-back, and that nothing here is a gate.** [1]
- **The module's declared surface and its two decision-carrying constants: the owners this pipeline does not derive, and the operation name its own refusal carries.** [2]
- The request's shape, the property that reports which owner statuses it did not carry, and the two accessors that let a caller assert what the report-only section holds. [3]
- **The report shape: one field per act, a two-member `state`, and no field that could hold a merged verdict.** [4]
- **The operation's order and its three short-circuits, and the `_refused` builder that keeps whatever was resolved and the refusal that stopped it.** [5]
- **The five-act composition, and where three of the five statuses are derived while the two caller-reported ones pass through untouched.** [6]
- The refusal a request that omits an owner's status receives, by name, in the shipped vocabulary; and the record identities indexed by the subject spelling the routing rows use. [7]
- **The retention record: the only claim it can make is about two read-backs, readability together is strictly stronger than a match, and a failure answers with the destination and both observed states rather than with "published".** [8]
- **Publication plus immediate read-back, with the destination resolved by the shipped publication function rather than by this one.** [9]
- **The disposal predicate is one expression over the durable reference count a caller supplies, and its docstring, its expression and the shipped case agree: a count of zero — the row is the only pointer to the evidence — answers `False` and the row is kept.** [10]
- The read-only open the operation reads the recorded run through, and the two lower-route owners it delegates to in order. [11]
- The five owners, their declared order, and the validator that requires exactly one entry per owner in that order. [12]
- **The routing record's arithmetic tie, which is why the report cannot grow a fourth actionability term; the shipped formula it consumes; and the detector-status derivation the seam calls by name.** [13]
- **The publication and read-back owners this module delegates to, whose `matched()` composes into the retention record.** [14]
- The subject spelling the routing rows address and the section renderer `section_lines()` delegates to, both defined by their own owners. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A status owner's reported status, an authored
review record and a durable evidence destination are all properties of one coordination root's own task
tree, and nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
