# test_read_ar_files.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_read_ar_files.py`                  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-02T01:05+02:00                             |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_read_ar_files.py` is the slice-07 test suite for the `read_ar_files` tool:
it pins the ranged-read helper, the application entry point's onboarding/status semantics and
path-confinement boundary, the auto-attached front-door dedup, the served-ledger
durability, and the facts-only `read.packet`.

## Code Commentary

### Logic

Five `unittest.TestCase` classes, plus fixture helpers that write a real
`overview.index.json`, real sidecar markdown, and real overviews (the route-index
and storage machinery are consumed, not re-implemented):

- `RangedReadTests` unit-tests `filesystem.read_text_range`: full read via
  `read_text`, an inclusive `[start, end]` slice, a single-line range, `end`
  clamped to EOF, `start` beyond EOF → empty, and an inverted range → empty.
- `ApplicationStatusTests` drives a directly-constructed `CoordinationContext`
  (`_context` seam) per storage mode to isolate status: `found` when the sidecar
  is present and covered; `missing` (no probe) when in-scope but uncovered;
  out-of-scope at the nearest index deferring to a more-general index without a
  probe; the no-index fallback to a mirror-path probe (found vs missing);
  `disabled`; `inline` → `unsupported`; `external` treated as sidecar;
  `not_requested` when `onboarding: false`. It also pins source independence — an
  exact range slice, a full read that is **not** truncated (a >4 KB file returned
  byte-for-byte), an absent file and a binary file both omitting `source` — and
  the input-validation rejections (inverted range, zero `endLine`). The
  path-confinement boundary gets its own block: a `../` escape, an absolute path,
  a symlinked file escaping the repo, a symlinked directory escaping via a child
  path, and a mid-path `..` that climbs out are each rejected with `AuthorityError`
  (resolution happens before the check, so it is the real path, not a literal
  token, that is judged).
- `FrontDoorDedupTests` installs an ambient lifecycle over a temp `EventStore` and
  pins the per-lifecycle dedup: the first read attaches the repo overview + the
  governing route chain; a second unchanged read omits both; a changed repo
  overview is re-served while the unchanged route overviews stay deduped;
  `refresh=true` forces a re-serve; and writing the `compact-reset.json` marker
  re-serves and consumes the marker exactly once.
- `ServedLedgerAndEventTests` pins the on-disk ledger and the event: a read writes
  the `served_key("repository_overview", "overview.md", <hash>)` into the
  lifecycle's `served.jsonl`; the emitted `read.packet` is `observed`, carries
  `data.repoId == REPO` (slice 07b — the read's repo) plus per-file
  `{path, lines, status, bytes}` and *nothing else* (the assertion checks the exact
  per-file key set and that the serialized event contains no source/onboarding
  content), records `"full"` for a full read, and projects out a stray smuggled
  `source`/`onboarding` key — proving the privacy invariant is structural in
  `emit_read_packet`, not caller-dependent.
- `FiveFileCapAndPayloadTests` runs end-to-end through the real resolver + the
  `read_ar_files_payload` builder + the token choke point: six files are rejected,
  five accepted (with `tokens` / `tokenCountExact` stamped by the choke point), and
  committed source is read back verbatim.

### Conventions

Fixtures build a real `McpRuntimeConfig` (via `test_config.settings_payload`) whose
coordination root anchors `observer_root` and the reset marker, and reset the
ambient singleton (`reset_ambient`) in setUp/tearDown for isolation. The
helper-written sidecars and overviews exercise the route-index chain and
`meaningful_body` extraction (the test asserts the seeded `## Update History` is
stripped from the served body).

### Invariants And Boundaries

- The route-index and storage machinery are consumed, not re-implemented — the
  fixtures write real index/sidecar/overview files.
- The `read.packet` privacy guarantee is asserted structurally: no content key may
  appear in the serialized event regardless of what the caller passes.
- Source presence is asserted independent of onboarding status.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point under test. | `read_ar_files_tool` | mcp/src/agents_remember/application/read_files.py:77-133 |
| The payload builder driven end-to-end. | `read_ar_files_payload` | mcp/src/agents_remember/mcp/tools/read_files.py:13-22 |
| The net-new ranged reader unit-tested here. | `read_text_range` | mcp/src/agents_remember/kernel/filesystem.py:44-62 |
| The served-ledger store asserted on disk. | "self._root / \"lifecycles\" / lifecycle_id / \"served.jsonl\"" | mcp/src/agents_remember/observer/served_store.py:90-90 |
| The ambient lifecycle whose `emit_read_packet` + served set are exercised. | `emit_read_packet` | mcp/src/agents_remember/observer/ambient.py:395-422 |
| Shared config/settings test helpers. | "\"coordinationRoot\": str(coordination_root)" | mcp/tests/test_config.py:34-34 |

## Update History

- 2026-08-02T21:32+02:00 — W2-B08 curator: anchored 10 citation findings to the application entry point, payload builder, ranged reader, served ledger, and config helper evidence. Verification metadata stays pinned until closeout.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — No content impact: the only non-format edit is the ambient-lifecycle
  construction in the `FrontDoorDedupTests` and `ServedLedgerAndEventTests` fixtures, which now
  passes `timing=AmbientTiming(heartbeat_seconds=3600)` instead of the loose `heartbeat_seconds`
  keyword; the card names neither the keyword nor the heartbeat value, and both fixtures still
  install a real ambient lifecycle over a temp `EventStore` and reset the singleton around each
  case. The rest is `ruff format` reflow of `_write_route_index`, the two `_read` helpers, and one
  trailing comma. Re-checked the five test classes and every enumerated case against the source:
  none was added, removed, renamed, or re-asserted, so the status-semantics, path-confinement,
  dedup, served-ledger, facts-only `read.packet`, and five-file-cap claims all still hold.
- 2026-06-23T01:40+02:00 — Slice 07b v1: the emission test now also asserts the `read.packet`'s `data.repoId == REPO` (the read's repo carried alongside the per-file facts). Body only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07: the `read_ar_files` test suite (ranged read, status semantics, path-confinement, facts-only `read.packet`, served-ledger dedup/reset, five-file cap + payload end-to-end). Verification metadata pinned until closeout stamps the slice-07 code commit.
