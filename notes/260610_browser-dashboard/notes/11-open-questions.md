# 11 — Open Questions And Truth Gaps

| Field | Value |
| --- | --- |
| Topic | Everything unresolved, in one place, so per-topic discussions can burn this list down |
| Status | Living list — strike items as topic discussions settle them; promote settled answers into the topic note + eventually task files |

## Architecture (notes 01/02/04)

1. ~~Lifecycle identity~~ **SETTLED 2026-06-10** (note 01): explicit
   `lifecycle_start/pause/resume/end` family, minted adjacent to
   `context_packet` (governance confirmed ⇒ start), end = task end, worktree =
   commitment boundary (lingers with the fixture), TTL auto-abandon otherwise.
   2026-06-11: a lifecycle represents *work*, not a repo — the contract
   enclosure is the identity anchor and may conceptually span multiple repos
   of one larger product (untested; don't design it out).
2. **Id propagation — mostly settled** (note 01, rounds 2–3): the model only
   sends signals (start/end/pause/resume/block/switch/phase); ids are
   system-managed — guarded start (start-while-active rejected with a
   reminder; no identifier), contract-driven resume, `switch_lifecycle` as the
   only id-carrying signal for pivots (save gate when leaving a fleeting
   lifecycle: offer worktree+notes+task-file promotion, else deliberate
   discard; auto-pause persistent / auto-end fleeting), TTL fleeting-only
   (~1h, missing signals; persistent never auto-reaped — dev steps in).
   Remaining: per-harness verification of session-scoped stdio server (ambient
   auto-tagging), blocked→running auto-unblock on gate approval,
   attach-vs-active-lifecycle precedence table, phase enum + field names
   (with 02).
3. ~~lifecycle vs session vs run~~ **SETTLED 2026-06-10:** lifecycle is the
   public primary, owned by MCP + contract; harness session is correlated, not
   causal (a lifecycle survives chat sessions); session id = provenance metadata.
4. **Reducer naming/placement:** `agents_remember.observer` producing
   "projections"? Decide the words before they fossilize.
5. **Event store layout:** per-lifecycle `events.jsonl` (#43) vs one workspace
   log vs both (truth per-lifecycle + derived workspace feed).
6. **Emit points:** `_tool_payload` choke point (observed) + skill-declared
   events (declared) — confirm the trust split and the minimum v1 event set
   (incl. the fleeting→persistent promotion event from the save gate, note 01).
7. **Retention:** what is forever-truth (ledger-like) vs rolling window; the
   observer branch's 1-day/250MB defaults are too small for trend charts.
8. **Gate return channel:** durable gate state + tool enforcement + agent
   polling as backbone (note 04 lean) — what poll affordance does the blocked
   agent get (existing tool? new `gate_status`? blocking long-poll is hostile to
   stdio)?
9. **3.0 scope line:** which breaking changes are *in* (tool params, response
   envelopes, contract v2) and what stays compatible? When does the version
   actually flip?
10. **Server placement:** dashboard/SSE server as part of the pip package
    (`agents-remember dashboard` command) vs separate repo/app. Affects packaging,
    release cadence, and how the static frontend ships.
11. **Security model:** localhost-only bind + no auth for v1? What happens the
    first time someone tunnels it?
12. **Multi-workspace:** one cockpit per coordination root, or aggregate? (Defer,
    but don't design it out.)
23. **Save-gate landing zones (design note 2026-06-11, note 01):** task roots
    are repo-grouped, but saved fleeting work is not always bound to one
    tangible repo (e.g. research across many pages) — give it a home in a
    `0_misc` task folder; multi-repo enclosure work likewise needs
    `1_inter-repo-work` so no save forces an arbitrary single-repo choice.
    Number prefixes sort both above the repo folders. Final names improvable;
    settle before the save gate is built. The persistence/sharing substrate
    for the task layer itself (tasks + worktree wrapper contracts in a neutral
    repo) is parked as backburner issue #79.

## Product (notes 05/06)

13. **Attention queue "Can we do this better?"** — mandated sub-task, parked
    until lifecycle/event/gate primitives exist (prerequisites in note 06).
14. **Read packet scope for observability:** facts-only event trail (note 05
    lean) — confirm; and does doctrine eventually discourage harness-native
    reads in managed repos?
15. **What does v1 ship?** Read-only first light over existing surfaces vs
    waiting for lifecycle/events. (Note 03 suggests the read-only slice keeps
    the visual track unblocked — but confirm against the "no pretty toy" bar:
    is read-only v1 acceptable as a *milestone* if interaction is v2?)

## Verification debts (cheap to clear, do before task definition)

16. **2.8.0 delta:** recon inventoried 2.7.0 @ `ab7e21b`; #54's fix + new
    `worktree_sync` tool landed since. Re-run the surface inventory delta
    (tool list, any new files/contracts) before designing against it.
17. ~~Red-pen annotations~~ **RESOLVED 2026-06-10:** they were the developer's
    mid-iteration *directions to the Open Design agent* (the pivot→queue arrow
    produced the combined Attention / By repo / By lifecycle panel), already
    absorbed into mc2 — the designated endpoint. No pending feedback content.
18. **`logs/mcp/` transcripts:** confirmed empty — is there a config flag that
    populates it today, or is transcript capture genuinely unimplemented?
19. **#43 session-id model vs observer-branch correlation model:** reconcile the
    two vocabularies explicitly when drafting the event schema (note 02).
20. **Issue states:** re-check #54 (should be closeable/closed now) and whether
    the other chat's landing changed any worktree_start response shapes the
    boot-sequence design depends on (`setup-progress.json` contract).

## Spawned follow-ups (decisions made here that need their own work)

22. **Worktree-only closeout alignment — TASK CREATED 2026-06-10 (planning):**
    `tasks/agents-remember/260610_worktree-only-closeout-alignment/task.md`.
    Clarified: worktree-only was the *original* design intent of the lifecycle
    skill; `direct_closeout_*` is leftover from an incomplete cleanup. The task
    carries the full removal plan (tools, l-01/c-12, docs, sync) + two rulings
    it needs from the developer: memory-only edits (worktree too?) and release
    placement (standalone vs 3.0). Prerequisite alignment, separate from the
    dashboard series.

## Meta

21. **Task decomposition:** when notes 01–09 are individually discussed, the
    likely task series shape is: (i) lifecycle entity + event contract design,
    (ii) emission + reducer/projection, (iii) serving layer (SSE) + read-only
    cockpit v1, (iv) gate tools + interaction v2, (v) read packet, (vi) visual
    polish/boot/audio, (vii) attention-queue challenge. Validate this cut when
    the per-topic discussions land — do not pre-commit.
