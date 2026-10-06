# docs/design/ — Design Documentation Overview

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
