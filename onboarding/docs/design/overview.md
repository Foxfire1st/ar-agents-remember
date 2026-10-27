# docs/design/ — Design Documentation Overview

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

`docs/design/` holds the repository's design references for the observable lifecycle, Python testing and evidence authority, dashboard review and scenarios, and the engine-room visual language. These documents describe intent and contracts beside the implementation. They do not establish implementation behavior or execution acceptance by themselves.

## Hot Path Summary

Start with the document for the question: `observable-lifecycle.md` for the historical session-lifecycle architecture, `python-pytest-bootstrap.md` for development test policy and commands, `python-evidence-system.md` for evidence construction and maintenance, and `python-test-evidence.md` for accepting authority and consumers. The dashboard documents separate review doctrine, intended workflows, recorded candidate evidence, and serving-contract gaps. `canvas-host.md` describes the generated review page's host and retained presenter contracts: the two serving surfaces, the origin arrangement, the policy that gates script execution on the browser proof, readiness before a revision becomes ready, the host protocol and sessions, and confinement limits. Its current amendment retires the old authoring POSTs and the native launch that attached dedicated presenter tools: authoring runs through the explainer's seat on the normal task server, while the retained presenter port uses `UnconfiguredPresenterRunner` when no confined runner is configured and refuses `no-confined-harness` (MIK-R186 at v2 Scope, MIK-R105 at v4). This is the design reference's stated boundary, not new installed-host or browser qualification. The [engine-room overview](engine-room/overview.md) covers the visual-language reference and scenario prototype.

The lifecycle design separates code and memory-content Git outputs from the computed ledger cache. The inspected closeout owner produces or reuses the memory commit before refreshing that cache. Source inspection here supplies no new CODE qualification, test result, native-host verification, whole-build result, landing acceptance, or memory acceptance.

## Construction

### Historical session-lifecycle architecture

`observable-lifecycle.md` records the former session lifecycle, events and developer gates. Its R112 amendment and its old session-driven account are historical under the R113 status banner; they are not a retained live session/gate promise. The document points to docs/reference/mcp-tools.md for the present surface. Retained task/knowledge/landing owners are not retired merely because this older session design is historical.

The older operator-inbox runbook is retained as historical text, including its ladder-resolved vocabulary. R113 removes that runtime inbox/seat sweep; this overview does not instruct a current user to quarantine its log or invoke removed sweep paths.

`harness-matrix.md` is explicitly history under R113: its ambient-scoping, wake and loop observations record the former hosted-session design, not live capability or adapter availability. The current harness reference is docs/reference/harnesses.md.

### Python verification references

`python-evidence-system.md` describes evidence altitudes and executable categories, durable evidence lifecycle, fixture authority, quality obligations by surface, dependency-owned selection, retry proof, causal failure localization, supported routes, and maintenance rules.

Its durable-evidence section specifies a canonical form for `mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`: contract rows ordered by `id`, artifact rows by `path`, lists ascending without duplicates, and one path per line. It describes Git union merging and loaders that reject noncanonical input. The documented writer is `python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write`; without `--write`, the command validates both catalogs.

The document says the writer orders rows and lists, removes duplicate lines, derives `exact` and `exact-source` consumers from source, retains and names lists for rows with no derived consumer, removes references to missing files, removes no row, and refuses unreadable or unpreservable input without writing either catalog. It pins no catalog bytes, counts, or inventory size: source-derived relationships and permitted field values are the stated checks.

The selection contract requires typed incomplete ownership to stop before Gate 2, removes deleted tests from the population, and keeps irrelevant inputs explicit. The immutable selector result binds candidate, configuration, scope, and dependency reasons. Retry binds its digest and, when proof cannot be reused, refreshes the already admitted population. These are the document's standing contracts; this overview does not certify every corresponding implementation predicate.

`python-pytest-bootstrap.md` gives the behavior-based admission policy for tests, ordinary isolated host pytest commands, Git-checkout prerequisite, diagnostic metrics, and isolation rules. Host pytest has no certification authority. Coverage is diagnostic; production CRAP20 prompts review rather than blocking delivery. The current document and root `pyproject.toml:333-334` declare 10,000 unit cases and 2,000 integration cases. D226's earlier 4,000-to-5,000 unit policy raise and L54's 5,000-to-6,000 raise are historical; both later unit-only raises leave integration and the enforcing guard unchanged. The earlier 1,000/150-versus-4,000/1,000 source discrepancy is a prior-pair observation, not the current reading.

`python-test-evidence.md` states that Python acceptance requires a passed, immutable, candidate-bound publication of the pinned Dagger quality graph. Non-accepting investigation artifacts cannot satisfy accepting consumers. It names `worktrees.route_review_scope.require_current_route_review` as the route-review owner and separates independent route-review authority from test evidence. The inspected owner defers atomic children and atomic master closeout review until the accumulated master integration review; contracts outside that atomic scope call the existing independent review owner.

The authority document records retirement of Candidate A's host diagnostic command, analyzer, manifest, bootstrap, runner, and measurement machinery. Ordinary isolated development pytest does not restore those surfaces. The three retained Python references carry the evidence-system, development-policy, and acceptance-authority accounts formerly described by the narrower notes.

### Dashboard references and child route

- `dashboard/review-doctrine.md` describes dashboard acceptance bars, observability parity, visual grammar, motion, settled-beat sampling, freshness honesty, and review posture.
- `dashboard/scenario-catalog.md` retains the non-session workflow design. W6 and its old AR terminal/composer inventory are specifically marked history by R113; that does not demote unrelated current workflows or qualify implementation.
- `dashboard/session-cockpit-closeout-evidence.md` has the required R113 History banner and retains its dated FEUI-L8 measurements/pre-audit. Its historical internal Dagger measurement boundary is not a new run or acceptance. The RV01 protected certificate line is unchanged in content at current line151; the old whole-file hash and line146 are historical provenance, not a current whole-file freeze.
- `dashboard/session-cockpit-upstream-register.md` is marked history: its former session-cockpit asks and Chats decision remain dated evidence, not current requests to reintroduce removed frontend/serving surfaces.
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









































### Integration headroom

On 2026-10-26, the integration ceiling rises from 1000 to 2000; unit remains 10000. The source-file cases protect Git listing, bounded reads and readable excluded citations. The original 16-case shape measured 18.56 s and independently 20.15 s; grouping preserved its scenarios in four cases and 14 subtests at 19.70 s. The two link-class regressions produce four cases and 16 subtests: v2 measured 27.47 s and v3 38.20 s. No case was weakened or moved to the unit lane. Both over-budget refusal directions remain enforced. These are scenario-run measurements, not whole-suite runtime or a claimed speedup.

## Evidence
- The RV01 dated certificate line is unchanged in content after the allowed R113 History banner; its current location is151. [36]
- The scenario catalog of the cockpit dashboard. [1]
- The upstream register and the Chats decision brief. [2]
- The closeout evidence index of the session cockpit series. [3]
- The former observable session-lifecycle design is explicitly historical under R113. [6]
- The former harness capability matrix is explicitly historical, not current adapter availability. [7]
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
- The historical session design records former recovery/cache boundaries; its R113 status makes the session-driven promise non-operative. [28]
- The Python evidence design describes selection, retry, and maintenance contracts. [29]
- The authority document records Candidate A retirement and the review consumer; the current review owner defers atomic scope. [31]
- The cockpit index describes its historical candidate and internal measurement boundary. [32]
- The dashboard review doctrine defines review bars and visual grammar. [33]
- Engine-room references identify the visual-language library and choreography prototype. [34]
- The current complete closeout function preserves the memory-before-cache sequence; exact-tree validation independently refuses ungated memory. [35]
- The root pytest declaration sets 10000 unit and 2000 integration selected cases; the repository collection guard enforces this pair. [27]
- The testing design and root configuration agree on 10000 unit and 2000 integration selected cases; historical values describe their earlier policy epochs. [30]
- The canvas-host amendment retires the old authoring POSTs and standalone presenter-tool launch while retaining the explicit runner/confinement and browser-readiness limits. [37]
- The canvas-host amendment retires old authoring POSTs and the dedicated native presenter launch; retained authoring port and explicit browser readiness remain bounded. [37]
- The dated raise states the headroom, measured scenario costs and preserved refusal directions. [38]
