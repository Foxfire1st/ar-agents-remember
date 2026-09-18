# mcp/src/agents_remember/mcp/registration/closeout.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/closeout.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated |  2026-09-18T14:55+02:00 |
| lastVerifiedCommitHash | `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| lastVerifiedCommitDate | 2026-09-18T15:05:30+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## CCR-R12@v5 Current Public Contract

The registered closeout and integration tools advertise transaction previews and applies. A
closeout apply validates explicit approval, candidate/source identity, and Git safety before
committing code, refreshing and committing attributed external memory, and refreshing the
consumer ledger cache when possible.
Integration validates the prepared pair and publishes it through the existing ref-atomic path.
Neither public route promises or invokes strict code quality, memory quality, selected
certification, curator coherence, or independent review during normal execution; full suites are
only an explicit developer request. The older altitude-ladder wording below is historical
pre-R12 documentation and is superseded for these routes.

## Historical pre-CCR-R12 EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## 260731-EFA-L17 Change

The five tool declarations are all keyword-only (bare `*` — the L8 remediation completed
here for `worktree_cleanup`/`worktree_abandon`, which still had positional parameters),
and the published docstrings now state the quality altitude ladder: preview/apply
describe the leaf change-set-scoped contract (`--targeted`: changed files +
reverse-import closure + derived test subset, mandatory CRAP over the changed modules)
and say the full wrapper is NOT a leaf gate; `worktree_integrate` states that it runs the
altitude-routed gate itself before any merge (leaf targeted; master full with
host-managed RAM/swap by default and an optional explicit
`orchestration.qualityGate.memoryCapBytes`). The registered tool surface is
unchanged.

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a task:
`direct_landing` (the explicitly selected branch-addressed delivery for a leaf implemented without
an enclosure — L16-R8, policy-gated by `directExecutionEnabled`),
`worktree_closeout_preview`, `worktree_closeout_apply`,
`worktree_integrate`, `worktree_checkpoint_landing`, `worktree_cleanup`, `worktree_abandon`.

`worktree_checkpoint_landing` (260831-LOCR-L30, docstring corrected by 260831-LOCR-L34 and again by 260831-LOCR-L36) is the
partial-master landing route registered between `worktree_integrate` and `worktree_record_landing`.
Its published docstring is the contract a client sees: it **partially publishes** an **unfinished**
atomic master's accumulated line and keeps the master open, shares `worktree_integrate`'s whole preflight and ref move
while dropping only the completion assumptions (`worktree_integrate` proves the task document
`Completed`, one landed enclosure per canonical leaf, **and a completed closeout** — an unfinished master
has none of those), captures the master's own committed refs (the live series code work branch tip
and the live memory work branch tip) and proves the source ancestry before landing
exactly those, records the integration cell as `checkpointed` rather than `completed`, retires nothing
and runs no cleanup, and is MUTATING with a `dry_run` preview. The L34 correction matters because the
published text is the only thing a client reads: the old wording omitted the closeout requirement,
which is exactly what made the route unreachable.

**The L36 correction is the route's name.** The description used to open "Use this to pause a
master", which routes an ordinary stop request into a protected-branch publication: the ref move puts
the master's committed code and memory where every other master sees them, under an explicitly
required developer approval. A pause is a separate matter — it stops the master's work, publishes
nothing, moves no ref, and leaves its branch, worktrees and enclosure private. The published text says
so, and a case in `mcp/tests/test_tools.py` pins the distinction. **The stop itself is real since
260831-LOCR-L37**, registered as `worktree_pause` by the sibling working-half registrar
(`mcp/registration/worktrees.py::_register_worktree_stop_tools`), and its own description points back
at this publication as the separate, explicitly requested one. This route registers only the
publication; the L36 sentence above must not be read as "no such tool exists" — it did not at L36, and
it does now.

The public registration entry delegates to four cohesive helpers:
`_register_direct_landing_tools` for the branch-addressed direct landing (260815-DAG-L16),
`_register_closeout_command_tools` for preview/apply,
`_register_integration_command_tools` for integration/cancellation, and
`_register_reclamation_command_tools` for cleanup/abandonment. The `_tools` suffix is deliberate:
the structural exemption remains attributable only to tool declarations and registrar functions,
not arbitrary helpers. The split changes registration structure only; tool names, signatures, and
payload owners remain unchanged.

## Code Commentary

Closeout apply accepts typed `RedCatalogDisposition` values and forwards them as a tuple to the payload/application owner. These are explicit corrective dispositions, not permission to bypass a failed catalog or weaken gate authority.

Current IAS policy treats coverage as diagnostic and production CRAP above 20 as a review signal, not a numeric rejection. The retained registration docstrings still contain older mandatory-CRAP wording; that wording is stale and must not restore a metric gate. Full suite and whole-master review remain master-end obligations. The registrar preserves distinct commit messages and approval intent, and an accepted journal generation survives disposable queue loss.

### Logic

Current registered signatures expose only code and memory commit messages; direct landing
accepts only the memory message because its code commit already exists. Integration and checkpoint
landing take no ledger message, and PR landing records only code plus optional memory content.
The retained ledger is a downstream computed cache, never an MCP-requested Git output.

The preview/apply pair (`worktree_closeout_preview` L24-L46, `worktree_closeout_apply` L47-L76)
share `CloseoutCommitMessages(code, memory)`, built in each body from
the two flat message arguments. Apply keeps a **second** object, `CloseoutApproval(intent_note,
dry_run)`, precisely so the approval-bearing half cannot be confused with the commit text: folding
`dry_run` in with the messages would let a preview read as an approved apply.

**Historical quality-gate registration, superseded by the current transaction boundary above.**
The former docstrings stated a pre-commit gate order. Preview reports whether strict
project-owned quality under the selected project checks will run — since 260731-EFA-L4 the
description is specific about *what it runs over*: "over the staged task worktree before the code
commit", not merely "before the code commit".

Apply's docstring was rewritten in the same leaf, and it is now a conditional statement rather
than an unconditional one. It reads: when code would commit **AND the checkout carries the
project-owned quality wrapper**, apply resets the index, stages the whole task worktree, and runs
strict quality with diagnostic CRAP reporting **over exactly that staged content**, before any
code, memory, ledger, contract, or applied-gate **commit**; then commits code, memory and ledger
in order. It states four things the previous text did not:

- **Staging is what lets the gate see files the task created**, not only the ones it edited; the
  **reset** is what makes a retry stage what a first run would, instead of inheriting a refused
  attempt's index.
- **Staging is not undone when the gate refuses** — the checkout staged is the task's own
  disposable worktree.
- The **two refusals guard that staging step**, so they run only where the gate runs: apply
  refuses before staging when the code checkout is not a task worktree (a series/master contract
  records the repository path itself) or has unresolved merge conflicts.
- A checkout carrying **no wrapper** runs neither the gate nor those refusals and reaches the
  ordinary commit step's own `git add -A` exactly as it always has.

The blocker wording also narrowed from "before any … mutation" to "before any … commit", which is
the accurate claim now that staging is itself a mutation the gate performs. The published process
recommends preview before approval/apply, but apply independently validates the same effective
input and does not treat a prior preview as authority; apply requires `intent_note`.

The publication and reclamation tools forward flat:

- `worktree_integrate(contract_path, strategy='ff-only'|'replay', dry_run)` —
  checks accepted candidate/source and Git authority, then moves branch refs; protected branches need explicit approval.
- `worktree_checkpoint_landing(contract_path, strategy='ff-only'|'replay', dry_run)` — **partially publishes** an **unfinished** atomic master's line and keeps the master open;
  requires the same explicit developer approval as `worktree_integrate`; captures the master's own
  live code and memory work-branch tips and proves source ancestry; records `checkpointed`,
  retires nothing, runs no cleanup. It is not the pause: a pause publishes nothing and moves no ref.
- `worktree_cleanup(contract_path, dry_run, teardown_providers=True)` — removes worktrees and merged
  task branches **after** integration, and by default reclaims the worktree's isolated provider stack.
- `worktree_abandon(contract_path, dry_run, force)` — discards a task without integrating it. Unlike
  cleanup it needs no completed integration; without `force` it refuses dirty worktrees and unmerged
  branches and reports the commits, with `force=true` it discards them
  (`git worktree remove --force`, `git branch -D`). Since 260831-LOCR-L30 the series abandon guard
  also refuses a master whose integration cell reads `checkpointed`, not only `completed`.

### Conventions

Keep registered signatures and descriptions aligned with the application request models. Registrars pack inputs; they do not acquire a second publication authority.

### Invariants And Boundaries

- Keep `CloseoutApproval` separate from `CloseoutCommitMessages`.
- The public direct-landing description must distinguish its narrow leaf-without-enclosure route
  from ordinary master/series closeout and integration; contract kind alone does not select direct
  execution, and those ordinary lifecycle routes never require `directExecutionEnabled`.
- Preview is the non-mutating inspection surface, but it is not durable authority that apply may
  trust. Preview and direct apply each normalize the same effective input independently; apply
  additionally carries `CloseoutApproval`. A direct apply must therefore remain safe without a
  preceding preview.
- Closeout is worktree-only; the retired `direct_closeout_*` tools are not registered anywhere.
- Application composition lives in `application/worktree_tools.py`; Git publication and recovery
  belong to the worktree operation owners.
- **These docstrings are the published MCP tool descriptions**. They must describe the current
  candidate/source checks, explicit approval, and code/memory publication behavior. The historical
  wrapper-gate description above is superseded and must not restore a normal quality gate.
- Keep internal registrar helper names ending in `_tools`; the suffix is part of the narrow
  structural-rule attribution for this declaration-only route.
- **The checkpoint docstring must name the whole completion refusal set, not two of three
  (260831-LOCR-L34).** It said the route dropped only the two "master is finished" assumptions while
  the code also demanded a completed closeout — and that omission described a route a client could
  not actually use. A published refusal list is a promise about what will *not* happen; keep it
  complete when the gate changes.
- **The checkpoint description must present a partial publication and deny being the pause
  (260831-LOCR-L36).** "Use this to pause a master" invited an agent to publish unfinished work for
  an ordinary stop request — changes the developer never asked to publish. The text must keep saying
  that the route moves committed refs onto the protected source branch under explicit approval, and
  that pausing is a separate matter which is NOT this call. `mcp/tests/test_tools.py` pins the
  wording (`PUBLISH`, "not a pause", "separate matter and is NOT this call") and asserts the old
  invitation is gone.

### Todos

No additional file-local TODO is established by this candidate review.

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registered direct/ordinary closeout and integration tools expose no ledger message or landed-ledger argument. | `_register_direct_landing_tools` | mcp/src/agents_remember/mcp/registration/closeout.py:45-89 |
| The payload builders these forward to. | `worktree_closeout_preview_payload`; `worktree_closeout_apply_payload`; `worktree_integrate_payload`; `worktree_checkpoint_landing_payload`; `worktree_record_landing_payload`; `worktree_operation_control_payload`; `worktree_cleanup_payload`; `worktree_abandon_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:110-238 |
| The checkpoint-landing tool declaration and the payload builder it forwards to. | `worktree_checkpoint_landing_payload`; `worktree_checkpoint_landing` | mcp/src/agents_remember/mcp/tools/worktree.py:159-174; mcp/src/agents_remember/mcp/registration/closeout.py:172-199 |
| `CloseoutCommitMessages` and `CloseoutApproval` remain distinct request concepts. | `CloseoutApproval` | mcp/src/agents_remember/application/worktree_tool_requests.py:131-136 |
| Refuse to stage anywhere except a task's own throwaway worktree. | "Refuse to stage anywhere except a task's own throwaway worktree." | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:26-26 |
| Refuse before staging when the checkout has unresolved conflicts. | `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:44-56 |
| Prepare and certify a fresh candidate through the ordinary gate entry point. | "Prepare and certify a fresh candidate through the ordinary gate entry point" | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:145-145 |
| The case that pins the checkpoint description as a partial publication and denies it is the pause. | `test_the_checkpoint_description_publishes_rather_than_pausing` | mcp/tests/test_tools.py:289-311 |
| The wrapper condition decides whether the gate — and therefore staging and its refusals — runs; the preview exposes the selected mode, executor, and cap. | `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:149-192 |

## Historical R39 Integration Tool Contract

Before the current transaction-only boundary, the integration description stated that leaf integration lands the acceptance already
bound to its closeout commit without rerunning it. Only master integration owns a new acceptance
run: full mode through the pinned Dagger executor.

## 260815-DAG Master Full-Gate Repair

`_register_direct_landing_tool` was renamed to `_register_direct_landing_tools` (the direct-landing registration group); the registered tool surface is unchanged.

## 260821-CLIVE-L1 Public Surface

Worktree closeout and direct landing expose optional message fields syntactically because enabledness is route/contract/candidate-dependent; runtime validation requires each enabled field to be stripped and nonblank. Worktree preview/apply accepts code and memory fields and returns `effectiveInput` or field-specific `invalidFields` with `resolvedPlan` and `correctedCall`. Direct landing accepts memory intent only: verified-existing code is not applicable. The memory message is required only when its contract-derived leg is enabled; a typed not-applicable leg may omit it. Invalid input is refused before authority or Git.

## 260821-CLIVE-L2 Current Contract

The current source seams include `register_closeout_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `register_closeout_tools` at this ownership boundary. | `register_closeout_tools` | mcp/src/agents_remember/mcp/registration/closeout.py:37-42 |

## 260821-CLIVE Final Closeout Tool Descriptions

The public descriptions now state the durable ownership boundary directly: direct landing and
closeout recovery use the retained operation journal, never a transient landing lock or queue row;
queue invalidation does not affect an accepted generation. Cleanup and abandon first archive and
read back bounded canonical enclosure evidence, publish the external receipt, and only then remove
worktrees, branches, reports, providers, and the enclosure root. Active, ambiguous, unreadable, or
mismatched evidence refuses deletion. Shared grade/admission request types come from the canonical
closeout-source model.


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation source applies. | N/A | N/A |

## Update History
- 2026-09-18T14:55+02:00 — 260918-TSIP-L3 curator (citation repair, `ar/260918-tsip-l3-ar`, base `a12c511f`): `test_the_checkpoint_description_publishes_rather_than_pausing` was repointed `:287-309 → :289-311`. The claim's wording was re-read against the new bytes and is unchanged — only the range moved, because this leaf's edit to `mcp/tests/test_tools.py` inserted lines above it. `lastUpdated` advances with this repair; `lastVerifiedCommitHash` is deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real code commit.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Documented the removed public ledger arguments and the surviving two-output publication contract. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-13T17:20:55+00:00: Generated citation repair: `worktree_closeout_preview_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:110-118. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: corrected the L36 paragraph, which ended "and no worktree
  tool performs it" — true at L36, false since this leaf added `worktree_pause` in the sibling
  working-half registrar. The paragraph now records the L36 state as history, points at the stop's own
  registration, and states that the two descriptions name each other. This route's registration,
  signature, order and payload owner are unchanged by L37. Verification metadata remains closeout-owned;
  no acceptance claim.
- 2026-09-13T17:42+02:00 — 260831-LOCR-L36: recorded the corrected published description of
  `worktree_checkpoint_landing`. It opened "Use this to pause a master", which invited an agent to
  publish unfinished work for an ordinary stop request: the route moves the master's committed code
  and memory refs onto its super branch under an explicitly required developer approval, where every
  other master sees them. The description now presents a partial **publication** and states that
  pausing is a separate matter which is NOT this call (stopping the master's work publishes nothing,
  moves no ref, and leaves its branch, worktrees and enclosure private; no worktree tool performs
  it). Added the matching invariant, the pinning case reference in `mcp/tests/test_tools.py`, and the
  L36 correction note on the route's name. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:50+00:00 — 260831-LOCR-L34: recorded the corrected published docstring for
  `worktree_checkpoint_landing`. It had listed only the two "master is finished" assumptions the route
  drops, omitting the **completed-closeout** requirement `worktree_integrate` also proves — the
  omission described a route no client could use. The docstring and this card now state the full
  refusal set, that the checkpoint captures the master's own committed refs and proves their ledger
  mapping, and that the explicit developer approval is unchanged. Added the matching invariant that a
  published refusal list must stay complete. Docstring only in the source; no behavior change.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: registered `worktree_checkpoint_landing` in
  `_register_integration_command_tools` between `worktree_integrate` and `worktree_record_landing`,
  recorded its published docstring contract, added it to the landing-half purpose list and the
  destructive-tools list, noted the widened series abandon guard, and re-derived the shifted
  reference ranges. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_closeout_preview_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:98-106. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `register_closeout_tools` repointed to mcp/src/agents_remember/mcp/registration/closeout.py:36-41. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `CloseoutCommitMessages`; `CloseoutApproval` repointed to mcp/src/agents_remember/application/worktree_tool_requests.py:111-117; mcp/src/agents_remember/application/worktree_tool_requests.py:120-125. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=ae77428650fdcc422422a1323a9aed533d4bfbf787961cff35f2a561d7ff7f13; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T22:15:27+00:00 — Reconciled retained registration behavior and removed deleted wiring-test claims; current policy and verification provenance preserved.

- 2026-09-05T06:24:16+00:00: Generated citation repair: `worktree_closeout_preview_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:127-135. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T20:30+02:00 — 260831-DER: corrected the published direct-landing description so MCP
  clients see the exact policy boundary: an explicitly selected leaf delivery without an enclosure,
  not ordinary master/series closeout or master-to-parent integration.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout model/control import relocations; registered tools, request behavior, and quality/closeout boundaries are unchanged.
- 2026-08-24T21:43+02:00 — No content impact: the file-size repair repointed
  `LifecycleControlAction` to its canonical integration owner; registered tools, schemas, and
  behavior are unchanged. The closeout request-concept reference now targets their extracted
  single owner. Verified at source commit `23d35f77`.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged final journal recovery and terminal archive/destruction semantics into the registered public tools. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: aligned the published
  direct-landing description with enabled-leg-dependent messages and typed not-applicable omission;
  corrected the already-impacted card's stale registrar name and preview-as-authority wording from
  exact source. Bound to reviewed candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`,
  full diff SHA `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`,
  same-reviewer PASS; commit-derived verification metadata remains unchanged until governed closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: renamed the direct-landing registration helper to `_register_direct_landing_tools`. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: registers `direct_landing` (branch-addressed direct
  landing, L16-R8) through the new `_register_direct_landing_tool` helper; preview/apply
  citations re-anchored to their shifted lines. Verified at code commit a9d50e08.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: aligned the registered tool description with the
  leaf-no-rerun/master-full boundary. Verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the closeout tool descriptions to the
  extracted staged-quality owner and retained the same Dagger-before-commit promise. Verification
  remains closeout-owned.

- 2026-08-13T12:26+02:00 — L23 structural-rail repair: recorded the exact three internal registrar
  names and their `_tools` suffix, which keeps the registration exemption constrained to tool
  declarations/registrars. Public tool names, schemas, descriptions, and payload owners are
  unchanged; verification provenance remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: recorded the three cohesive registration groups while preserving the one public registration entry point and tool contracts. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: aligned the MCP
  closeout/integration tool descriptions with the host-managed full-gate
  default and optional explicit cap. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: regenerated closeout staging
  ranges after the quality-runner responsibility split; registered behavior is unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the completed
  keyword-only signatures (cleanup/abandon), the altitude-ladder tool docstrings
  (leaf `--targeted`; full wrapper at the master integration gate, memory-capped;
  `memory_quality_check` per leaf), and refreshed the preview/apply ranges plus the
  closeout/gate reference rows to the post-L17 source. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 5 citation rows (payload builders, CloseoutCommitMessages/CloseoutApproval, wiring/description/staged-gate tests) and converted 2 history prose line citations to cit: forms; the preview/apply ranges L24-L42/L45-L76 verified still exact against the frozen source. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:28+02:00 — 260731-EFA-L4 curator: the card summarised both docstrings as
  "apply runs that quality before any code",
  which is now both under- and over-stated. Verified against the diff and the current source and
  corrected it. Preview cit:([`worktree_closeout_preview`], mcp/src/agents_remember/mcp/registration/closeout.py:82-104) now says quality runs "over the staged task worktree" before the
  code commit. Apply cit:([`worktree_closeout_apply`], mcp/src/agents_remember/mcp/registration/closeout.py:106-141) became conditional — the gate runs only when code would commit
  **and** the checkout carries the project-owned quality wrapper — and now states the four facts
  the card was missing: the reset-then-stage-the-whole-worktree step (so the gate sees files the
  task created, not only those it edited, and a retry stages what a first run would rather than
  inheriting a refused attempt's index), that staging is *not* undone when the gate refuses
  (the checkout is the task's own disposable worktree), that the two refusals — code checkout is
  not a task worktree, or has unresolved merge conflicts — guard the staging step and so fire only
  where the gate runs, and that a wrapper-less checkout runs neither and reaches the ordinary
  commit step's `git add -A` unchanged. The blocker wording also narrowed from "before any …
  mutation" to "before any … commit", which is the accurate claim now that staging is itself a
  mutation the gate performs; the two reference rows that echoed "quality-before-mutation" were
  reworded to match. Added the docstrings-are-published-contract invariant, line ranges for the
  preview/apply pair, and two reference rows (the modules implementing the staging/refusals, and
  the gate's test file). The Repo-Internal References header gained the `Citations` column.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The five landing-half
  declarations moved out of `server.py`; preview/apply now pack `CloseoutCommitMessages` and apply
  additionally packs `CloseoutApproval`. Verification metadata pinned to the pre-change commit until
  closeout stamps the L2 code commit.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
