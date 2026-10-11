# docs/design/ — Design Documentation Overview

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Design now removes model-facing signals while retaining session-driven states/gates.

### Superseded inventory

- Pre-repair card claim: Route Model still names lifecycle_gate as the public junction. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `docs/design/observable-lifecycle.md:1-5,73-94`.
- Source comparison: `docs/design/observable-lifecycle.md:275-312`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| sourceRoute            | `docs/design/`                              |

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

`docs/design/` holds the design documentation that is kept in the code repository: the design of
the observable lifecycle, the Python test and evidence design, the dashboard's review and scenario
documents, and the engine-room design reference. The documents are references beside the code;
they are not shipped application code.

## Child Routes

- `engine-room/`: the engine-room design reference, a visual-language document and a scenario
  prototype for the dashboard's engine-room renderer. See
  [engine-room/ overview](engine-room/overview.md).

## Route Model

- `observable-lifecycle.md`: the design of the observable lifecycle. Its sections cover the
  lifecycle entity, the event substrate, gates and the return channel (with `lifecycle_gate` as
  the public gate junction), the read packet, placement and packaging, the scope line, the
  preserved design principles and what is left to the implementation phases.
- `harness-matrix.md`: which harness capabilities the observable lifecycle relies on (ambient
  stdio scoping, background-completion wake, sleep or loop) and what is verified for each harness.
- `python-evidence-system.md`: the Python test evidence system: evidence altitudes, the executable
  evidence categories, the durable evidence lifecycle, fixture authority, quality obligations by
  surface, dependency-owned selection, the dependency-aware retry proof, causal failure
  localization, the supported commands and the maintenance rules.
  Its section on the durable evidence lifecycle states how the two test catalogs
  (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) are kept: one
  canonical form (contract rows ordered by `id`, artifact rows by `path`, every list ascending
  without duplicates, one path per line), a union merge by Git declared in `.gitattributes`,
  loaders that refuse a catalog that is not canonical, and the command
  `python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write`.
  The document describes the command: it makes no decision, orders rows and lists, removes
  duplicate lines, sets each `exact` and `exact-source` consumer list to the set derived from the
  source tree, keeps and names the list of a row for which the source tree shows no consumer,
  removes the lines of files that no longer exist, removes no row, refuses what it cannot read,
  and is the validator without `--write`.
  The document states that no byte or count of a catalog is pinned: the loader checks what the
  source tree can prove, and the other descriptive fields of a row are checked only against the
  loader's rules for their values. The document states no size of the inventory.
- `python-pytest-bootstrap.md`: the Python test policy and commands: when a test case is
  justified, the commands for unit, integration and combined runs, the need for a Git checkout,
  diagnostic metrics and isolation.
- `python-test-evidence.md`: the Python test evidence authority: one accepting authority (a passed,
  immutable, candidate-bound publication of the pinned Dagger quality graph), the consumer
  inventory, and the contract of non-accepting investigation routes. Its consumer inventory names
  `worktrees.route_review_scope.require_current_route_review` as the owner of the route review.
- `dashboard/review-doctrine.md`: the acceptance bars and the visual grammar that the dashboard
  experience review applies.
- `dashboard/scenario-catalog.md`: the user workflows the cockpit dashboard must support and the
  views that serve each.
- `dashboard/session-cockpit-closeout-evidence.md`: the evidence index of the session cockpit
  series: coverage matrix, accessibility evidence, performance and fetch evidence, scenario matrix
  and invariant audit.
- `dashboard/session-cockpit-upstream-register.md`: the serving contracts the frontend renders as
  gaps instead of fabricating them, and the outcome of the Chats cutover.

## Invariants And Boundaries

- The route lies outside the memory's onboarding path rules (`docs/**` is excluded), so the
  onboarding gate raises no item for a card of its own for a changed document. This overview is
  where a change of a document is described.
- The engine-room documents are design references for the dashboard's renderers, not code the
  dashboard ships.
- A design document describes intent and contract. What the code does is established from the
  code and its cards.

## Evidence

- The scenario catalog of the cockpit dashboard. [1]
- The upstream register and the Chats decision brief. [2]
- The closeout evidence index of the session cockpit series. [3]
- The design document's statement of the catalogs' canonical form, their union merge, the write command, and that no byte or count is pinned. [10]
- The observable lifecycle design states its scope. [6]
- The harness capability matrix. [7]
- The test commands and the need for a Git checkout. [8]
- The one accepting authority for Python test evidence. [9]
## Hot Path Summary

`observable-lifecycle.md` describes code/memory-content Git transaction phases and a separate computed ledger cache. A cache refresh is not a third transaction phase or a closeout/integration acceptance condition.

In-repo design documentation for the dashboard and Python verification architecture. Child route `engine-room/` is the engine-room design
reference — a living spec paired with the prototype/scenario player the React engine room was built from.
The `dashboard/` folder now carries the FEUI-L8 scenario matrix and reproducible accessibility/performance
evidence, the closeout evidence pack, and the upstream-register boundary for contracts the frontend must not
fabricate. Top-level notes include `observable-lifecycle.md`, `harness-matrix.md`, and the three Python
evidence documents listed below.
## R39 Design Evidence Disposition

The cockpit performance/evidence design document now labels its test-capable measurement command as
an internal nonce-attested Dagger invocation and explicitly refuses host execution. This is an
evidence-location clarification; the dashboard architecture is unchanged.
### Repo-Internal References

The engine-room design reference child route ([engine-room overview](engine-room/overview.md), living spec + prototype) governs the dashboard engine room.
The dashboard engine-room renderer ([dashboard engine-room overview](../../dashboard/src/panels/engine-room/overview.md)) is governed by the engine-room design docs.
- FEUI-L8's canonical scenario, accessibility, performance, and invariant evidence.
- The explicit upstream gaps and one-Chats cutover ruling.
- The bounded series closeout evidence pack.

- FEUI-L8's canonical scenario, accessibility, performance, and invariant evidence. [20]
- The explicit upstream gaps and one-Chats cutover ruling. [21]
- The bounded series closeout evidence pack. [22]

- FEUI-L8's canonical scenario, accessibility, performance, and invariant evidence. [23]
- The explicit upstream gaps and one-Chats cutover ruling. [24]
- The bounded series closeout evidence pack. [25]

Current working-candidate evidence for this route:

- The implementation produces/reuses memory content before refreshing its cache (since MIK-R09 validating a converted leaf's exact tree first). [26]

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

`python-pytest-bootstrap.md` now permits ordinary isolated host pytest for development and the repository declares `unit_case_budget = 4000` / `integration_case_budget = 1000` (`pyproject.toml:278-279`). It **superseded** the 2,000 / 300 figures this paragraph carried (themselves raised 1000 → 1500 → 2000 (unit) and 150 → 250 → 300 (integration) by `260915-CAPS-L8`, `260831-LOCR-L37` and the 2026-09-17 ruling); 4346e697/TSIP-L13 raised them to 4,000 / 1,000. Coverage is diagnostic, and production CRAP20 prompts review rather than blocking delivery. Focused checks support leaf work; full-suite execution and whole-candidate review belong at the end of the assembled master. Dagger admission remains mandatory for certification; the retired Candidate-A analyzer and route-measurement machinery are not restored.
## CCR-L42 Review-Authority Route Update

`python-test-evidence.md` now names `worktrees.route_review_scope.require_current_route_review` as
the route-review owner. Review runs at the owning altitude: atomic child leaves defer to the
accumulated canonical master review at master-to-parent integration, while standalone and
organizational leaves retain their applicable independent route review. The evidence and
certification model remains unchanged; this update records where the route review is owned.
### Cross-Repo References

The FEUI-L8 design evidence and Chats ruling are repository-local. No cross-repository implementation was
needed to establish the route model.

No applicable cross-repository source was found.
### Docs References

The active memory repository's `system/sources.md` has no configured Domain Documentation entries. This
overview was refreshed from the same-repository design documents, reviewed FEUI-L8 implementation/tests,
and the accepted worker/reviewer evidence.

No configured external Domain Documentation source governs this route.
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
the repository declares `unit_case_budget = 4000` and `integration_case_budget = 1000`
(`pyproject.toml:278-279`), changed by 4346e697/TSIP-L13 from 2,000 unit / 300 integration. The superseded values are recorded
rather than deleted, and this is a `T45` find — no check reads a number in prose.
## 260713-TES-L5 Route Impact — Fact-Relay Recovery Language

`observable-lifecycle.md` (this route's design authority) refreshed its recovery runbook:
`ladder-resolved` is legacy parse-compat (the timed escalation ladder is retired) and
retired/absent-target rows resolve through the sweep's landing/ceiling/grace paths.

</details>