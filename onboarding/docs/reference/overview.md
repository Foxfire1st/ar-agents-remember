# docs/reference

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | docs/reference |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-16T07:27+02:00 |
| lastVerifiedCommitHash | `d99a1a7f3ac251957ae155ea9beb878b9ba1ab25`|
| lastVerifiedCommitDate | 2026-07-16T07:36:40+02:00|

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

## Update History
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
