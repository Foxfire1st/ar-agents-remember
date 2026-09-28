# mcp/tests/test_review_route_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_route_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:30:43+00:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and lane
marker, the bare-app helpers, the actionable field set, and the six cases. Every anchor in a row occurs
inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The docstring's own statement of what the module is (the fast transport contract, driving the real route), of the two shapes a refusal arrives in, and of what it deliberately does not re-derive.** | `register_review_routes`; `KnowledgeReviewResult` | mcp/tests/test_review_route_refusals.py:1-22; mcp/tests/test_review_route_refusals.py:24-42; mcp/tests/test_review_route_refusals.py:65-69; mcp/tests/test_review_route_refusals.py:151-172 |
| The real route constants, registrar and typed models under test. | `KNOWLEDGE_REVIEW_ENTRIES_ROUTE`; `KNOWLEDGE_REVIEW_ROUTE`; `register_review_routes` | mcp/tests/test_review_route_refusals.py:24-42 |
| The lane marker that keeps this a hermetic unit module. | `pytestmark` | mcp/tests/test_review_route_refusals.py:43-43 |
| The task context, the recorded subject, and **the module's own definition of actionable**. | `TASK`; `SUBJECT`; `ACTIONABLE` | mcp/tests/test_review_route_refusals.py:45-53 |
| A configuration naming no real root, because these routes resolve nothing from it. | `runtime_config` | mcp/tests/test_review_route_refusals.py:54-63 |
| **The one app builder: a bare `FastAPI()` with the real routes registered and the ports injected.** | `served` | mcp/tests/test_review_route_refusals.py:65-69 |
| The typed refusal builder whose own action the cases assert survives the transport. | `typed_refusal` | mcp/tests/test_review_route_refusals.py:71-78 |
| **An unwired adapter refused on both routes with an actionable body naming the composition root.** | "test_an_unwired_adapter_answers_with_the_action_that_wires_it" | mcp/tests/test_review_route_refusals.py:80-93 |
| **An unadmitted selector refused by the transport itself before the port runs, naming the input and both admitted kinds.** | "test_an_unadmitted_selector_names_the_input_and_the_admitted_kinds" | mcp/tests/test_review_route_refusals.py:96-112 |
| **The `AuthorityError` mapping this leaf made actionable.** | "test_a_refused_authority_carries_the_action_that_clears_it" | mcp/tests/test_review_route_refusals.py:115-130 |
| **The `FileNotFoundError` mapping this leaf made actionable, keeping the path and adding the action.** | "test_a_missing_path_names_the_path_it_does_not_hold_and_a_next_action" | mcp/tests/test_review_route_refusals.py:133-148 |
| **The packet's conforming example at the transport: `404` + `candidate_dataset_absent` + the whole refusal, with no `payload` key so it cannot read as a degraded success.** | "test_a_typed_refusal_travels_whole_in_the_body_of_its_own_status" | mcp/tests/test_review_route_refusals.py:151-172 |
| **The status family derived from the refusal's own code, driven through the entry route.** | "test_the_entry_route_maps_each_refusal_code_onto_its_own_status" | mcp/tests/test_review_route_refusals.py:175-204 |
| **The transport this module pins: the one actionable refusal body builder and the one 400/404 mapping both adapters reach through.** | `_transport_refusal`; `_port_outcome`; `_AUTHORITY_NEXT_ACTION`; `_NOT_FOUND_NEXT_ACTION` | mcp/src/agents_remember/serving/review.py:113-170 |
| The result-to-status mapping the parametrized case pins from the code's own side. | `_status_for` |mcp/src/agents_remember/serving/review.py:522-607|
| **The lane row that puts this module in the hermetic unit population.** | `unit-regression`; `test_review_route_refusals` | mcp/tests/test-evidence-lanes.toml:135-135 |
| The client that reads these bodies whatever the status, which is why the status family stays the route's own contract. | `getReviewJson`; `reviewFailureToken` | dashboard/src/data/reviewTransport.ts:70-98; dashboard/src/data/reviewTransport.ts:158-171 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. The routes serve one repository namespace's
candidate and the app under test is built in-process.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 1 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_review_route_refusals` repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **sync follow-up: lane row re-derived to the merged tree (`:114` → `:115`).** ICR-L7 inserted its revision-selection row above, moving this registration one line down; re-read against the line that carries it. No verification stamp was advanced.


- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the six cases are *for* — the transport contract that every refusal the review route publishes is actionable in the body of its own status — and the two design facts a later reader would otherwise have to rediscover: the ports are injected **because the route is transport-only by design** (`serving` ranks below `application`, so an injected port is the only way to reach the route's own two exception mappings), and the two `AuthorityError`/`FileNotFoundError` cases are this leaf's actual server-side change, asserted as `ACTIONABLE` plus their own fields so a body that lost its next action would fail here. The card also records the module's **deliberate non-claims**: it does not re-measure the real adapter's refusals or the task-context review, which `test_knowledge_review_source_endpoints.py` owns over a real enclosure, and it says nothing about the rendered surface. `mcp/tests/evidence-lifecycle.toml` is unchanged by this leaf and `LIFECYCLE_CATALOG_SHA256` is therefore **not** re-pinned: the module registers no contract and no artifact and consumes no catalog-registered support module, so only the lane manifest row was needed. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.
