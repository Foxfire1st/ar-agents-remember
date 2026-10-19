# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Dashboard CLI and configuration-bound composition root. `run` declares its process role, resolves
trusted settings and chooses daemon supervision, dev reload, or foreground live/sim serving.
Serving receives application-ranked read callables rather than importing those owners. This adapter
is neither a review-result cache nor a semantic acceptance authority.

## Complete-review collaborator wiring

`review_port` forwards to `read_complete_knowledge_review(config, request)`. Shared resolution and
current record collections belong to that application owner. The retained broad docstring still
names retired detection/verification/evidence channels: it is historical commentary, not today's
payload contract. Tree, entry-list, source-content, summary and knowledge-reader reads retain separate
ports; a tree answer no longer carries the retired aggregate knowledge diff.

## Code Commentary

### Composition (`serving_collaborators`)

The root creates one `ReviewerWorklistProcesses` per composed app, supplies it to tree reads and
injects its `shutdown` for lifespan cleanup. It also supplies complete review, entry-list,
source-content, config-bound summary, knowledge-reader, config-bound native role-launch routes and
host-activity reconciliation. `create_app` registers extra routes before static mounting. No capsule
compiler, terminal-catalog registrar or operator-inbox execution registrar is bound here.

### Exact live memory-root admission

The added `review_memory_root=partial(_review_memory_root, config)` resolves a root for the live review
watcher; it does not compute a worklist or read knowledge. Repo/master/leaf selectors must be nonempty,
contain neither slash form and not start with a dot. `recorded_leaf_contract` selects a readable,
non-abandoned matching contract; this adapter additionally requires leaf kind, external memory mode,
this coordination/task authority and an enclosure under that task.

The memory root must be an existing directory, already equal its resolved path, not be a symlink,
differ from the code root and worktree-group root, lie below that resolved group and contain no
`provider-runtime` path component. The code root must also be a directory. Rejection returns `None`,
not an empty index or measured-zero knowledge answer. The helper performs no Git capture or index
read. Root admission does not authenticate every descendant, prove artifact currentness or authorize
mutations.

### Serving modes (`run`)

- Resolve `args.config or discover_config()` through shared `load_config`; settings/discovery errors
  print their error and return `1`. Explicit settings are not replaced by discovery.
- Daemon/status/stop dispatch to recorded dashboard supervision and reject sim/reload. Status probes
  the dashboard, prints best-effort background diagnostics when alive, then observes host status;
  it returns `1` for dashboard-down, otherwise `0` for host-ready or `3` for host-not-ready.
  Diagnostic failure prints unavailable without changing this policy. Stop targets the recorded
  dashboard process only and returns `0`. Ensure prints dashboard and host outcomes, returning `1`
  for a failed dashboard action and otherwise `0`/`3` by host readiness.
- Reload supplies the import-string `_dev_app` factory, carrying config/interval and an explicitly
  supplied heartbeat through `AR_DASHBOARD_DEV_*`. The spawned factory declares its own dashboard
  role and binds archive-aware worktree services. Reload plus sim is rejected.
- Foreground `_build_app` uses the same collaborator root. Live serving carries interval/heartbeat;
  sim carries interval and `ProjectionReplay(now=sim.clock.now, before_tick=sim.feeder.feed)`.
  The returned SimSetup retains its temporary root until `run` cleans it after serving. Shared
  composition is not proof of equal live/sim payload bytes or indistinguishable UI states.
- Both Uvicorn calls request `timeout_graceful_shutdown=3` for endless SSE responses. That setting
  is not a freshly measured total process/lifespan shutdown bound.
- Live foreground/reload paths start host readiness on a daemon thread when not parent-owned; sim
  does not. Status observes rather than ensures; dashboard stop is not a host-stop operation.

### Arguments

The parser declares config, host (default `127.0.0.1`), port, interval (default1.0), heartbeat, reload,
sim/speed, mutually exclusive daemon/status/stop, no-access-log and the suppressed parent-owner flag.
Loopback is a default, not authentication: another host can be supplied, and help warns against exposure.

### Role Runtime and Scope

`run` and `_dev_app` stamp process roles, not `create_app`. Advisory shared-store writer/compaction
selection differs from unconditional log locking. Both dashboard entry paths bind default worktree
services with `LeafAgentArchive(config)` after resolving config and before composition.

## Invariants And Boundaries

A missing watch root, an unavailable port, a read-only data answer and a semantic verdict are different
facts. Stored discovery/latency assertions are not fresh tests, latency acceptance or a MEMORY grade.
The source comment's Uvicorn0.49.0 startup refusal is a retained historical version-specific observation,
not a fresh check of today's installed version.

## Leaf agent archive binding (MIK-R76)

Archive-aware services are bound by `run` and `_dev_app`; this composition does not itself finalize,
abandon, archive or commit a task.

## 260718-CHATS-L5I Current Delta

The historical shutdown intent is retained as a requested three-second graceful window for endless
SSE responses. No new signal/runtime observation was performed in this curation pass.

## 260821-CLIVE Task-Execution Registration Wiring

Native role-launch routes remain injected beside retained review/reader ports. Deleted execution
registrars and capsule-launch/compiler wiring are not restored by an available field declaration.

## 260928-MIK-L96 The host in dashboard supervision

Status/stop/ensure and the background readiness worker are distinguished above. CLI stop calls no host
termination; a diagnostic failure cannot change status supervision.

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

- Frozen implementation of serving_collaborators supporting the stated file behavior. [22]
- Frozen implementation of _dev_app supporting the stated file behavior. [23]
- Frozen implementation of run supporting the stated file behavior. [24]
- The command-line arguments. [25]
- The entry: role, settings, daemon commands, reload, foreground, and the fixture's cleanup. [26]
- The reload server passes its configuration through the environment. [27]
- The live app and the replayed fixture are both composed through serving_collaborators. [28]
- The daemon commands. [29]
- The process owner that the composition creates. [30]
- The stored leaf-wide latency case exercises this composition and asserts source capture/worklist reuse; this is not fresh execution or a latency grade. [31]
- The CLI requests a three-second Uvicorn graceful window and injects current registrar collaborators; the timeout alone is not a measured whole-process shutdown bound. [32]
- The composition: one worklist process owner per app, the ports, and the owner's shutdown. [33]
- The reload worker's factory declares the process role and composes the same collaborators. [34]
- The status/stop/daemon dispatch with host handling. [35]
- The background host-start worker. [36]
- Host status is observed by the host-supervision owner; CLI status prints its answer without invoking host ensure. [37]
- The actual serving collaborator calls the complete-review owner. [38]
- The deferred import of the reader. [39]
- The reader port, bound on the collaborator record beside the reviewer ports. [40]
- The reader entry point delegates to the knowledge-reader owner and this CLI supplies its config-bound caller. [41]
- The tree port forwards its query with the app-local worklist process owner; fifth-port is a historical ordinal, not a current census. [42]
- The module imports the summary adapter and binds its returned port to this configuration. [43]
- The umbrella dispatcher that registers this subcommand. [44]
- Explicit settings precede trusted discovery; discovery and load failures return the CLI settings-error path. [45]
- The daemon-control branch delegates supervision to the daemon owner with requested endpoint and cadence, separately from foreground/reload serving. [46]
- The watcher owner defines the default heartbeat and ChangePacer; the CLI imports and passes cadence rather than implementing a watcher. [47]
- The parser declares interval/heartbeat, which reload parent/worker, live-app and daemon calls carry; sim constructs interval-only cadence. [48]
- The serving factory accepts ProjectionReplay; the CLI sim path supplies now/before_tick through that value, not obsolete direct factory keywords. [50]
- The sim builder/speed parser construct temporary replay state; the CLI keeps SimSetup alive until foreground server cleanup. [51]
- McpRuntimeConfig/load_config is the shared runtime-settings contract used by this CLI settings adapter. [52]
- Role declaration selects advisory writer/compaction ownership, not unconditional per-log locking; the durable-store owner defines both boundaries. [53]
- The MCP process declares its role in its actual main entry point, not an in-process app factory. [54]
- Frozen implementation of serving_collaborators supporting the stated file behavior. [55]
- Frozen implementation of _dev_app supporting the stated file behavior. [56]
- Frozen implementation of run supporting the stated file behavior. [57]
- Every create_app call in this CLI obtains collaborators from its config-bound composition root in the reload factory or live/sim builder. [59]
- The source-content closure forwards the supplied request with this config; third-port is a historical ordinal, not a current census. [61]
- Stored discovery cases cover convention precedence, nearest directory, malformed entries and missing config; they are not a fresh test run. [62]
- The live memory-root resolver rejects unsafe selectors and roots, admits the addressed external leaf contract under this authority and is bound into the app without Git capture or index reads. [63]
- The shared collaborator record exposes the injected memory-root and retained read/route ports; this CLI binds no capsule-compiler port. [64]

## 260928-MIK-L177 Recorded Reads Are Kept By Their Exact Inputs

The reviewer's task-context `intent`, its `entries` and its tree view now pass through
`RecordedReviewAnswers` — the composition root wires `dashboard_review_reads.RecordedReviewAnswers`
over `serving.review_answer_reuse.RecordedAnswerReuse` — so a recorded comparison's answers are served
again unchanged while the record, its directories, the worklist and the objects it names all hold, and
a live comparison is computed on every read. The read bodies themselves are unchanged: the kept
answer is produced by the same call the route used before.
