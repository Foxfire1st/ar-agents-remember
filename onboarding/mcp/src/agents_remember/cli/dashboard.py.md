# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

The command-line entry of the dashboard server and its composition root. `run` resolves the settings,
declares the process role and serves the app in the foreground, under the reloader, from a recorded
fixture, or as a background daemon. `serving_collaborators` binds the application's callables to the
ports of the serving package, which may not import the application itself.

## Complete-review collaborator wiring

The dashboard knowledge-review collaborator invokes read_complete_knowledge_review: one source/knowledge resolution is shared with record collection and composition. Tree reads retain their own port. This adapter introduces no cache or currentness policy.


- The actual serving collaborator calls the complete-review owner.

## Code Commentary

### Composition (`serving_collaborators`)

Every `create_app` call of this module goes through `serving_collaborators(config)`. It returns the
execution-evidence registrars of `EXECUTION_REGISTRATION_COLLABORATORS` together with:

- `capsule_launch`: `compile_launch_capsule` bound to the configuration;
- `knowledge_review`: `read_complete_knowledge_review`, which resolves the candidate once for the records
  and the composition;
- `knowledge_review_entries`: `list_knowledge_review_entries`;
- `review_source_content`: `read_review_source_content`;
- `review_intent_summary`: `read_review_intent_summary`;
- `review_trees`: `read_review_trees`, called with `processes=worklist_processes`;
- `review_trees_shutdown`: `worklist_processes.shutdown`;
- `knowledge_reader`: `read_knowledge_reader`.

`worklist_processes` is one `ReviewerWorklistProcesses` object created per call of
`serving_collaborators`, that is, one per composed app. It is the owner of the child processes that
compute the reviewer's leaf-wide worklist. The tree port passes it to every read, and the app's lifespan
calls its `shutdown` when serving ends, so the children of one dashboard are bounded and stopped by that
dashboard. The application imports are made inside the function.

### Serving modes (`run`)

- `run` calls `declare_process_role("dashboard")` first, then loads the settings (`--config`, or
  discovery from the working directory). The port is `--port` or the settings' `dashboard.port`.
- `--daemon`, `--status` and `--stop` go to `_run_daemon_command`, which probes, stops or ensures the
  background daemon recorded under the coordination root. They are refused together with `--sim` or
  `--reload`.
- `--reload` goes to `_run_reload_server`. uvicorn's reloader needs an import-string factory, so the
  resolved configuration path, interval and heartbeat are passed through the environment variables
  `AR_DASHBOARD_DEV_CONFIG`, `AR_DASHBOARD_DEV_INTERVAL` and `AR_DASHBOARD_DEV_HEARTBEAT`, and `_dev_app`
  builds the app in the worker. `_dev_app` declares the process role itself, because the reload worker
  is a spawned process that never runs `run`. `--reload` is refused with `--sim`.
- Otherwise `_build_app` builds a live app, or with `--sim` an app that replays a recorded fixture
  through a replay clock and feeder; the fixture's temporary root is kept until the server stops and is
  then cleaned up.
- Every server is started with `timeout_graceful_shutdown=DASHBOARD_GRACEFUL_SHUTDOWN_SECONDS` (3). The
  bound makes a termination signal close the endless event streams and run the lifespan shutdown instead
  of waiting for them.

### Arguments

`add_arguments` declares `--config`, `--host` (default `127.0.0.1`), `--port`, `--interval` (default 1.0),
`--heartbeat`, `--reload`, `--sim`, `--sim-speed`, the mutually exclusive `--daemon`, `--status` and
`--stop`, and `--no-access-log`.

### Role Runtime and Scope

serving_collaborators retains MIK reviewer/knowledge ports and adds extra_api_routes=partial(register_role_launch_routes, config=config). Ordinary and reload factories bind existing worktree services before composition. The serving app registers the injected launch routes before static mount; the reviewer resolution owner is unchanged. Local app variables only flatten the existing create_app return expressions.


### Role Runtime and Scope

serving_collaborators retains MIK reviewer/knowledge ports and adds extra_api_routes=partial(register_role_launch_routes, config=config). Ordinary and reload factories bind existing worktree services before composition. The serving app registers the injected launch routes before static mount; the reviewer resolution owner is unchanged. Local app variables only flatten the existing create_app return expressions.

## 260928-MIK-L29 The Knowledge Reader Port

`serving_collaborators` binds one more callable, `knowledge_reader_port(query)`, which returns
`read_knowledge_reader(config, query)` (`application/knowledge_reader/__init__.py`) and is placed on the
collaborator record as `knowledge_reader`. It is imported at function scope with the same deferred-composition
idiom as the reviewer ports. It is **not** a reviewer port: the path-based knowledge reader (MIK-R29) needs no
task, so it is its own port rather than a mode of the review adapter. It serves read-only views of any
converted memory tree at `GET /api/knowledge/reader/{view}`; an unconverted tree answers `not-converted` and the
landed routes answer byte-identically (the worker's and reviewer's unconverted comparisons). The worker's
real-data reads and the browser walkthrough were served through this composition.

- The deferred import of the reader.
- The reader port, bound on the collaborator record beside the reviewer ports.
- The entry point the port calls.

## 260928-MIK-L25 The Fifth Reviewer Port: The Tree View

`serving_collaborators` binds a **fifth** reviewer callable, `review_trees_port(query)`, which returns
`read_review_trees(config, query)` (`application/review_tree_knowledge.py`) and is placed on the collaborator record
as `review_trees`. It is imported at function scope with the same deferred-composition idiom as its siblings. It
answers, for a leaf whose memory is converted, what the dataset review cannot: the four Git trees, the Git diff of
the memory trees, the per-side currentness and the worklist view (MIK-R25 rules 1–3). The same composition is what
the worker's real-data captures and the dashboard fixtures were served through.

- The deferred import and the fifth port bound on the collaborator record.

## 260921-ICR-L47 The Fourth Reviewer Port: The Changed-Intent Summary

`serving_collaborators` binds a **fourth** reviewer callable, `review_intent_summary_port(repository_id,
master, leaf_id)`, which returns `read_review_intent_summary(config, repository_id, master, leaf_id)` and
is placed on the collaborator record as `review_intent_summary`. It is imported at function scope with the
same deferred-composition idiom as its siblings. Its docstring states the reason it is its own port: it
answers a fourth question — how many statements each side of the comparison alone holds — from the **same
resolution** as the other two task-context ports, so the numbers beside the task entry describe the review
it opens, and it reads no subject catalogue to produce them (`ICR-R24@v3`).

- The deferred import and the fourth port bound on the collaborator record.

## 260921-ICR-L3 The Third Reviewer Port, And Who Chooses The Generation

`serving_collaborators` now binds **three** application-tier reviewer callables, and the third one is
what lets a browser open the entry a reader clicked:

```python
def review_source_content_port(request):
    return read_review_source_content(config, request)
```

It is imported at function scope with the same deferred-composition idiom as its siblings —
`from agents_remember.application.review_source_content import (  # noqa: PLC0415 - composition
read_review_source_content,)` — and placed on the collaborator record as `review_source_content`.

The docstring states the division of labour this port exists to make explicit, and it is the reason the
closed-over value is not a config lookup: **the request carries the generation the browser is looking
at, rather than the server choosing one.** The application owner re-resolves the leaf only to *measure*
whether that generation is still the candidate's; it then reads those two objects and nothing else — no
working tree, no `HEAD`. So an entry opened after the branch moved still shows the **listed**
generation's bytes and says the leaf has moved past them, instead of silently substituting whatever the
branch holds now. Supplying the port is also what decides the route's behaviour: a process that omits it
refuses that route **by name**, because "this process cannot read the entry" and "this entry has no
content" are different facts and only one of them is true.

This is the third instance of one shape of decision on this record: production wires every reviewer port
in this one config-bound composition root, and each port's absence refuses its own route rather than
serving an empty surface.

## 260915-KS-L45 Both Reviewer Ports Wired From One Composition Root

**The count in this section is superseded: the root now binds three reviewer callables since
260921-ICR-L3** (see the section above). The wiring site, the function-scope import idiom and the
refuse-by-name reason it records are still exactly right, so the entry is retained rather than
rewritten.

`serving_collaborators` now binds **two** application-tier reviewer callables, and the second one is
what makes a task view able to ask the question the first one needs an answer to:

```python
def review_entries_port(repository_id, master, leaf_id):
    return list_knowledge_review_entries(config, repository_id, master, leaf_id)
```

It imports `list_knowledge_review_entries` beside `read_knowledge_review` and `review_records_for`
from `agents_remember.application.knowledge_review` at function scope, and places both on the
collaborator record as `knowledge_review` and `knowledge_review_entries`. The two ports are one
composition and one resolution: the entry call takes the **task context alone**, because a subject is
exactly what it is being asked for, and the task view calls it *before* any subject exists. The
docstring states the property this buys: resolving the entry list "through the identical operation
the review route uses … is what keeps the entry a caller is offered and the review it then opens on
one candidate". Supplying a port is also what decides its route's behaviour — the serving layer
refuses each route **by name** when its field is absent, because an empty pane (or an empty entry
list, which would read as "nothing is reviewable here") and an unreachable adapter are different
facts.

## 260921-ICR-L14 The Review Port Supplies The Complete Record Collection

`serving_collaborators`'s `review_port` is unchanged in *shape* — it still serves one review through the application adapter, now calling `read_complete_knowledge_review(config, request)` after resolving once for both halves (MIK-R40 rule 2) — and what changed is what
that loader is: `review_records_for` is now
[`application/review_evidence_records.py`](../application/review_evidence_records.py.md)'s complete
resolver, so the production port supplies the **detector signals, the verification observations, the
authored effects, the evidence claims and the published assessments**, each with the availability fact
its owner's answer earned, instead of the assessment collection alone. The port's own docstring states
it for a reader of this file: every collection is read "from the owner's own operation for the candidate
this request resolves to", a collection an owner answers for and holds none is a measured zero, expected
content that could not be read is `unavailable` with that owner's provenance, and a dependency-currentness
measurement is reported `not_measured` rather than omitted — so "the bundle never presents an empty tuple
where three different facts are possible, and one unreadable authority does not withdraw the collections
that were readable."

**This is the composition the packet's conformance is measured through.** The verification evidence for
`ICR-R14@v1` drives `serving_collaborators(config).knowledge_review` — the same port `create_app` places
on the collaborator record — rather than the loader directly, which is why a port that kept supplying
only assessments would fail the cases even with a correct resolver behind it. **No behaviour moved in
this module**: the call site, the function-scope import, the placement on the collaborator record and the
refuse-by-name rule for an absent port are all as they were; only the docstring and the reach of the
loader changed.

## 260915-KS-L22 Reviewer-Adapter Composition Root

This section is retained for the wiring it recorded, and its last sentence about the loader's reach is
**superseded** by the ICR-L14 section above: `review_port` no longer reads "the assessment collection …
from the curator authority's own publication" alone — it hands over every owner-produced collection.
The wiring site, the function-scope import and the one-configuration-per-app reason it recorded are
unchanged.

This section records the L22 increment, which wired the first of those two ports. The section above
supersedes its count and adds the entry half; the wiring site, the function-scope import and the
refuse-by-name reason it recorded are unchanged. It reads: `serving_collaborators` binds a second
application-tier callable beside the capsule compiler, importing `read_knowledge_review` and
`review_records_for` at function scope, defining the local `review_port` and placing it on the
collaborator record as `knowledge_review` — so every `create_app` call in this module, live, reload,
sim and daemon alike, resolves the reviewer adapter through the one function that already knows which
configuration the app serves. The adapter is composed with its published records: `review_port` calls
`read_knowledge_review(config, request, review_records_for(config, request))`, reading the assessment
collection from the curator authority's own publication for the candidate the request resolves to. A
candidate with no published assessment supplies an empty collection, which the surface displays as
`unassessed` rather than inventing an assessment — the honest state, and the one a reviewer needs to
see.

## Invariants And Boundaries

- **Localhost-only by default** (`--host 127.0.0.1`); the help text warns against exposing it.
- Resolves config through the same `load_config` the MCP server uses — no bespoke path handling.
- **Discovery only fills an omitted flag** — `args.config or discover_config()`; an explicit
  `--config` is never second-guessed, and discovery failures exit `1` with the both-patterns
  error rather than guessing.
- **Foreground behavior is unchanged by the daemon feature** — no control flag means the same
  serve-in-this-terminal flow as before (the `--reload` dev loop included); daemon logic lives in
  `serving/daemon.py`, this file only dispatches.
- **Sim never mutates the fixture** — `build_sim` runs against a throwaway temp root; the
  frontend cannot tell sim from live.
- **`--reload` is live-state only** — it is mutually exclusive with `--sim` (rejected with exit
  `1`), and it must hand uvicorn the `_dev_app` import-string factory (`factory=True`), never a
  built app object. Handing uvicorn a built object does **not** make hot-reload silently no-op —
  uvicorn **refuses to start, loudly**. Pinned: **uvicorn 0.49.0**, `uvicorn/main.py` lines
  **604-607** — `if (config.reload or config.workers > 1) and not isinstance(app, str):` logs the
  `uvicorn.error` warning `"You must pass the application as an import string to enable 'reload' or
  'workers'."` and calls `sys.exit(1)`. Measured: `uvicorn.run(<built app object>, reload=True)`
  under the repo `.venv` printed that warning and exited with code **1**, before binding the port.
  So a `factory=True` regression is a hard startup failure, not a silently degraded dev loop.

## Leaf agent archive binding (MIK-R76)

Both dashboard composition entry points (`_dev_app` and `run`) build the default worktree services
with `leaf_agent_archive=LeafAgentArchive(config)` after the configuration is resolved, so a
dashboard-driven finalize or abandon reaches the archive service. The declaration order and the
existing process-role stamps are unchanged.

## Evidence

- The bounded graceful shutdown and the registrar collaborators. [32]
- The composition: one worklist process owner per app, the ports, and the owner's shutdown. [33]
- The reload worker's factory declares the process role and composes the same collaborators. [34]
- The command-line arguments. [25]
- The entry: role, settings, daemon commands, reload, foreground, and the fixture's cleanup. [26]
- The reload server passes its configuration through the environment. [27]
- The live app and the replayed fixture are both composed through serving_collaborators. [28]
- The daemon commands. [29]
- The process owner that the composition creates. [30]
- The dashboard's tree port resolves once and computes the leaf-wide view once per comparison. [31]

### Runtime Source References

- Frozen implementation of serving_collaborators supporting the stated file behavior. [22]
- Frozen implementation of _dev_app supporting the stated file behavior. [23]
- Frozen implementation of run supporting the stated file behavior. [24]

- The actual serving collaborator calls the complete-review owner. [38]
- The deferred import of the reader. [39]
- The reader port, bound on the collaborator record beside the reviewer ports. [40]
- The entry point the port calls. [41]
- The deferred import and the fifth port bound on the collaborator record. [42]
- The deferred import and the fourth port bound on the collaborator record. [43]
- The umbrella dispatcher that registers this subcommand. [44]
- The trusted-settings discovery the optional `--config` falls back to. [45]
- The daemon supervisor behind `--daemon`/`--status`/`--stop` (heartbeat plumbed on spawn/restart only). [46]
- The serving layer defines the idle heartbeat default and implements change-or-heartbeat scheduling in `ChangePacer`. [47]
- This CLI defines `--interval`/`--heartbeat` and threads their cadence through reload parent/worker, live-app, and daemon paths; sim deliberately carries interval only. (The `add_arguments` named here is this module's, not the identically named function in the CLI module `cli/knowledge_ingest.py`.) [48]
- The dashboard CLI argument parser (`add_arguments`).

- The discovery config tests — convention-wins at 43, nearest-directory at 53, malformed-skipped at 63, miss-error at 80; the discovery behavior lives in the test module, not in this CLI's `add_arguments`. [62]

- The app factory it serves (and the `now`/`before_tick` seams it passes). [50]
- The sim builder / clock / feeder / speed parser it wires. [51]
- The `--config` → `McpRuntimeConfig` contract it mirrors. [52]
- The durable-store contract whose process role `run` declares — what the role decides, and what the unconditional per-log lock decides instead. [53]
- The MCP server's mirror of the same declaration, in `main` rather than `create_server`. [54]
- Frozen implementation of serving_collaborators supporting the stated file behavior. [55]
- Frozen implementation of _dev_app supporting the stated file behavior. [56]
- Frozen implementation of run supporting the stated file behavior. [57]
- The composition root and the config-bound compiler it binds. [58]
- Every `create_app` call in this module resolves its collaborators through that root. [59]
- The port the bound callable satisfies, and the record it is placed on. [60]
- **The third reviewer port this root binds: the deferred import and the closure that closes over the config, so every app resolves one listed entry's content through this composition root.** [61]

## 260718-CHATS-L5I Current Delta

Dashboard shutdown now uses a bounded three-second Uvicorn graceful window. This explicitly terminates intentionally endless SSE responses so lifespan cleanup can cancel projector, landing, and supervisor tasks instead of leaving a process alive after SIGTERM.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260821-CLIVE Task-Execution Registration Wiring

The production dashboard supplies the task-plane registrars for both terminal-catalog rows and
operator-inbox reports when it constructs serving collaborators. Those registrars durably record
worker/reviewer/curator first evidence before the serving retention loops may reclaim their source
rows. This is the production dependency-injection boundary; omitted test seams remain fail-closed
for task-bound deletion rather than using a compatibility reader.

## 260915-CAPS-L15 Capsule-Compiler Composition Root

`serving_collaborators(config)` builds the collaborator record **bound to the configuration this
dashboard serves**, and every `create_app` call in this module goes through it — the reload factory,
the live app and the sim app alike. Its first job is the capsule compiler: `compile_launch_capsule`
is an `application`-rank callable and `serving` may not import it, so this composition root — the one
place that already knows which configuration the app serves — binds it with `partial(...)`. A partial
rather than a zero-arg factory is the point: the port hands the serving gate a callable that already
carries the config, so the serving rank never sees a `McpRuntimeConfig` it has no business resolving.

The rule this section exists to state: **a dashboard process can never serve a role-configured launch
with no compiler behind it.** `EXECUTION_REGISTRATION_COLLABORATORS` remains the config-free base
record; `serving_collaborators` is a `dataclasses.replace` over it, so a future collaborator added to
the base is not silently dropped by this composition.

- The composition root and the config-bound compiler it binds.
- Every `create_app` call in this module resolves its collaborators through that root.
- The port the bound callable satisfies, and the record it is placed on.
- **The third reviewer port this root binds: the deferred import and the closure that closes over the config, so every app resolves one listed entry's content through this composition root.**

## 260928-MIK-L96 The host in dashboard supervision

`--daemon` now also makes sure the configured host runs: it prints the dashboard line, ensures the host, and ends 0 when dashboard and host are up (or no host is configured) and 3 when the dashboard is up and a configured host is not. `--status` prints the host's line after the dashboard's and uses the same exit statuses; `--stop` still signals only the dashboard's recorded process, and the dashboard's own stop, restart, TERM/KILL and Ctrl-C paths leave the host untouched. A foreground or background serve starts the host from a bounded worker without delaying the dashboard, and an adopting start records the host outcome for the running daemon.

- The status/stop/daemon dispatch with host handling. [35]
- The background host-start worker. [36]
- The host observation the status line comes from. [37]
