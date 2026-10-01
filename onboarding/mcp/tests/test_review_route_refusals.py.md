# mcp/tests/test_review_route_refusals.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **fast transport contract** for ICR-R16: every refusal the review transport publishes is actionable,
in the body of its own status.

The route answers a refusal with the change-set routes' `400`/`404`/`503` idiom and puts the answer in
the *body*, in one of two shapes — this route's own typed refusal (`state = "refused"`) or one of the
transport-level bodies it builds itself (a selector it does not admit, an unwired adapter, a port's two
named failures). The module's docstring states why that matters and what it does **not** do: this module
drives the REAL route over `TestClient` and reads the exact bodies, registering the real
`register_review_routes`; it does not re-implement the route, and it does not re-derive what other
modules already measure. The real adapter's own refusals and the task-context review that keeps source
inspection available while intent is not are measured by `test_knowledge_review_source_endpoints.py`
over a real enclosure, and the same bodies were measured over real HTTP against the production
composition in this leaf's evidence run (`ar-coordination/temp/icr/evidence-l16-refusals.txt`, §2/§3).

The ports are injected rather than composed because the route is transport-only **by design**: `serving`
ranks below `application` in `layers.toml` and reaches every answer through its port, so an injected port
is the only way the route's own two exception mappings are reachable at all. The module says so instead
of leaving a reader to wonder why a transport test injects its subject.

## Code Commentary

### Logic

**The module is registered in the `unit-regression` lane, and it is hermetic.** `pytestmark =
pytest.mark.evidence_unit` marks the population; `runtime_config()` builds an `McpRuntimeConfig` that
names no real root (`/nonexistent-workspace`, `/nonexistent-coordination`, …) with the docstring saying
so — the routes resolve nothing from it — and `served(port, entries=None)` builds a bare `FastAPI()` app
and registers the real routes on it. No enclosure, no network, no temporary repository: the module is an
ordinary unit module, which is why its one lane row could be added without touching any budget.

**`ACTIONABLE = ("status", "detail", "nextAction")` is the module's own definition of actionable, and
every case asserts it as a set inclusion.** A body that omitted any of the three would fail the assertion
before any other claim in the case; `offendingInput` and `expected` are asserted where an input is what
was refused.

**The cases walk the refusal shapes the route itself builds.** An unwired adapter answers `503` with
`status: "unavailable"`, a non-blank `detail` and a `nextAction` naming the composition root — on **both**
the comparison route and the entry route, so the two cannot drift about what "not served" means. An
unadmitted selector is refused **before the port runs** (the injected port raises `AssertionError` if it
is called at all, which is how "the route refuses it itself" is proven rather than assumed) with
`status: "bad-request"`, `offendingInput: "latest"` and both admitted kinds in `expected`.

**The two port-level exception mappings get their own cases, and they are the ICR-R16 addition.** A port
raising `AuthorityError` yields `400` `bad-path` with the error's own message as `detail` **and** a
`nextAction` naming the authority; a port raising `FileNotFoundError` yields `404` `not-found` carrying
the path in **both** `path` and `offendingInput`, alongside the action. Those two are what the fix round
added to the bodies (`_transport_refusal`/`_port_outcome` in the transport), and they are asserted as
`ACTIONABLE` plus their own fields, so a body that lost the action again would fail here.

**The conforming example is pinned at the transport.** A port returning
`KnowledgeReviewResult(state="refused", …)` with `candidate_dataset_absent` and
`offending_input: "knowledge-candidate.sqlite"` answers `404` with `state: "refused"` and **no `payload`
key** — the assertion that a refusal cannot be read as a degraded success — and the `refusal` object is
compared **whole** (all four fields), so a field cannot quietly disappear from the typed answer.

**The parametrized case pins the status family from the refusal's own published code.** Five codes —
`candidate_dataset_absent`, `candidate_not_live`, `candidate_unresolved`, `subject_unresolved` to `404`
and `comparison_refused` to `400` — are driven through the **entry** route, each asserting the status,
`state: "refused"`, `entries: []` and a non-blank `refusal.next_action`. Its docstring states the point
precisely: the client reads the body whatever the status, so the status family stays the route's own
contract rather than something the client depends on.

### Conventions

The module imports the real route constants and registrar from `agents_remember.serving.review`, the
typed models from `agents_remember.models.knowledge.review`, `AuthorityError` from the kernel's error
module and `McpRuntimeConfig` from the kernel primitives — it declares no production behaviour. Upper-case
constants carry the task context, the recorded subject and the actionable field set; module-level
`runtime_config`/`served`/`typed_refusal` helpers build the app; and each case is a one-purpose
`test_*` function with a prose docstring naming what it protects. Bodies are asserted field by field
rather than compared to a golden blob, so a failure names the missing field.

### Invariants And Boundaries

- **The route under test is the real one.** The real `register_review_routes` is called on a bare app;
  only the ports are injected, and the module states why that is the only way to reach the mappings.
- **Every refusal body carries `status`, `detail` and `nextAction`.** `ACTIONABLE` is asserted as a set
  inclusion in each transport-level case, so the requirement is enforced rather than described.
- **A refusal must not be readable as a success.** The typed-refusal case asserts `"payload" not in
  body`, and the parametrized case asserts `entries == []`.
- **The transport refuses what it can refuse itself, before the port.** The unadmitted-selector case
  proves it with a port that raises if it is called.
- **The two port exception mappings carry an action, not only a message.** That is the leaf's change and
  it has its own case for each exception type.
- **Boundary.** It pins the transport's own bodies and status codes. It does **not** re-measure the real
  adapter's refusals or the task-context review (those belong to
  `test_knowledge_review_source_endpoints.py` over a real enclosure), and it makes no claim about the
  rendered surface — the refusal-visibility and A01/A13 journeys belong to the dashboard cases and, for
  the browser level, to R25 with R24/R17.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and lane
marker, the bare-app helpers, the actionable field set, and the six cases. Every anchor in a row occurs
inside the range that row cites.

- **The docstring's own statement of what the module is (the fast transport contract, driving the real route), of the two shapes a refusal arrives in, and of what it deliberately does not re-derive.** [1]
- The real route constants, registrar and typed models under test. [2]
- The lane marker that keeps this a hermetic unit module. [3]
- The task context, the recorded subject, and **the module's own definition of actionable**. [4]
- A configuration naming no real root, because these routes resolve nothing from it. [5]
- **The one app builder: a bare `FastAPI()` with the real routes registered and the ports injected.** [6]
- The typed refusal builder whose own action the cases assert survives the transport. [7]
- **An unwired adapter refused on both routes with an actionable body naming the composition root.** [8]
- **An unadmitted selector refused by the transport itself before the port runs, naming the input and both admitted kinds.** [9]
- **The `AuthorityError` mapping this leaf made actionable.** [10]
- **The `FileNotFoundError` mapping this leaf made actionable, keeping the path and adding the action.** [11]
- **The packet's conforming example at the transport: `404` + `candidate_dataset_absent` + the whole refusal, with no `payload` key so it cannot read as a degraded success.** [12]
- **The status family derived from the refusal's own code, driven through the entry route.** [13]
- **The transport this module pins: the one actionable refusal body builder and the one 400/404 mapping both adapters reach through.** [14]
- The result-to-status mapping the parametrized case pins from the code's own side. [15]
- **The lane row that puts this module in the hermetic unit population.** [16]
- The client that reads these bodies whatever the status, which is why the status family stays the route's own contract. [17]

### Cross-Repo References

No cross-repository behavior is exercised in this file. The routes serve one repository namespace's
candidate and the app under test is built in-process.

No meaningful cross-repo references found.
