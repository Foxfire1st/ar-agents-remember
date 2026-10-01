# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/dashboard.py` is the `agents-remember dashboard` subcommand adapter: it parses the serving
flags and launches the FastAPI app under uvicorn. It mirrors the MCP server's `--config` contract
so the dashboard resolves the identical coordination context — and since 260703 L1 the flag is
**optional**: an omitted `--config` is discovered by `cli/discovery.py`'s upward walk, so the
command runs flag-free from anywhere under the workspace. It wires sim replay via
`--sim` / `--sim-speed` (4b), offers dev hot-reload via `--reload` (task 26), and since 260703 L2
fronts the daemon supervisor: `--daemon` / `--status` / `--stop` dispatch to `serving/daemon.py`
so the dashboard can outlive the terminal that started it.

## Code Commentary

`add_arguments(parser)` registers `--config` (default `None`; its help documents the discovery
fallback), `--host` (default `127.0.0.1`), `--port` (260703 L2: default `None` — resolved after
config load as `args.port or config.dashboard.port`, so the settings key governs and an explicit
flag wins), `--interval` (default `1.0s`; **re-documented by 260712-PTS-L3 as the fast-path
projection cadence floor** — change-driven re-projections are never spaced closer than this, a
continuously-busy world still projects once per interval, and it stays the fixed tick cadence
under `--sim` or when the change watcher is unavailable; also the `/api/events` raw-tail poll
cadence), `--heartbeat` (**260712-PTS-L3**, default `None` ⇒ the serving
`DEFAULT_HEARTBEAT_SECONDS` = 15s: the idle re-projection cadence — with no detected input change
the projection still refreshes at this cadence, the staleness bound for `/api/state` and for
time-derived fields such as `ageSeconds`/`staleSeconds` and stale/overdue flips), `--reload` (a
`store_true` dev hot-reload flag, live
state only), the 4b sim flags `--sim` (a fixture dir with `logs/observer/...`, default `None`)
and `--sim-speed` (default `"1"`; a multiplier or `"paused"`), a mutually exclusive daemon
control group `--daemon` / `--status` / `--stop` (260703 L2), and `--no-access-log` (serve
without per-request access logs; the daemon child uses it to keep its log bounded — both
foreground `uvicorn.run` call sites pass `access_log=not args.no_access_log`).

`run(args)` opens with `declare_process_role("dashboard")` (260731-EFA-L5, L148 — the first
statement in the function, before any settings work), then calls `_resolve_settings(args)`
(260731-EFA-L2), which resolves
`config_path = args.config or discover_config()` — an explicit flag always wins — and loads it,
printing the message and returning `None` for **either** `ConfigDiscoveryError` or `ConfigError`;
`run` turns that `None` into exit `1`. It then resolves the effective `port`, routes any
daemon control flag to `_run_daemon_command(args, config, port)` — `--status` prints the probed
state (exit 0 running / 1 not), `--stop` prints the stop outcome, `--daemon` runs
`serving_daemon.ensure(config, serving_daemon.DaemonEndpoint(host=args.host, port=port),
cadence=ProjectionCadence(interval=args.interval, heartbeat=args.heartbeat))` and
exits 0 only for `adopted`/`started`/`restarted` (heartbeat, like interval, reaches the child only
when ensure spawns/restarts — an adopted daemon keeps its cadences); all three reject
`--sim`/`--reload` combos — then dispatches in priority order:

- **reload** (`--reload` set): delegated to `_run_reload_server(args, config_path, port)`
  (260731-EFA-L2). It rejects `--sim` (`error: --reload is not supported with --sim`,
  return `1`). Otherwise it sets `AR_DASHBOARD_DEV_CONFIG` (the resolved absolute settings path —
  discovered or explicit) and `AR_DASHBOARD_DEV_INTERVAL` env vars — plus (260712-PTS-L3)
  `AR_DASHBOARD_DEV_HEARTBEAT` only when `--heartbeat` was explicit — then calls
  `uvicorn.run("agents_remember.cli.dashboard:_dev_app", factory=True, reload=True,
  reload_dirs=[<package source dir>], host=..., port=...)` and returns `0`.
- **sim or live**: both are built by `_build_app(args, config) -> _DashboardApp | None`
  (260731-EFA-L2) — "the app to serve: live state, or a replayed fixture; `None` when the fixture
  is unusable". With `--sim` it runs
  `build_sim(config, Path(args.sim), speed=parse_sim_speed(args.sim_speed))` (printing and
  returning `None` on `SimError` — bad speed or empty fixture), then
  `create_app(sim.config, cadence=ProjectionCadence(interval=args.interval),
  replay=ProjectionReplay(now=sim.clock.now, before_tick=sim.feeder.feed))` — no `heartbeat` and no
  watcher, so replay stays time-driven on the fixed `--interval`. Without `--sim` it is
  `create_app(config, cadence=ProjectionCadence(interval=args.interval, heartbeat=args.heartbeat))`
  (260712-PTS-L3 — live serving gets change-driven + heartbeat pacing). `run` then serves
  `built.app` with `uvicorn.run(...)`.

**`_DashboardApp(app, sim)`** (a `NamedTuple`) is why the sim survives the server: it carries the
`SimSetup` alongside the app rather than dropping it at build time, **because the sim owns the
throwaway coordination root the server is reading** — releasing it would reclaim the directory
under a running server. `run` keeps `built` referenced for the whole `uvicorn.run` call and, in a
`finally`, calls `built.sim.temp_dir.cleanup()` when there is a sim. Closing it there is what ends
the root's life: dropping the reference instead would leave the directory to
`TemporaryDirectory`'s finaliser, which is a ResourceWarning, not a cleanup.

`_dev_app()` is the zero-arg import-string app **factory** for the reload path: uvicorn's reloader
re-imports the app per worker restart, so it needs a factory, not a pre-built app object. Passing
an object does **not** silently disable reload — uvicorn refuses to start and exits `1` (pinned
citation in the `--reload` invariant below). The factory re-reads the resolved config from
`AR_DASHBOARD_DEV_CONFIG` (`load_config(...)`), the interval from `AR_DASHBOARD_DEV_INTERVAL`
(default `1.0`), and (260712-PTS-L3) the optional heartbeat from `AR_DASHBOARD_DEV_HEARTBEAT`
(absent/empty ⇒ `heartbeat=None`, the serving default) — the env vars the parent `run` set — and
returns `create_app(config, cadence=ProjectionCadence(interval=..., heartbeat=...))`. It is
live-state only; it never builds a sim. `reload_dirs` watches only the
package source dir (`Path(agents_remember.__file__).parent`) so unrelated trees don't churn the
reloader. `os`, `uvicorn`, `create_app`, and the sim helpers are imported at module top (the
established CLI convention); `import agents_remember` is local to the reload branch.

### 260731-EFA-L5: the durable-store process role (the whole change here)

This file's entire L5 change is seven lines — the `declare_process_role` import (L20) and a
five-line comment plus the call as the first statement of `run` (L143-L148; `def run` is L142). No
flag, no dispatch order, no exit code and no serving call moved.

`controlplane/durable_store.py` names two concurrent writers of the six control-plane JSONL logs,
`"mcp"` and `"dashboard"`; the declaration is what lets code shared by both processes — most
importantly `mcp/tools/gates.py::gate_decide_payload`, which `serving/app.py` calls **directly** —
ask which one it is in. It sits at the top of `run` rather than inside `create_app` for the same
reason the MCP server's sits in `main` rather than `create_server`: `create_app` is a factory the
test suite calls in-process, `durable_store._declared` is a module-level dict with no reset, and a
declaration made in the factory would stamp `"dashboard"` onto the interpreter and every later test
in it.

**Which serving processes this actually reaches, measured rather than assumed:**

| Path | Serves in | Declares `"dashboard"` |
| --- | --- | --- |
| foreground live / `--sim` | this process (`uvicorn.run(built.app, ...)`) | yes |
| `--daemon` | a child `sys.executable -m agents_remember.cli dashboard ...` (`serving/daemon.py` L201-L214), which re-enters `run` | yes |
| `--reload` | a **spawned** uvicorn worker, not this process | **no** |

The `--reload` row is a real gap, and it is worth stating precisely rather than rounding off.
`uvicorn.run(..., reload=True)` keeps only the reload supervisor in the process that called it and
serves from a child built by `multiprocessing.get_context("spawn")` (uvicorn 0.49.0,
`uvicorn/_subprocess.py` L18 + `uvicorn/supervisors/basereload.py` L84-L85). A spawn-context child
does not inherit the parent's module globals — measured directly: a parent that mutates a module
dict before `Process.start()` and a child that reports the same dict give `{'role': 'dashboard'}`
and `{}`. So under `agents-remember dashboard --reload`, the process that serves HTTP, decides
gates and writes these logs has declared no role at all, and `StoreOwnership.is_compaction_owner()`
answers `True` for every log (`role is None`). A dev-reload dashboard therefore *does* run the gate
reclaim pass that a normal dashboard skips.

That is an ownership-advisory gap, not a durability one, and the difference is the point of the
contract: the reclaim still holds the log's `flock` across its read **and** its rewrite like every
other writer, so no record is lost either way. What it falsifies is the contract's stated reason for
letting an undeclared process count as owner — "a CLI or test run is nobody's competitor"
(`durable_store.StoreOwnership.is_compaction_owner`) — because a `--reload` dashboard can be running
against the same coordination root as a live MCP server. Closing it means declaring the role inside
`_dev_app()` as well; nothing else about this file would change.

## 260928-MIK-L29 The Knowledge Reader Port

`serving_collaborators` binds one more callable, `knowledge_reader_port(query)`, which returns
`read_knowledge_reader(config, query)` (`application/knowledge_reader/__init__.py`) and is placed on the
collaborator record as `knowledge_reader`. It is imported at function scope with the same deferred-composition
idiom as the reviewer ports. It is **not** a reviewer port: the path-based knowledge reader (MIK-R29) needs no
task, so it is its own port rather than a mode of the review adapter. It serves read-only views of any
converted memory tree at `GET /api/knowledge/reader/{view}`; an unconverted tree answers `not-converted` and the
landed routes answer byte-identically (the worker's and reviewer's unconverted comparisons). The worker's
real-data reads and the browser walkthrough were served through this composition.

- The deferred import of the reader. [1]
- The reader port, bound on the collaborator record beside the reviewer ports. [2]
- The entry point the port calls. [3]

## 260928-MIK-L25 The Fifth Reviewer Port: The Tree View

`serving_collaborators` binds a **fifth** reviewer callable, `review_trees_port(query)`, which returns
`read_review_trees(config, query)` (`application/review_tree_knowledge.py`) and is placed on the collaborator record
as `review_trees`. It is imported at function scope with the same deferred-composition idiom as its siblings. It
answers, for a leaf whose memory is converted, what the dataset review cannot: the four Git trees, the Git diff of
the memory trees, the per-side currentness and the worklist view (MIK-R25 rules 1–3). The same composition is what
the worker's real-data captures and the dashboard fixtures were served through.

- The deferred import and the fifth port bound on the collaborator record. [4]

## 260921-ICR-L47 The Fourth Reviewer Port: The Changed-Intent Summary

`serving_collaborators` binds a **fourth** reviewer callable, `review_intent_summary_port(repository_id,
master, leaf_id)`, which returns `read_review_intent_summary(config, repository_id, master, leaf_id)` and
is placed on the collaborator record as `review_intent_summary`. It is imported at function scope with the
same deferred-composition idiom as its siblings. Its docstring states the reason it is its own port: it
answers a fourth question — how many statements each side of the comparison alone holds — from the **same
resolution** as the other two task-context ports, so the numbers beside the task entry describe the review
it opens, and it reads no subject catalogue to produce them (`ICR-R24@v3`).

- The deferred import and the fourth port bound on the collaborator record. [5]

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

`serving_collaborators`'s `review_port` is unchanged in *shape* — it still calls
`read_knowledge_review(config, request, review_records_for(config, request))` — and what changed is what
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

## Evidence

### Repo-Internal References

- The umbrella dispatcher that registers this subcommand. [6]
- The trusted-settings discovery the optional `--config` falls back to. [7]
- The daemon supervisor behind `--daemon`/`--status`/`--stop` (heartbeat plumbed on spawn/restart only). [8]
- The serving layer defines the idle heartbeat default and implements change-or-heartbeat scheduling in `ChangePacer`. [9]
- This CLI defines `--interval`/`--heartbeat` and threads their cadence through reload parent/worker, live-app, and daemon paths; sim deliberately carries interval only. (The `add_arguments` named here is this module's, not the identically named function in the CLI module `cli/knowledge_ingest.py`.) [10]
- Discovery unit tests (hits, precedence, template skip, miss error). [11]
- The app factory it serves (and the `now`/`before_tick` seams it passes). [12]
- The sim builder / clock / feeder / speed parser it wires. [13]
- The `--config` → `McpRuntimeConfig` contract it mirrors. [14]
- The durable-store contract whose process role `run` declares — what the role decides, and what the unconditional per-log lock decides instead. [15]
- The MCP server's mirror of the same declaration, in `main` rather than `create_server`. [16]

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

- The composition root and the config-bound compiler it binds. [17]
- Every `create_app` call in this module resolves its collaborators through that root. [18]
- The port the bound callable satisfies, and the record it is placed on. [19]
- **The third reviewer port this root binds: the deferred import and the closure that closes over the config, so every app resolves one listed entry's content through this composition root.** [20]
