# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Run dashboard supervision or live/reload/sim serving and bind configuration-scoped application readers, native role-launch and developer-tray routes.

## Code Commentary

The composition root wires PaseoExplainerHost, application ports and the master contract locator into serving. _master_contract uses the declared master series contract or existing canonical folder contract; no other line is borrowed.

serving_collaborators is the rank boundary: complete review, numbered entry catalogue, source content, summary, tree and knowledge reader are injected application callables, and `held_reset_delivery=reset_delivery_ports(config)` wires the independent held-message reset adoption and delivery ports into serving. It creates app-local ReviewerWorklistProcesses pools (tree reads and lowered-priority _leaf_build precompute), supplies tree reads and their shutdown, and wraps recorded intent/catalogue/tree questions in RecordedReviewAnswers. The application owners define their payloads; retained all-owner-record and knowledge-diff docstrings do not restore retired channels.

review_entries_port now takes optional number and calls list_comparison_review_entries with that exact selector through the reuse owner. api_routes registers native role launch, then developer chat/tray seat/send/sent-pick routes, supplying the same admitted leaf-memory resolver for review references. This is composition, not a second developer-delivery implementation.

_review_memory_root requires valid simple repo/master/leaf names, an external leaf under the matching coordination/task enclosure and an existing canonical non-symlink memory directory below its group, distinct from code/group roots and outside provider-runtime. It performs no Git capture/index read and rejection is None. This admission does not authenticate every descendant or authorize a mutation.

run declares the process dashboard role, loads explicit settings or trusted discovery, binds archive-aware worktree services and chooses daemon/status/stop, reload or foreground serving. Config/discovery failures print and return1. Process roles are declared at entry points, including the spawned _dev_app factory, not create_app; they do not replace unconditional durable-log locking.

Foreground and reload Uvicorn calls now request h11_max_incomplete_event_size=64*1024 as well as the existing3-second graceful window. The finite request-head allowance supports the up-to500-invariant card query named in the source rationale. This is explicit configuration, not a fresh network/runtime/version measurement or a whole-process shutdown guarantee.

Both foreground and reload Uvicorn calls pass `log_config=dashboard_log_config()`. `dashboard_log_config()` deep-copies `uvicorn.config.LOGGING_CONFIG`, references dotted subclasses `_UtcDefaultFormatter` and `_UtcAccessFormatter` (each setting `converter = staticmethod(time.gmtime)` without mutating global `logging.Formatter.converter`) with `datefmt="%Y-%m-%dT%H:%M:%SZ"` on the `default`, `access`, and `package` formatters so every formatted line carries a UTC ISO-8601 prefix while keeping the config pickleable for `--reload`, and binds the `agents_remember` logger at `INFO` with `propagate: False` on an uncolored `stderr` `StreamHandler`. Uvicorn applies this configuration in foreground and reload workers; stubbing `uvicorn.run` leaves the caller's logging unconfigured.

Reload carries config/interval/explicit heartbeat through AR_DASHBOARD_DEV_* and uses an import-string factory; reload+sim is refused. Live apps receive interval/heartbeat. Sim uses interval plus ProjectionReplay, retains SimSetup for the server lifetime and cleans its temporary root in finally. Shared composition is not byte-equivalence proof.

Daemon/status/stop reject sim/reload; `_run_daemon_command` hands them to `cli/dashboard_daemon.run_daemon_command` with this module's host observe and host start. Status identifies the dashboard by the process that answers on its port, prints its build currentness and best-effort diagnostics without changing exit policy and observes host: dashboard-down or identity-unknown1, otherwise host-ready0 or host-down3. Stop targets dashboard only and returns1 when the dashboard's identity is unknown. Ensure delegates dashboard supervision and installed-host readiness without installing/upgrading a host. Foreground/reload starts host readiness on a daemon thread unless parent-owned; sim does not.

Parser defaults remain loopback host, config-driven port, interval1.0 and optional heartbeat, with sim/speed, no-access-log and mutually exclusive control flags. Loopback is a default, not authentication. Native role routes and archive services do not themselves accept/commit/finalize a task.


The composition root binds the projector's host-activity refresher to `RoleRegistryActivityReader`. Its attempt restores missing receipt-backed role records and evaluates reclaimable rows before a qualified boot can read the bridge activity snapshot. A later independent publication can retry an incomplete attempt.

## Invariants And Boundaries

Configuration identity, admitted watch/reference roots, read availability, delivery and semantic approval remain distinct. Recorded questions may be reused only through their owner rules and exact inputs; working-view reads stay fresh.

## Evidence

- The finite64KiB incomplete-header allowance is an explicit serving constant. [65]
- The root admits only the matching canonical external live-leaf memory directory. [66]

- Numbered catalogue questions and developer-tray routes use configuration-scoped owners.

- Reload workers declare their own role and bind archive-aware services. [68]

- Foreground serving passes the finite header limit and cleans sim state. [69]

- Reload passes the same header/shutdown settings through its factory path. [70]

- Live/sim composition and daemon supervision retain separate ownership and outcomes. [71]




- The composition root wires PaseoExplainerHost, application ports and the master contract locator into serving. _master_contract uses the declared master series contract or existing canonical folder contract; no other line is borrowed. Anchor: `PaseoExplainerHost` [72]




- The daemon, status and stop commands delegate to the dashboard daemon adapter with this module's host observe and host start. [73]



- The dashboard binds a registry-aware activity reader. A qualifying attempt checks role records before reading the activity snapshot. [74]


- Foreground and reload Uvicorn paths pass `dashboard_log_config()`, configuring UTC ISO-8601 timestamps through `_UtcDefaultFormatter` and `_UtcAccessFormatter` and binding `agents_remember` `INFO` logging on stderr without mutating global `logging.Formatter.converter`. [75]
