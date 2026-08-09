# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/tests/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

### 260713-TES-L1 Rename — Test Surface

The three supervisor test modules were renamed 1:1 (`test_agent_notifier*.py`), and the touched
suites now reference `AgentNotifier*` identifiers, `agentNotifierHeartbeat` /
`agentNotifierBanner`, the `orchestration.agentNotifier` settings family, and the renamed module
paths; legacy-value acceptance and dual-key cases are covered by the new regression tests.

### 260713-TES-L2 Relay Suites

Three forcing suites were added for the worker-state relay: `test_terminal_evidence_projection.py`
(per-vendor outcome mapping, pi tail paging, seat-truth persistence, origin resolution, no-loss
cursor retry), `test_state_signal_relay.py` (incident-#1 proof, busy-manager boundary hold past
SLA/backoff with exactly one landing, origin/rebinding/idle-flap, non-reaction residue, dedupe,
boundary drain), and `test_state_signal_delivery.py` (fail-closed row-kind gate,
unreachable-landed regression, terminal-vs-queued acceptance). The existing suites shifted their
expectation fixtures from `briefed-by` to `ack-by` and pinned the retired turn-report surface
(`RetiredDispatchExpectationTests`, `REMOVED_FACADE_NAMES`, 63-key wire pin).

### 260713-TES-L3 Compound-Idle Relay Suite

`test_compound_idle_relay.py` (24 tests) forces the compound-idle relay to orchestrators:
manager + all workers idle → exactly one durable `state-signal` naming every set member;
partial/unknown/retired/zero-worker/unbound sets never fire; flap re-arm; busy-orchestrator
boundary hold with exactly one landing (t+301 s / t+901 s zero mid-turn pushes); master-scoped
membership on every arm (foreign-master spawn neither blocks nor joins); manager non-reaction
residue relayed to the orchestrator; emitter skip branches; and the action-time episode
signature in ask + marker. The existing `test_state_signal_relay.py` rebinding fixture now
keeps its replacement manager `working` so the L2 behavior stays isolated. The wire pin moved
63→64 (`compoundIdleEmittedFor`) in `test_serving_response_conformance.py`.

### 260713-TES-L4 Inbox Arrival And Rebinding Suites

Two forcing suites were added for deliver-until-LANDED:
`test_inbox_arrival_guarantee.py` (25 tests — scoped architect custody, post-time rebinding,
owner-address branches, explicit supersession, terminal inspectability, TTL/cap eviction,
settings last-good resilience, relay-death watch, retire surfacing) and
`test_inbox_rebinding_mechanics.py` (33 tests — transition idempotence, row-owner derivation,
rebind/expire/unresolved action branches, grace/evaluation branches, retention branches,
legacy-landed fold, cap-fill, F1 stale-snapshot terminal authority, supersede-during-in-flight
e2e, rebound delivery-to-B). The notifier/liveness/dispatch/expectation/reclamation/
escalation/conformance families updated their fixtures to the N16 terminal truth (ack-by →
verdict-by, attribution-only consume, `state="landed"` seeds, attempt-ceiling `unresolved`,
dead-seat expiry to the architect mailbox, one-per-row-per-sweep expiry emission), and the
registration suite pins the `include_terminal` poll kwarg plus the `operator_inbox_supersede`
wiring.

Regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

The stable structured-conversation contract gate: the contract suite uses
hostile sibling-product matrices to pin purpose-bound cursors, exact provenance, canonical status,
evidence-backed capabilities, operation identity/rollback, authoritative queued withdrawal
recovery, attachments, metrics, and fixture non-promotion. The foundation suite separately pins
exactly two read ports, three owned child routers, one global registration seam,
repository-only native-helper resolution, and redacted installed-runtime fixtures. These tests do
not claim a projector, native-history implementation, control service, or renderer exists.

The active conversation serving regression set: four focused suites cover
the implemented slice — canonical status classification/revision discipline with full-product
orchestration parity, per-harness mapper grammars with hostile shapes, the projector engine and
store (hydration, ordering, idempotence, provenance, rehydration, tool convergence, overflow and
zipper gap mechanics), and the production routes over a REAL composition (bridge + IPC server on
a real socket, real catalog row, the single route registration, HTTP over loopback uvicorn) proving
native identity, cursor forgery refusals, dual-cursor agreement, epoch-flip gap+close,
provenance through the real authority, orchestration parity, and absence of PTY/runner-log/
fixture production authority. The foundation pin asserts the active child's exact three-route
surface.

The native conversation library regression set: six focused suites cover the
implemented slice on doubled boundaries — ASGI routes with the exact O4 status ladder, cursor/key
and scope contracts, live gate demotion rules, port normalization with hostile shapes, and the
open service's idempotence/race/ownership arms — while the opt-in installed-runtime suite proves
the live Codex and Pi gates, both real end-to-end opens, and the Claude version-mismatch
fail-closed posture. The foundation pin asserts the library child's exact five-route surface and
the extended helper source set; the three runtime fixtures record observed (never enabling)
gate/open rows.

The native control-plane regression set: the contract suite
(`test_harness_control_plane.py`, 25 tests + 35 subtests) pins the interrupt write/ack/replay-once
with exact-turn and expected-operation guards plus the successor zero-write refusal, the paged
never-bodies timeline (all sources/kinds, union completeness, eviction-floor honesty, the full
256-record budget edge, epoch-flip typed), the asset channel (schema/traversal/verification
batteries, native construction with zero-write rejection, unsupported receipt, asset-conditional
digest), the once-only withdrawal recovery with byte-preserved tombstone/`cockpit_only`, and the
strict client validators. The opt-in installed suite (`test_harness_control_plane_installed.py`)
captures the same seams live against pinned codex 0.144.5 and pi 0.80.7 and enforces the Claude
version-honesty rows; the three runtime fixtures gain redacted `control-plane/*` rows with
`enablesCapabilities: false` — evidence, never enablement.

The authoritative control-API regression set: a shared topology
(`_control_plane.py`) runs the real bridge + IPC server on a real socket, the real submission
authority, and the single route composition with only the harness adapter doubled, plus the manager-
authorized `NOW`-anchored control service seeded into the `_SERVICES` memo so lease arithmetic is
time-consistent. Four focused service/route suites drive it: `test_conversation_control_operations.py`
(interrupt ledger — ack≠settlement, fingerprint idempotence with native-write counting, lost-response
reconcile, the guard battery, and both the Finding 1 content-ful and Finding 2 oversized/clipped pi
settlement regressions, each proven non-vacuous), `test_conversation_control_queue.py` (never-bodies
queue truth, the queued→dispatching race, the bounded recovery lease with an untouched frozen-clock
expiry proof, and the forgery battery), `test_conversation_control_attachments.py` (boundary-exact
limit refusals, one-use exact-receipt submit, recoverable-under-lease rebind with on-disk deletion,
timeline-driven reconcile, GET-only policy, and absent-not-zero telemetry), and
`test_conversation_control_api.py` (the seventeen routes over a real uvicorn wire with O4 mapping,
remote-peer 403, policy 405s, and the no-paste/no-substitution source scan). The opt-in
`test_conversation_control_installed.py` proves live codex/pi interrupt ack+settlement, queue truth,
withdrawal recovery, typed attachment submit, and telemetry through the registered routes plus the
Claude version-honesty gate. The foundation pin asserts the control child's exact seventeen-route
surface.

The evidence-backed hardening regression set for the production-E2E gate:
`test_chats_l5_hardening.py` pins the two master hardening obligations at their origin, each
non-vacuous on stashed source: the hosted-interaction synchronizer 500 that aborted the whole
terminal-catalog sweep (now quarantined fail-loud per row, with logging only on state change) and
the unknown-input provenance-validator 500 from a native re-map splitting a resolved user item's
authority triple (now pinned, with an identical re-map a true no-op). `test_conversation_active_service.py`
gains the projector-tier companions (the model-valid re-map and the three twin-suppression
tests, driving the real poll path), and the opt-in `test_conversation_control_installed.py` gains the
installed regression proving a settled live codex turn projects EXACTLY once on the re-read
conversation page (`2 != 1` on stashed `projector.py`). The 10,000-item DOM/interaction baseline + axe
tripwire lives in the dashboard test tree (`renderer.test.tsx`), not here.

The half-time functional regression set: `test_chats_l5f_leaks.py`
pins the per-session bounds (`SessionLockLeakTests`: `release_session` drops the lock + every
epoch channel; `_locks` bounded evicting idle-first; a held lock is never evicted; and
`QueueRowsBoundTests`: `queue_rows` capped with oldest eviction). `test_conversation_active_projectors.py`
gains the codex startup-burst-mints-zero-unknown-vendor / method-carried-mapping /
truly-unknown-names-the-method tests plus the claude `command_lifecycle` recognized-and-drift and
`rate_limit_event` drop tests; `test_conversation_active_service.py` gains the non-user-echo-skip
and the `DormantReleaseTests` (heavy-projection release + shell retire).
`test_conversation_contracts.py` pins that `FeatureCapability` has no `for_observed_runtime` predicate
(the contract is the only gate), `test_conversation_control_operations.py` pins the unverified
refusal now carries a contract reason (not a version comparison), and
`test_conversation_library_gates.py`/`test_conversation_library_installed.py` pin that a version drift
still ENABLES when the contract probe passes (the codex/pi exact-identity installed skips
on drift are recorded conservatism). `test_harness_control_evidence.py` pins the native method carried
onto the frame + stripped from the byte-identical snapshot + IPC round trip,
`test_harness_control_client.py` pins that a refused control socket yields the honest note and unlinks
the stale socket, `test_harness_launch.py` pins accepting an alias collapsed onto the default
resolved model while still refusing a genuinely different model, and `test_provider_containment.py` pins
the docker-ps timeout bounded into an error-annotated sample.

The first end-to-end authoritative submit/withdraw regression matrix: the new
focused authority suite and expanded common/API/native-adapter suites prove one epoch-bound
prompt/setter timeline, atomic queued-withdraw versus dispatch, exact full-ref completion,
completion-before-receipt dominance, no native queue/steer fallback, bounded privacy-aware retention,
and browser-visible status semantics. All backend blockers found during review are closed.

A fake-adapter conformance suite covers normalized harness control,
correlated acceptance/reconciliation, private IPC, bounded queue/ledger behavior, shutdown failure
paths, and surface-owned draft preservation. Existing settings, harness, catalog, opener, and
WebSocket tests pin the additive launch/API projections and preserve legacy behavior.
Fake and stdio transport coverage pins the Codex app-server:
exact initialize/model/thread setup, protocol-only effort validation and echoing, structured
status/completion and server requests, explicit busy behavior, bounded malformed/oversized input,
and reconnect correlation without resend. An opt-in live smoke proves exact-version readiness using
an ephemeral thread with no prompt or credential output.

The current Codex completion regressions prove that a null protocol `requestId` is resolved only by
the protocol-owned text vendor correlation on exactly one accepted inbox row in the same hosted
session. Missing, non-text, unmatched, and ambiguous correlation evidence fails loudly. Completion
records adapter delivery metadata on that same row while explicit inbox state remains `pending` and
unconsumed; terminal state is `idle` / `immediate` without a queued replacement and
`settling` / `queued` only for an actual replacement. Exact 2.1.207, 0.144.3, and 0.80.7 values
remain fixture/smoke evidence, not production pins.

Pinned Claude Code 2.1.207 JSONL fixtures, fake-transport conformance,
a real-local-subprocess lifecycle tier,
and an opt-in credential-safe live smoke cover the Claude adapter boundary. The smoke submits the advertised local `/cost` command
through the same correlated acceptance/result path without a model API request.
The lifecycle tier sits between the fake and the credentialed smoke: `test_claude_stream_transport.py`
drives a real stdin-waiting child through start -> completed stop -> start to pin process-ownership
release plus the live double-start refusal, and `test_harness_control_claude.py` drives the real
adapter over the real transport against a local stream-json stub to prove the floor probe's
stop/re-launch reaches control readiness with a selectable model and effort. Both use local
interpreter children, so this tier costs no credentials and no model tokens. A mixed
`success`/`is_error=true` API-429 regression remains failed and retains only safe terminal metadata;
no result text, stderr, credentials, environment, or settings are emitted or retained.

The active Claude fake-transport fixture root is 2.1.210. Its initialization
fixture is the current test authority for separate control initialization, `system/init`, a
zero-turn bootstrap result, and correlated `list_models`; its interaction and turn companions keep
durable gates and acceptance-versus-completion covered in the same versioned cohort. The 2.1.207
fixtures remain historical evidence and are no longer loaded by the active adapter suite.

The test route additionally proves the projection/landing boundary: slow or failed remote observations do not delay local publication; observer results remain exact-contract and freshness-labeled; stale landing rendering is visible but motion-inert; invalid snapshot reads preserve local status; and a failed refresher does not skip serving shutdown. These are focused regressions; the full repository gate runs above this route.

`test_change_watcher.py` (plus touched `test_serving.py`/
`test_dashboard_daemon.py` fixtures) proves change-driven projection pacing: the derived watch-root
list and self-trigger event filter, the pure `ChangePacer` deadline table (heartbeat/debounce/
interval-floor/max-delay/degraded), heartbeat-only quiet-world projection, debounce-bounded change
latency, burst coalescing, LOUD fixed-interval degrade on missing `watchfiles`/crashed
watcher/failed root derivation (with retry), watch-task lifecycle ownership, exact legacy pacing
without a watcher, `--heartbeat` CLI/daemon argv plumbing, and one real-inotify end-to-end pass.
The projection scaling suite proves the shared per-tick contract
snapshot: one contract enumeration and at most one parse per contract per projection tick, zero
re-parses while the `(mtime_ns, size, ctime_ns)` stat identity holds, reader-output parity with and
without the injected snapshot, cache retention bounded to live contracts, chmod-000 and
utime-pinned-rewrite invalidation via ctime, and parse failures retried every build.

## Runtime-Truth Regression Gate

Serving coverage spans four exact boundaries: client/build fingerprint and
HTML revalidation; raw-event record realignment and invalid/non-object cursor progression; owned
tmux client environment under contaminated launcher state; and omission of fictitious pre-session
adapter control. Integration coverage skips only when tmux itself is absent.

## Atomic Folded-State Stream Gate

`test_serving.py` now forces both formerly lost state paths. One case publishes while the initial
snapshot generator is suspended but already subscribed and requires the exact next delta. One case
registers before failed-prime recovery, requires one full build-decorated snapshot, proves the
identical state is not duplicated, and then requires an ordinary later delta. A third case cancels a
waiting stream and proves immediate subscriber removal. These are synchronization-driven assertions,
not sleep-based race probabilities.

## Route-Index And Carryover Authority Gate

`test_route_index.py` pins the production census boundary across ignored and generated paths,
tracked/untracked identity, symlinks without target following, sparse checkouts, index/worktree
deletions, gitlinks, all eight ambient Git repository selectors, non-UTF-8 names, and typed Git,
timeout, OS, and `lstat` failures with preserved causes. Regular, linked-worktree, and selector-
contaminated generation must produce identical bytes and a zero-write second pass.

`test_carryover.py` pins official-memory write authority before full apply. JSON and Markdown
settings with missing, invalid, unsupported, reset-to-empty, blank-member, or otherwise
semantically empty path rules must refuse with exact zero mutation. Positive retention,
repopulation, mode/layout selection, root fallback, and official-over-source cases prove the raw
preflight agrees with the typed settings parser rather than creating a second settings language.
`test_worktree_support.py` provisions explicit supported storage authority in initialized-memory
fixtures, while `conftest.py` imports the production selector inventory so tests cannot drift from
the Git boundary they exercise. That import-time strip is fixture safety and stays, but read the
Single-Runner Git Gate below before trusting it as coverage: it also removes the variables a
redirection test needs, so any suite that leans on it can only prove the harness stripped them.

## Dashboard Bundle Placement Gate (260731-EFA-L1)

`test_sync_dashboard.py` no longer tests a sync check. The cockpit bundle left version control
(master decision OQ6), so `scripts/sync-dashboard.py` is a release build step and the suite pins one
property: it cannot place an artifact that was not built from the dashboard source as it stands
right now. Three tests that asserted the opposite — absent `dist` passes, absent fingerprint
sidecar passes, absent `dashboard/src` passes — were replaced by their inversions, two of them
carrying docstrings that name the fail-open they encoded, so the history cannot be readopted by
accident. The `--check` flag's absence is asserted through a real `subprocess`, because the process
boundary is where the old fail-open lived: hooks and CI invoked `--check` and read its exit status.

Fixtures reproduce Vite's handshake rather than mocking it: `emit_bundle` writes a `dist` whose
JavaScript contains the build-input fingerprint verbatim, which is what `vite.config.ts` compiles in
as `__AR_DASHBOARD_BUILD__` and what the script searches for. Nothing in the suite reads the real
tree, and no test requires a frontend build to have happened.

`GeneratedDashboardWhitespacePolicyTests` was **removed** with the committed bundle it policed.
Root `.gitattributes` still disables `blank-at-eol` for
`mcp/src/agents_remember/package_data/dashboard/assets/*.js`, but that path is now git-ignored, so
the rule has no tracked subject and the regression had nothing to prove. The reason it existed
still holds and still forbids post-build normalization — the generated tab is CodeMirror
Python-completion indentation and removing it changes the runtime string — so if a generated path
ever returns to version control, the attribute and this regression return together.

## Static Surface Gate (260731-EFA-L1)

`test_static.py` is the new deterministic owner of both legitimate states of the serving static
surface: a built bundle and an honest absence. It never reads the repository's own bundle, so it
gives the same verdict before and after a frontend build. Its non-obvious assertion is method
parity — for `POST`/`PUT`/`DELETE`/`PATCH` on an `/api` route, the missing-bundle mount and the real
`StaticFiles` mount must return the *same* status (405), because the greedy `/` mount outranks an
API route that matched the path but not the method.

`test_serving.py` keeps the `create_app`-level version of the same two states, but its
build-dependent assertions were rewritten: `/` is served from a patched stand-in bundle rather than
the repository's, `dashboardBuild` is asserted present-or-omitted rather than indexed, and
`StaticTests` skips when this checkout has no build instead of failing.

## Single-Runner Git Gate (260731-EFA-L3)

`test_git_command.py` is the new owner of this package's git boundary, and it is written against a
**decoy repository**. Every redirection test builds a real `real/` and a real `decoy/`, points all
eight selectors (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`) at the decoy
inside a `patch.dict`, and asserts **both** halves — the real branch advanced and the decoy did not
move. Asserting only the real repository would still pass if the write were duplicated into both.

**Those `patch.dict` blocks deliberately undo `conftest.py`.** The conftest strips the selectors at
import, which meant no test anywhere could observe a call site that failed to strip them: the
mitigation for the production hazard was installed in the only place that could have detected it.
`test_a_commit_lands_in_the_real_repository_not_the_decoy` asserts
`set(GIT_REPOSITORY_SELECTOR_ENV).issubset(os.environ)` before it acts, so it passes because
production strips, not because the harness did — delete the conftest lines and it still passes;
delete `env=` from the runner and it fails.

`SingleRunnerTests` is the decay guard and it is `test_subprocess_hygiene.py`'s shape: an AST sweep
over every package module asserting that the only file that spawns git is `kernel/git_command.py`.
Six near-identical runners is exactly how the defect was born, so the rule is that no module may
grow a seventh. **Its reach is stated rather than assumed** — it recognises a spawn whose argv is a
list literal whose head names git, so `benchmarks/runner_modules/commands.py`, which composes its
argv through `git_command()`, is invisible to it and is asserted directly by
`BenchmarkRunnerEnvironmentTests` instead. That is not a formality: the benchmark runner holds the
most destructive argv in the package (`clone`, `checkout --detach`, `reset --hard`, `clean -fdx`).

**`SingleRunnerGuardReachTests` is the guard on the guard, and it exists because of how this sweep
fails.** `SingleRunnerTests` reports safety as an *empty offender list* — which is also exactly what
it reports when its sweep cannot see the offender, so a hole in the reach does not look like a
failure, it looks like a clean tree. Each test there plants a bypass form and fails if the sweep
stops catching it. Three of those forms were live blind spots the fix workers closed: a spawn
reached through `from subprocess import run` rather than `subprocess.run`
(`test_a_spawn_imported_off_subprocess_is_still_a_spawn`, plus
`test_an_import_alias_is_followed_to_the_name_it_binds`), a path-qualified argv head such as
`/usr/bin/git` (`test_an_absolute_path_to_git_is_git`), and a `**kwargs` splat previously counted as
proof that `env=` had been passed, whose contents the syntax tree cannot see
(`test_a_kwargs_splat_is_not_proof_that_env_was_passed`). It also pins the negatives so the sweep
cannot be "fixed" into over-reporting — a program that merely *starts with* `git` is not git, a
local function named `run` is not a subprocess spawn — and pins the one remaining hole as
deliberate: `test_a_computed_argv_remains_the_documented_blind_spot`, which is the debt
`BenchmarkRunnerEnvironmentTests` pays.

`TimeoutClassTests` pins the *other* half of the consolidation, and it is the half that could have
shipped a regression invisibly. Before the leaf the kernel's runner hard-coded `timeout=5`, so
moving these reads onto a runner whose default is the local bound would have loosened them 60x —
on commands that sit under `resolve_context`, which runs on essentially every tool call. Its
`_recorder` stand-in takes `timeout` as a **required keyword**, so a call site that leaves the class
to the default fails the recorder rather than quietly recording the default.
`test_read_git_facts_bounds_its_three_ref_reads_at_the_metadata_band` and
`test_branch_freshness_classes_each_of_its_commands_by_what_it_does` assert the exact
`{command: bound}` map per module — including that `status --porcelain` and
`rev-list --left-right --count` keep the *local* bound because neither is constant time — and
`test_one_command_means_one_bound_across_the_kernel` asserts the rule itself: `branch
--show-current` and `rev-parse HEAD` are called from both `cross_repo.py` and `git_facts.py`, were
bounded at 30s in one and 300s in the other, and must now agree.
`test_the_metadata_bound_is_the_shortest_of_the_three` keeps the ordering from being reshuffled.

The rest of the module pins the runner contract the consolidation depended on. Stdin is `DEVNULL`
unless `input_text` is passed (`git patch-id` in `memory/carryover.py` is the only caller that needs
it — GitHub #49). A command that deliberately outlives the runner's old hard-coded `timeout=5`
completes, while a caller-named short timeout still raises `TimeoutExpired`, so raising the default
did not amount to removing the bound; `GIT_REMOTE_TIMEOUT_SECONDS < GIT_LOCAL_TIMEOUT_SECONDS` is
asserted rather than assumed. `RemoteBranchStallTests` pins the two remote calls in
`worktrees/modules/cleanup.py` — which previously ran with no timeout at all — reporting
`remote-unreachable` on a stall instead of holding an uncancellable MCP tool call open.
`QualityGateGitTests` covers the gate's own git calls specifically because the gate runs from the
**pre-push hook, where git itself exports `GIT_DIR`**, and keeps both wrappers converting failure
into their typed `DiffScopeError` / `ScopeError` rather than an empty scope that would certify
nothing.

**One consequence when editing an existing suite:** a module that used to spawn git now calls
`run_git`, so a test that patches `subprocess.run` in it patches nothing. `test_serving.py`'s
`BuildInfoTests` was moved onto `agents_remember.serving.build_info.run_git` for exactly that
reason, and its fake now takes `(repo, arguments)` instead of a full argv.

## Cold-Start Gate (260731-EFA-L3)

`test_cold_start.py` proves the server imports and starts with **no network egress**. It is a
subprocess, and both reasons decide whether it can fail at all. tiktoken memoizes loaded encodings
in `tiktoken.registry.ENCODINGS`, so in-process the load under test would be a dictionary hit left
warm by an earlier test in the session, and the assertion would pass against a package that ships no
vocabulary at all. And the caches must be cold: the child gets `TIKTOKEN_CACHE_DIR`,
`DATA_GYM_CACHE_DIR`, `TMPDIR` and `HOME` pointed at one empty directory — pointing the operator
variable at a *cold* directory is deliberate, because it also proves the package's own vendored copy
wins over an exported cache that would send the load back to the network.

The child blocks `socket.connect`, `connect_ex`, `create_connection`, `getaddrinfo` and
`gethostbyname`, then **proves the block took** by attempting one connection before importing
anything — a block that silently did not take would make every later assertion vacuous. It then
builds a real server through `create_server(McpRuntimeConfig(...))` and prints what it counted, and
the parent asserts the child's count equals its own warm counter's count of the same fixed payload:
same tokenizer name (`tiktoken:o200k_base`), same `exact`, same number. A lazy load behind an
approximate fallback would pass the start test and fail that one, which is why the vocabulary is
vendored rather than made optional.

**The module under test is imported through a helper, never at module scope.** `tokens_module()`
returns it per call, so no test in this file can be the one that warms
`tiktoken.registry.ENCODINGS` for the others, and the `mock.patch.object(tokens,
"VENDORED_VOCABULARY_DIR", ...)` redirections below act on a module the file does not hold a stale
reference to.

`VendoredVocabularyTests` re-derives both hashes from the installed tiktoken rather than restating
them — the SHA-1-of-URL filename `read_file_cached` looks up, and the SHA-256 tiktoken asserts on
load — so a tiktoken upgrade that moves the URL, or a truncated copy, fails here instead of quietly
sending the next cold machine back to the network. Since the loader now has to check the digest
*before* tiktoken sees the file, the package holds its own copy of it
(`tokens.VENDORED_VOCABULARY_SHA256`), and `test_the_shipped_file_is_the_one_tiktoken_asks_for`
asserts that copy equals the `expected_hash` recorded off `openai_public.o200k_base()` — which is
what keeps a restated constant from becoming a second source of truth. It also pins that an absent
vocabulary and any encoding this package does not ship raise `TokenizerVocabularyError` rather than
falling through to a download, and that the `TIKTOKEN_CACHE_DIR` override never outlives one load
(the vendored directory sits inside the installed package, which is routinely read-only).

Two further pins in that class earn their place by naming a failure that has no traceback.
`test_the_gitattributes_entry_names_the_shipped_file` asserts the root `.gitattributes` `-text`
entry is *exactly* the shipped filename: the entry is a literal path and the path is `sha1(URL)`, so
a tiktoken release that moves the URL renames the file and leaves the rule protecting nothing —
silently, and only on `core.autocrlf=true` clones, which are precisely the clones that need it.
`test_holding_the_context_open_around_a_counter_does_not_deadlock` covers the obvious use of an
exported context manager, `with vendored_vocabulary_cache(name): TiktokenTokenCounter()`, where the
counter's own load re-enters the manager on the same thread. On a non-reentrant lock held across the
`yield` that is a permanent hang — no timeout, no traceback, a gate that never returns — so the test
runs on a worker with a **bounded join** and asserts the thread finished, in order to *report* a
regression rather than reproduce the hang inside the suite.

`CorruptVendoredVocabularyTests` is the newer half and the one that states the real threat model:
present-but-wrong, not absent. tiktoken does verify the SHA-256, but it does not fail closed —
`read_file_cached` deletes the offending file and downloads a replacement over it, so "tiktoken
checks it" would have meant a corrupt vendored copy becoming a silent network fetch into the
installed package on the startup path. The class docstring records that this was *measured*, not
reasoned: CRLF-mangling the vendored file and truncating it to half its bytes both passed while the
file was quietly restored underneath.

Its shared `assert_corruption_is_refused` helper builds a **copy** of the shipped file in a
temporary directory and points `VENDORED_VOCABULARY_DIR` at that, so a test that fails part-way
cannot leave the checkout damaged and have the suite assert against its own debris. Each case
asserts four things: the refusal is raised; the message names the file, the expected digest and the
found digest (an operator's next move is to compare their copy against the one tiktoken asks for,
and "corrupt" alone does not say against what); and **the copy is still on disk afterwards** —
tiktoken was never handed the directory, so nothing was deleted and nothing was downloaded over it.
The corruptions are the ways bytes actually go wrong: CRLF-mangled
(`test_a_line_ending_mangled_copy_is_refused` — what a `core.autocrlf=true` checkout does, and the
reason the `.gitattributes` entry exists) and truncated to half
(`test_a_truncated_copy_is_refused` — a partial write, whose prefix is byte-identical, so anything
short of hashing the whole file accepts it). `test_a_counter_will_not_build_on_a_corrupt_copy` then
drives the production entry point — `TiktokenTokenCounter()`, the statement that runs while
`mcp/tools/base.py` is importing — over a **single flipped byte**, same length and same line
endings as the original, and patches `tiktoken.load.read_file` with a stub that raises: the refusal
must land before tiktoken reads anything, which is both the assertion and what stops a regression
here from actually downloading 3.6 MB over the corrupt copy.

## Durable Store Integrity Gate (260731-EFA-L5)

Nine files in this route changed for one defect: the six control-plane JSONL stores were losing
appended records. Four suites are new and five existing suites had an assertion replaced. Begin at
`_store_durability.py` — it is the instrument the numbers came from, and it explains why they can
be trusted.

**`_store_durability.py` is support code with no assertion in it, and that is the point.** It
expresses each store as four operations (`open` / `write` / `write_decoy` / `reclaim_now`), where
`reclaim_now` is always that store's own shipped reclaim entry point and never a reimplementation,
and drives three scenarios: `stress`, `forced_lost_update`, `forced_unlink`. It now covers **eight**
stores, not six — the two `providers/` logs have the identical shape and are measured by the
identical instrument — with `CASES` deliberately held at the six control-plane stores beside a
separate `PROVIDER_CASES` so the control-plane contract test is not silently widened. Every record
it writes is one of **three classes**: `survivor-*` (what policy must keep, and the only class the
accounting counts), `decoy-*` (what policy should drop, so a reclaim tick does real work instead of
returning early), and `anchor-keepalive` (never prunable, never counted, present so the kept set
stays non-empty and the tick takes the temp-and-rename path rather than the `unlink` branch). That
is what makes a reported "loss" mean *a row nobody decided to drop* rather than ordinary
bounded-store reclamation. Three properties make its output evidence rather than anecdote:

- **Real processes, never threads** (`multiprocessing` with the `fork` context). The defect is
  cross-process; the GIL would serialise the very window under test.
- **It is dual-mode, and the second mode is what pins a run to one tree.** Importable by pytest,
  and executable as a script whose caller sets `PYTHONPATH` to the `mcp/src` it wants measured —
  the live worktree for the contract assertion, a `git archive` of the leaf's base commit for the
  reproducible baseline. `_require_source_root` refuses with `SystemExit` if `agents_remember`
  resolved anywhere else. A measurement that cannot name the tree it measured is worthless, so
  that guard is fatal rather than a warning.
- **Loss accounting deliberately does not go through the store's own `read`.** A raw tolerant
  JSON-lines reader counts "record lost" and "line torn" as two separate quantities, so a strict
  reader cannot turn a measurement into an exception and a tolerant one cannot report a torn line
  as a lost record. The appenders journal an id only *after* the store call returned, so anything
  on that list and not on disk is a record the store accepted and then lost, and a write that
  raised is counted as an error rather than as a loss.

**The instrument had a defect of its own, and the guard that closed it is the fourth property.**
The harness derived its work directory — including the reclaimer's **stop flag** — from
`root.parent`. `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`,
so **all cases shared one stop flag**: the first case to finish set it and every case after it left
the tick loop after roughly one tick. Measured directly before the fix: **25 reclaim ticks for the
first store and exactly 1 for each of the other seven, with all eight reporting 0.00% loss**. The
same layout also let the forced scenarios share `forced.id` and the `*.err` files, so a case whose
appender wrote nothing was scored off its predecessor's receipts. The fix is
`harness_work_dir(root) = root.with_name(root.name + "-harness")` — a **sibling**, chosen over a
child because `root` does not name one place: the six control-plane adapters resolve their log
under `root/workspace`, the two provider adapters under `root/logs/observer/providers`, and
`GateStore` additionally globs `root/lifecycles/*/gates.jsonl`, while the accounting reads that
whole tree as raw bytes. The guard is `MIN_RECLAIM_TICKS = 10`, raising `VacuousRunError` at the
end of `run_stress`, and it lives **in the instrument rather than in either suite**, so the
control-plane suite, the provider suite and bare `main()` script runs are covered by one floor. The
floor is evidence-based: real runs give 22-39 ticks idle and 34-49 under 24-way CPU load — load
*raises* the count, because appender pacing stretches in wall clock while the reclaimer keeps
polling — so 10 sits an order of magnitude above a vacuous run and under half the lowest of 32
observed runs; 20 was rejected because the observed minimum is 22, which is no margin. The card
[`_store_durability.py.md`](_store_durability.py.md) carries the line-level detail.

**The base-commit numbers are quoted, not reproduced here.** `BASE_COMMIT` is `e52edaf5` and
`STRESS_PROFILE` is 4 appenders × 50 records at 2 ms against 1 reclaimer at 5 ms — both are literals
in `_store_durability.py` and are checkable. The *rates* are not: **no base-commit measurement
artifact is committed anywhere in the tree**, `main` can write a JSON payload but none is stored, no
test asserts a rate, and no committed invocation passes `runs`, so "10 runs per store" is a source
claim too. Two figures are carried at several independent sites and are quoted on that authority:
attention dismissals **31.45%** lost (`durable_store.py`, `agent_notifier_signals.py`,
`test_durable_store_contract.py`, `test_observer_projection.py`) and gate **11.50%**
(`durable_store.py`, `store.py`, `test_interaction_retention.py`). The rest come from
`durable_store.py`'s module docstring alone: agent-notifier signals 10.50%, expectation rows 10.20%,
orchestration nudges 9.20%, operator inbox 0.00% (the one store that already took a lock), **127 of
2000** writes *raising*, and "zero torn lines in every run" — the last being the claim that records
disappeared whole, which is what would explain why no reader-side validation could have detected
this.

**Those base-commit rates survived the harness fix, and that is the reassuring half.** Re-measured
through the same `git archive` under the working harness — four runs each, percentage of records
the store reported written and then did not have — the leaf's means are attention **23.91%**, gate
**9.38%**, supervisor-signals **8.00%**, expectation-rows **7.63%**, nudges **7.50%**,
operator-inbox **0.00%**: the documented ordering store for store, with the same lone survivor at
exactly zero. They survived because `main`, the entry point base-commit work runs through, already
built each case a root under its **own** parent, so `root.parent` was distinct there and the stop
flag was never shared. **The bug never corrupted the historical measurements; it hollowed out the
ongoing regression**, which is measured against the live tree and was passing over one tick per
store. Note what those six figures are and are not: they are this leaf's **four-run means and do
not appear in the source**. The source carries the *ranges* they were taken from, in
`test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring — attention
18.27-30.10, gate 7.50-10.50, supervisor_signal 7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00,
operator_inbox 0.00 (all four runs) — and each mean falls inside its own range. A reviewer grepping
the harness for `23.91` will find nothing, and that is expected rather than drift.

**Against the current tree, what is asserted is narrower than "all six stores, all three
scenarios"** and is worth reading precisely, because
`test_controlplane_store_durability.py::MultiProcessDurabilityTests` is where a reader checks it.
`lost == 0` (with `stragglers == []`) holds in all three scenarios — over six stores in
`forced_lost_update` and `stress`, and over **five** in `forced_unlink`, which iterates
`APPEND_CASES`. Attention dismissals is excluded there by construction, not by oversight: it has no
`append` at all, so it cannot be stranded in an unlinked inode, and that same whole-file
read-modify-write is why it measured worst. `torn_lines == 0` is asserted in the **`stress` scenario
only**, as are `append_error_count == 0` and `reclaim_error_count == 0` — the latter two in their
own stress run against their own root, with the "the run actually happened" guards repeated so a
zero can never be reported over zero write calls.

The two provider adapters have since landed in the instrument and do **not** widen the counts
above: the registry is split into `CONTROLPLANE_ADAPTERS` and `PROVIDER_ADAPTERS`, `CASES` stays at
the six control-plane stores beside a separate `PROVIDER_CASES`, and `APPEND_CASES` still derives
from `CASES`. The counts above are anchored on those names; verify the names, not the numerals.

`test_controlplane_store_durability.py` turns that into three assertions — no loss (R10), the
per-store torn-line policy (R8, derived from named call sites rather than from docstrings), and
sensitivity proven against the base-commit archive (R14, asserting both that the five unlocked
stores each lose a record *and* that operator-inbox loses none, which is what proves the harness
is measuring the defect). Loss and raising are asserted separately on purpose: a store that starts
raising instead of losing has moved the failure, not fixed it. R14 has a second half:
`HarnessVacuityGuardTests` drives the shipped `run_case` path to a one-tick run and requires
`VacuousRunError`, then asserts the floor from both sides — above the vacuous run, and below the
lowest tick count ever measured on this profile. That is the test that proves the refusal above is
real and reachable rather than a constant nobody consults.

`test_provider_store_durability.py` is the same three assertions over the two `providers/` stores,
and is a **fifth** new file in this gate that the "nine files / four new suites" count above
predates. Read it for one thing the control-plane suite cannot show: its `case_root` docstring is
where the shared-stop-flag defect was first found and worked around locally, before the fix moved
into the instrument where it also covered the control-plane suite, which had the same layout and no
workaround.

`test_gate_replay_window.py` states what the loss cost. **The entire defence against spending one
human approval twice is a single appended record**: `_mark_closeout_gate_applied` appends
`apply_gate`, and `enforcement.py`'s `applied` branch refuses. No flag, no marker file, no
timestamp comparison. The counterfactual test deletes *only* that line — asserting the two
remaining snapshots survive, so the deletion cannot have been indiscriminate — and the same
approval becomes spendable again. Against the pristine base commit the suite exits 1 with
`AssertionError: 'approved' != 'applied'`; against the fixed tree it exits 0.

`test_durable_store_contract.py` is the in-process axis the multiprocess harness cannot see: two
**threads** of one process, which is what the dashboard is. **Read what it claims about the mutex
before repeating it.** `flock` already excludes two threads of one process — the lock lives on the
open file description and `exclusive_access` opens a fresh one per non-reentrant acquisition — and
that was measured, not assumed, so the thread-level lost update was already closed and
`thread_mutex_for` **is not fixing a reproducible race**. What it closes is that the exclusion
rested on *where the handle came from*: cache one lockfile handle on the store — the obvious fix
for an append path that opens two files per record — and every thread shares one description,
`flock` silently stops excluding, and nothing in the tree fails. The mutex makes the in-process
half a stated property, and the first test asserts it directly via a non-holding thread's
`acquire(blocking=False)` probe rather than inferring it from an ordering `flock` alone would
produce. The re-entrancy case follows: that mutex is a second lock a thread can hang itself on.
Its unsafe-filesystem tests **fake the filesystem, not the code** — a stand-in whose `flock` is
accepted and takes no lock, exactly as WSL DrvFs behaves, substituted for `durable_store`'s own
module reference alone so no other thread in the interpreter loses its locks; every assertion is
on the raised type, the message text, and what is on disk, including that no log was created.

**The five updated suites all had an assertion that a pruned log stops existing.** That unlink is
the defect L5 removed: `_replace` called `path.unlink(missing_ok=True)` on an empty kept set, so a
concurrent appender holding an `"a"`-mode handle wrote into an inode with no remaining links.
Four of them now assert **emptiness** — `is_file()` true, `read_bytes() == b""` — which is
strictly stronger, because zero bytes proves the records physically left where a missing file only
proved a file was removed.

`test_interaction_retention.py` is the exception and is worth reading as one. Its assertion was
never about absence: it passed only because the base commit physically rewrote every gate log **on
the projection tick**, which is the behaviour this leaf removed. Restating it as emptiness would
have restated the removed behaviour. It was split into two proven claims instead — the projection
leaves the log byte-identical (non-destructiveness, newly asserted and never held anywhere before)
and `GateStore.compact`, in the owning process, is what empties it.

## Hot Path Summary

The harness sub-agent regression set: `_agent_wire_fixtures.py` (shared
codex vendored-shape builders), `test_codex_adapter_thread_demux.py` (the 2026-07-24
bridge-death incident regression — three sub-agents mid-turn, multiplexed approvals answered by
request-id, collab identity binding, degrade-not-die, native-page thread demux — plus the
remediation pins: concurrent parent pendings answered per id with the oldest in the singular
slot, the method-first degrade split, the bounded per-thread pending map, and the load-shed
event queue with its honest `ar/load-shed` notice),
`test_conversation_projector_codex_agents.py` (roster/multiplexed projection/per-thread twin-suppression
dedupe/plural pendings in one cursor domain, incl. concurrent-parent projection and the
singular-rotation resolution), `test_conversation_projector_claude_agents.py`
(`parent_tool_use_id` sidechain binding, `task_*` roster lifecycle, the fail-closed
`--forward-subagent-text` floor), and `test_conversation_library_agents.py` (both harnesses'
agent grouping with visible `agents_note` degrade and nested-agent naming). Authority-level
multiplexed respond + plural-pending serialization round-trips extend `test_harness_control.py`
(incl. the entry-thread operation guard for concurrent parent tuple entries);
the flag-floor probe/relaunch flow extends `test_harness_control_claude.py`; the reordered
`task_started` binder pin extends `test_conversation_active_service.py`; the additive agent
fetch at the fake boundary extends `test_conversation_library_ports.py`.

For the dashboard release path, begin at `test_sync_dashboard.py` for the placement refusals and
the process-boundary proof that `--check` is gone, then `test_static.py` for what a checkout with
no bundle serves. Use `dashboard/vite.config.ts` for the compiled fingerprint the fixtures embed
and `.github/workflows/publish-mcp-to-pypi.yml` for the only production caller. Do not route this
seam through generated asset file cards or a generic normalizer, and do not expect a committed
bundle to compare against.

For the local gate itself, begin at `test_code_quality_check.py`: one test scans
`.githooks/_gate.sh` and the CI workflow for the wrapper command with no threshold opt-out, and a
second pins each hook to its tier (`pre-commit` → `fast`, `pre-push` → `full`) so neither can be
silently promoted or demoted. Since 260731-EFA-L2 the same module also holds the gate's honesty
contracts: `RadonIsAReportNotAGateTests` (exactly the two Radon steps are declared reports; the
section header and the help text say so; a report step that exits non-zero still fails, because a
tool that exits 0 on every finding can only exit non-zero when broken),
`EveryEnforcingStepCanFailTests` (the `ruff` step routes **no** rule away from itself; `C901`,
`PLR0911`, `PLR0912` and `PLR0915` are selected, unignored and proven to reject a real over-complex
function at this repository's configuration; the format step is enforcing over the derived scope;
and `test_the_complexity_baseline_and_its_gate_step_are_gone` keeps the deleted ratchet deleted),
`ToolSignatureExemptionTests` (`PLR0913`'s one exemption covers the MCP registration directory and
nothing else — an AST walk over every file the `pyproject.toml` pattern really resolves to proves
each function there is a published `@server.tool()` declaration or its registrar),
`CrapThresholdEnforcementTests` (every offender named, the clearing branch coverage inverted from
the CRAP formula, "split it" when no coverage can clear it, and no exemption file anywhere),
`GateScopeDerivationTests` (no hand-written scope constant may return; `git ls-files` reads the
index; a file in no importable package still reaches both rails; an underivable scope refuses
rather than certifying nothing; `main` reports the gate's verdict rather than owning one), and
`PytestConfigurationTests` (strictness switches, `python_classes`, an **exact-count** cap of 5 on
`filterwarnings` ignores, and two-way reconciliation between registered markers and the suite's
real `AR_*` environment gates).

**For "does the gate reach everything?", begin at `test_gate_scope.py`** — it is a different kind of
test from the above. It does not read the wrapper's dataclasses; it recomputes `git ls-files`
itself, builds the real `ruff` and `pyright` argument vectors, and asserts every tracked path
appears in them, because a scope that is declared but not passed to a tool is not a scope. It also
reads the frontend rails (`eslint.config.*` directories and `tsconfig*.json` includes, with a
hand-written glob translator because `fnmatch`'s `*` crosses `/` and would silently widen every
pattern). **It has no allowlists.** Three empty ones stood there mid-leaf and were deleted with the
complexity baseline they were shaped like; every population they were built for was brought onto a
rail instead (`.pi/extensions/tsconfig.json` for the Pi extension, `tsconfig.driver.json` for the
Playwright/perf layer, `panda.config.ts` into `tsconfig.node.json`). All four failure messages say
so: "There is no allowlist to record it in."

**For the changed-lines coverage floor, begin at `test_diff_coverage.py`** — the 100% per-diff floor
this leaf added, where every statement and branch arc on a changed line must be exercised and the
failure names each uncovered line rather than reporting a percentage. Every test drives a **real
throwaway git repository**: a fake `git diff` string would only prove the parser agrees with whoever
wrote the fixture, not with git's hunk headers for an added file, a one-line deletion, a rename, or
a working-tree-only change.

**For "is any gated path actually reachable?", begin at `test_gated_integration_runner.py`.** Eight
`AR_*` markers were registered and reconciled with the suite's skip decorators while **nothing
applied or ran any of them** — a registered marker that decorates nothing selects zero tests, and
pytest reports that as a successful run of an empty selection. This module reconciles registered
markers, applied markers and `scripts/run-gated-integration.py` entries in both directions, and pins
the two credential-free paths CI runs (`ar-run-pi-rpc-smoke`, `agents-remember-real-mcp-config`)
against the six that stay behind the local runner.

**For the generated harness trees, begin at `test_sync_harness.py`.** Its first test is the
enforcing one: any drift — content **or** file mode — between `scripts/harness/` and the nine
generated trees fails the suite, so drift is caught for a contributor who has not installed the
hooks and in CI. Note the `sys.modules` registration in `load_script`: the generator defines
frozen dataclasses, which resolve their defining module through `sys.modules` at class-creation
time, so a path-imported script must be registered before `exec_module`.

**There is no complexity ratchet.** `test_complexity_baseline.py`,
`code_quality/complexity_baseline.py`, `quality/complexity-baseline.txt` and the wrapper's baseline
step were all built during 260731-EFA-L2 and then **deleted** when the developer ruled that
ratchets, baselines, grandfather lists and burn-down schedules are all forbidden. All 67 complexity
offenders were fixed by extraction instead, and 274 of 293 long signatures were fixed by
introducing 163 parameter objects. Do not reintroduce any of them — 
`test_code_quality_check.py::EveryEnforcingStepCanFailTests::test_the_complexity_baseline_and_its_gate_step_are_gone`
fails if you do.

For closeout enforcement, begin at
`test_worktree_closeout_quality_gate.py`, whose argument spy is the only thing standing between the
mandatory gate and a silent no-op at an unannotated call site.

For route-index/carryover authority changes, begin with `test_route_index.py` for the frozen census
and byte-convergence matrix, then `test_carryover.py` for full-apply zero-mutation refusals and
parser-equivalent positive controls. Use `test_worktree_support.py` for closeout caller wiring.

For folded-state transport changes, begin at `test_serving.py::StreamEventsTests`: those
cases pin atomic activation, first-recovery snapshot semantics, later-delta continuity, and
close/cancellation cleanup against the production `Projector` and `stream_events` seam.

`test_conversation_contracts.py` carries semantic authority and
`test_conversation_foundation.py` the package/router/helper/fixture topology. The three
`fixtures/conversation_runtime/*.json` files are allow-listed installed observations with
`enablesCapabilities:false`; exact versions and observed counts are evidence, never maintained
feature declarations. Helper protocol behavior is also covered in its own Node test package.

The active-serving set centers four focused suites: `test_conversation_active_status.py` (canonical
classification, revision discipline, full-product orchestration parity),
`test_conversation_active_projectors.py` (per-harness mapper identity/blocks/tools/provenance),
`test_conversation_active_service.py` (engine hydration/ordering/idempotence plus the landed
review-fix pins), and `test_conversation_active_api.py` (production routes over a real socket, incl.
selected-child hydration, the live epoch-flip gap, and the no-PTY source scan). The foundation pin
asserts the active child's exact three routes; fixture rows stay evidence-not-enablement.

The library set centers six focused suites: `test_conversation_library_api.py` (real-ASGI routes
and the O4 status ladder), `test_conversation_library_cursor.py` (signed token and scope
contracts), `test_conversation_library_gates.py` (capability demotion rules),
`test_conversation_library_ports.py` (hostile normalization), `test_conversation_library_open.py`
(idempotent exact open arms), and `test_conversation_library_installed.py` (opt-in live gates and
both real opens). The foundation pin asserts the library child's exact five routes and the
four-file helper source set; fixture rows stay evidence-not-enablement.

The control set centers four focused suites plus a shared topology and an installed proof:
`_control_plane.py` (the real bridge/IPC/authority/composition seam with only the harness adapter doubled and
the `NOW`-anchored control service), `test_conversation_control_operations.py` (interrupt ledger,
Finding 1/Finding 2 pi settlement regressions), `test_conversation_control_queue.py` (never-bodies
queue truth, withdrawal race, bounded recovery lease + frozen-clock expiry, forgery battery),
`test_conversation_control_attachments.py` (limit refusals, one-use submit, recoverable-lease rebind,
policy/telemetry), and `test_conversation_control_api.py` (the seventeen routes over a real uvicorn
wire, O4 mapping, no-paste source scan), with `test_conversation_control_installed.py` the opt-in
version-locked live proof. The foundation pin asserts the control child's exact seventeen routes;
fixture rows stay evidence-not-enablement.

`test_conversation_runtime_composition.py` and
`test_conversation_authorization.py` cover the runtime composition repair: single install-once
binding at both composition seams, duplicate/missing/foreign/missing-member fail-closed shapes,
per-app child isolation over real HTTP, no import-time singleton, no production identity-injection
or fixture/PTY/browser-identity reliance, server-resolved local-operator identity, loopback-only
resolution, and cross-principal rejection in both directions through an injected seam double.

`test_harness_control_evidence.py` covers the native evidence and resume
substrate: per-harness reserved-key round-trips with the no-leak guarantee across `snapshot.raw`,
projected `control_raw`, and subscriber snapshots; unknown-vendor pass-through; buffer bounds and
clip visibility at two sizes; native-page continuation without overlap/gap, null-terminated, with
typed cross-domain rejection and epoch-mismatch detection; the provenance matrix through the sole
queue delegation; and the codex resume channel end-to-end with pre-spawn refusals.
`test_harness_control_evidence_installed.py` captures the same seam against installed runtimes
(opt-in, version-locked) into redacted `substrate-evidence/*` fixture rows, keeping the
version-mismatched Claude row honestly `not-exercised` and `enablesCapabilities` false everywhere.

`test_harness_control_evidence.py` also carries the evidence-truncation settlement
coverage: `ClipHelperTests` gains three byte-level clip terminal-identity preservation tests (a
clipped pi `message_end` keeps only `type` + `message.stopReason`; a clipped codex `turn/completed`
keeps only `turn.id` + `turn.status`; absent identity is never invented) plus a giant-scalar
drop-whole regression with a 256/257 boundary check, and the new
`EvidenceTruncationSettlementIpcTests` drives oversized (>32 KiB) production pi/codex terminal frames
end-to-end through the real bridge clip and the real `read_control_evidence` IPC surface, asserting
the preserved enums survive to scan helpers that mirror the control child's `_pi_stop_reason` /
`_codex_terminal_outcome` reads verbatim (the acceptance proxy for `probe_l3_delta.py`).

`test_harness_control_plane.py` centers the control-plane contract suite:
the interrupt batteries (bridge epoch guard, codex exact-turn, pi expected-operation guard,
successor zero-write refusal, content-less `message_end` honesty), the timeline batteries
(all-sources/kinds union, eviction floor, the 256-record budget edge), the asset batteries
(schema/traversal/verification/construction/digest/unsupported), the recovery battery, and the
client validation battery. `test_harness_control_plane_installed.py` captures the same seams live
against pinned codex 0.144.5 and pi 0.80.7 (opt-in, version-locked) into redacted
`control-plane/*` fixture rows, with the Claude version-honesty test keeping those rows
`not-exercised` and `enablesCapabilities` false everywhere.

`test_harness_submission_authority.py` centers the authority matrix: slow-adapter responsiveness,
dispatch/withdraw races, early terminal completion, full-ref id reuse, ordering, idempotency/source-
payload conflicts, certified pre-dispatch retry, impossible safe retry after possible bytes, epoch
mismatch, privacy, and retention. `test_harness_control.py` extends the same timeline across IPC,
outer response loss, durable sources, reconcile, and raw-free projection. API tests pin 64-id
status/withdraw and typed 409/503 mapping. Claude/Codex/Pi suites each prove their guarded write and
exact completion semantics; Codex/Pi live smokes remain opt-in installation evidence, not generic
authority.

Live-conformance and Claude discovery-isolation regressions complete the capability-gate coverage. Claude
fake-transport cases cover separate variadic/repeated and equals-attached MCP selectors, the `--`
suffix boundary, exactly one strict empty discovery config, and byte-preserved normal startup. The
explicit-opt-in Codex live case performs dynamic initialize/model-list discovery without a thread or
token event, validates a settings-shaped launch pair, then spends exactly two bounded turns to prove
queued model/effort promotion and subsequent-turn retention on the same PID/thread. Its recorder
retains only method, selection, thread, version, timing, and numeric token-usage evidence; ordinary
suites skip the token-spending case. Captured versions, catalog rows, and counts remain live evidence
rather than production constants.

The frozen daemon consumer boundary and its production races are pinned. Capability
catalog cases prove token-free current-environment discovery, install fingerprint invalidation,
bounded single-flight retention, failed-refresh quarantine/recovery, and protection of a later
concurrent success. API/client/IPC/queue cases prove strict normalized advertise/set parsing,
first-byte ambiguity without blind retry, whole UTF-8 multiline submit, pending and retained
request-id idempotency, retained-known reconciliation without native resend, raw-free public
serialization, and liveness-first 404/409 classification. Opener/app cases prove complete-pair
pre-spawn validation, same-pair live reopen, changed launch conflict with actual retained truth,
fresh dead replacement, and a cross-process different-pair race with one host creation/catalog row.
Role-spawn uses that same opener and conflicts without an alternate launch path.

The complete same-session setter delegate graph is pinned. Shared contract and queue
coverage fail closed outside the five `SetResult` outcomes, reject contradictory effective values,
preserve FIFO set/prompt order, and prove a cancelled waiter cannot poison later commands. Claude
tests require exact session, UUID, canonical command replay, and terminal evidence; near-miss
labels, late/duplicate replay, generic native refusal, and successful dynamic Fable-shaped rows are
separate cases. Codex tests pin desired/pending/effective state, captured prompt selection epochs,
fresh-turn status gating, reversal-to-effective behavior, unrelated drift rejection, and no
reconnect. Pi tests bound mutation/state/catalog stalls, preserve requested-versus-clamped effort,
reject incoherent catalogs atomically, and keep late cancelled responses from the next request.
Scaling cases at 8 and 64 requests prove Codex/Pi cancellation reclamation without tombstone
growth. A static 17-module dependency guard covers the full shared/Claude/Codex/Pi setter graph and
rejects composer, tmux, session-command, terminal-paste, injector, and terminal-surface imports.
The daemon serving endpoints are covered while retaining the same no-paste delegate graph.

Focused and production-path coverage pins settings-resolved initial
configuration. `test_harness_launch.py` proves the normalized contract, Pi's exact
provider-qualified identity, model-gated effort, honest echoes, and the complete Codex selector
grammar. Runner, opener, spawn, settings, and registry suites prove pre-discovery conflict refusal,
token-free discovery before configured vendor startup, native Claude/Codex/Pi launch channels,
roleless Codex dynamic defaults, persistent exact failure evidence, and removal of normalized
model/effort paste synthesis. Adapter tests pin Codex thread/resume configuration and Claude
effective-model mismatch classification. No launch test submits a prompt or turn.

Dynamic, token-free catalog discovery is pinned across all three native adapters.
Claude uses the 2.1.210 initialize/bootstrap/`list_models` fixture, Codex proves paginated hidden
catalog retention without thread creation, and Pi proves provider-qualified identity plus
model-gated thinking menus without prompting. Exact fixture versions remain test evidence only.

Exact Claude/Codex/Pi versions are preserved only as fixture and smoke baselines,
while structured capability acceptance/rejection and the exact additive inbox allowlist are pinned.
Inbox compatibility stays optional-only `adapterDeliveryState` and `adapterDeliveryDetail`,
unrelated extras are rejected, and resource performance is not documented as current behavior.

The IPC regression additionally proves that a delayed reply after accepted dispatch can lose its
peer without an unhandled callback exception: only `BrokenPipeError`/`ConnectionResetError` during
write/drain/close/`wait_closed` are contained, while dispatch, identity, protocol, validation, and
unrelated failures remain loud. The accepted timeout remains ambiguous but bridge-reconcilable, and
the regression confirms the preserved vendor correlation with no retry or fallback.

Worktree-contract read/heal split coverage proves: zero-traversal contract loads (loud
tripwires on the resolver entry points and pathlib walk primitives), legacy leaf ids returned verbatim
by reads, heal parity with the removed read-time normalization, canonical-skip idempotence without
resolution, dry-run reporting, torn-contract tolerance, and the `heal-leaf-ids` CLI seam.

Confirmed-gone reconciliation coverage proves the narrow eligibility boundary, terminal and tmux
positive-gone evidence, fail-closed indeterminate behavior, one-fold/one-snapshot boundedness,
same-lock resolve-plus-compact ordering, stale-snapshot non-resurrection, unchanged TTL fallback,
persisted folded-id removal counts, body-free aggregate events, and silence on no-op sweeps.

Pi boundary coverage proves four levels: the **recorded** capability/framing surface,
fake-adapter queue/retry/compaction/settlement, extension UI, disconnect, cursor
reconciliation, and no-resend behavior, the event mapper's frame classification
(`test_pi_rpc_events.py`), and the real subprocess's correlation, malformed stdout,
EOF ambiguity, and clean stop. The opt-in real smoke installs Pi **0.80.7** under a temporary
prefix/HOME/cache, verifies `get_state` readiness without changing global tools, and re-records
the capability fixture from a live probe.

**The Pi capability recording is version-addressed, and that is the anti-drift mechanism.**
`fixtures/pi_rpc/0.80.7-capabilities.json` is read as `f"{PI_RPC_VERSION}-capabilities.json"` by
both `test_pi_rpc_real_smoke.py` (which defines the pin) and `test_pi_rpc_adapter.py` (which imports
it). Bumping the pin without re-recording therefore fails **offline** with `FileNotFoundError` in
the ordinary suite, rather than waiting on the network-gated smoke test that would re-record it; and
`test_capability_fixture_documents_the_smoke_baseline` asserts exactly **one** `*-capabilities.json`
exists, because a second recording leaves no rule about which is authoritative — which is why
0.80.6 was renamed rather than copied. The old 0.80.6 recording was under-recorded: it listed 4
commands where the adapter drives 7 (`abort`, `get_available_models`, `set_model`,
`set_thinking_level` were all absent) and omitted the `model` state field that `parse_pi_state`
reads to derive `model_key`. Every field is now produced by `_pi_rpc_capabilities.py`, which drives
a real installed Pi — including a deliberate unknown-command negative control, without which
"every recorded command was accepted" would prove nothing.

Regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

## Route-Wide: Call Sites Now Build Parameter Objects (260731-EFA-L2)

`PLR0913` was armed and 274 of 293 long signatures were fixed **by extraction**, introducing 163
parameter objects. About a hundred modules in this route changed as a consequence, and almost all of
that change is one kind: a call site that used to pass a long keyword list now builds a parameter
object first.

**What a future agent should take from that:** those modules prove exactly what they proved before.
A file card in this route that describes what a suite *asserts* is still true even though the
module's diff is large; a card that quotes a *keyword argument* may not be. Examples corrected in
this pass: `create_app(watch_changes=False)` is now `cadence: ProjectionCadence` /
`live_inputs: LiveProjectionInputs` / `collaborators: ServingCollaborators`;
`_provider_operation_result(launch_capable_provider=…)` is now
`ProviderOperation(required_provider=…)`; `task_doc_tool` takes `TaskDocTarget` + `TaskDocEdit`;
`create_operator_inbox_entry` takes `InboxMessage` / `InboxAddress` / `InboxPoster` /
`InboxRouting`; `test_agent_notifier.py`'s `_entry(...)` no longer mirrors the catalog row's fields.

The one place a long signature is still allowed is `mcp/src/agents_remember/mcp/registration/`,
where the signature **is** the published MCP input schema — see
`test_code_quality_check.py::ToolSignatureExemptionTests` and `test_mcp_registration_wiring.py`.

## Wire-Contract Conformance Gate (260731-EFA-L4)

Three new suites are the **enforcement** half of this leaf. The leaf replaced `dict[str, Any]`
escape hatches with real types; without these three, those types would be conventions — the models
would say what a payload is, and nothing would compare that to what a producer actually emits. All
three are written against the same failure shape: a **set difference** between what a producer can
write and what a boundary declares, invisible because both sides look declared. Each stops
somewhere specific, and the stopping point is the part to read before trusting one of them.

### `test_serving_response_conformance.py` — the HTTP wire, all 61 routes

**What it proves.** Every HTTP route on the serving app declares a response model
(`ServingRouteInventoryTests`), and — the part that matters — the body a real request actually gets
back validates against the model declared *for the status that came back*
(`responses[status]["model"]` when there is one, `response_model` otherwise). It has to be
end-to-end, because **the declaration cannot be the gate**: FastAPI applies `response_model` only
to values it serializes itself, and a handler returning a `Response` instance is handed back
untouched and never reaches `serialize_response`. 57 of the 61 handlers do exactly that and two
more are async-generator SSE routes, so on 59 of them the decorator buys an OpenAPI schema and
enforces nothing at runtime. A suite that asserted only "every route declares a model" would have
gone green the day the decorators landed and caught no drift on those 59 ever.

Three mechanisms carry weight beyond the plain validation:

- `validate_wire` validates with `by_alias=True, by_name=False`. Both `WireResponse` and
  `conversation/models.WireModel` set `populate_by_name=True`, so a plain
  `TypeAdapter(...).validate_python(body)` accepts `identity_digest` as happily as
  `identityDigest` — flip one handler's `model_dump(by_alias=True)` to `by_alias=False` and every
  key on that route goes snake_case, a total break for the cockpit, while every model still
  validates. Alias-only makes a field-name key an undeclared key against `extra="forbid"`, and
  `test_a_field_name_body_fails_the_declared_contract` proves the axis is load-bearing by
  rewriting a real body into field-name form and requiring it to fail.
- `ValidatedRouteHazardTests` covers the two routes FastAPI genuinely validates (`GET
  /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`), where drift is an
  HTTP 500 rather than a red test. `TerminalCatalogEntry.to_json`'s emitted key set is read by
  **AST scan** — not from a constructed instance, because `to_json` is conditional and every
  optional key is absent when `None` — and asserted equal to `TerminalCatalogEntryWire`'s declared
  aliases in *both* directions, pinned at 52 keys so a scan that read nothing cannot satisfy the
  equality.
- `RouteWalkerTests` puts the inventory's own "these are all the routes" clause under test:
  each registration form FastAPI accepts is registered on a throwaway app and served. The
  websocket exemption is **structural** — an `APIWebSocketRoute` has no `response_model` attribute
  and the test asserts its absence — so it cannot widen into a path skip-list that swallows the
  next undeclared HTTP route. The walk runs inside a *started* app, because `add_api_route` is
  legal from the lifespan.

**Where the guarantee stops.** It is a body-shape guarantee, and it is a *counted* one.
`DeclaredSurfaceCoverageTests::test_the_conformance_table_accounts_for_every_declared_pair` pins
286 declared `(method, path, status)` pairs, **133 driven against a real body and 153 not**, with
every undriven leg listed in `UNDRIVEN_DECLARATIONS` beside its reason and the remainder asserted
as an exact equality — a ledger, not a suppression list, so a leg that stops being driven has to
be written in by hand and one that becomes drivable has to be removed. The undriven legs are the
ones needing a real vendor harness, a bridge that accepts a connection and then fails mid-write,
or a pre-prime startup race the fixtures deliberately do not have. What does hold without
exception is `test_every_route_has_at_least_one_driven_status`: all 61 routes are driven on at
least one status, so the ledger lists unexercised *legs*, never unexercised routes. Before this
existed the drivers kept a `self.checked` set no assertion ever read — 88 of 286 pairs driven,
and seven declared models could be made mathematically unsatisfiable (a required `str` retyped to
`int`) without one test going red.

### `test_served_state_conformance.py` — the served projection type

**What it proves.** Nothing anywhere validated `/api/state`, the SSE `snapshot` event, or the
projection *as served*. Both keys of the serve-time tail — `servingBuild` and
`agentNotifierHeartbeat` — were injected into the dumped projection with nothing declaring them, so
the emitted body validated against no model at all, `WorkspaceProjection` (`extra="forbid"`)
included. The suite drives the real route and the real SSE generator and pins the three shapes the
assembly is allowed to take: the 200 body **is** a `ServedWorkspaceProjection` and is
**not** a `WorkspaceProjection` (`test_state_body_validates_against_the_served_model` asserts the
`ValidationError` explicitly — that is the assertion that used to be unmakeable), the 304 branch
carries the same ETag and a zero-byte body even after the volatile heartbeat has moved, and a
`delta` frame is a bare projection node that carries none of `SERVED_TAIL_FIELDS`. That asymmetry
is what stops the tail from being declared as a projection field, and
`test_serving_only_fields_stay_out_of_the_persisted_projection` names the second consumer that
would have paid for it: `latest-state.json` is a `WorkspaceProjection` artifact.
`ServedStateTailTests` additionally pins that `SERVED_TAIL_FIELDS` *is* the served model's
extension over the projection, that an absent half is a missing key rather than a null
placeholder, and that the two halves serialize under **opposite** null rules — the build stamp
omits what it could not prove, the heartbeat reports a never-ticked supervisor as an explicit
`null` — which is why `served_state_tail` is two dumps and not one shared `exclude_none`.

**Where the guarantee stops.** One route plus the two generators; every other route is the
sibling suite's problem. And its strength is bounded by the projection it validates over: built
over an empty temp directory — which is what this file used to do — `lifecycles`, `enclosures`,
`engineProcesses` and `providers` all come back `[]`, and a body with empty collections validates
against any node model whatsoever. `_populate` writes two leaf enclosure contracts at different
lifecycle positions, an observer event log and a provider snapshot, and `_assert_populated`
refuses a body whose collections are empty, so a fixture that quietly stops seeding fails here
instead of silently reducing every assertion to a check on the top-level key set.

### `test_wire_vocabulary_exhaustiveness.py` — vocabulary exhaustiveness

**What it proves.** That every value a producer can emit validates at the wire boundary it
crosses. The failure is not a typo, it is a set difference: a producer's vocabulary grows, the
response model's hand-written `Literal` copy does not, and nothing notices until a real payload
carries the new member — at which point pydantic raises a `ValidationError` inside an
`@server.tool()` handler that has no `except` for one. Measured before the suite existed: **165 of
the 213 `series-contract.md` files on disk (77.5%) made `context_packet` raise, across seven
independent gaps.** Three rules, deliberately different in kind so a fix that satisfies one cannot
fake the others: `GuidanceWalkTests` walks every branch of the `lifecycle_guidance` state machine
and every writable `cleanup` value and crosses each result through `WorktreeSummary` (behavioural
— it catches a phase the machine emits from a branch nobody remembered); `ProducedLiteralTests`
reads the package's own source, requiring every literal written onto a contract vocabulary field
or handed to `next_guidance` to validate at its wire field, every such write to be statically
readable, and none of them to be spelled as a `dataclasses.replace` keyword; and
`AdvertisedVocabularyTests` holds the published *input* contract to the published *output*
contract in both directions — the `workflow_kind` set `worktree_start`'s docstring advertises must
**equal** the alias, so a member no tool advertises and no producer writes cannot be added
silently.

**Where the guarantee stops, and this one matters most.** The AST scan is the weakest of the three
and the module says so in its own header: **it reads bare string literals**. It does not evaluate
expressions, so `"a" + "b"`, an f-string, `_MAP["x"]`, a name imported from another module and a
plain local variable all pass through it unseen. Any claim that the scan alone keeps a vocabulary
honest is false. What makes the six contract cells total is pyright at `ContractCells`' and
`WorktreeContract`'s typed fields, **plus** the two invariants the scan supplies: no
`dataclasses.replace` call may carry one of those keywords, and every value written at a typed
writer must be an expression the scan can enumerate. The `replace` rule is not hygiene —
typeshed types it `**changes: Any`, so `replace(contract, cleanup="reclaimed-ish")` produced
*zero* pyright diagnostics against a four-member `Literal`; `amend_contract(contract,
ContractCells(...))` exists to put those fields back in front of the checker, and the no-`replace`
rule is what stops a future edit from routing around it. `cast` still passes both mechanisms, as
it must, and is refused by the readability rule instead. `ContractTask.workflow_kind` and
`.memory_mode` are deliberately plain `str` — they are what a caller asked for, arriving from
`worktree_start`'s MCP signature — and are defended at runtime by `_task_vocabulary`, not by a
type. Seven further vocabularies (`RepoSummary.state`, `BranchFreshness.state`,
`DriftCheckResponse.status`, `FileRead.status`, and the three `models.terminal` session
responses) are covered by the same three rules; all seven were measured *aligned* before they were
typed and are here because they had the identical construction, not because they had failed.
`ContractBoundaryTests` owns the other half: what the **reader** does with a contract cell it
cannot classify (degrade and name it, never strand the task) versus what the **writer** refuses to
put on disk.

### Route-wide: the fixtures were carrying values the vocabulary does not contain

`WorkflowKind` is `Literal["chat-task", "light-task"]` — exactly two members. Test fixtures across
this route were writing `"light"`, `"chat"`, `"master-series"`, `"master-task"` and `"master"`,
and **nothing failed**, which is the concrete evidence for why the suite above exists.
`fixtures/build_rich_sim.py` now records the mechanism in place: `load_contract` does not reject an
off-vocabulary cell — it degrades to the declared fallback and records the raw token on
`unknown_cells`; the refusal lives at `validate_contract`, the *write* boundary, which writing a
contract as markdown text bypasses entirely. So a wrong value in a fixture produced a whole
simulated workspace of contracts each carrying a quarantined cell, silently.
`test_context_packet.py`, `test_landing.py`, `test_landing_state.py`,
`test_projection_scaling_cs6.py`, `test_resolver_parity.py` and
`test_worktree_and_observer_helpers.py` are corrected to real members;
`AdvertisedVocabularyTests::test_the_workflow_kinds_advertised_and_declared_are_the_same_set` is
what fails if the set drifts again.

The second route-wide edit is mechanical and worth recognising rather than re-deriving: producers
that returned `dict[str, Any]` now return models or `TypedDict`s, so a test that read
`step["nextTool"]` now reads `step.nextTool` (`next_step_for` returns `NextStep`, not a dump of
it), and a test that read `guidance["nextTool"]` now reads `guidance.get("nextTool")` because
`LifecycleGuidance` declares that key `NotRequired`. A card in this route describing what a suite
*asserts* is unaffected; a card quoting a subscript is not.

## Choke-Point And Closeout Gate Coverage (260731-EFA-L4)

**`test_tool_response_conformance.py` now captures its payloads in the state where the choke point
fires.** The suite sits exactly at the mutation point — `_tool_payload` is where `nextStep` and
`agentNotifierBanner` are set — but its fixtures were a workspace whose supervisor had **never**
ticked, which is deliberately silent, so `agentNotifierBanner` never appeared and the suite validated
the one shape the choke point cannot break. `_stale_supervisor` ticks the heartbeat six hours into
the past, and `test_the_choke_point_injections_are_actually_exercised` asserts both fields are
present in the captures, so a fixture that quietly stops producing them fails there rather than
hollowing out every assertion below it.

The mechanism behind that is the leaf's central repair: `TOOL_RESPONSE_MODELS` was typed
`dict[str, type[BaseModel]]`, which made `nextStep`/`agentNotifierBanner` unreachable **by type**, so
the choke point wrote them into the already-dumped, already-token-counted dict. Consequences,
each now pinned: a stale supervisor made every response fail its own `model_validate` (nothing
declared `agentNotifierBanner`), and the advertised `tokens` excluded the largest thing the choke
point adds. `test_next_step.py::test_advertised_token_count_covers_the_attached_next_step` and
`::test_advertised_token_count_covers_the_agent_notifier_banner` state the invariant as a fixed
point — recounting the emitted dict with `count_response_tokens` must reproduce `payload["tokens"]`
exactly — and each also asserts the field is *genuinely inside* that number by recounting the
payload without it and requiring a smaller total, so an incidental equality cannot pass.
`test_a_raising_staleness_probe_degrades_to_silence` keeps the banner opportunistic: a probe that
raises yields no banner and still a valid `PingResponse`. `amb.emit_tool` is now called off the
final payload for the same reason — the lifecycle's recorded token count used to be the same short
number the wire advertised.

**`test_worktree_closeout_quality_gate.py` roughly doubles, and the three new classes are about
what the gate is *shown*.** `derive_scope` picks what ruff and pyright are handed with `git
ls-files`, which reads the index; `diff_coverage` diffs the base against the tracked tree, which
is blind to the same paths; and closeout commits with `git add -A`. Everything in that gap — every
path a task created and never staged — went into the commit with no rail of the gate having read
a line of it, while the gate reported green. Leaf 3's own `abc7cbcc` shipped four files that way.
Closeout now resets the index and stages the whole task worktree before running the gate, and:

- `CloseoutGateSeesCreatedFilesTests` drives the real `derive_scope` into a real `ruff` run
  (`_ScopeRecordingGate` — substituting anything less real would miss the defect entirely, which
  was never in ruff but in *which files ruff was handed*). A created file carrying `import os`
  fails the gate with `F401` **at that file's path**, no commit is created and
  `closeout_status` stays `not-started`. `test_the_gates_scope_is_the_commits_content` asserts the
  invariant as an equality — the lint paths equal the `.py` paths in the resulting commit tree —
  which covers the mirror defect too: a path the leaf *deleted* stayed in `ls-files` until the
  removal was staged, so the pre-fix gate handed ruff a file that no longer existed and took an
  `E902` for it.
- `TaskWorktreePreconditionTests` guards the staging step, and it tests **git's own definition** of
  a linked worktree (`--git-dir` differing from `--git-common-dir`) rather than the contract's
  `kind`, because that is the property the safety argument rests on. The refusal is asserted as
  *damage that does not happen*: with the guard removed, `git add -A` in a repository's own
  checkout rewrites a partial `git add -p` selection and writes a durable blob for a deliberately
  untracked `secret.env`. `test_a_series_contracts_code_worktree_is_exactly_that_checkout` proves
  the shape is reachable — `default_series_contract` records `code_worktree = code.repo_path`.
- `ConflictedIndexTests` covers the second refusal: `git add -A` over an unmerged index does not
  refuse, it resolves every conflict to whatever the working tree holds and closeout commits the
  `<<<<<<<` markers. `test_the_reset_runs_after_the_conflict_check_not_before_it` asserts the
  *ordering* through what survives — `MERGE_HEAD` still present after the refusal — because a
  mixed reset run first would drop the unmerged entries, leave `diff --diff-filter=U` with nothing
  to report, and make the refusal permanently unreachable.
- `RetryStagesWhatAFirstRunWouldTests` is why the reset exists at all. `git add -A` applies ignore
  rules only to paths git does not already track or hold staged, so a file staged by a refused gate
  stays staged after the leaf adds it to `.gitignore`, and the retry commits it — which is exactly
  how a `.dmypy.json` reached this leaf's own first commit. The property is asserted as an
  **equality of committed trees** between a retried worktree and a fresh one that never saw the
  refusal, not as the presence of a `reset` call.

There is no rollback and the tests say so rather than leaving it to be discovered:
`test_a_refused_gate_leaves_the_task_worktree_staged` asserts the staging survives, no
`index.lock` is left, and no `ar-closeout-index-*` snapshot is orphaned — the index-copy machinery
an earlier attempt used is gone rather than fixed.

`test_observer_projection.py` gains the same shape of proof for the lifecycle state vocabulary:
`MetricsBucketVocabularyTests` (every live state has a metrics bucket **and** every bucket is
fillable, plus `test_the_vocabulary_scan_found_the_states` so a scan matching nothing cannot pass),
`StatePartitionTests` (`State` is exactly its live half plus its terminal half — nothing filed
twice, nothing filed nowhere), and `TerminalityIsStructuralTests` (filing a state terminal is a
claim about the reducer, held by driving a log into it). The reported symptom it pins is concrete:
an `awaiting-developer` lifecycle counted in the total and in no bucket.

## Invariants And Boundaries

- Authority races use explicit synchronization at the preflight/claim/write seams; sleep timing is
  not accepted as proof of withdrawal linearization.
- Every completion test carries epoch + sequence + id + kind. Bare-id/FIFO completion must fail to
  release a successor.
- Safe retry tests distinguish the exact certified pre-dispatch error from first-byte ambiguity and
  assert native submit call counts to catch duplication.
- Bounds may trim terminal history but never live, active, or unknown work; public fixtures remain
  raw-free and terminal records do not retain full prompt text.
- Live smokes are credential-safe, explicit opt-in evidence for installed harnesses. Deterministic
  protocol truth remains in fake/stdio tests.
- Structured-conversation tests preserve separate active/library cursors and ports, exact
  authorization/identity/generation binding, and fail closed on contradictory state products.
- Runtime fixtures and locked helper packages are evidence surfaces only; neither enables history
  or control capability without a production-seam pass.
- Folded-state race regressions force ordering through explicit generator/task boundaries; timing
  sleeps alone are not accepted as proof of snapshot/subscription convergence.
- First recovery is exactly one full snapshot with boot identity, identical state is silent, later
  content uses the normal delta grammar, and every closed/cancelled consumer releases its queue.
- Route-index tests compare complete generated bytes and require a zero-write second pass; source
  counts and covered-file membership must come from the same frozen Git/path-rule snapshot.
- Carryover authority refusals assert official HEAD, status, non-Git bytes, source bytes, and
  route-index absence so parser-default authority cannot mutate any official-memory surface.
- A test that proves git cannot be redirected must re-set the repository selectors inside its own
  scope. `conftest.py` strips them at import, so a redirection assertion that relies on the ambient
  environment proves the harness stripped them and nothing about the call site under test.
- A cold-start assertion must run in a child process with cold caches. In-process, a warm
  `tiktoken.registry.ENCODINGS` makes the load a dictionary hit, so the assertion passes against a
  package that ships no vocabulary; and a network block must be proven to have taken effect before
  anything that depends on it is trusted.
- Generated dashboard whitespace coverage must exercise Git's real attribute resolution. Only direct
  shipped `assets/*.js` may suppress `blank-at-eol`; authored source and generated near misses remain
  strict, and semantic JavaScript string bytes must remain identical through sync.
- A response-model declaration is not a runtime check. FastAPI validates only what it serializes
  itself, so a route whose handler returns a `Response` must be driven and its **returned body**
  validated; asserting that the decorator is present proves nothing about 59 of the 61 routes.
- Wire validation must be alias-strict. `populate_by_name=True` makes field-name and alias forms
  equally valid, so a suite that validates without `by_name=False` cannot see a handler flipping to
  `by_alias=False` — which renames every key on that route.
- A coverage claim must be a counted set, not an impression. Where a conformance suite cannot drive
  a declared leg, the undriven remainder is enumerated with a reason and asserted exactly, so an
  exercised leg that stops being exercised fails rather than disappearing.
- A shape assertion is worth exactly as much as the payload it was made over. Empty collections
  validate against any node model, so a fixture that seeds the projection must assert it seeded it.
- An AST literal scan is never a vocabulary guarantee on its own — it cannot see concatenation,
  f-strings, dict lookups, imported names or locals. It supplements a type checker; the invariants
  that make the pair total (no `dataclasses.replace` on a typed cell, every write statically
  readable) must themselves be asserted, because `replace` is typed `**changes: Any` and produces
  no diagnostic at all.
- The token count a response advertises must be a fixed point over the payload as served.
  Recounting the emitted dict must reproduce it, and each choke-point field must be provably inside
  it (recount without the field and require a smaller total, so equality cannot be incidental).
- A gate that reads the git index must be shown the content that will be committed. Assertions
  about the closeout gate compare its scope to the resulting commit tree, because a file the task
  created and never staged is invisible to `git ls-files` and to a diff against the base alike.
- Ordering between a refusal and a destructive step is asserted through what survives, not through
  call bookkeeping: `MERGE_HEAD` still present after a conflict refusal is what proves the reset has
  not run yet.
- A durability measurement must not be taken through the instrument it is measuring. Loss is
  counted from appender receipts against a raw on-disk read, never through a store's own `read`,
  and "record lost" and "line torn" are counted separately — a strict reader would turn the
  measurement into an exception and a tolerant one would report tearing as loss.
- **A measurement must refuse to report a vacuous result.** A loss figure is a figure about a
  window; open it twice instead of two hundred times and "0 records lost" costs the store nothing
  to earn. `MIN_RECLAIM_TICKS` / `VacuousRunError` therefore sit **in the instrument**, at the
  return of the run, and not in any suite — a check each caller has to remember holds only until
  the next caller, and the script entry point carries no assertions at all.
- **Sibling roots under one temp directory must remain legitimate.** The harness derives its own
  scratch space from `root` itself, so no caller has to know anything about it. A guard that
  instead required callers to pick distinct *parents* would be the same defect rewritten as a
  convention. Correspondingly, nothing the harness writes for its own bookkeeping may live inside
  `root`: the accounting reads that tree as raw bytes, and `root` resolves to a different
  subdirectory per store family, so a sibling is the only rule that holds for all eight adapters.
- A cross-process defect must be reproduced with real processes. Threads let the GIL serialise the
  window under test, so a thread-based reproduction of these stores measures nothing.
- A measurement must name the tree it measured. The harness is pinned to one `mcp/src` through
  `PYTHONPATH` and refuses fatally if `agents_remember` resolved elsewhere; the base-commit
  baseline comes from a `git archive`, never a second git worktree under a coordination tree.
- A prune to nothing is asserted as an EMPTY FILE, never a missing one. `assertFalse(path.exists())`
  over a control-plane log is the shape 260731-EFA-L5 removed: absence proves a file was deleted,
  emptiness proves the records left.
- A projection read must be assertable as non-destructive. Where a test's evidence was produced by
  a rewrite riding on a read, the repair is to split the claim — the read changes nothing, and the
  owning process's reclaim entry point is what removes the record — not to restate the removed
  behaviour in stronger words.
- The per-log in-process mutex is a STATED exclusion, not a fix for a reproducible thread race.
  `flock` already excludes threads through the open file description; the mutex removes the
  dependence of that exclusion on how the handle happened to be opened. Any comment, card or test
  name asserting it closes an existing race is wrong.
- Where a platform cannot be mounted, fake the platform and not the code. The unsafe-lock tests
  substitute an `fcntl` stand-in for one module's reference only, and assert exclusively on raised
  type, message text and on-disk state — never on the substitution.

## Docs References

The resolved Domain Documentation registry has no entries. This route uses direct repository code,
fixtures, and tests and makes no external behavioral claim from dependency names alone.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this test-route update. | — | — |

## Cross-Repo References

The structured-conversation contract and helper/fixture tests execute entirely inside
`agents-remember`; no neighboring repository governs them.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structured-conversation hostile matrices pin cursor-family non-interchangeability, fail-closed provenance, fixed status mapping, capability evidence, operation and attachment semantics, withdrawal recovery, metric evidence, and non-enabling runtime fixtures. | `test_cursor_families_are_runtime_non_interchangeable`; `test_unknown_input_and_controlled_terminal_provenance_fail_closed`; `test_canonical_status_mapping_and_terminal_evidence_are_fixed`; `test_capability_state_tier_and_evidence_matrix_fails_closed`; `test_open_and_attachment_operations_carry_semantic_revision_and_fingerprint`; `test_withdrawal_operation_enforces_phase_outcome_recovery_products`; `test_attachment_operation_enforces_phase_outcome_recovery_products`; `test_every_metric_retains_scope_freshness_precision_and_runtime_evidence`; `test_runtime_fixture_is_evidence_and_cannot_enable_capabilities` | mcp/tests/test_conversation_contracts.py:184-193; mcp/tests/test_conversation_contracts.py:248-269; mcp/tests/test_conversation_contracts.py:373-394; mcp/tests/test_conversation_contracts_operations.py:153-202; mcp/tests/test_conversation_contracts_operations.py:251-284; mcp/tests/test_conversation_contracts_operations.py:489-539; mcp/tests/test_conversation_contracts_operations.py:542-587; mcp/tests/test_conversation_contracts_wire.py:53-73; mcp/tests/test_conversation_contracts_wire.py:76-115 |
| Foundation coverage pins the two ports, child route ownership, one registration seam, exact helper resolution/source set, and raw-free non-enabling fixtures. | `test_exactly_two_conversation_ports_exist`; `test_root_composes_three_owned_child_routers`; `test_global_registration_has_one_stable_inclusion_seam`; `test_helper_package_and_lock_select_only_the_exact_repository_dependencies`; `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement`; `test_runtime_fixtures_contain_no_raw_secret_path_or_conversation_material` | mcp/tests/test_conversation_foundation.py:22-29; mcp/tests/test_conversation_foundation.py:32-107; mcp/tests/test_conversation_foundation.py:110-122; mcp/tests/test_conversation_foundation.py:125-136; mcp/tests/test_conversation_foundation.py:163-188; mcp/tests/test_conversation_foundation.py:191-202 |
| Active serving coverage pins canonical status/parity, per-harness mapper grammars, engine/store mechanics, and the real-socket production routes with the no-PTY source scan. | `ProductionRouteTests`; `PiProductionRouteTests`; `test_orchestration_parity_with_canonical_status`; `test_no_pty_runner_log_or_fixture_production_authority` | mcp/tests/test_conversation_active_api.py:379-945; mcp/tests/test_conversation_active_api.py:948-1035 |
| Installed-library coverage pins live Codex and Pi gate/list/read/resolve paths, malformed helper-protocol rejection, exact real Pi and Codex opens, and Claude contract-not-version gate honesty. | `CodexInstalledTests`; `PiInstalledTests`; `PiOpenEndToEndTests`; `CodexOpenEndToEndTests`; `ClaudeGateHonestyTests` | mcp/tests/test_conversation_library_installed.py:103-186; mcp/tests/test_conversation_library_installed.py:189-281; mcp/tests/test_conversation_library_installed.py:284-413; mcp/tests/test_conversation_library_installed.py:416-551; mcp/tests/test_conversation_library_installed.py:554-586 |
| Control coverage pins the interrupt ledger, queue and withdrawal truth, typed attachment lifecycle, read-only policy, evidence-bound telemetry, and production control routes over the shared control-plane topology. | `ControlApiTests` | mcp/tests/test_conversation_control_api.py:26-378 |
| Composition contract coverage pins install-once, fail-closed binding shapes, per-app isolation, no singleton, and no injected identity or fixture/PTY reliance. | `test_production_composition_installs_one_typed_runtime`; `test_duplicate_installation_fails_closed`; `test_child_composition_is_isolated_per_app`; `test_no_import_time_mutable_singleton`; `test_production_composition_accepts_no_injected_identity` | mcp/tests/test_conversation_runtime_composition.py:113-132; mcp/tests/test_conversation_runtime_composition.py:142-146; mcp/tests/test_conversation_runtime_composition.py:197-208; mcp/tests/test_conversation_runtime_composition.py:211-224; mcp/tests/test_conversation_runtime_composition.py:227-233 |
| Authorization contract coverage pins local-operator identity, loopback-only resolution, no identity channel, ignored browser claims, and cross-principal rejection. | `test_server_resolves_one_local_operator_workspace_identity`; `test_loopback_peers_resolve`; `test_resolution_has_no_principal_or_tenant_input_channel`; `test_browser_identity_claims_are_never_read`; `test_injected_resolver_proves_cross_principal_rejection` | mcp/tests/test_conversation_authorization.py:109-118; mcp/tests/test_conversation_authorization.py:121-126; mcp/tests/test_conversation_authorization.py:153-157; mcp/tests/test_conversation_authorization.py:160-181; mcp/tests/test_conversation_authorization.py:262-282 |
| Evidence contract coverage pins per-harness round-trips, no-leak, bounds, continuation, cross-domain and epoch rejection, provenance, and the resume channel. | `EvidenceBufferTests`; `EvidenceIpcTests`; `CodexEvidenceTests`; `PiEvidenceTests`; `ClaudeEvidenceTests`; `ResumeChannelTests` | mcp/tests/test_harness_control_evidence.py:360-602; mcp/tests/test_harness_control_evidence_ipc.py:48-337; mcp/tests/test_harness_control_evidence_ipc.py:340-507; mcp/tests/test_harness_control_evidence_other.py:60-153; mcp/tests/test_harness_control_evidence_other.py:156-279; mcp/tests/test_harness_control_evidence_other.py:282-350 |
| Installed-runtime coverage captures the redacted substrate-evidence fixture rows through the production seam with version-locked honesty. | `CodexInstalledEvidenceTests`; `PiInstalledEvidenceTests`; `ClaudeInstalledHonestyTests` | mcp/tests/test_harness_control_evidence_installed.py:114-278; mcp/tests/test_harness_control_evidence_installed.py:281-352; mcp/tests/test_harness_control_evidence_installed.py:355-377 |
| Control-plane contract coverage pins the interrupt guards and replay, the paged never-bodies timeline, asset schema/traversal/verification/construction, once-only recovery, and strict client validators. | `InterruptBridgeTests`; `OperationTimelineTests`; `AssetChannelTests`; `AssetNativeConstructionTests`; "class WithdrawalRecoveryTests(unittest.IsolatedAsyncioTestCase):"; `ClientValidationTests` | mcp/tests/test_harness_control_plane.py:289-376; mcp/tests/test_harness_control_plane_assets.py:249-483; mcp/tests/test_harness_control_plane_channels.py:52-318; mcp/tests/test_harness_control_plane_channels.py:321-481; mcp/tests/test_harness_control_plane_recovery.py:32-32; mcp/tests/test_harness_control_plane_recovery.py:107-207 |
| Installed-runtime control-plane coverage captures the redacted control-plane fixture rows through the production seam and enforces the Claude version-honesty posture. | `CodexInstalledControlPlaneTests`; `PiInstalledControlPlaneTests`; `ClaudeInstalledHonestyTests` | mcp/tests/test_harness_control_plane_installed.py:124-266; mcp/tests/test_harness_control_plane_installed.py:269-373; mcp/tests/test_harness_control_plane_installed.py:376-394 |
| Focused authority concurrency, completion, identity, retention, epoch, and privacy matrix. | `HarnessSubmissionAuthorityTests`; `SubmissionLedgerTests` | mcp/tests/test_harness_submission_authority.py:230-755; mcp/tests/test_harness_submission_authority.py:758-926 |
| Common timeline, IPC/response loss, idempotency, reconcile, status, and withdraw coverage. | "class HarnessControlConformanceTests1(unittest.IsolatedAsyncioTestCase):"; "class HarnessControlConformanceTests2(unittest.IsolatedAsyncioTestCase):"; `HarnessControlIpcTests` | mcp/tests/test_harness_control_conformance_1.py:39-39; mcp/tests/test_harness_control_conformance_2.py:29-29; mcp/tests/test_harness_control_ipc.py:77-77 |
| Public API epoch/conflict/certificate/privacy/status matrix plus bounded control-route liveness memo retention. | `HarnessControlApiTests`; `ControlLivenessMemoRetentionTests` | mcp/tests/test_serving_harness_control_api.py:79-776; mcp/tests/test_serving_harness_control_api.py:779-890 |
| Claude stream-json adapter coverage pins discovery/launch, interaction responses, model/effort mutation, replay/reconciliation, interruption, and real-transport relaunch. | "class ClaudeStreamJsonAdapterTests1(unittest.IsolatedAsyncioTestCase):"; "class ClaudeStreamJsonAdapterTests2(unittest.IsolatedAsyncioTestCase):"; `ClaudeInterruptTests`; `ClaudeProductionTransportRelaunchTests` | mcp/tests/test_harness_control_claude_stream_1.py:32-32; mcp/tests/test_harness_control_claude_stream_2.py:30-30; mcp/tests/test_harness_control_claude_interrupt.py:40-40; mcp/tests/test_harness_control_claude_interrupt.py:438-438 |
| Codex app-server adapter coverage pins handshake/discovery, exact turn acceptance, model/effort mutation, server-request correlation, reconnect, and fixture schema. | `test_handshake_uses_stable_protocol_and_exposes_effort_menu`; `test_turn_acceptance_blocking_and_terminal_mapping`; `test_codex_set_rejects_unadvertised_model_and_model_local_effort_without_rpc`; `test_correlated_server_approval_and_elicitation_responses`; `test_reconnect_resumes_reads_and_reconciles_without_resend` | mcp/tests/test_codex_app_server_adapter_basic.py:26-83; mcp/tests/test_codex_app_server_adapter_correlation.py:260-282; mcp/tests/test_codex_app_server_adapter_reconnect.py:43-86; mcp/tests/test_codex_app_server_adapter_reconnect.py:129-185; mcp/tests/test_codex_app_server_adapter_turns.py:23-57 |
| Pi RPC adapter coverage pins protocol framing, discovery, prompt acknowledgement, model/thinking mutation, reconnect/reconciliation, and ledger bounds. | `PiRpcProtocolTests`; "class PiRpcAdapterTests1(unittest.IsolatedAsyncioTestCase):"; "class PiRpcAdapterTests2(unittest.IsolatedAsyncioTestCase):"; `PiSubmissionLedgerTests` | mcp/tests/test_pi_rpc_adapter.py:424-546; mcp/tests/test_pi_rpc_adapter_ledger.py:18-121; mcp/tests/test_pi_rpc_adapter_ops_1.py:23-23; mcp/tests/test_pi_rpc_adapter_ops_2.py:33-33 |
| `_agent_wire_fixtures` defines the reusable Codex collab-agent, sub-agent activity, thread, turn, item, and server-request frame builders. | `CollabAgents`; `collab_agent_tool_call_item`; `sub_agent_activity_item` | mcp/tests/_agent_wire_fixtures.py:63-77; mcp/tests/_agent_wire_fixtures.py:80-106; mcp/tests/_agent_wire_fixtures.py:109-124 |
| The Codex thread-demux incident suite imports the shared wire fixtures and pins multiplexed parent and sub-agent routing. | "from _agent_wire_fixtures import"; `test_spawned_subagent_traffic_never_fails_the_bridge` | mcp/tests/test_codex_adapter_thread_demux.py:16-16; mcp/tests/test_codex_adapter_thread_demux.py:117-180 |
| The Codex projector suite imports the shared wire fixtures and pins collab mapping, roster lifecycle, multiplexed interactions, and child hydration. | "from _agent_wire_fixtures import agent_message_item, item_completed_params"; `CodexCollabMapperTests`; "class CodexAgentEngineTests1(unittest.IsolatedAsyncioTestCase):"; "class CodexAgentEngineTests2(unittest.IsolatedAsyncioTestCase):" | mcp/tests/test_conversation_projector_codex_agents.py:22-22; mcp/tests/test_conversation_projector_codex_agents.py:132-373; mcp/tests/test_conversation_projector_codex_agents_engine_1.py:7-7; mcp/tests/test_conversation_projector_codex_agents_engine_1.py:89-89; mcp/tests/test_conversation_projector_codex_agents_engine_2.py:9-9; mcp/tests/test_conversation_projector_codex_agents_engine_2.py:23-23 |
| The Claude projector suite uses locally synthesized probe-locked stream-json frames to pin sidechain correlation, roster lifecycle, and launch-flag handling. | `ClaudeAgentLifecycleTests`; `ClaudeLaunchFlagTests` | mcp/tests/test_conversation_projector_claude_agents.py:219-466; mcp/tests/test_conversation_projector_claude_agents.py:469-491 |
| The library-agent suite uses fake Codex and Claude native boundaries to pin parent grouping, visibility of unproven shapes, agent reads, and fail-closed resume. | `CodexLibraryAgentTests`; `ClaudeLibraryAgentTests` | mcp/tests/test_conversation_library_agents.py:256-412; mcp/tests/test_conversation_library_agents.py:471-648 |
| Folded-state stream regressions force the handoff mutation, failed-prime snapshot/non-duplication/later delta, and cancellation cleanup. | `test_snapshot_subscription_cannot_lose_an_interleaved_projection`; `test_failed_prime_recovery_emits_one_snapshot_then_normal_deltas`; `test_cancelled_waiting_stream_releases_its_subscription` | mcp/tests/test_serving.py:401-421; mcp/tests/test_serving.py:423-451; mcp/tests/test_serving.py:453-463 |
| Route-index regressions cover ignored/generated exclusion, symlink/sparse/gitlink/non-UTF-8 identity, ambient selectors, typed failures, and repeat convergence. | `RouteIndexTests` | mcp/tests/test_route_index.py:82-907 |
| Carryover full-apply regressions compare raw JSON/Markdown authority with typed parser semantics and prove exact zero mutation for every refusal. | "class CarryoverOverviewApplyTests1(unittest.TestCase):"; "class CarryoverOverviewApplyTests2(unittest.TestCase):" | mcp/tests/test_carryover_apply_1.py:20-20; mcp/tests/test_carryover_apply_2.py:21-21 |
| Worktree fixtures install explicit supported external-memory storage settings so closeout tests exercise real write authority. | `initialized_memory_repo` | mcp/tests/test_worktree_support.py:242-270 |
| Placement succeeds only for a bundle carrying the current build-input fingerprint; every refusal path writes nothing, and `--check` fails through the process boundary. | `BuildPlacementTests` | mcp/tests/test_sync_dashboard.py:63-219 |
| The static surface is pinned in both states without reading the repository own bundle, including method parity against the real `StaticFiles` mount. | `DashboardStaticDirTests`; `MountedBundleTests` | mcp/tests/test_static.py:29-52; mcp/tests/test_static.py:55-144 |
| The placement step under test refuses an absent or non-current `dist` and writes the sidecar only after the tree. | `sync`; `replace_tree` | scripts/sync-dashboard.py:120-135; scripts/sync-dashboard.py:138-159 |
| The production dashboard build invokes Vite after Panda generation and TypeScript compilation. | "panda codegen && tsc -b && vite build" | dashboard/package.json:10-10 |
| Vite recreates `dashboard/dist` and embeds the current dashboard-source fingerprint in `__AR_DASHBOARD_BUILD__`. | `dashboardSourceFingerprint`; "dist"; `__AR_DASHBOARD_BUILD__` | dashboard/vite.config.ts:36-55; dashboard/vite.config.ts:65-65; dashboard/vite.config.ts:67-67 |
| `.gitattributes` preserves whitespace-only lines in packaged dashboard JavaScript and disables text conversion for the content-addressed tiktoken vocabulary. | "whitespace=-blank-at-eol"; "-text" | .gitattributes:3-3; .gitattributes:13-13 |
| The cold-start suite requires the `.gitattributes` vocabulary filename to match the shipped content-addressed file. | `test_the_gitattributes_entry_names_the_shipped_file` | mcp/tests/test_cold_start.py:246-259 |
| Two tests hold the local gates to the wrapper after the hook split: the shared tiered body plus CI carry the command, and each hook is pinned to its tier. | `test_repository_gates_use_default_strict_wrapper`; `test_git_hooks_delegate_to_the_shared_tiered_gate` | mcp/tests/test_code_quality_check.py:128-142; mcp/tests/test_code_quality_check.py:144-152 |
| Six further classes pin the gate honesty: Radon steps are reports, enforcing steps can fail at full strength, the one PLR0913 exemption is AST-bound, CRAP is threshold-enforced, scope is derived, and pytest strictness contracts hold. | `RadonIsAReportNotAGateTests`; `EveryEnforcingStepCanFailTests`; `ToolSignatureExemptionTests`; `CrapThresholdEnforcementTests`; `GateScopeDerivationTests`; `PytestConfigurationTests` | mcp/tests/test_code_quality_check.py:182-237; mcp/tests/test_code_quality_check.py:240-351; mcp/tests/test_code_quality_check.py:354-430; mcp/tests/test_code_quality_check.py:433-525; mcp/tests/test_code_quality_check_scope.py:22-212; mcp/tests/test_code_quality_check_scope.py:215-261 |
| An independent recomputation asserts the wrapper real ruff and pyright argument vectors reach every tracked Python file and every tracked TypeScript file is linted and type-checked. | `PythonGateScopeTests`; `TypeScriptGateScopeTests` | mcp/tests/test_gate_scope.py:151-194; mcp/tests/test_gate_scope.py:197-216 |
| The 100% changed-lines coverage floor is driven against real throwaway repositories for base resolution, hunk parsing, per-line uncovered statements and arcs, and wrapper exit status. | `BaseResolutionTests`; `ChangedLineTests`; `MeasurementTests`; `WrapperIntegrationTests` | mcp/tests/test_diff_coverage.py:81-254; mcp/tests/test_diff_coverage.py:257-351; mcp/tests/test_diff_coverage.py:354-551; mcp/tests/test_diff_coverage.py:554-672 |
| Every registered AR marker is applied to at least one test and reachable from the gated runner in both directions; the two credential-free CI paths are pinned by name. | `GatedPathInventoryTests` | mcp/tests/test_gated_integration_runner.py:86-154 |
| CRAP consumes branch coverage and refuses a report without branch measurement; a partially taken branch lowers a score a statement reader calls perfect. | `CrapCalculatorTests`; `test_a_partially_taken_branch_lowers_the_score_a_statement_reader_calls_perfect`; `test_a_report_without_branch_measurement_is_refused` | mcp/tests/test_crap_calculator.py:17-235 |
| Drift between `scripts/harness/` and the nine generated harness trees fails the suite, covering content and file mode. | `GeneratedTreesTests`; `test_drift_is_reported_for_content_and_for_mode` | mcp/tests/test_sync_harness.py:35-107 |
| The closeout gate suite covers all three statuses and spies on the real argument passed from unannotated closeout call sites. | `CodeQualityGateTests`; `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:49-423; mcp/tests/test_worktree_closeout_quality_gate.py:424-550 |
| The gate is shown the commit content: a created file reaches ruff through real `derive_scope`, a deleted one leaves it, and the lint-path set equals the Python paths in the resulting commit tree. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_quality_gate.py:642-748 |
| Both staging refusals are asserted as damage that does not happen: the repository checkout preserves its `add -p` selection and untracked secret, and a conflicted worktree keeps `MERGE_HEAD` intact. | `TaskWorktreePreconditionTests`; `ConflictedIndexTests` | mcp/tests/test_worktree_closeout_quality_gate.py:791-903; mcp/tests/test_worktree_closeout_quality_gate.py:906-960 |
| A retry commits the tree a first run would: two worktrees driven to the same end state, one through a refused gate, are asserted to produce the identical commit tree, so the ignored `.dmypy.json` a refused attempt staged is not carried into the retry (`RetryStagesWhatAFirstRunWouldTests`). | `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:966-1025 |
| The whole HTTP surface is driven and validated against the model declared for the returned status, alias-strict, with the inventory, walker coverage, two runtime-validated dict routes, and the exact 286-declared / 133-driven / 153-listed ledger. | `_grouped`; `_driven_pairs`; "class DeclaredSurfaceCoverageTests(unittest.TestCase):" | mcp/tests/test_serving_response_conformance_live.py:441-445; mcp/tests/test_serving_response_conformance_live.py:458-481; mcp/tests/test_serving_response_conformance_live.py:484-484; mcp/tests/test_serving_response_conformance_cases_1.py:12-12 |
| `/api/state` and the SSE snapshot validate as `ServedWorkspaceProjection` and refuse `WorkspaceProjection`; 304 is bodyless, deltas omit `SERVED_TAIL_FIELDS`, and the populated-projection guard rejects an empty scaffold. | `ServedStateTailTests`; `ServedStateRouteConformanceTests`; `ServedSnapshotConformanceTests` | mcp/tests/test_served_state_conformance.py:213-257; mcp/tests/test_served_state_conformance.py:260-352; mcp/tests/test_served_state_conformance.py:355-410 |
| Every producible vocabulary member validates at its wire field by three mechanisms; the module header states which vocabulary each mechanism defends. | "class GuidanceWalkTests(unittest.TestCase):"; "class ProducedLiteralTests(unittest.TestCase):"; "class AdvertisedVocabularyTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:230-294; mcp/tests/test_wire_vocabulary_exhaustiveness.py:632-817; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:45-45; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:450-450 |
| The reader tolerates an unclassifiable contract cell by degrading and naming it while the writer refuses it, and every refusal names the contract file it was reading (`ContractBoundaryTests`). | "class ContractBoundaryTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:144-144 |
| Tool-response conformance captures `nextStep` and `agentNotifierBanner` where both envelope additions fire, then validates representative payloads against their registered models. | `ToolResponseConformanceTests`; `test_the_choke_point_injections_are_actually_exercised` | mcp/tests/test_tool_response_conformance.py:538-616 |
| Next-step regressions require advertised token counts to cover the served payload including `nextStep` and `agentNotifierBanner`. | `test_advertised_token_count_covers_the_attached_next_step`; `test_advertised_token_count_covers_the_agent_notifier_banner` | mcp/tests/test_next_step.py:305-317; mcp/tests/test_next_step.py:319-331 |
| The lifecycle state vocabulary is partitioned live and terminal with both halves total and disjoint, every live state counted, and terminality held to the reducer that produces it. | `MetricsBucketVocabularyTests`; `StatePartitionTests`; `TerminalityIsStructuralTests` | mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:236-300; mcp/tests/test_observer_projection_metrics.py:303-420 |
| The rich-sim fixture records the raw token in `unknown_cells`, and writing the document as Markdown text bypasses `validate_contract`. | "records the raw token on"; "unknown_cells"; "validate_contract"; "writing the document as markdown text bypasses entirely" | mcp/tests/fixtures/build_rich_sim.py:524-526 |
| A decoy repository named by all eight selectors receives none of the real repository writes or reads, an AST sweep asserts `kernel/git_command.py` is the only git-spawning module, and the benchmark runner argv including `reset --hard` is asserted directly. | `DecoyRepositoryTests`; `SingleRunnerTests`; `BenchmarkRunnerEnvironmentTests` | mcp/tests/test_git_command.py:155-211; mcp/tests/test_git_command.py:393-465; mcp/tests/test_git_command.py:663-791 |
| The sweep reach is planted and asserted for subprocess aliases, a path-qualified git argv head, a `kwargs` splat that is not proof of `env`, and per-command timeout bands. | `SingleRunnerGuardReachTests`; `TimeoutClassTests` | mcp/tests/test_git_command.py:468-547; mcp/tests/test_git_command.py:550-660 |
| The runner scrubs repository selectors on every call, uses `input_text` for git patch-id and DEVNULL otherwise, and carries the local, remote, and metadata timeout constants. | `GIT_REPOSITORY_SELECTOR_ENV`; `GIT_LOCAL_TIMEOUT_SECONDS`; `GIT_REMOTE_TIMEOUT_SECONDS`; `GIT_METADATA_TIMEOUT_SECONDS`; `git_environment`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:33-42; mcp/src/agents_remember/kernel/git_command.py:70-72; mcp/src/agents_remember/kernel/git_command.py:76-82; mcp/src/agents_remember/kernel/git_command.py:70-70; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| A cold-cache child process with blocked sockets starts the real server and matches the warm parent count; the shipped vocabulary name and bytes are re-derived and the filename pin and re-entrant-load guard are covered. | `ColdStartTests`; `VendoredVocabularyTests` | mcp/tests/test_cold_start.py:199-218; mcp/tests/test_cold_start.py:221-331 |
| A present but incorrect vendored vocabulary is refused and left on disk across CRLF, truncation, and flipped-byte cases. | `CorruptVendoredVocabularyTests` | mcp/tests/test_cold_start.py:334-417 |
| The measurement instrument uses eight store adapters, three forked scenarios, raw on-disk loss accounting, and a dual-mode script path guarded by `_require_source_root`. | `StoreAdapter`; `ADAPTERS`; `SCENARIOS`; `surviving_ids`; `run_case`; `_require_source_root` | mcp/tests/_store_durability.py:109-166; mcp/tests/_store_durability.py:560-562; mcp/tests/_store_durability.py:577-602; mcp/tests/_store_durability.py:1058-1062; mcp/tests/_store_durability.py:1077-1081; mcp/tests/_store_durability.py:1220-1227 |
| `harness_work_dir` derives each run bookkeeping directory as a sibling named from that run root, preventing sibling cases from sharing stop or error files. | `harness_work_dir` | mcp/tests/_store_durability.py:847-874 |
| The shared non-vacuity gate refuses incomplete durability results or runs below `MIN_SUCCESSFUL_RECLAIMS` by raising `VacuousRunError`. | `MIN_SUCCESSFUL_RECLAIMS`; `VacuousRunError`; `require_stress_measurement` | mcp/tests/_durability_measurement.py:11-11; mcp/tests/_durability_measurement.py:14-15; mcp/tests/_durability_measurement.py:18-55 |
| No record reported written is missing afterwards for the six record types; loss and raising are asserted separately, torn-line policy is held per consumer class, and the harness detects the defect against a git archive of the base commit. | `MultiProcessDurabilityTests`; `TornLinePolicyTests`; `HarnessVacuityGuardTests`; `HarnessSensitivityTests` | mcp/tests/test_controlplane_store_durability.py:123-205; mcp/tests/test_controlplane_store_durability.py:208-336; mcp/tests/test_controlplane_store_durability.py:339-386; mcp/tests/test_controlplane_store_durability.py:389-444 |
| The provider durability suite is the second consumer covered by the instrument tick floor; its `case_root` docstring records the shared-stop-flag defect and source fix. | `ProviderStoreDurabilityTests`; `case_root` | mcp/tests/test_provider_store_durability.py:262-277; mcp/tests/test_provider_store_durability.py:280-351 |
| One human approval is consumable exactly once, and the counterfactual proves the defence is one appended record. | `GateReplayWindowTests`; `test_the_applied_record_is_the_only_thing_closing_the_window` | mcp/tests/test_gate_replay_window.py:176-324 |
| The in-process axis covers the mutex, re-entrancy across both locks, unsafe-filesystem refusal, schema major/minor policy, and failed-rewrite temp cleanup. | `InProcessExclusivityTests`; `UnsafeLockFilesystemTests`; `SchemaVersionMajorTests`; `FailedRewriteTests` | mcp/tests/test_durable_store_contract.py:167-365; mcp/tests/test_durable_store_contract.py:368-431; mcp/tests/test_durable_store_contract.py:434-520; mcp/tests/test_durable_store_contract.py:650-728 |
| The contract the four suites are named after: what prevents loss (the unconditional lock) stated apart from what merely documents (advisory ownership), the rewrite that never unlinks, and the record validator that gives both read policies their behaviour with no version branch in either. | `exclusive_access`; `rewrite_lines`; `require_lock_held`; `thread_mutex_for`; `DurableRecord` | mcp/src/agents_remember/controlplane/durable_store.py:248-271; mcp/src/agents_remember/controlplane/durable_store.py:301-315; mcp/src/agents_remember/controlplane/durable_store.py:348-394; mcp/src/agents_remember/controlplane/durable_store.py:397-415; mcp/src/agents_remember/controlplane/durable_store.py:439-446 |
| The projection tick this leaf stopped rewriting on — the reclaim pass that ran in a process owning nothing here, and the source of the measured gate-log loss. | "def read_gates(coordination_root: Path, *, now: date" | mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:104-104 |
| Interaction retention separates projection non-mutating reads from owner-side compaction, and owner compaction leaves an empty named log. | `test_an_open_gate_past_24h_leaves_the_projection_then_leaves_the_log` | mcp/tests/test_interaction_retention.py:31-76 |
| Projection-side attention acknowledgement pruning leaves an empty file rather than unlinking the log. | `test_project_and_write_prunes_completed_lifecycle_attention_acknowledgement` | mcp/tests/test_observer_projection_snapshot.py:511-545 |
| GateStore compaction that removes the last gate leaves an empty workspace log rather than unlinking it. | `test_pruning_the_last_gate_empties_the_workspace_log_without_unlinking_it` | mcp/tests/test_packaged_assets_and_context_values.py:419-444 |
| Serving attention-store pruning requires zero rows and zero bytes while retaining the log path. | `test_attention_store_upserts_and_prunes_lifecycle_rows` | mcp/tests/test_serving_actions.py:355-388 |
| The worktree contract's front matter read under the same major/minor rule as the JSONL records, through the same helper, so the two version policies cannot drift. | `ContractSchemaVersionTests` | mcp/tests/test_worktree_contract_lifecycle.py:84-145 |
### Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Harness Sub-Agent Regression Route Impact

Harness sub-agents are first-class in test coverage: one shared codex
vendored-shape fixture module plus five focused suites prove the thread demux (the 2026-07-24
production bridge-death incident class), both projectors' agent grammar (roster, multiplexed
pendings, per-thread twin suppression, sidechain binding, the claude flag floor), and both
libraries' agent grouping with visible degrade notes. Four existing suites gain targeted
extensions (plural-pending authority + serialization, flag-floor probe/relaunch, the reordered
binder pin, the additive fake-boundary agent fetch). Native-helper sub-agent enumeration and the
agent transcript read are covered at the Python port boundary in
`test_conversation_library_agents.py`; the helper's own Node suite is unchanged.
The remediation adds twelve pins: nine in the demux suite (concurrent parent server requests
answered per id with the oldest in the singular slot, the method-first degrade split —
experimental/unknown METHODS decline + degrade on the parent while known-method malformed shapes
and boolean rpc ids still fail loud, the bounded pending map declining only the newest request,
and the load-shed queue's delta-shed/consumer-mint/notice-before-sentinel ordering), two in the
codex-agents projector suite (concurrent-parent projection with plain parent entries, the
singular-rotation resolution semantics), and one in `test_harness_control.py` (the entry-thread
operation guard for concurrent parent tuple entries); the legacy experimental-request case in
`test_codex_app_server_adapter.py` flips to decline-not-fail with the decline itself unchanged.
Verification metadata remains pre-commit.

## Codex Native-History And Projection-Containment Regression Route Impact

`test_codex_native_history.py` pins items-first/turns-second runtime probing, exact `-32601`-only
legacy entry, 16 MiB complete source-response refusal, 64 MiB/64-walk one-shot continuation,
linear once-only source reads, cycle/repeated-id termination, aggregate legacy bounds, eviction
without refetch, and typed IPC survival. `test_codex_history_production_path.py` composes the exact
4,846,576-byte response through stdio, installed-shaped items `-32601` then turns/full success,
adapter, Unix IPC, and selected-child projection; its cyclic second-wave child fails locally while
parent and sibling remain live.

The protocol suite owns increasing below-fuse sizes, exact 128 MiB payload-plus-newline acceptance,
one-byte-over refusal, and shared-fatal above-fuse evidence. Projector/API/browser suites own
selected-child-only hydration, unlocked child I/O, same-child singleflight, necessary 64-entry
capacity bounds, valid persisted-focus one-shot hydration, stale-focus non-hydration, and visible
retry/recovery without parent stream failure. The dormant library full-read path is not covered as
repaired and remains a named follow-up.

## Serving Performance And Quality-Gate Route Impact

The regression set covers the serving performance/truth changes (single-pass repository discovery, projection-body reuse, gzip/SSE separation), opt-in heap diagnostics, landing-final reopen safety, structured multi-question interaction responses, native interrupt correlation, active page/event bootstrap recovery, and terminal startup/liveness boundaries. The final focused additions prove mandatory default CRAP failure and wrapper parity, fail-closed closeout with zero mutation on quality failure and quality-before-commit on success, updated public tool descriptions, and Claude mutation parsing through public projector paths for valid and malformed vendor inputs. These tests are split across the existing focused suites; no new test route is introduced. Existing verification metadata remains pre-commit.

## 260731-EFA-L16 Route Impact — cross-store lock-order forcing tests

`test_cross_store_lock_order.py` pins the 2026-08-05 ABBA repair against the daemon's real
sharing shape (ONE catalog + ONE inbox log per process): a placement property proving the
hosted-interaction synchronizer's inbox/gate locks are never taken under the catalog batch —
driven on the full sweep AND the starting fast path, with the legacy inline direct-observe path
pinned beside it; a rendezvous-parked reproduction running the real liveness sweep and
agent-notifier sweep on threads, which deadlocks by timeout on the pre-fix tree ("the ABBA is
live") and passes on the fix, on daemon threads so the proof cannot hang the suite; and
thread-identity proofs that control/active resolution and the terminal-image handler run their
blocking reads on worker threads, never the event loop. Every test asserts the synchronizer
actually ran — no vacuity. The closeout citation-gate tests joined them: a changed construct
completes with the stamp advanced to the new code commit, and a deleted construct refuses in
the citation gate BEFORE the code commit with no commit spent.

## 260731-EFA-L7 — Test-Tree Remediation And New Suites

All 27 over-limit test modules were split in place into families (79 new modules; every original `test_*` name reconciled item for item, plus one intentional new name for R17). New suites added: `test_file_size_detector.py` (the File Size Budget rail — bands, exit codes, wiring, scope), `test_facade_surface.py` (the eight-facade surface pin), and the harness-control conformance family `test_harness_control_conformance_1.py` / `_2.py` + `test_harness_control_ipc.py` (L8's deterministic receipt-before-release rewrite applied verbatim). `test_quality_scope_reporting.py` now asserts the live 426-TypeScript-input count.


## 260731-EFA-L17 — Targeted-Contract And Altitude Proofs

The test tree gained three focused suites for the quality ladder: `test_code_quality_targeted.py`
(derivation selectors, transitive reverse-import closure, uncovered-module refusal, real targeted
wrapper runs with radon consuming the changed module files), `test_code_quality_memory_cap.py`
(systemd/rlimit planning and the wrapper's cap enforcement and policy naming), and
`test_worktree_integrate_quality_gate.py` (leaf targeted / series full+capped altitude routing,
settings-owned cap, refusal-before-merge, dry-run planned-gate payload). Existing families were
extended: closeout gate mode/cap/kill-shape assertions, hook-tier `pre-push → targeted`, settings
`qualityGate` family, scope-reporting integration invocation labels, and the deterministic
observer ticker-exit assertions (`ticker.join` replacing poll loops — test-only, kills a
race-dependent diff-coverage class).

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 route impact: recorded the two new inbox
  arrival/rebinding forcing suites (25+33 tests) and the terminal-honesty fixture updates
  across the notifier/liveness/dispatch/expectation/reclamation/escalation/conformance and
  registration-wiring families. Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 route impact: recorded the new
  `test_compound_idle_relay.py` forcing suite, the L2 rebinding-fixture isolation change, and
  the 63→64 wire-key pin in the conformance family. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 route impact: recorded the three new relay suites and
  the expectation/facade/wire-pin updates in the existing families. Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 route impact: route body reviewed and updated for the supervisor -> agent-notifier rename (see the route-specific body section above); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the three new suites and the
  extended closeout/hook/settings/scope-reporting/observer families. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 route impact: recorded the in-place test-family splits, the detector/facade-surface/conformance suites, and the count fix. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: test_quality_scope_reporting.py was re-scoped to run the real hook with an npm shim; the tests route's meaning is unchanged.
- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the cross-store lock-order forcing tests (placement, rendezvous ABBA reproduction, offload proofs, anti-vacuity). Verification metadata pinned until closeout stamps the code commit.
- 2026-08-04T14:41:21+02:00 — 260731-EFA-L6 S18-B01 closing same-reviewer correction: narrowed the rich-sim claim to the complete raw-token/unknown_cells and Markdown-bypass relationship under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. The Durable Store Integrity Gate section named
  three properties that make the instrument's output evidence and **was silent about the instrument's
  own defect**, which is the property that failed. Added the fourth: the harness derived its work
  directory — including the reclaimer's **stop flag** — from `root.parent`, and
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`, so all cases
  shared one flag and every case after the first left the tick loop after roughly one tick.
  Measured before the fix: **25 reclaim ticks for the first store and exactly 1 for each of the
  other seven, all eight reporting 0.00% loss**; the forced scenarios additionally shared
  `forced.id` and the `*.err` files, so a case whose appender wrote nothing was scored off its
  predecessor's receipts. Recorded the fix as
  `harness_work_dir(root) = root.with_name(root.name + "-harness")` — a **sibling**, because `root`
  does not name one place (control-plane logs under `root/workspace`, provider logs under
  `root/logs/observer/providers`, `GateStore` also globbing `root/lifecycles/*/gates.jsonl`) while
  the accounting reads that whole tree as raw bytes — and the guard as `MIN_RECLAIM_TICKS = 10`
  raising `VacuousRunError` at the end of `run_stress`, **in the instrument rather than in either
  suite**, so both contract suites and bare `main()` runs share one floor. The floor's evidence is
  recorded with its direction: 22-39 ticks idle, 34-49 under 24-way load, load *raising* the count,
  with 20 rejected because the observed minimum is 22. **The reassuring half is recorded beside
  it:** the documented base-commit rates survived, re-measured at attention 23.91% / gate 9.38% /
  supervisor-signals 8.00% / expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00% — same
  ordering, same lone survivor — because `main` already built each case a root under its own
  parent. The bug never corrupted the historical measurements; it hollowed out the ongoing
  regression. Those six figures are **labelled as the leaf's four-run means that do not appear in
  the source**, with the source's *ranges* named and located
  (`HarnessSensitivityTests`' class docstring) and each mean checked to fall inside its range. Two
  invariants added: *a measurement must refuse to report a vacuous result*, and *sibling roots under
  one temp directory must remain legitimate* — a guard demanding distinct parents would be the same
  defect rewritten as a convention. **Drift repaired:** the section described the instrument as
  covering six stores and carried the provider adapters as unstaged mid-flight work; they have
  landed, so it now says eight with `CASES` / `PROVIDER_CASES` held apart, and the three record
  classes (`survivor-*` / `decoy-*` / `anchor-keepalive`) are stated because they are what make
  "loss" mean a row nobody decided to drop. The two `_store_durability.py` and
  `test_controlplane_store_durability.py` evidence rows carried ranges from shorter versions of both
  files and were re-derived; rows were added for the instrument's fix/guard and for the provider
  suite. **Citations:** every range was opened and checked against each symbol the row names, ends
  included. `_store_durability.py` (now 1153 lines) and `test_controlplane_store_durability.py` are
  staged with no unstaged edits and are cited by line; `test_provider_store_durability.py` still
  carries unstaged edits and is cited **by symbol name only**, as are all `controlplane/` and
  `providers/` source modules. Verification metadata untouched; closeout owns it.
- 2026-08-01T19:10+02:00 — Measured-claim repair in the Durable Store Integrity Gate section; nothing
  about the instrument's three trustworthiness properties, the torn-line policy, the replay-window
  counterfactual or the mutex was touched, because it was right. The section asserted six
  base-commit loss rates, "127 of 2000", "10 runs per store" and "zero torn lines in every run" as
  measurements, and closed with "0 lost, 0 raised, 0 torn, all six stores, all three scenarios"
  against the current tree. **No base-commit measurement artifact is committed anywhere in the
  tree** — `_store_durability.py::main` can write a JSON payload but none is stored, no test asserts
  a rate, and no committed invocation passes `runs` — so that is now stated once and the rates are
  separated from what *is* checkable. `BASE_COMMIT = e52edaf5` and the `STRESS_PROFILE` literals
  (4 × 50 @2 ms against 1 reclaimer @5 ms) stay asserted, because they are literals in the file.
  31.45% and 11.50% stay asserted, on the authority of four and three independent sites
  respectively. 10.50 / 10.20 / 9.20 / 0.00%, 127 of 2000, "10 runs per store" and the whole-not-torn
  property are attributed to `durable_store.py`'s module docstring, which is the text these cards
  document. **The post-fix claim was overstated on two axes and is corrected against the test
  source, citing the class:** `MultiProcessDurabilityTests` asserts `lost == 0` in all three
  scenarios, but `forced_unlink` iterates `APPEND_CASES` — **five** stores, attention dismissals
  excluded by construction because it has no `append` — and `torn_lines == 0`,
  `append_error_count == 0` and `reclaim_error_count == 0` are asserted in the **`stress` scenario
  only**. Recorded as mid-flight, not as landed: `_store_durability.py` carries unstaged edits
  adding two provider adapters, which do not widen those counts because the working tree keeps
  `CASES` at the six control-plane stores beside a separate `PROVIDER_CASES`. The R14 sentence
  beneath it was already exact and was left alone. The 14:20 entry below
  carried the same six-rate list and was reduced to a pointer at this entry. Verification metadata
  untouched; closeout owns it.
- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator. Nine files in this route changed for one defect —
  measured record loss in the six control-plane JSONL stores — and **four of them are new**, so the
  card gained a section, nine invariants and nine evidence rows. **Durable Store Integrity Gate**
  documents the four new suites with the instrument first, because the numbers depend on it:
  `_store_durability.py` holds no assertion at all, expresses each store through its own shipped
  reclaim entry point rather than a reimplementation, and is trustworthy for three stated reasons —
  real processes via `multiprocessing` fork (the defect is cross-process; the GIL would serialise
  the window), **dual-mode** operation where a script run pins `PYTHONPATH` to exactly one
  `mcp/src` and `_require_source_root` refuses fatally if `agents_remember` resolved elsewhere
  (which is what let it measure a `git archive` of the pristine base commit), and **loss accounting
  that deliberately bypasses every store's own `read`** — a raw tolerant JSON-lines reader counting
  "record lost" and "line torn" separately, so a strict reader cannot turn a measurement into an
  exception and a tolerant one cannot report tearing as loss. Recorded the baseline the sources
  report at `e52edaf5` against the checkable `STRESS_PROFILE` literals (4 appenders × 50 records
  @2 ms against 1 reclaimer @5 ms) — corrected by the 19:10 entry above, which splits those rates by
  corroboration and restates the post-fix claim at its true strength.
  Recorded `test_controlplane_store_durability.py`'s three claims (R10/R8/R14, with loss and
  raising asserted separately because a store that raises instead of losing has moved the failure),
  `test_gate_replay_window.py`'s counterfactual (the whole defence is one appended record; delete
  only the `applied` line and the approval is spendable again — base commit exits 1 with
  `AssertionError: 'approved' != 'applied'`, fixed tree exits 0), and
  `test_durable_store_contract.py`'s in-process axis. **The mutex is documented as what it is and
  not as a race fix:** `flock` already excludes two threads of one process through the open file
  description, that was measured rather than assumed, and `thread_mutex_for` closes the
  *dependence of thread exclusion on where the handle came from* — cache one lockfile handle on the
  store and `flock` silently stops excluding, with nothing in the tree failing. Its
  unsafe-filesystem tests fake the **filesystem** at the `fcntl` boundary, scoped to one module's
  reference, and assert only on raised type, message text and on-disk state. Recorded that the five
  updated suites replaced "the pruned log stops existing" with emptiness (`is_file()` +
  `read_bytes() == b""`), which is strictly stronger since zero bytes proves the records left
  rather than that the file did — and that `test_interaction_retention.py` is the **exception**:
  its assertion had been reading a side effect of the projection tick's physical rewrite, the very
  behaviour the leaf removed, so it was split into two proven claims (the projection leaves the log
  byte-identical — newly asserted — and `GateStore.compact` in the owning process empties it)
  rather than restated. Added nine invariants covering measurement independence, real processes,
  naming the measured tree, emptiness-not-absence, splitting a claim whose evidence was a removed
  side effect, the mutex's exact scope, and faking a platform rather than the code. Added nine
  Repo-Internal rows. **Citations:** every added row's range was opened and checked against each
  symbol the row names, ends included; the four new suites' self-ranges are stable (none of the
  nine test files carries unstaged edits). Six control-plane source modules
  (`durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py`,
  `orchestration_nudges.py`, `supervisor_signals.py`) were still being edited in the code worktree
  during this pass, so rows pointing into them are cited **by symbol name** rather than by line
  range; the symbol is the durable anchor and closeout should treat the linked file cards as
  authoritative for line numbers. Verification metadata pinned until closeout stamps the L5 commit.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), one clause. The 00:50 entry below
  said `response_model` "enforces nothing on the 59 handlers that return a `Response`", which
  mis-describes the composition of the 59: **57** of the 61 HTTP routes return a `Response` subclass
  and **2** are SSE async generators feeding an `EventSourceResponse` (`GET /api/stream`,
  `GET /api/events`) — that is the 59 on which the decorator contributes an OpenAPI schema and
  validates nothing. The remaining **2** (`GET /api/terminal/sessions`, `GET /api/harnesses`) return a
  bare `dict` and *are* validated by FastAPI. The conclusion the entry draws was right; only the
  breakdown was wrong. Verified against `serving/response_contract.py` L11-L18 and against this
  card's own body. Nothing else changed.

- 2026-08-01T00:50+02:00 — 260731-EFA-L4 curator. Twenty-one modules in this route changed and
  **three are new**, so the card gained two sections. **Wire-Contract Conformance Gate** documents
  the three new suites as the enforcement half of the leaf, each with its stopping point stated
  rather than implied: `test_serving_response_conformance.py` (drives all 61 HTTP routes because
  `response_model` enforces nothing on 59 of them — **57** whose handler returns a `Response`
  subclass and **2** SSE async generators feeding an `EventSourceResponse`, `GET /api/stream` and
  `GET /api/events`; only `GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`
  and are validated by FastAPI; alias-strict
  `validate_wire`; the AST key-set equality behind the two genuinely-validated `dict` routes, pinned
  at 52 keys; **and the counted ledger — 286 declared `(method, path, status)` pairs, 133 driven,
  153 listed in `UNDRIVEN_DECLARATIONS` with a reason and asserted exactly**, with every one of the
  61 routes driven on at least one status), `test_served_state_conformance.py` (the 200 body
  validates as `ServedWorkspaceProjection` and is required to FAIL as `WorkspaceProjection`; the 304
  is body-less; a `delta` carries none of `SERVED_TAIL_FIELDS`; the tail stays out of
  `latest-state.json`; and `_assert_populated` is what stops the whole file from measuring an empty
  scaffold), and `test_wire_vocabulary_exhaustiveness.py` (three mechanisms of different kinds over
  the contract cells and seven further vocabularies; **the AST scan reads bare string literals only
  and is explicitly not a guarantee on its own** — pyright plus the no-`dataclasses.replace` rule is
  what makes it total, because typeshed types `replace` as `**changes: Any` and produced zero
  diagnostics against a four-member `Literal`). Recorded the measured motivation from the module
  header (165 of 213 `series-contract.md` files, 77.5%, made `context_packet` raise across seven
  gaps) and the route-wide evidence for it: fixtures were writing `"light"` / `"chat"` /
  `"master-series"` / `"master-task"` / `"master"` against a two-member `WorkflowKind`, and nothing
  failed, because `load_contract` degrades and quarantines while the refusal lives at the write
  boundary a markdown fixture bypasses. **Choke-Point And Closeout Gate Coverage** records the
  `TOOL_RESPONSE_MODELS` retyping consequences now pinned (a stale supervisor made every response
  fail its own `model_validate`; the advertised `tokens` excluded `nextStep`/`supervisorBanner`, and
  so did `amb.emit_tool`) and the four new closeout-gate classes (real `derive_scope` into real
  `ruff`; scope-equals-commit-tree as an equality covering the deleted-file mirror; both staging
  refusals asserted as damage that does not happen, with ordering proven by a surviving `MERGE_HEAD`;
  and retry/first-run committed-tree equality). Added ten invariants. **Citations:** all 33
  citation-bearing evidence rows in `Repo-Internal References` were re-checked against the current
  files (range in bounds, and the named symbol read back at the boundary); 2 had moved and were
  repaired — `test_serving.py` L430-L492 → **L441-L503** (the class shifted +11 when `_build_wire`
  was added; the range now runs from
  `test_snapshot_subscription_cannot_lose_an_interleaved_projection` at L441 through the end of
  `test_cancelled_waiting_stream_releases_its_subscription`, which the old range cut off by one
  line) and `test_worktree_closeout_quality_gate.py` L38-L222 → **L49-L369** (the old range covered
  only part of `CodeQualityGateTests` and never reached the `CloseoutCodeQualityGateTests` argument
  spy the claim names; both class statements confirmed at L49 and L248). Added eleven evidence rows.
  Also repaired a rendering defect: five rows in the 3-column `Repo-Internal References` table
  carried only two cells, so their source path was rendering in the Citations column; each gained an
  explicit `n/a` citation cell with no text changed. Verification metadata pinned until closeout
  stamps the commit.

- 2026-07-31T22:30+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers).
  **Both new suites were restructured, so every citation into them was re-derived from the current
  files and every one had moved.** `test_git_command.py` (697 lines): `DecoyRepositoryTests`
  L151-L207 (was L84-L140), `SingleRunnerTests` L389-L459 (was L322-L402),
  `BenchmarkRunnerEnvironmentTests` L656-L693 (was L405-L442); each range re-read and confirmed to
  open on the named `class` statement. `test_cold_start.py` (421 lines): `ColdStartTests` L199-L218
  (was L153-L171), `VendoredVocabularyTests` L221-L331 (was L174-L228). `git_command.py` L24-L96
  re-checked and still correct (`GIT_REPOSITORY_SELECTOR_ENV` at L24 through the end of `run_git`).
  Added two evidence rows for the suites that did not exist when the first entry was written:
  `SingleRunnerGuardReachTests` L462-L540 and `TimeoutClassTests` L543-L653;
  `CorruptVendoredVocabularyTests` L334-L417. **Corrected the `.gitattributes` row**, which said the
  file's rule was inert and its regression removed — true of the `blank-at-eol` rule (still L1-L3)
  but no longer of the file: L13's `-text` entry names the shipped vocabulary by filename and
  cit:([`test_the_gitattributes_entry_names_the_shipped_file`], mcp/tests/test_cold_start.py:246-259) is its live regression. Wrote up the
  guard-on-the-guard reasoning (an AST sweep reports a hole and a clean tree identically, so each
  bypass form is planted: `from subprocess import run`, `/usr/bin/git`, `**kwargs` mistaken for
  `env=`), the per-command timeout assertions and their required-keyword recorder, the
  no-module-scope-import discipline via `tokens_module()`, the bounded-join deadlock guard, and
  `CorruptVendoredVocabularyTests` — including that it works on copies, asserts the corrupt file is
  *still there* afterwards, and that CRLF-mangling and truncation were measured to pass silently
  before the digest check moved into `models/tokens.py`. Verification metadata pinned until closeout
  stamps the code commit.

- 2026-07-31T21:05+02:00 — 260731-EFA-L3 curator: two modules joined this route and both are here
  because the property they guard cannot be observed the ordinary way. Added the **Single-Runner Git
  Gate** (`test_git_command.py`: the decoy repository whose `patch.dict` blocks deliberately undo
  `conftest.py`'s selector strip, the `SingleRunnerTests` AST sweep pinning
  `kernel/git_command.py` as the only module that spawns git, the stated blind spot covered by
  `BenchmarkRunnerEnvironmentTests`, the stdin/`input_text` and three-timeout-class contract, the
  `cleanup.py` remote-stall arms, and the pre-push-hook framing of `QualityGateGitTests`) and the
  **Cold-Start Gate** (`test_cold_start.py`: the subprocess probe with cold caches and a
  proven-effective socket block, the warm-versus-cold count equality, and the re-derived vocabulary
  hashes). Qualified the `conftest.py` selector-inventory sentence, which read as coverage and is
  only fixture safety. Recorded that `test_serving.py::BuildInfoTests` now patches
  `serving.build_info.run_git` — patching `subprocess.run` in a consolidated module patches nothing.
  Added two invariants and three evidence rows. Verification metadata pinned until closeout stamps
  the code commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 8 cross-file line citations, each re-anchored on a read-back boundary. `test_conversation_control_api.py` L1-L379 (382-line file; also dropped the "seventeen routes" phrase — that count is pinned in `test_conversation_foundation.py`, not here); `test_conversation_runtime_composition.py` L113-L252 (was L106-L260 in a 252-line file); `test_harness_submission_authority.py` L1-L675 (was L1-L687 in a 678-line file); `test_harness_control.py` L1-L1958 (was L1-L1180; the file is 1961 lines and the IPC class runs to L1958); `test_serving_harness_control_api.py` L1-L891 (was L1-L700; extended the claim to name `ControlLivenessMemoRetentionTests` at L779); `test_serving.py` L430-L492 (the three `StreamEventsTests` the claim names, was L395-L457); `test_route_index.py` L199-L907 (fixture through the last test, off the `unittest.main()` guard); `test_static.py` L29-L144.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator, **correcting and completing the mid-leaf entry
  below**. `test_complexity_baseline.py` was deleted along with the whole complexity ratchet and its
  file card removed; `test_gate_scope.py`'s three allowlists were deleted, so the routing paragraph
  and evidence row that described them were wrong and are rewritten. Twenty-two further modules
  joined the route and now have file cards: the gate suites `test_diff_coverage.py` and
  `test_gated_integration_runner.py`; the Pi capability helper `_pi_rpc_capabilities.py` with its
  recording `fixtures/pi_rpc/0.80.7-capabilities.json` (renamed from 0.80.6) and
  `test_pi_rpc_events.py`; the serving suites `test_serving_app_routes.py`,
  `test_serving_app_background_loops.py`, `test_serving_helper_behaviour.py`; the platform suites
  `test_platform_edge_refusals.py`, `test_platform_long_tail.py`,
  `test_packaged_assets_and_context_values.py`, `test_provider_runtime_helpers.py`; the conversation
  suites `test_conversation_control_and_library_helpers.py`,
  `test_conversation_control_projector_edges.py`,
  `test_codex_adapter_thread_routing_and_registry.py`; the harness suites
  `test_harness_control_runner_config.py`, `test_harness_logs_user_message_readers.py`,
  `test_harness_submission_authority_adapter_contract.py`; the worktree suites
  `test_worktree_and_observer_helpers.py`, `test_worktree_edge_paths.py`; plus
  `test_mcp_registration_wiring.py` and `test_onboarding_integrity_edges.py`. Recorded the Pi
  capability anti-drift contract, the branch-coverage CRAP change, and three pre-existing 1:1
  fixture gaps closed. The route index is now strictly 1:1 at 210 files. Verification metadata
  pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 curator (mid-leaf, partly superseded above): three new test modules joined this route —
  `test_gate_scope.py` (the gate's scope is the tree, asserted against real argument vectors, with
  shrink-only reason-bearing allowlists), `test_complexity_baseline.py` (the shrink-only complexity
  ratchet in all four failing directions plus the `--write` cap asymmetry), and
  `test_sync_harness.py` (drift between `scripts/harness/` and the nine generated trees, content and
  mode). `test_code_quality_check.py` roughly doubled with four classes holding Radon-is-a-report,
  every-enforcing-step-can-fail, scope derivation, and the pytest strictness/marker/warning
  contracts. Rewrote the "local gate" routing paragraph accordingly and added five evidence rows.
  Verification metadata pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: replaced the Generated Bundle Whitespace Policy
  Gate with the Dashboard Bundle Placement Gate and added a Static Surface Gate. `test_sync_dashboard.py`
  inverted three fail-open tests into refusals and proves `--check` no longer exists through a real
  subprocess; `GeneratedDashboardWhitespacePolicyTests` was removed because the `.gitattributes`
  exception it policed now names a git-ignored path. Added the new `test_static.py` (both static
  states, deterministic, including method parity against the real `StaticFiles` mount) and recorded
  the three build-dependent rewrites in `test_serving.py`. Recorded the two-test split that holds
  the local gates to the wrapper after the hook tiering, and the closeout-gate argument spy.
  Refreshed the affected hot-path routing and reference rows. Verification metadata remains
  pre-commit.
- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: routed the new real-local-subprocess lifecycle tier for
  Claude (transport ownership release across start -> stop -> start, and the adapter's floor
  probe/re-launch to control readiness over the real transport), and recorded that the live smoke's
  `/cost` arm asserts the still-unimplemented harness slash-command capability owned by an upcoming
  master, so its red state there is expected rather than a regression.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: added the two new native-history
  regression suites and routed measured-size transport, exact probe/fallback, one-shot resource
  bounds, cycle/legacy behavior, typed IPC, selected-child concurrency/continuity, and dashboard
  persisted-focus/retry coverage. Updated active route ownership from two to three. Verification
  metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent surface remediation
  regression pins — nine new demux-suite tests (concurrent parent pendings, method-first degrade,
  bounded pending map, load-shed queue), two codex-agents projector tests (concurrent-parent
  projection, singular rotation), one `test_harness_control.py` guard test, and the flipped
  decline-not-fail experimental-request case in `test_codex_app_server_adapter.py`; Hot Path
  Summary and route-impact sections updated. Verification metadata stays pinned (remediation
  uncommitted).

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: added the harness sub-agent regression set —
  the NEW shared `_agent_wire_fixtures.py` and five NEW focused suites (thread demux, codex
  projector agents, claude projector agents, library agents) plus targeted extensions to
  `test_harness_control.py` (multiplexed respond + plural serialization), `test_harness_control_claude.py`
  (flag floor + relaunch), `test_conversation_active_service.py` (reordered binder pin + per-thread
  dict assertions), and `test_conversation_library_ports.py` (additive agent fetch at the fake
  boundary). New-file sidecars registered; verification metadata stays pinned until L7 closeout
  stamps the candidate commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  added the default-threshold, closeout mutation-order, public-tool-description,
  and Claude public-projector regression contracts. Verification metadata remains
  pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T12:00+02:00 — 260718-CHATS-L5P curator: body-reviewed against the post-L5 pyright fixup
  (commit `352d5cd`) that changed `test_chats_l5_hardening.py` after the L5 verification (`68b3205`). The
  change is strict-pyright conformance only (protocol-conformant fake-host param naming, an
  `isinstance`-narrowed assertion, an explicit transcript-`state` annotation, a `Mapping` import) — zero
  behavior change, no `type: ignore`, all seven H1/H2/F2/F4 regressions identical in intent — so the
  route's hardening-regression enumeration (H1 quarantine + F2, H2 authority-pin + F4, the projector-tier
  and installed companions, the 10k baseline) is UNAFFECTED and stands as written. No body change;
  verification metadata advanced to `352d5cd` (the enumeration was reviewed this cycle).
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the half-time functional regression
  narrative — the NEW `test_chats_l5f_leaks.py` (R5 `SessionLockLeakTests` + `QueueRowsBoundTests`) and
  the R1-R6/R4 additions across `test_conversation_active_projectors.py`, `..._active_service.py`,
  `..._contracts.py`, `..._control_operations.py`, `..._library_gates.py`, `..._library_installed.py`,
  `test_harness_control_evidence.py`, `test_harness_control_client.py`, `test_harness_launch.py`, and
  `test_provider_containment.py`. Corrected no version-lock language in this route's narrative (the R4
  contract-only gate is captured in each test sidecar). The new-file sidecar's verification is blank
  (uncommitted); route index refresh registers it. Verification stays pinned until L5F closeout.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: added the evidence-backed hardening regression
  narrative — the new `test_chats_l5_hardening.py` (H1 catalog-sweep quarantine + F2, H2
  authority-pin + F4), the projector-tier H2/F1 companions in `test_conversation_active_service.py`,
  and the F1 installed regression in `test_conversation_control_installed.py` — and noted the 10k
  renderer DOM/interaction baseline lands in the dashboard test tree, not here. New file card
  `test_chats_l5_hardening.py.md` registered in the route index. Verification metadata stays pinned
  until L5 closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: added the authoritative control-API regression
  set — the shared `_control_plane.py` topology (real bridge/IPC/authority/L0 seam, `NOW`-anchored
  service), the four focused suites (operations incl. Finding 1/2 pi settlement regressions; queue
  incl. the frozen-clock expiry proof; attachments incl. on-disk spool deletion; the seventeen-route
  API over a real wire), and the opt-in installed proof — plus the seventeen-route foundation pin, a
  control coverage reference row, and the corrected "control empty" claim. Verification metadata stays
  pinned until L3 closeout stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: added the evidence-truncation settlement
  coverage to the `test_harness_control_evidence.py` description — the `ClipHelperTests` byte-level
  terminal-identity preservation tests plus the giant-scalar drop-whole (256/257 boundary)
  regression, and the new `EvidenceTruncationSettlementIpcTests` oversized-frame end-to-end
  regressions mirroring L3's `_pi_stop_reason` / `_codex_terminal_outcome` reads. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: added the native control-plane regression
  set — the contract suite `test_harness_control_plane.py` (interrupt/timeline/asset/recovery and
  client-validation batteries, 25 tests + 35 subtests), the opt-in version-locked installed
  capture `test_harness_control_plane_installed.py`, and the redacted `control-plane/*` fixture
  rows with `enablesCapabilities: false`. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library regression-set content with the L1 active regression-set content after the master
  memory branch advanced — both suite families, the merged foundation-pin coverage (active two
  routes + library five routes; control empty), and both reference rows survive. Verification
  metadata remains pinned until L1 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: added the active conversation serving
  regression set — four focused suites (canonical status/parity, mapper grammars, engine/store
  with the F1/F2/F3 fix pins, and the real-socket production routes proving identity, cursor
  refusals, epoch-flip gap+close, provenance, parity, and no-PTY authority) plus the foundation
  pin's exact two-route active-child assertion. Verification metadata remains pinned until
  closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: added the native conversation library
  regression set — six focused suites over doubled boundaries (ASGI status ladder, cursor/scope,
  gates, ports, open arms) plus the opt-in installed-runtime suite proving the live Codex/Pi
  gates, both real end-to-end opens, and the Claude version-mismatch posture — the foundation
  pin's exact five-route library assertion and helper source set, and the observed
  evidence-not-enablement fixture rows. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: added the native evidence contract suite and
  the opt-in installed-runtime capture — per-harness round-trips with no-leak proofs, buffer and
  continuation bounds, cross-domain/epoch typed rejection, the provenance matrix, the codex resume
  channel, and the redacted version-locked `substrate-evidence/*` fixture rows. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: added the conversation runtime composition
  and authorization contract suites — install-once/fail-closed composition shapes, per-app
  isolation, no-singleton and no-injected-identity proofs, loopback-only local-operator resolution,
  and cross-principal rejection — plus the one-line `coordination_root` call-shape follows in the
  two harness-control suites. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-positive/authored-negative
  whitespace regression, the direct shipped-JavaScript `blank-at-eol` boundary, Vite/raw-sync byte
  ownership, the rejected-normalization rationale, retained near-miss checks, and the two-build
  byte/fingerprint determinism proof. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the deterministic Git/path-rule census matrix,
  regular/linked/contaminated byte-convergence proof, typed failure coverage, and full-apply
  JSON/Markdown carryover-authority refusal/retention matrix with exact zero-mutation assertions.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: added route-level coverage for deterministic
  snapshot/subscription handoff, first-recovery full snapshot with build identity, identical-state
  silence, later named delta, and explicit close/cancellation subscriber cleanup. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the build/static, raw-event, tmux-environment, and
  narrow harness-discovery regression matrix. Verification metadata remains pinned pending
  candidate closeout.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the hostile normalized-contract
  matrix, exact two-port/three-router topology, repository-only helper resolution, and redacted
  non-enabling runtime fixtures. Added current governing/reference structure; verification remains
  pinned to committed source truth until closeout stamps the candidate.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the authoritative submit/withdraw
  adversarial matrix, exact-ref and early-completion proofs, safe-retry/first-byte split, raw-free
  status/API bounds, native no-queue guarded-write semantics, and retention/privacy invariants after
  canonical review round 6 PASS.
- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: added route coverage for the complete Claude
  discovery-selector grammar and normal-launch preservation, plus the explicit-opt-in two-turn
  Codex live advertise/launch/queued-set/retention proof with sanitized evidence recording.
  Verification metadata remains pinned until closeout stamps the L5 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: added route coverage for install/auth cache
  fencing, failed-refresh quarantine, complete-pair launch, live-reopen/dead-replacement truth,
  cross-process one-process publication, exact-session first-byte ambiguity, request-id idempotency,
  retained reconciliation without resend, raw-free public responses, liveness-first status, and
  shared role-spawn conflict behavior. Verification metadata remains pinned until closeout stamps
  the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: added route coverage for exact five-value
  setter truth, FIFO/cancellation behavior, Claude correlated terminal and dynamic Fable evidence,
  Codex ordered selection epochs and successful fresh-turn promotion, Pi bounded coherent
  error/clamp readback, 8/64 reclamation scaling, and the transitive 17-module no-paste guard.
  Daemon setter endpoints remain L4. Verification metadata remains pinned until closeout stamps
  the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added route coverage for the normalized
  launch contract, complete settings fixtures, native per-harness application, Codex selector
  census and roleless defaults, Pi exact identity, Claude mismatch failure, no-paste enforcement,
  and token-free failure/echo evidence. Verification metadata remains pinned until closeout stamps
  the L2 code commit.
- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: made the 2.1.210 Claude JSONL cohort the
  active fake-transport fixture authority and documented token-free dynamic catalog coverage across
  Claude, Codex, and Pi. Verification metadata remains pinned until closeout stamps the L1 commit.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: added route-level delayed-reply IPC peer-disconnect
  containment and bridge reconciliation evidence.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added route-level Codex completion correlation,
  same-row pending semantics, loud failure cases, replacement-only queue state, and fixture-only pins.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the test-route body for structured
  capability negotiation, rolling inbox compatibility, and the deferred R10 boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: added fake protocol, pinned JSONL fixture, and
  credential-safe `/cost` live-smoke coverage for Claude 2.1.207, including failed API-429 semantics.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added route coverage for the Codex app-server
  fixture, adapter/protocol fake tests, and credential-safe live smoke. Verification remains pinned
  until closeout stamps the leaf commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: added governing route coverage for the Pi RPC
  protocol, subprocess, adapter, fixture, and isolated real-smoke regression files. Verification
  metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: added route-body coverage for the
  bridge conformance suite and its five changed serving regression files.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3 curator: added route coverage for the change-driven
  projection pacing regressions — new `test_change_watcher.py` (roots/filter/pacer/projector/real
  inotify) plus the `test_serving.py` `watch_changes=False` ETag fixture note and the
  `test_dashboard_daemon.py` heartbeat plumbing pins. Verification metadata remains pinned until
  closeout.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2 curator: added route coverage for the shared per-tick
  contract-snapshot regressions in `test_projection_scaling_cs6.py` (one enumeration/parse pass per
  tick, stat-identity cache with ctime hardening, output parity, live-set retention, failure retry).
  Verification metadata remains pinned until closeout.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 curator: added route coverage for walk-free contract loads
  and the explicit heal sweep (parity, idempotence, dry-run, error tolerance, CLI seam) in
  `test_leaf_ref_resolution.py`. Verification metadata remains pinned until closeout.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: added governing route coverage for the new
  inbox-reclamation regression suite and its final PASS delta tests, including event silence and
  corrected persisted removal semantics. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: added route coverage for bounded landing observation, no-wait projection, stale rendering, invalid-snapshot containment, and shutdown after observer failure.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
