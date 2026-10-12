# docs/design/ — Design Documentation Overview

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

`docs/design/` holds the repository's design references for the observable lifecycle, Python testing and evidence authority, dashboard review and scenarios, and the engine-room visual language. These documents describe intent and contracts beside the implementation. They do not establish implementation behavior or execution acceptance by themselves.

## Hot Path Summary

Start with the document for the question: `observable-lifecycle.md` for lifecycle architecture, `python-pytest-bootstrap.md` for development test policy and commands, `python-evidence-system.md` for evidence construction and maintenance, and `python-test-evidence.md` for accepting authority and consumers. The dashboard documents separate review doctrine, intended workflows, recorded candidate evidence, and serving-contract gaps. The [engine-room overview](engine-room/overview.md) covers the visual-language reference and scenario prototype.

The lifecycle design separates code and memory-content Git outputs from the computed ledger cache. The inspected closeout owner produces or reuses the memory commit before refreshing that cache. Source inspection here supplies no new CODE qualification, test result, native-host verification, whole-build result, landing acceptance, or memory acceptance.

## Construction

### Lifecycle architecture

`observable-lifecycle.md` describes the lifecycle entity and state machine, event substrate and retention, gates and their return channel, read packet, packaging, scope, preserved design principles, and deferred implementation questions. Its MIK-R112 amendment removes model-facing signal tools while retaining session-driven transitions and the states and gates of the design. The former overview's public `lifecycle_gate` junction is therefore superseded. This amendment does not establish that every retained design mechanism is currently implemented.

The design also retains the operator-inbox recovery runbook: save live work, use normal daemon controls, quarantine the inbox log, preserve live-seat rows, and let normal sweep paths resolve retired or absent targets. It identifies `ladder-resolved` as legacy vocabulary after retirement of the timed escalation ladder.

`harness-matrix.md` describes ambient stdio scoping, background-completion wake, and sleep or loop capabilities. Its verification entries are recorded document metadata, not fresh host qualification from this inspection.

### Python verification references

`python-evidence-system.md` describes evidence altitudes and executable categories, durable evidence lifecycle, fixture authority, quality obligations by surface, dependency-owned selection, retry proof, causal failure localization, supported routes, and maintenance rules.

Its durable-evidence section specifies a canonical form for `mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`: contract rows ordered by `id`, artifact rows by `path`, lists ascending without duplicates, and one path per line. It describes Git union merging and loaders that reject noncanonical input. The documented writer is `python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write`; without `--write`, the command validates both catalogs.

The document says the writer orders rows and lists, removes duplicate lines, derives `exact` and `exact-source` consumers from source, retains and names lists for rows with no derived consumer, removes references to missing files, removes no row, and refuses unreadable or unpreservable input without writing either catalog. It pins no catalog bytes, counts, or inventory size: source-derived relationships and permitted field values are the stated checks.

The selection contract requires typed incomplete ownership to stop before Gate 2, removes deleted tests from the population, and keeps irrelevant inputs explicit. The immutable selector result binds candidate, configuration, scope, and dependency reasons. Retry binds its digest and, when proof cannot be reused, refreshes the already admitted population. These are the document's standing contracts; this overview does not certify every corresponding implementation predicate.

`python-pytest-bootstrap.md` gives the behavior-based admission policy for tests, ordinary isolated host pytest commands, Git-checkout prerequisite, diagnostic metrics, and isolation rules. Host pytest has no certification authority. Coverage is diagnostic; production CRAP20 prompts review rather than blocking delivery. The current document and root `pyproject.toml:298-299` both declare 5,000 unit cases and 1,000 integration cases. D226 raises only the unit ceiling from 4,000; integration and the enforcing guard remain unchanged. The earlier 1,000/150-versus-4,000/1,000 source discrepancy is a prior-pair observation, not the current reading.

`python-test-evidence.md` states that Python acceptance requires a passed, immutable, candidate-bound publication of the pinned Dagger quality graph. Non-accepting investigation artifacts cannot satisfy accepting consumers. It names `worktrees.route_review_scope.require_current_route_review` as the route-review owner and separates independent route-review authority from test evidence. The inspected owner defers atomic children and atomic master closeout review until the accumulated master integration review; contracts outside that atomic scope call the existing independent review owner.

The authority document records retirement of Candidate A's host diagnostic command, analyzer, manifest, bootstrap, runner, and measurement machinery. Ordinary isolated development pytest does not restore those surfaces. The three retained Python references carry the evidence-system, development-policy, and acceptance-authority accounts formerly described by the narrower notes.

### Dashboard references and child route

- `dashboard/review-doctrine.md` describes dashboard acceptance bars, observability parity, visual grammar, motion, settled-beat sampling, freshness honesty, and review posture.
- `dashboard/scenario-catalog.md` describes intended workflows and the views meant to serve them. Its carried gaps and historical status entries are design and review material, not current implementation qualification supplied by this overview.
- `dashboard/session-cockpit-closeout-evidence.md` indexes the recorded FEUI-L8 candidate's coverage, accessibility, performance and fetch evidence, scenario matrix, and invariant pre-audit. Its measurement command is described as internal to a nonce-attested Dagger environment with host execution refused. The recorded measurements and pre-audit do not constitute a new run or independent acceptance here.
- `dashboard/session-cockpit-upstream-register.md` separates serving-contract asks from the Chats cutover decision and records boundaries against fabricating absent frontend authority. Its recorded cutover outcome is not fresh implementation acceptance from this inspection.
- `engine-room/` contains `engine-room-visual-language.html` and `podstage.html`, the visual-language reference and choreography prototype. See the [engine-room overview](engine-room/overview.md) and the [dashboard engine-room renderer overview](../../dashboard/src/panels/engine-room/overview.md) for the linked design and implementation routes.

## Invariants And Boundaries

Design intent and actual source behavior remain separate accounts. A retained design statement is not promoted into an implementation guarantee by its presence here. Where they disagree, the discrepancy remains visible for the owning authority to decide.

The resolved memory settings exclude `docs/**` from onboarding path rules. This overview provides an area-level description of the design documents; it does not turn those excluded documents into required file-card coverage.

The ledger is described as an ignored consumer cache computed from memory commit trailers. Its bytes and rows are neither durable approval evidence nor transaction authority. The inspected closeout sequence commits or reuses memory content before refreshing the cache and gates converted memory against its exact output tree before publication or recovered acceptance.

Lifecycle implementation and status authority are not established by the design document's status label. The direct-owner 7≠8 discrepancy and sync-operation legacy fallback versus c09 doctrine remain awaiting Architect disposition; this overview neither resolves them nor declares source and standing intent coherent.

## Non-operative Metadata

The following excluded metadata is preserved verbatim. It does not grant operative promises or current acceptance.

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| sourceRoute            | `docs/design/`                              |

## Evidence



- The enforced collected-case pair is 5000 unit/1000 integration; the unit-only policy raise leaves the guard unchanged. [27]

- The scenario catalog of the cockpit dashboard. [1]
- The upstream register and the Chats decision brief. [2]
- The closeout evidence index of the session cockpit series. [3]
- The observable lifecycle design states its scope. [6]
- The harness capability matrix. [7]
- The test commands and the need for a Git checkout. [8]
- The one accepting authority for Python test evidence. [9]
- The design document's statement of the catalogs' canonical form, their union merge, the write command, and that no byte or count is pinned. [10]
- FEUI-L8's recorded scenario, accessibility, performance, and invariant evidence entry point. [20]
- The upstream gaps and recorded one-Chats cutover ruling entry point. [21]
- The bounded series closeout evidence pack entry point. [22]
- FEUI-L8's recorded scenario, accessibility, performance, and invariant evidence reference. [23]
- The upstream gaps and recorded one-Chats cutover ruling reference. [24]
- The bounded series closeout evidence pack. [25]
- The implementation produces or reuses memory content before refreshing its cache. [26]
- The amended lifecycle design retains session-driven transitions and describes recovery and cache boundaries. [28]
- The Python evidence design describes selection, retry, and maintenance contracts. [29]
- The bootstrap note and root configuration now state 5,000/1,000; host development runs and diagnostic metrics remain documented. [30]
- The authority document records Candidate A retirement and the review consumer; the current review owner defers atomic scope. [31]
- The cockpit index describes its historical candidate and internal measurement boundary. [32]
- The dashboard review doctrine defines review bars and visual grammar. [33]
- Engine-room references identify the visual-language library and choreography prototype. [34]
- The current complete closeout function preserves the memory-before-cache sequence; exact-tree validation independently refuses ungated memory. [35]
