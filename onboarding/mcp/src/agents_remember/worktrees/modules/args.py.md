# mcp/src/agents_remember/worktrees/modules/args.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/args.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T12:32+02:00     |
| lastVerifiedCommitHash | `7679eb76a4c3137f7a4a5e02e455e7759f9d9c19`                         |
| lastVerifiedCommitDate | 2026-07-04T12:58:55+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP controllers and the worktree CLI into the worktree domain functions.
`WorktreeArgs` replaces the loosely typed `argparse.Namespace` that previously
flowed across those layers (F17), giving every layer a single explicit field set
to read and write.

## Code Commentary

`WorktreeArgs` is a `@dataclass(frozen=True)`. Every field carries a default, so
any operation can construct just the subset it needs without supplying the rest;
fields are grouped by concern (coordination/repository resolution, start inputs,
provider setup, lifecycle flags, and closeout/integrate commit messages). The
frozen dataclass means callers that need a variant produce a new instance rather
than mutating an existing one.

`from_namespace` builds an instance from an `argparse.Namespace`, falling back to
the field defaults. It iterates the dataclass `fields`, copies only attributes
the namespace actually defines (`hasattr` guard), and applies them onto a default
instance via `replace`. This tolerates argparse subparsers that only populate the
arguments they declare and tests that construct partial namespaces, so any field
the namespace omits keeps its dataclass default rather than raising.

`retry_provider_setup: bool = False` (GitHub #53): on an existing contract,
worktree start relaunches background provider setup instead of attaching;
refused while a live setup heartbeat exists.

`stale_base_choice: str | None = None` (GitHub #54): the stale-base preflight
recovery selector for worktree start — `fast-forward` (ff stale local source
branches, then proceed) or `proceed-stale` (explicit override); `None` means
block when a source branch is behind/diverged from its upstream.

`memory_sync_choice: str | None = None` (GitHub #54 sub-task D): the
`worktree_sync` recovery selector when the memory work branch has local
commits and the official memory moved — `merge-memory` or `skip-memory`;
`None` blocks with `needs-review`.

`lifecycle_id: str = ""` (slice 2c): the observable-lifecycle id the controller
resolves (the active lifecycle's id, or a fresh mint when none is active) and
threads through to `_build_start_contract`, which stamps it into the contract's
`lifecycle:` block — the durable resume anchor.

`gate_policy: GatePolicy = DEFAULT_GATE_POLICY` (260703-L4) is the parsed
server-side gate delegation policy threaded from MCP config into worktree
closeout. Existing CLI/tests that omit it keep the all-human default.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup config is typed through the companion worktree models module. | [models.py](agents-remember/mcp/src/agents_remember/worktrees/modules/models.py) |
| Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. | [cli.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cli.py) |
| Gate delegation policy model. | [controlplane/gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |

## Series-Contract Notes

`WorktreeArgs` carries `parent_task` and `leaf_id` through CLI, MCP, and source API entrypoints, giving all operations the same active-task and leaf-selection inputs.

## Update History

- 2026-07-04T12:32+02:00 — 260703-L4: `WorktreeArgs` now carries
  `gate_policy`, defaulting to all-human, so closeout preview/apply consumes the
  trusted MCP gate delegation policy. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `WorktreeArgs` now includes `parent_task` and `leaf_id` so all worktree operations can resolve nested active task roots and specific leaf enclosures without filesystem paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: added `lifecycle_id: str = ""` (the observable-lifecycle enclosure anchor the controller resolves and `_build_start_contract` stamps into the contract). Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:56+02:00 — Added `memory_sync_choice: str | None = None` (GitHub #54 sub-task D worktree_sync recovery selector).
- 2026-06-10T09:30+02:00 — Added `stale_base_choice: str | None = None` (GitHub #54 stale-base preflight recovery selector).
- 2026-06-10T07:30+02:00 — Added `retry_provider_setup: bool = False` (GitHub #53): on an existing contract, worktree start relaunches background provider setup instead of attaching; refused while a live setup heartbeat exists.
- 2026-06-01T20:45+02:00 — `WorktreeArgs` gained `force` and `teardown_providers` for the abandon/cleanup teardown path.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
