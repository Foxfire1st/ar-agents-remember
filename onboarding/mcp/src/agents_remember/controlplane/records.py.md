# mcp/src/agents_remember/controlplane/records.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/controlplane/records.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-01T18:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

`records.py` defines the `ar-gate-record/v1` envelope (`GateRecord`) — one
append-only, attributed snapshot of a decision point on a lifecycle — plus the
pure helpers that open and decide gates.

## Code Commentary

`GATE_RECORD_SCHEMA` is the versioned wire tag. `GateKind` (slice 09 extends it to
the full l-01 gate spine: plan-approval | worktree-intent | closeout-approval |
push-approval | integration-approval | cleanup-approval | agent-question |
provider-retry | alarm-ack), `GateState` (open | approved | rejected |
revision-requested | applied | cancelled | expired), and `DecidedVia` (chat |
dashboard | cli) are Literals so a typo cannot corrupt the audit trail. There is
**no separate `commit-approval` kind**: `closeout-approval` IS the commit gate —
closeout is the single commit-of-record for code + memory + ledger, and singular
commits route through it. Adding a gate kind stays a one-literal change (the
docstring's "extensible: a new gate kind is one literal" note). `DECISION_STATES` maps the
decision verbs (approve / reject / request-revision / cancel) to the resulting
state. `coerce_gate_kind(raw)` validates a raw string against the `GateKind`
literals (`get_args` + `cast`) so the MCP boundary can accept a plain `str`.

`GateRecord` is a Pydantic model with `extra="forbid"` and camelCase wire
fields (mirroring the observer event envelope); `schema_version` carries
`alias="schema"`, so records dump with `model_dump_json(by_alias=True,
exclude_none=True)`. **As of 260731-EFA-L5 it subclasses
`durable_store.DurableRecord` rather than `BaseModel` directly**, which is where the
`extra="forbid"` config now comes from (the local `model_config` line is gone) and which adds one
inherited field, `schemaVersion`.

The two version fields answer different questions and must not be collapsed: `schema`
(`ar-gate-record/v1`) names the record **vocabulary** — what these fields mean — while the
inherited `schemaVersion` versions the **durable-store contract** the log is written under: how
the file behaves, meaning ownership, serialization and torn-line policy. `schemaVersion` is
validated on the way in, so an unknown MAJOR raises `ValidationError` at parse time; that is what
lets `GateStore.read` fail loudly on it and `GateStore.read_for_projection` skip it, with no
version branch written into either reader. An unknown minor is accepted. Verified on this record
type: minor `1.99` accepted, major `2.0` rejected. L4 adds `GateEvidenceRef` (`kind="reviewer-verdict"`,
`ref`, optional `verdict`) plus `GateRecord.decidingRole` and
`GateRecord.evidenceRefs`.

**Three frozen parameter objects (260731-EFA-L2)** carry what a gate is raised against, what the
decider is handed, and what they answered:

- **`GateAnchor(lifecycle_id=None, enclosure=None, repo_id=None)`** — what the gate is raised
  against: the lifecycle that opened it, the enclosure it guards, the repository that enclosure
  changes. Every reader that matches a gate to work in flight matches on this triple.
- **`GateRequest(packet=None, required_decision=None, evidence_refs=None)`** — what the decider is
  handed: the packet to read, the decisions the gate will accept, and the evidence attached at
  open time.
- **`GateVerdict(decision, via, by=None, note=None, deciding_role=None)`** — one decider's verdict.
  These are load-bearing together: the closeout policy never reads them apart — a delegated
  approval is the `orchestration` channel AND a `manager` role AND an actor that is not the owning
  lifecycle — so a verdict assembled field by field is a verdict that can be assembled wrongly.

`create_gate(kind, *, gate_id, now, anchor=None, request=None)` returns a fresh `open` gate (the
caller mints the ULID `id` and `now`) and may attach initial evidence refs via the request;
`decide_gate(gate, verdict, *, now, evidence_refs=None)` returns a NEW snapshot (same `id`, new
`ts`) carrying the decision, the optional deciding role, and append-only evidence refs from the
previous snapshot plus the decision call. `verdict.decision` is one of `DECISION_STATES`; an
unknown verb raises `KeyError` here, because the tool boundary validates first for a clean message.
Note `decide_gate`'s `evidence_refs` stays a separate keyword — it is evidence attached *at
decision time*, distinct from `GateRequest.evidence_refs` attached at open time. `DecidedVia` now includes
`orchestration`, so delegated approvals can be attributed separately from
chat/dashboard/cli. `expire_gate(gate, now=...)` returns a NEW `expired`
snapshot for an open gate replaced by a newer lifecycle gate. `apply_gate(gate, ...)` (slice 6b)
returns a NEW `applied` snapshot — the transition a mutating tool writes once it
consumes an approval (decision attribution carries forward; only `state`/`ts`
advance). All helpers are pure.

## Invariants And Boundaries

- **Append a snapshot per state change; never mutate in place.** A gate's `id` is
  stable across its life; `ts` changes per snapshot, and readers fold by `id`
  (last-wins) for current state.
- `decidedBy` (actor/session/lifecycle), `decidedVia` (through what), and
  `decidingRole` (policy role) stay separate. Orchestration decisions name the
  deciding lifecycle/session in `decidedBy`; the policy layer rejects owner
  self-approval before such a snapshot is persisted.
- Evidence refs are append-only metadata on the gate snapshots. A reviewer
  verdict artifact is referenced by id/path, not inlined into the gate record.
- This is a persisted-record model, not an MCP response: the `gate_*` tools have
  their own response models in `models/gates.py`.
- **`schema` and `schemaVersion` version different things** — the record vocabulary and the
  durable-store contract respectively. Adding a gate field is a `schema` question; changing how the
  gate log locks, compacts or tolerates a torn line is a `schemaVersion` question.
- **No reader may branch on `schemaVersion`.** The validator on `DurableRecord` rejects an unknown
  major at parse time, which is what makes the strict and tolerant gate readers behave correctly
  without either of them knowing the rule. Add a version branch to a reader and the two policies
  stop following from one place.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mirrors the observer event envelope (camelCase, `extra="forbid"`, schema alias). | `Event` | mcp/src/agents_remember/observer/events.py:39-64 |
| The append-only store that serializes and folds these snapshots. | `GateStore` | mcp/src/agents_remember/controlplane/store.py:96-325 |
| Ids come from the local ULID mint. | `new_ulid` | mcp/src/agents_remember/observer/ulid.py:30-41 |
| `GateRecord` now subclasses `DurableRecord` and its docstring states why `schema` and `schemaVersion` answer different questions. | `GateRecord` | mcp/src/agents_remember/controlplane/records.py:84-116 |
| `DurableRecord` supplies the `extra="forbid"` config and the `schemaVersion` validator that rejects an unknown major and accepts an unknown minor. | `DurableRecord`; `schema_version_supported` | mcp/src/agents_remember/controlplane/durable_store.py:224-245; mcp/src/agents_remember/controlplane/durable_store.py:248-271 |

As of the 260703-L8 seam ruling the GateKind vocabulary includes `master-handover-approval`: the master-exit seam gate the manager raises with the reviewer verdict attached and the orchestrator decides (delegable, never human-pinned — human review concentrates at the super gate).

## 260718-CHATS-L5I Current Delta

`reopen_gate` now creates an answerable gate from a failed adapter decision while retaining the gate identity and attaching the failure detail. It is the records-layer counterpart to honest interaction failure handling; a failed delivery must not continue to look approved.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded that `GateRecord` now
  subclasses `durable_store.DurableRecord` instead of `BaseModel`: the local
  `model_config = ConfigDict(extra="forbid")` line is gone (the base supplies it) and one inherited
  field, `schemaVersion`, is added. Recorded why the record now carries two version fields and that
  they answer different questions — `schema` names the record vocabulary, `schemaVersion` versions
  the durable-store contract the log is written under — and that the validator on the base rejects
  an unknown major at parse time, which is what lets `GateStore.read` raise on it and
  `GateStore.read_for_projection` skip it with no version branch in either. Confirmed by direct
  construction: minor `1.99` accepted, major `2.0` rejected. No `GateRecord` field, alias, literal
  or helper changed. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `GateAnchor`, `GateRequest` and `GateVerdict` parameter objects and re-signed
  the two builders — `create_gate(kind, *, gate_id, now, anchor=None, request=None)` (the former
  `lifecycle_id` / `enclosure` / `repo_id` / `packet` / `required_decision` / `evidence_refs`
  keywords) and `decide_gate(gate, verdict, *, now, evidence_refs=None)` (the former `decision` /
  `by` / `via` / `note` / `deciding_role` keywords). `kind` became positional on `create_gate`.
  `decide_gate`'s decision-time `evidence_refs` stayed a separate keyword on purpose. All helpers
  remain pure and no `GateRecord` field changed. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): GateKind gains master-handover-approval (the ruled master-exit seam gate). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: added orchestration attribution
  (`decidedVia="orchestration"`, `decidingRole`) and append-only
  `GateEvidenceRef` / `evidenceRefs` so delegated gate decisions can cite
  reviewer-verdict artifacts. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-06-25T07:17+02:00 — Task 19: added pure `expire_gate(gate, now=...)` so creating a new lifecycle gate can supersede the previous open gate without deleting history. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S2 kind extension): `GateKind` gained `plan-approval`, `worktree-intent`, and `push-approval` (the full l-01 gate spine alongside the existing closeout/integration/cleanup/question/retry/ack kinds). NB `closeout-approval` IS the commit gate — there is no separate `commit-approval` (closeout is the commit-of-record for code + memory + ledger). Envelope/helpers otherwise unchanged. Refreshed the Code Commentary `GateKind` listing. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: added pure `apply_gate(gate, now=...)`, the `open/approved → applied` snapshot a mutating tool writes when it consumes an approval (the transition this module's docstring anticipated). No change to the envelope or the create/decide helpers. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the `GateRecord` envelope + pure `create_gate` / `decide_gate` / `coerce_gate_kind`. Verification metadata pinned until closeout stamps the 6a code commit.
