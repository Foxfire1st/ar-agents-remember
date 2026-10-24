# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Run dashboard supervision or live/reload/sim serving and bind configuration-scoped application readers, native role-launch and developer-tray routes.

## Code Commentary

The composition root wires PaseoExplainerHost, application ports and the master contract locator into serving. _master_contract uses the declared master series contract or existing canonical folder contract; no other line is borrowed.

serving_collaborators is the rank boundary: complete review, numbered entry catalogue, source content, summary, tree and knowledge reader are injected application callables. It creates one app-local ReviewerWorklistProcesses, supplies tree reads and its shutdown, and wraps recorded intent/catalogue/tree questions in RecordedReviewAnswers. The application owners define their payloads; retained all-owner-record and knowledge-diff docstrings do not restore retired channels.

review_entries_port now takes optional number and calls list_comparison_review_entries with that exact selector through the reuse owner. api_routes registers native role launch, then developer chat/tray seat/send/sent-pick routes, supplying the same admitted leaf-memory resolver for review references. This is composition, not a second developer-delivery implementation.

_review_memory_root requires valid simple repo/master/leaf names, an external leaf under the matching coordination/task enclosure and an existing canonical non-symlink memory directory below its group, distinct from code/group roots and outside provider-runtime. It performs no Git capture/index read and rejection is None. This admission does not authenticate every descendant or authorize a mutation.

run declares the process dashboard role, loads explicit settings or trusted discovery, binds archive-aware worktree services and chooses daemon/status/stop, reload or foreground serving. Config/discovery failures print and return1. Process roles are declared at entry points, including the spawned _dev_app factory, not create_app; they do not replace unconditional durable-log locking.

Foreground and reload Uvicorn calls now request h11_max_incomplete_event_size=64*1024 as well as the existing3-second graceful window. The finite request-head allowance supports the up-to500-invariant card query named in the source rationale. This is explicit configuration, not a fresh network/runtime/version measurement or a whole-process shutdown guarantee.

Reload carries config/interval/explicit heartbeat through AR_DASHBOARD_DEV_* and uses an import-string factory; reload+sim is refused. Live apps receive interval/heartbeat. Sim uses interval plus ProjectionReplay, retains SimSetup for the server lifetime and cleans its temporary root in finally. Shared composition is not byte-equivalence proof.

Daemon/status/stop reject sim/reload. Status probes dashboard, prints best-effort diagnostics without changing exit policy and observes host: dashboard-down1, otherwise host-ready0 or host-down3. Stop targets dashboard only. Ensure delegates dashboard supervision and installed-host readiness without installing/upgrading a host. Foreground/reload starts host readiness on a daemon thread unless parent-owned; sim does not.

Parser defaults remain loopback host, config-driven port, interval1.0 and optional heartbeat, with sim/speed, no-access-log and mutually exclusive control flags. Loopback is a default, not authentication. Native role routes and archive services do not themselves accept/commit/finalize a task.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY, NEW-R192-RULE19-PORT.** The composition root wires the refresher, so the answer the consumer compares is taken here. This is the composition root: it binds the real bridge read to the port serving declares, which is where the one permitted crossing is made. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

Configuration identity, admitted watch/reference roots, read availability, delivery and semantic approval remain distinct. Recorded questions may be reused only through their owner rules and exact inputs; working-view reads stay fresh. Historical compiler/terminal/execution registration, port ordinals, latency and installed-version observations below are not current registration or fresh evidence.

## Historical composition accounts — superseded, not current contracts

Original wording below preserves prior wiring decisions, port ordinals and historical producer/test
observations. Obsolete capsule compiler, dataset-review framing, all-owner record channels, loader
imports and execution claims are **not** current contracts or acceptance. The actual owners define
current complete-review, tree and reader semantics; these quotations do not override them.

> ## 260928-MIK-L29 The Knowledge Reader Port
>
> `serving_collaborators` binds one more callable, `knowledge_reader_port(query)`, which returns
> `read_knowledge_reader(config, query)` (`application/knowledge_reader/__init__.py`) and is placed on the
> collaborator record as `knowledge_reader`. It is imported at function scope with the same deferred-composition
> idiom as the reviewer ports. It is **not** a reviewer port: the path-based knowledge reader (MIK-R29) needs no
> task, so it is its own port rather than a mode of the review adapter. It serves read-only views of any
> converted memory tree at `GET /api/knowledge/reader/{view}`; an unconverted tree answers `not-converted` and the
> landed routes answer byte-identically (the worker's and reviewer's unconverted comparisons). The worker's
> real-data reads and the browser walkthrough were served through this composition.
>
> - The deferred import of the reader.
> - The reader port, bound on the collaborator record beside the reviewer ports.
> - The entry point the port calls.
>
> ## 260928-MIK-L25 The Fifth Reviewer Port: The Tree View
>
> `serving_collaborators` binds a **fifth** reviewer callable, `review_trees_port(query)`, which returns
> `read_review_trees(config, query)` (`application/review_tree_knowledge.py`) and is placed on the collaborator record
> as `review_trees`. It is imported at function scope with the same deferred-composition idiom as its siblings. It
> answers, for a leaf whose memory is converted, what the dataset review cannot: the four Git trees, the Git diff of
> the memory trees, the per-side currentness and the worklist view (MIK-R25 rules 1–3). The same composition is what
> the worker's real-data captures and the dashboard fixtures were served through.
>
> - The deferred import and the fifth port bound on the collaborator record.
>
> ## 260921-ICR-L47 The Fourth Reviewer Port: The Changed-Intent Summary
>
> `serving_collaborators` obtains the changed-intent summary port from `cli.dashboard_review_summary.review_intent_summary_port(config)`. The extracted adapter retains the application-tier summary boundary; this composition supplies configuration rather than defining another inline reader or summary cache.
>
> - The module-level `dashboard_review_summary.review_intent_summary_port` import and the config-bound fourth port on the collaborator record.
>
> ## 260921-ICR-L3 The Third Reviewer Port, And Who Chooses The Generation
>
> `serving_collaborators` now binds **three** application-tier reviewer callables, and the third one is
> what lets a browser open the entry a reader clicked:
>
> ```python
> def review_source_content_port(request):
>     return read_review_source_content(config, request)
> ```
>
> It is imported at function scope with the same deferred-composition idiom as its siblings —
> `from agents_remember.application.review_source_content import (  # noqa: PLC0415 - composition
> read_review_source_content,)` — and placed on the collaborator record as `review_source_content`.
>
> The docstring states the division of labour this port exists to make explicit, and it is the reason the
> closed-over value is not a config lookup: **the request carries the generation the browser is looking
> at, rather than the server choosing one.** The application owner re-resolves the leaf only to *measure*
> whether that generation is still the candidate's; it then reads those two objects and nothing else — no
> working tree, no `HEAD`. So an entry opened after the branch moved still shows the **listed**
> generation's bytes and says the leaf has moved past them, instead of silently substituting whatever the
> branch holds now. Supplying the port is also what decides the route's behaviour: a process that omits it
> refuses that route **by name**, because "this process cannot read the entry" and "this entry has no
> content" are different facts and only one of them is true.
>
> This is the third instance of one shape of decision on this record: production wires every reviewer port
> in this one config-bound composition root, and each port's absence refuses its own route rather than
> serving an empty surface.
>
> ## 260915-KS-L45 Both Reviewer Ports Wired From One Composition Root
>
> **The count in this section is superseded: the root now binds three reviewer callables since
> 260921-ICR-L3** (see the section above). The wiring site, the function-scope import idiom and the
> refuse-by-name reason it records are still exactly right, so the entry is retained rather than
> rewritten.
>
> `serving_collaborators` now binds **two** application-tier reviewer callables, and the second one is
> what makes a task view able to ask the question the first one needs an answer to:
>
> ```python
> def review_entries_port(repository_id, master, leaf_id):
>     return list_knowledge_review_entries(config, repository_id, master, leaf_id)
> ```
>
> It imports `list_knowledge_review_entries` beside `read_knowledge_review` and `review_records_for`
> from `agents_remember.application.knowledge_review` at function scope, and places both on the
> collaborator record as `knowledge_review` and `knowledge_review_entries`. The two ports are one
> composition and one resolution: the entry call takes the **task context alone**, because a subject is
> exactly what it is being asked for, and the task view calls it *before* any subject exists. The
> docstring states the property this buys: resolving the entry list "through the identical operation
> the review route uses … is what keeps the entry a caller is offered and the review it then opens on
> one candidate". Supplying a port is also what decides its route's behaviour — the serving layer
> refuses each route **by name** when its field is absent, because an empty pane (or an empty entry
> list, which would read as "nothing is reviewable here") and an unreachable adapter are different
> facts.
>
> ## 260921-ICR-L14 The Review Port Supplies The Complete Record Collection
>
> > **Historical record-reach account, superseded:** current complete review shares one resolution, but `review_records_for_resolution` supplies curator assessments/artifacts and currentness. Detection signals, verification observations and evidence claims are retired channels; `review_matrix` is removed. The old list below and the port docstring do not describe current readable collections.
>
> `serving_collaborators`'s `review_port` is unchanged in *shape* — it still serves one review through the application adapter, now calling `read_complete_knowledge_review(config, request)` after resolving once for both halves (MIK-R40 rule 2) — and what changed is what
> that loader is: `review_records_for` is now
> [`application/review_evidence_records.py`](../application/review_evidence_records.py.md)'s complete
> resolver, so the production port supplies the **detector signals, the verification observations, the
> authored effects, the evidence claims and the published assessments**, each with the availability fact
> its owner's answer earned, instead of the assessment collection alone. The port's own docstring states
> it for a reader of this file: every collection is read "from the owner's own operation for the candidate
> this request resolves to", a collection an owner answers for and holds none is a measured zero, expected
> content that could not be read is `unavailable` with that owner's provenance, and a dependency-currentness
> measurement is reported `not_measured` rather than omitted — so "the bundle never presents an empty tuple
> where three different facts are possible, and one unreadable authority does not withdraw the collections
> that were readable."
>
> **This is the composition the packet's conformance is measured through.** The verification evidence for
> `ICR-R14@v1` drives `serving_collaborators(config).knowledge_review` — the same port `create_app` places
> on the collaborator record — rather than the loader directly, which is why a port that kept supplying
> only assessments would fail the cases even with a correct resolver behind it. **No behaviour moved in
> this module**: the call site, the function-scope import, the placement on the collaborator record and the
> refuse-by-name rule for an absent port are all as they were; only the docstring and the reach of the
> loader changed.
>
> ## 260915-KS-L22 Reviewer-Adapter Composition Root
>
> This section is retained for the wiring it recorded, and its last sentence about the loader's reach is
> **superseded** by the ICR-L14 section above: `review_port` no longer reads "the assessment collection …
> from the curator authority's own publication" alone — it hands over every owner-produced collection.
> The wiring site, the function-scope import and the one-configuration-per-app reason it recorded are
> unchanged.
>
> This section records the L22 increment, which wired the first of those two ports. The section above
> supersedes its count and adds the entry half; the wiring site, the function-scope import and the
> refuse-by-name reason it recorded are unchanged. It reads: `serving_collaborators` binds a second
> application-tier callable beside the capsule compiler, importing `read_knowledge_review` and
> `review_records_for` at function scope, defining the local `review_port` and placing it on the
> collaborator record as `knowledge_review` — so every `create_app` call in this module, live, reload,
> sim and daemon alike, resolves the reviewer adapter through the one function that already knows which
> configuration the app serves. The adapter is composed with its published records: `review_port` calls
> `read_knowledge_review(config, request, review_records_for(config, request))`, reading the assessment
> collection from the curator authority's own publication for the candidate the request resolves to. A
> candidate with no published assessment supplies an empty collection, which the surface displays as
> `unassessed` rather than inventing an assessment — the honest state, and the one a reviewer needs to
> see.

> ## 260915-CAPS-L15 Capsule-Compiler Composition Root
>
> `serving_collaborators(config)` builds the collaborator record **bound to the configuration this
> dashboard serves**, and every `create_app` call in this module goes through it — the reload factory,
> the live app and the sim app alike. Its first job is the capsule compiler: `compile_launch_capsule`
> is an `application`-rank callable and `serving` may not import it, so this composition root — the one
> place that already knows which configuration the app serves — binds it with `partial(...)`. A partial
> rather than a zero-arg factory is the point: the port hands the serving gate a callable that already
> carries the config, so the serving rank never sees a `McpRuntimeConfig` it has no business resolving.
>
> The composition returns one explicit ServingCollaborators value with the source-owned reader ports and config-bound native role-launch routes. There is no dataclasses.replace over a config-free execution-registration base; a source-declared field alone is not host launch/acceptance evidence.
>
> - The composition root and the config-bound compiler it binds.
> - Every `create_app` call in this module resolves its collaborators through that root.
> - The port the bound callable satisfies, and the record it is placed on.
> - **The third reviewer port this root binds: the deferred import and the closure that closes over the config, so every app resolves one listed entry's content through this composition root.**

## Evidence

- The finite64KiB incomplete-header allowance is an explicit serving constant. [65]
- The root admits only the matching canonical external live-leaf memory directory. [66]
- Numbered catalogue questions and developer-tray routes use configuration-scoped owners. [67]
- Reload workers declare their own role and bind archive-aware services. [68]
- Foreground serving passes the finite header limit and cleans sim state. [69]
- Reload passes the same header/shutdown settings through its factory path. [70]
- Live/sim composition and supervision retain separate ownership and outcomes. [71]

- The composition root wires PaseoExplainerHost, application ports and the master contract locator into serving. _master_contract uses the declared master series contract or existing canonical folder contract; no other line is borrowed. [72]
