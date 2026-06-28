# test_read_ar_files.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_read_ar_files.py`                  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-22T22:33+02:00                             |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_read_ar_files.py` is the slice-07 test suite for the `read_ar_files` tool:
it pins the ranged-read helper, the controller's onboarding/status semantics and
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
- `ControllerStatusTests` drives a directly-constructed `CoordinationContext`
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

| Finding | Source Path |
| --- | --- |
| The controller under test. | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The payload builder driven end-to-end. | [mcp/tools/read_files.py](agents-remember/mcp/src/agents_remember/mcp/tools/read_files.py) |
| The net-new ranged reader unit-tested here. | [kernel/filesystem.py](agents-remember/mcp/src/agents_remember/kernel/filesystem.py) |
| The served-ledger store asserted on disk. | [observer/served_store.py](agents-remember/mcp/src/agents_remember/observer/served_store.py) |
| The ambient lifecycle whose `emit_read_packet` + served set are exercised. | [observer/ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| Shared config/settings test helpers. | [test_config.py](agents-remember/mcp/tests/test_config.py) |

## Update History

- 2026-06-23T01:40+02:00 — Slice 07b v1: the emission test now also asserts the `read.packet`'s `data.repoId == REPO` (the read's repo carried alongside the per-file facts). Body only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07: the `read_ar_files` test suite (ranged read, status semantics, path-confinement, facts-only `read.packet`, served-ledger dedup/reset, five-file cap + payload end-to-end). Verification metadata pinned until closeout stamps the slice-07 code commit.
