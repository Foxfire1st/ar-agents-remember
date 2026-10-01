# docs/design/ — Design Documentation Overview

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| sourceRoute            | `docs/design/`                              |

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

### 260713-TES-L1 Rename — Observable-Lifecycle Prose

`observable-lifecycle.md` was refreshed to agent-notifier wording (the sweep/heartbeat prose now
names the agent-notifier); the design specs themselves are historical records and their route
shape is unchanged.

`docs/design/` holds the **in-repo design documentation** for Agents Remember, including the dashboard and Python evidence system — durable design
references kept beside the code so the design intent survives across sessions without running the dashboard.
It covers the engine-room visualization, top-level observable-lifecycle and harness-matrix notes, and the
`dashboard/` evidence set. FEUI-L8 makes that evidence set the bounded home for the canonical Chats scenario
catalog, closeout evidence, and upstream contract register instead of packing those concerns into the root
dashboard route overview.

## Hot Path Summary

`observable-lifecycle.md` describes code/memory-content Git transaction phases and a separate computed ledger cache. A cache refresh is not a third transaction phase or a closeout/integration acceptance condition.

In-repo design documentation for the dashboard and Python verification architecture. Child route `engine-room/` is the engine-room design
reference — a living spec paired with the prototype/scenario player the React engine room was built from.
The `dashboard/` folder now carries the FEUI-L8 scenario matrix and reproducible accessibility/performance
evidence, the closeout evidence pack, and the upstream-register boundary for contracts the frontend must not
fabricate. Top-level notes include `observable-lifecycle.md`, `harness-matrix.md`, and the three Python
evidence documents listed below.

## Child Routes

- `engine-room/` — the engine-room design reference: the living visual-language spec + the prototype /
  scenario player the `dashboard/src/panels/engine-room/` renderer was built from. See
  [engine-room/ overview](engine-room/overview.md).

## Route Model

- `engine-room/` — the engine-room visual design reference (see child route above).
- `dashboard/scenario-catalog.md` — the canonical cockpit scenario/evidence catalog, including L8
  accessibility, performance, fetch, invariant, and end-to-end coverage.
- `dashboard/session-cockpit-closeout-evidence.md` — the bounded closeout evidence pack for the complete
  Sessions-to-Chats cockpit series.
- `dashboard/session-cockpit-upstream-register.md` — the explicit serving-contract gaps plus the ruled
  one-Chats cutover and duty-transfer record. Its UA-1-absent account describes the FEUI-L8
  handoff snapshot; later adapter-normalized conversation work must be checked in the serving
  and conversation routes rather than inferred from that old register.
- `observable-lifecycle.md` — top-level design note on the observable lifecycle, now including
  `lifecycle_gate` as the public gate junction plus the interaction-retention tiers: durable work
  records stay, gate/inbox interactions delete on response, dismiss, clear, consume, or the
  24-hour passive TTL. HFX2-L8 adds the operator-inbox storm recovery runbook: quarantine to `.bak`,
  park/terminate only dead terminal rows, restart cleanly, verify heartbeat/backlog metrics, and
  never delete transcripts.
- `harness-matrix.md` — top-level design note on the harness matrix. **Present but not yet file-onboarded**
  (no sidecar created in this pass).
- `python-evidence-system.md` — the consolidated evidence taxonomy, dependency-owned selection and
  retry, cadence, lifetime, and accepting-consumer design.
- `python-pytest-bootstrap.md` — the Dagger admission and reusable bootstrap boundary.
- `python-test-evidence.md` — the candidate-bound diagnostic-versus-certifying evidence authority.
  The former `python-direct-cohort.md` and `python-direct-diagnostics.md` notes were retired into
  these three canonical documents rather than retained as competing design contracts.

## Invariants And Boundaries

- These are **design reference documents**, not shipped application code. The engine-room HTML docs animate
  in CSS purely for portability; the dashboard itself animates in GSAP + Motion (CSS static-only) per the
  engine-room motion doctrine.
- Design intent flows **doc → code**: the design references are the authority the dashboard renderers are
  built to satisfy; keep them and the renderers in sync.
- The L8 evidence documents record tested behavior and missing upstream contracts. They do not enlarge the
  product contract: the one product-facing Chats destination is backed by the session cockpit, Operations
  remains the default, RailChat remains contextual, and the register's outstanding transcript/history asks remain dated FEUI evidence rather than a
  statement that the current product has no normalized conversation feed.
- `observable-lifecycle.md` is covered by file-level onboarding; `harness-matrix.md` remains present but
  not yet file-onboarded, so document only verified harness-matrix facts when it is onboarded later.

## Evidence

### Docs References

The active memory repository's `system/sources.md` has no configured Domain Documentation entries. This
overview was refreshed from the same-repository design documents, reviewed FEUI-L8 implementation/tests,
and the accepted worker/reviewer evidence.

No configured external Domain Documentation source governs this route.

### Cross-Repo References

The FEUI-L8 design evidence and Chats ruling are repository-local. No cross-repository implementation was
needed to establish the route model.

No applicable cross-repository source was found.

### Repo-Internal References

The engine-room design reference child route ([engine-room overview](engine-room/overview.md), living spec + prototype) governs the dashboard engine room.
The dashboard engine-room renderer ([dashboard engine-room overview](../../dashboard/src/panels/engine-room/overview.md)) is governed by the engine-room design docs.
- FEUI-L8's canonical scenario, accessibility, performance, and invariant evidence. [1]
- The explicit upstream gaps and one-Chats cutover ruling. [2]
- The bounded series closeout evidence pack. [3]

Current working-candidate evidence for this route:

- The implementation produces/reuses memory content before refreshing its cache (since MIK-R09 validating a converted leaf's exact tree first). [4]

## R39 Design Evidence Disposition

The cockpit performance/evidence design document now labels its test-capable measurement command as
an internal nonce-attested Dagger invocation and explicitly refuses host execution. This is an
evidence-location clarification; the dashboard architecture is unchanged.

## CCR Selection And Evidence Contract

`python-evidence-system.md` now requires typed incomplete selection to stop before Gate 2.
Unresolved ownership never silently expands to safe-full; deleted tests leave the population,
and irrelevant inputs remain explicit. The immutable selector result binds candidate,
configuration, scope and dependency reasons. Retry binds that selector digest and may refresh
only the already admitted population when its cached proof is unusable.

## 260824-PDLS Evidence-Authority Design

The Python test-evidence design now separates diagnostic execution from certifying evidence,
defines the package-root bootstrap boundary, and records Dagger as the sole acceptance authority.
The document also captures fixture ownership, proof lifetime, dependency-derived selection, and
the rule that diagnostic success cannot satisfy a lifecycle gate.

The final consolidation removes the two narrower direct-cohort/direct-diagnostics notes. Their
still-valid content is carried by `python-evidence-system.md`, `python-pytest-bootstrap.md`, and
`python-test-evidence.md`; deletion prevents an obsolete diagnostic-first contract from competing
with the accepted authority model.


## Integrated IAS Recovery Contract

`python-pytest-bootstrap.md` now permits ordinary isolated host pytest for development and the repository declares `unit_case_budget = 2000` / `integration_case_budget = 300` (`pyproject.toml:168,176`). It **superseded** the 1,000 / 150 figures this paragraph carried, which were raised 1000 → 1500 → 2000 (unit) and 150 → 250 → 300 (integration) by `260915-CAPS-L8`, `260831-LOCR-L37` and the 2026-09-17 ruling. Coverage is diagnostic, and production CRAP20 prompts review rather than blocking delivery. Focused checks support leaf work; full-suite execution and whole-candidate review belong at the end of the assembled master. Dagger admission remains mandatory for certification; the retired Candidate-A analyzer and route-measurement machinery are not restored.

## CCR-L42 Review-Authority Route Update

`python-test-evidence.md` now names `worktrees.route_review_scope.require_current_route_review` as
the route-review owner. Review runs at the owning altitude: atomic child leaves defer to the
accumulated canonical master review at master-to-parent integration, while standalone and
organizational leaves retain their applicable independent route review. The evidence and
certification model remains unchanged; this update records where the route review is owned.

## 260918-TSIP-L4 — The Bootstrap Note States Its Git Prerequisite, And Its Budget Figure Is Corrected

`docs/design/python-pytest-bootstrap.md` gained a three-line prerequisite (**`:22-24`**, file
**50 → 53 lines**): *"Every command needs a Git checkout: the evidence-lane hook enumerates the
test population through `git ls-files`, so an exported (`git archive`/tarball) tree must run
`git init` and `git add -A` first or collection fails instead of running."*

The requirement is new and it is real: `260918-TSIP-L4` registered
`agents_remember_test_support.testing.evidence_lanes` in `mcp/tests/conftest.py`, whose
`pytest_collection_modifyitems` calls `load_lane_manifest`; the loader enumerates the population
through `git ls-files`, so an exported tree now fails collection with
`ScopeError … fatal: not a git repository` rather than running. **This route is where an operator
reads test policy** (`AGENTS.md` routes a seat here for "the current test policy and commands"),
which is why the statement went here and not only into the comment at the registration site.

**The budget figure in this overview's body was wrong and is corrected in the paragraph above:**
the repository declares `unit_case_budget = 2000` and `integration_case_budget = 300`
(`pyproject.toml:168,176`), not 1,000 unit / 150 integration. The superseded values are recorded
rather than deleted, and this is a `T45` find — no check reads a number in prose.

## 260713-TES-L5 Route Impact — Fact-Relay Recovery Language

`observable-lifecycle.md` (this route's design authority) refreshed its recovery runbook:
`ladder-resolved` is legacy parse-compat (the timed escalation ladder is retired) and
retired/absent-target rows resolve through the sweep's landing/ceiling/grace paths.
