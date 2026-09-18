# mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T21:21+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T21:21+02:00 against this pair's code base `e9678c56`; the module itself is an
**uncommitted candidate** at that base — it is untracked in the code worktree
(`git status --porcelain` = `?? mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py`), so no
commit contains it and nothing here asserts that it passed review. Normal closeout owns the final
verification-metadata stamping.

## Purpose

Pins the reviewer role's half of the completion relay: a short-lived reviewer seat's **canonical
terminal truth**, produced by observation, wakes the reviewer's **current** manager as one durable
inbox row — with no completion post from the reviewer and no dependence on the terminal-session read
route. Six cases in one class, `ReviewerTurnOwnerWakeTests`
(`mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py:269-655`).

The module is deliberately not a second owner for the relay it rides. It asserts one role's
production wiring end to end — the reviewer's turn actually reaching its manager — where
[test_state_signal_relay.py](test_state_signal_relay.py.md) owns the relay's own structural contract
(current-manager replacement at action time, per-subject topology refusal, no-row/no-marker behavior
while an owner is absent). The two helpers it imports rather than rebuilds,
`_accepted_paster` and `_write_task_topology`, stay that module's fixture contract.

## Code Commentary

### Logic

The chain under test is the production chain, driven from adapter evidence rather than from catalog
truth the test typed in. `_Bridge` (`:230-266`) scripted for exactly one seat supplies the reviewed
seat's process activity and its native terminal-evidence page per pass, and reports a live turn in
progress with no terminal evidence for every other observed session — so the script belongs to the
reviewer alone and not to whichever row the sweep visits first. `_terminal_projection` (`:210-216`)
then runs the **real** lift, `latest_native_terminal_evidence` over a `NativeEvidencePage`, so the
terminal outcome and the evidence identity come out of the projector registry rather than out of this
module. The real `TerminalCatalogLivenessSweeper` over a real `TerminalCatalog` performs the
observation passes; `run_agent_notifier_sweep` then derives the finding, resolves the current
structural owner and persists one durable row. `_AliveHost` (`:163-184`) is the tmux double that
answers "session alive": it is the process boundary, not the relay under test, and its `gone` set
keeps a departed seat departed across a sweep instead of re-probing it back to life.

Six cases, each protecting a distinct boundary:

1. `test_leaf_reviewer_completion_reaches_the_current_manager_without_a_completion_post` (`:366-439`)
   is the wake itself. The row is asserted **truthless before** the observation pass (`turn_state`,
   `terminal_outcome` and `terminal_evidence_id` all `None`) and produced by that pass, so a relay fed
   by a hand-written `completed` row, a worker-only relay, or a relay that stopped lifting terminal
   evidence would each leave the manager asleep. The durable row is addressed to the manager's
   **document** and current occupancy, carries the leaf as the subject document, and holds while the
   owner is mid-turn: zero submissions, `state=pending`, `deliveryState=queued`, no read-side traffic
   in the scenario. The manager then reaches a turn boundary on a later tick and the *same* row lands
   exactly once.
2. `test_liveness_readiness_and_pane_text_alone_never_authorize_the_reviewer_wake` (`:441-480`) is the
   non-vacuity guard on eligibility. The row is proven endable through the real observer — live
   bridge, `control_state="ready"`, and a pane diagnostic that itself reads `turn-ended` — while
   carrying no canonical outcome and no evidence identity, so liveness, control readiness and the
   pane's own opinion authorize nothing. The control half appends a canonical projection and the
   identical row wakes the manager, so the silence is about missing evidence and not about a fixture
   that could never emit.
3. `test_interrupted_reviewer_wakes_as_interrupted_and_is_never_read_as_accepted` (`:482-515`) proves
   the other eligible outcome survives the relay as itself: `interrupted` is reported as
   `outcome interrupted` with `interrupted_by=unknown` (no developer interrupt is attributed that
   never happened), the leaf document's bytes are unchanged, and no verdict vocabulary is spoken.
4. `test_reviewer_wake_follows_the_current_manager_not_a_departed_generation` (`:517-553`) is the
   addressing boundary. The reviewer's recorded `spawned_by_session` names an exited manager
   generation; a relay that reused that brief-stamped runtime id would wake a dead seat and leave the
   live manager asleep. The one durable row is addressed only to the current manager, and the departed
   generation receives nothing.
5. `test_one_terminal_evidence_identity_yields_exactly_one_reviewer_signal` (`:555-603`) is
   idempotence: re-observing the same evidence identity after the first row has landed — when
   coalescing onto a pending row can no longer absorb a repeat — mints no second signal, and the row
   id and text are unchanged.
6. `test_a_failed_reviewer_turn_never_wakes_the_manager_and_stays_eligible` (`:605-651`) is the
   negative control that makes the eligible set a claim rather than an accident. `failed` **is** real
   terminal truth — the pi projector settles `stopReason="error"` into `outcome="failed"` while still
   carrying an evidence identity, so the row arrives with both terminal fields present and a
   non-canonical outcome. Widening the eligible set to any non-null outcome would leave every
   truthless row refused and expose only this one, which is why the case is asserted on the derived
   row rather than on an empty terminal claim. The refusal also consumes nothing: no marker is
   stamped, and the same seat waking later with a canonical turn still reaches its manager.

### Conventions

`unittest.TestCase` with module-local private harness classes; a `tempfile` coordination root whose
topology is written by the imported `_write_task_topology`, and one seeded structural row per seat.
Nothing here composes the serving app or issues an HTTP request, starts a process, touches a provider,
or publishes anything durable except the ordinary inbox row under test, so the hermetic
`unit-regression` lane is its behaviour-preserving classification (see the lane row below). The
structural rows are created directly, which is the permitted setup boundary; what may not be
pre-populated is the terminal truth under test, and case 1 asserts that absence before the pass.

### Invariants And Boundaries

Eligibility is the canonical completion fact and nothing else: a live session, a ready control state,
a pane that self-reports the turn ended, or the mere presence of *some* terminal outcome must not
authorize a wake. The eligible outcome set is production's — `completed` and `interrupted`
(`mcp/src/agents_remember/serving/state_signals.py:245-251`) — and the `failed` boundary is
load-bearing rather than defensive: it is the one non-canonical outcome that is production-reachable
*with* an evidence identity, so a test that only proved "no terminal claim means no wake" would not
constrain the real decision.

The wake must be addressed by current occupancy and by the manager's **document**, never by the
runtime id the reviewer spawned under, and it must be minted once per evidence identity. Silence on a
refused outcome must not consume the episode: the `state_signal_emitted_for` marker stays unstamped so
a later canonical turn still reaches the manager.

The relay wakes; it does not read. No case allows verdict vocabulary in the row's own text, and the
relay is asserted not to depend on the terminal-session read route, which is the point of driving
observation rather than a read-side projection. What is faked stops at the external process port (the
tmux host) and at the reader seam (`_Bridge` supplies a snapshot and a native page); the lift, the
outcome and the evidence identity are production's.

The module claims nothing about the relay's own structural rules — action-time owner replacement,
per-subject topology refusal and absent-owner behavior are
[test_state_signal_relay.py](test_state_signal_relay.py.md)'s contract — and nothing about
`worker`-role or `manager`-role relays, which have their own leaves. Lane membership is selection and
cost classification only: it is not execution, certification or acceptance evidence.

### Todos

None. The six cases are complete for `LOCR-R06@v1`; the candidates for extension (another role's
relay, or a further terminal outcome) belong to the leaves that decide them.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned relay behavior, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These rows describe the production behavior and the candidate that protects it. They are not a
certification result, and the candidate is uncommitted.

| Finding | Anchor | Source |
| --- | --- | --- |
| The eligibility decision the module pins: a harness row, still running, with a resolvable owner, an ended turn, a canonical outcome, an evidence identity, and no marker already stamped for that identity. | `_state_signal_finding` | mcp/src/agents_remember/serving/state_signals.py:237-260 |
| The exact eligible outcome set — `completed` and `interrupted` — which is why `failed` is refused rather than merely unproven. | "completed"; "interrupted" | mcp/src/agents_remember/serving/state_signals.py:245-251 |
| The idempotence marker: the same seat does not re-emit for an evidence identity it already emitted for, which is what makes one review produce one wake. | "entry.state_signal_emitted_for != entry.terminal_evidence_id" | mcp/src/agents_remember/serving/state_signals.py:250-250 |
| Current-occupancy addressing for a subordinate, including the reviewer branch that resolves a reviewer's manager from the structural parent role and document. | `_manager_for_subordinate` | mcp/src/agents_remember/serving/state_signals.py:86-109 |
| The finding evaluation the module drives directly in its silence cases, returning no finding while the eligible set is unsatisfied. | `evaluate_state_signal_findings` | mcp/src/agents_remember/serving/state_signals.py:199-207 |
| The derived durable row's own text, asserted to carry the outcome and evidence identity and to speak no verdict vocabulary. | `state_signal_ask`; `state_signal_response` | mcp/src/agents_remember/serving/state_signals.py:506-518; mcp/src/agents_remember/serving/state_signals.py:521-527 |
| The real notifier sweep the module drives to persist the wake and to land it at the owner's next boundary. | `run_agent_notifier_sweep` | mcp/src/agents_remember/serving/agent_notifier.py:96-190 |
| The real terminal-evidence lift the module uses instead of typing an outcome: the projector registry decides the outcome and the evidence identity. | `latest_native_terminal_evidence` | mcp/src/agents_remember/serving/terminal_evidence.py:146-184 |
| The real observer whose passes produce the terminal truth the wake rides on. | `TerminalCatalogLivenessSweeper`; `LivenessProbe` | mcp/src/agents_remember/serving/terminal_liveness.py:149-322; mcp/src/agents_remember/serving/terminal_liveness.py:90-113 |
| The wake scenario class and its single-seat scripted adapter endpoint. | `ReviewerTurnOwnerWakeTests`; `_Bridge` | mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py:269-655; mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py:230-266 |
| The tmux double that answers "session alive", with the `gone` set that keeps a departed generation departed. | `_AliveHost` | mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py:163-184 |
| The negative control: `failed` is real terminal truth with an evidence identity, is not wakeable, and consumes nothing. | `test_a_failed_reviewer_turn_never_wakes_the_manager_and_stays_eligible` | mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py:605-651 |
| The fixtures this module imports rather than rebuilds, owned by the sibling relay card. | `_accepted_paster`; `_write_task_topology` | mcp/tests/test_state_signal_relay.py:120-132; mcp/tests/test_state_signal_relay.py:149-193 |
| The sibling module that owns the relay's own structural contract. | `StateSignalRelayTests` | mcp/tests/test_state_signal_relay.py:196-607 |
| The candidate classifies this module once, in the explicit unit-regression lane. | "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" | mcp/tests/test-evidence-lanes.toml:114-114 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py"` → `mcp/tests/test-evidence-lanes.toml:92-92`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T19:21:00+00:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l06`, pair code base `e9678c56`, memory base `ee93a0fc`): created this file card for
  the leaf's new reviewer-relay module — 6 cases in one class, 655 lines, sha256 `aaed2736…` — and
  recorded the contract each case protects: the wake produced by observation rather than seeded, the
  eligibility boundary that refuses liveness/readiness/pane text, the `interrupted` outcome preserved
  as itself, current-occupancy addressing past a departed manager generation, one signal per evidence
  identity, and the `failed` negative control that makes the eligible set a claim. Recorded the
  production anchors that make the boundary real rather than defensive — the eligible set at
  `state_signals.py:245-251`, the marker at `:250`, and the reviewer-specific owner resolution at
  `:86-109` — and the boundary the module deliberately does not claim (the relay's own structural
  rules, owned by the sibling card). The lane row this card cites is
  `mcp/tests/test-evidence-lanes.toml:68`. The candidate is uncommitted, so no acceptance is implied
  and verification metadata remains closeout-owned; no stamp advanced.
