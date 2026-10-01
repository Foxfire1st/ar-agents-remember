# Closeout Integration Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

Closeout-door publication, structured curator-coherence authority, source reconstruction, organizational repair, and recovery projection. It separates disposable scheduling
evidence, candidate acceptance evidence, and the durable operation journal.

## Hot Path Summary

Door dependency identity binds task, code and substantive memory candidates. It carries no ledger digest, row, provenance or third commit. The retired ledger recovery module has no replacement writer; existing journal/Git owners prove the two actual outputs.

## Detailed Route Context

`prepared_certification.py` (relocated here from `memory_quality/` by commit `deb032fb`) composes the
actual affected closure and full memory checks against a proved private code view;
`curator_coherence.py` captures and validates the exact code/memory/task/attestation candidate;
`curator_coherence_publication.py` publishes the sole live content-addressed authority;
`curator_coherence_judgments.py` binds agent-owned decisions to evidence bytes; and
`curator_coherence_render.py` produces a one-way human projection. `door_source.py` reconstructs
the exact waiting source; the operation journal and Git mutation evidence prove code and memory outputs after partial
closeout without making the disposable queue own commit evidence. `integration_reopen.py` decides
whether exact newly produced code or memory output needs another plane-owned integration.
For graph-backed candidates, both door reconstruction and curator-coherence observation pass the
already resolved authored graph to the shared queue/task-domain context and use its bound immutable
sprint snapshot. The door, coherence record, and projection therefore cannot mix graph generations.

CCR now binds canonical semantic `taskIntent` and declared direct dependency digests through
curator coherence, waiting/claimed doors, and lifecycle admission. A stale or missing intent
refuses current use and names republishing, rather than accepting topology alone.
`task_intent_identity.py` resolves the exact contract-owned leaf;
`task_intent_legacy_census.py` separately counts current legacy containers before decoder
removal. Historical generations remain audit evidence. These existing door/journal owners
are distinct from the selected certification graph: admission and code-suffix execution are now
composed under `certification/`; prepared-memory and finalization execution are separate registered continuation responsibilities.

## De-Entanglement Cut Relocations

Three member cards left this route and one arrived, all by explicit relocation commits:

- `future_code_candidate.py`, `memory_candidate_pair.py` (commit `0b63d6fc`) and
  `memory_census_scope.py` (commit `be517eec`) moved to `memory_quality/`, because a pre-closeout
  quality service must be able to mint and prove its own memory-candidate identity without the
  closeout plane. This route may depend on `memory_quality/`; not the reverse.
- `prepared_certification.py` moved in from `memory_quality/` (commit `deb032fb`) as the
  closeout-facing certification adapter.

The public closeout-door *tool entry point* was deleted by the same cut (commit `6982c6a7`, which
removed `application/closeout_door.py`, `mcp/tools/closeout_door.py`, the `models/lifecycles/door_response.py`
response model and the tool registration). The closeout-internal door modules on this route
(`door.py`, `door_control.py`, `door_evidence.py`, `door_source.py`, `initial_door_recovery.py`)
were not removed by that commit.

## Selected Certification Route

[The selected certification overview](certification/overview.md) follows actual frozen admission, explicit predecessor/publication readback, journal CAS and suffix execution. It also explains retained red evidence, current Gate-5 observations and the narrowly proven code-output recovery comparison. These responsibilities extend the existing door/coherence/journal separation; they do not make queue state own certification or themselves establish memory/finalization execution.

## KS-R24@v1 Prepare States The Publication Inputs

`curator_coherence_publication.py::_prepare` now composes its summary from
`publication_input_statement()` — read from the request model's `PUBLICATION_MEMBERS` declaration — so
the prepared response states the complete input set `publish` requires: the per-candidate judgments
**and** all nine publication members, with `semantic_requirement_revision` and `delivery_attempt`
marked as caller-supplied delivery identities `prepare` does not derive from the observation it
returns. Before this, the summary mentioned only the judgments, so a caller following the documented
`prepare` → supply a judgment per candidate → `publish` flow was refused without ever being told the
last two members existed; that is the message defect two leaves of this master recorded as an
impassable tool defect (`notes/DISCLOSURES.md` D-11). The text is a pure function of the declaration, so
an appended member reaches this response with no edit here. `prepare` still invents neither identity,
returns no value for either, and `_publish` is untouched: the only change in this module is the summary
string.

## 260928-MIK-L09 The Closeout Validator Recomputes The Mandatory Invariant Gate

**Route meaning extended (MIK-R09@v2 rule 3).** `curator_coherence.require_current_curator_coherence` is one of the
two closeout routes MIK-R09 names. After every existing check passes it now calls `_require_knowledge_gate`, which
asks `worktrees/knowledge_gate.leaf_gate_refusal` over the very code and memory candidate trees the coherence authority
binds. On converted memory the gate recomputes the leaf's worklist over those trees, decides every item through its
kind's own predicate, and runs the validator as a leaf publication against the parent line's memory tip; any open
item, incomplete run or violation raises `curator-coherence-knowledge-gate-refused` (next action
`memory_quality_check`) naming every finding. A converted leaf with no bound gate refuses (`GATE_UNBOUND`); an
unconverted leaf is not gated and is validated exactly as before. The coherence record, its identity checks and pair
identity are unchanged (MIK-R09 Preservation); normally the curator publication has already evaluated the same memo
key, so this read is served from the gate's memo. Tested through the real validator by
`test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`. The certified (prepared) path of
[`certification/`](certification/overview.md) refuses on converted memory (gap 3). **Inert until the cutover.**

- The closeout validator's gate over the authority's exact candidate. [1]

## Local Invariants And Traps

- Door publication authorizes entry; the operation journal owns running and terminal evidence.
- Recovery is idempotent and candidate-bound; missing or conflicting proof refuses loudly.
- Queue invalidation never erases an already-claimed lifecycle operation.
- One stable structured coherence manifest selects one immutable generation per leaf. Historical
  Markdown is neither parsed nor searched.
- Memory readiness, door evidence, and closeout admission share one currentness validator.
- The validated record projects exact content/route no-impact identities to onboarding body gates;
  only unchanged stale content is eligible, while untraced edits remain closed.
- Malformed live authority bytes remain replaceable only through exact prepared CAS.
- Graph-backed closeout consumers share one admitted immutable graph generation per observation.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `door_source.py` | [door_source.py.md](door_source.py.md) | covered |
| `prepared_certification.py` | [prepared_certification.py.md](prepared_certification.py.md) | covered |
| `curator_coherence.py` | [curator_coherence.py.md](curator_coherence.py.md) | covered |
| `curator_coherence_judgments.py` | [curator_coherence_judgments.py.md](curator_coherence_judgments.py.md) | covered |
| `curator_coherence_publication.py` | [curator_coherence_publication.py.md](curator_coherence_publication.py.md) | covered |
| `curator_coherence_render.py` | [curator_coherence_render.py.md](curator_coherence_render.py.md) | covered |
| `integration_reopen.py` | [integration_reopen.py.md](integration_reopen.py.md) | covered |

## Evidence

### Docs And Boundary References

No configured external source applies. The lifecycle and queue overviews describe adjacent owners.

### Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

- Door source facts use current Git and task authority. [2]
## MCAR-L03 Pair-Bound Closeout

The coherence authority, its source attestation, immutable record, publication fingerprint,
generated report, closeout preview, completed apply, and post-commit recovery now share the exact
pair model. Preview/normal closeout obtain it from current coherence; initial apply and recovery
re-prove it from the same exact contract so stale pre-commit evidence is never treated as a repo-id
fallback.

## L34 Preparation Ownership

[Preparation](preparation/overview.md) now owns selected private code/memory-content creation, genuine existing-output reuse, physical code views and prepared-memory result currentness. [preparation_selection.py](preparation_selection.py.md) retains original objects and command outcomes through canonical journal CAS. Final memory evidence comes from the registered prepared-memory producer; private output selection alone is not ref publication or approval.


## Integrated IAS Recovery Contract

Preparation selection requires the exact four original code certificates and, for memory legs, the selected fifth certificate. Prepared finalization recovery is attempted before fresh original-head admission so the original generation can finish code/memory-content publication after its owned refs advance. This is recovery of retained outputs, not permission to rerun commands or certify a changed candidate.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## 260915-KS-L15 The Assessment Evidence Destination

This route gains one module: `curator_assessment_evidence.py`, which owns the one destination an
assessment's cited bytes publish to, `<task_root>/notes/reports/evidence/<assessment_id>/<filename>`,
and the read-back that proves they survived. Three properties chose that destination and each is a
measurement rather than a preference: it is the shipped durable precedent for exactly this property
(the curator-coherence authority's own route onto the coordination task root), it is **outside** the
worktree group terminal cleanup removes, and the terminal enclosure archive **cannot** hold it — that
archive's scanner admits a fixed artifact set and refuses an unclassifiable canonical-root file.

The publication path was extended in the same leaf:
`curator_coherence_publication.py` gained `_exact_review_assessments`, which stamps authorship from the
**authenticated caller** rather than from submission text, and `_published_evidence_bytes`, which
publishes each cited byte and then opens every one again by its recorded path and digest before it
returns. A failed read-back is a blocked terminal state carrying the destination, the expected digest
and the observed state; it is never repaired by a second copy, never re-homed into the terminal
archive, and never reported as published. `curator_coherence.py` gained the read projection and the
record-side edge recomputation. The shipped exact-coverage obligation is untouched: the assessment
collection is content beside `judgments`, and publishing one does not disturb it.

## 260921-ICR-L15 Measured assessment currentness

Coherence's assessment projection now reads the shipped measurement classifier instead of deciding
currentness for itself. `curator_coherence_assessments` and
`curator_coherence_subject_assessment_state` in `curator_coherence.py` (795 → 800 lines) classify every
stored record through `models/lifecycles/review_assessment_binding.supplied_measurement_statuses`, so a
record's state comes from that record's own measurement rather than from a collection-wide verdict.

**Omitting `current` now means nothing measured anything.** The old default read an absent measurement as a
movement: every record the caller supplied no entry for was reported `stale`. That published a fact the
store never held — an unmeasured binding stated as a measured change. A caller that supplies no measurement
at all, or an empty one, now gets what the binding module answers for "nothing measured this":
`not-measured`, which is neither a clearance nor a movement. A supplied measurement is read the shipped
comparison's way: an identity it covers that disagrees is a measured movement (`stale`), an identity it
does not cover is unmeasured (`not-measured`), and only a record whose whole declaration is covered and
agrees is `current`. `unavailable` stays the failed measurement's state and `none-recorded` stays a subject
with no stored assessment — neither is manufactured here.

**The helper that computed the old default is gone rather than aliased.** `_stale_assessment_ids` — the
local list of ids whose recorded binding the caller's mapping disagreed with, which both entry points built
and then passed as `stale_ids` — was deleted with the `assessment_currentness_for_record` import it used.
Its one replacement is the private `_measured_state`, which converts the caller's mapping once and is the
single path both public entry points take, so the collection projection and the per-subject projection
cannot classify the same record two different ways.

## Shared curator integrity and live readiness

Curator path/namespace resolution and immutable generation integrity have focused shared owners. Judgment publication retains admitted bytes under the existing task artifact root; historical reads use that custody and publisher-recorded assessment destinations. The shared generation read runs before canonical pointer replacement. Strict live validation still checks live quality, dependencies and original cited inputs; durable integrity never substitutes for readiness.
