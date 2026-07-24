# docs/reference

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | docs/reference |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-24T14:44Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|

## Purpose

Reference contract for harnesses, MCP tools, and settings. ACPUI makes role settings the initial
native-selection authority: Claude, Codex, and Pi discover token-free per-install/account catalogs,
validate effort under the selected model, launch through adapter-owned native channels, and retain
honest same-session mutation evidence. The harness manual now keeps Claude's three startup evidence
sources distinct: correlated initialize supplies command rows, `system/init` supplies live session
state, and a separate correlated `list_models` response supplies the dynamic catalog and model-local
effort metadata. Settings-defined non-native harness mappings remain an explicit compatibility
surface rather than the default path. The route also retains the three-state hosted dispatch,
readiness, catalog-concurrency, and serving-cutover contracts.

## Hot Path Summary

For native launch and control questions, read `harnesses.md` for the dynamic catalog,
model-gated effort, duplicate-selector refusal, distinct Claude startup evidence sources, and the
Claude/Codex/Pi launch/set matrix; read `settings-json.md` for the complete `roles.<role>` /
`rolesPerLevel` model-and-effort authority. Exact harness versions and captured catalog rows are
live/fixture evidence, not production pins; in particular, Claude Code 2.1.210 live-confirmed Fable
switching supersedes the earlier launch-only assumption without creating a Fable-name policy.
Structured hosted dispatch, complete serving reload, and the bounded R9 compatibility exception
remain separate contracts.

For commit-gate and closeout questions, `mcp-tools.md` is the public tool-surface
reference, `worktrees-c09.md` owns the quality-before-commit sequence, and
`skills.md` records that synchronized skill copies are checked at both
pre-commit and pre-push.

## 260718-CHATS-L5I Commit-Gate Reference Impact

The public reference route now exposes the same mandatory source-quality order
as the implementation and runtime guidance. `worktree_closeout_apply` runs the
strict project-owned wrapper before an Agents Remember source commit;
`worktrees-c09.md` places that gate before code, onboarding, memory, and ledger
commit steps; and the skills reference names both pre-commit and pre-push sync
checks. These are documentation projections of the existing gate authority, not
independent bypasses or alternative check sequences.

## Update History
- 2026-07-24T14:44Z — 260718-CHATS-L5I preview-gate remediation: refreshed the
  route body for the public MCP closeout description, strict
  quality-before-commit worktree order, and pre-commit/pre-push skill-sync
  checks. Verification metadata remains pinned until the code commit.

- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: aligned the reference route with the final
  three-source Claude startup contract, live native advertise/launch/set evidence, dynamic Fable
  switching, and the rule that captured versions/catalog rows remain evidence rather than pins.
- 2026-07-15T23:31+02:00 — 260714-ACPUI-L2 closeout-preview delta: replaced the stale static
  registry/session-command launch summary with settings-owned complete selection, token-free
  per-install catalogs, model-local effort validation, native Claude/Codex/Pi launch channels, and
  honest startup evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the reference route body for the
  negotiated capability model, full reload ownership, and deferred R10 boundary.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the reference route for structured harness
  capability negotiation, full serving reload ownership, and the deferred R10 boundary.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: refreshed the reference route body for
  the final harness effort policy and explicit control-bridge boundary.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
