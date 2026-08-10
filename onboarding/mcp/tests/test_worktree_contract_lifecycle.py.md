# test_worktree_contract_lifecycle.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_worktree_contract_lifecycle.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-01T14:20+02:00                                  |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`              |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Covers the slice-2c contract lifecycle anchor: `lifecycle_id` round-trips through
`contract_to_text` / `load_contract`, and a contract written before the field
existed (no `lifecycle:` section) loads with `lifecycle_id == ""`.

Since 260731-EFA-L5 it also covers the contract front matter's `schemaVersion` — the **same**
major/minor rule the control-plane JSONL records are read under, applied through the **same**
`schema_version_supported` helper.

## Code Commentary

### Logic

cit:([`ContractLifecycleAnchorTests`], mcp/tests/test_worktree_contract_lifecycle.py:51-81) build a contract through
`default_contract(ContractTask(...), leaf=LeafIdentity(worktree_name=..., lifecycle_id=...),
code=RepoBranchPlan(...))` over a `tempfile` coordination root and assert: the default id is
`""`; `contract_to_text` emits a `lifecycle:` / `id:` section; a `write_contract` →
`load_contract` round-trip preserves the id; and a contract with the `lifecycle:`
block stripped (mimicking a pre-2c contract) loads with `lifecycle_id == ""`
(backward compatibility). The anchor the suite drives is therefore
`LeafIdentity.lifecycle_id`, not a loose `default_contract` keyword.

cit:([`ContractSchemaVersionTests`], mcp/tests/test_worktree_contract_lifecycle.py:84-145) is the 260731-EFA-L5 addition (R6), six cases over one
rule. cit:([`_write_with_version`], mcp/tests/test_worktree_contract_lifecycle.py:99-110) writes a **real** contract through `contract_to_text` and
then rewrites just the `schemaVersion:` line — or deletes it — so each case differs from a valid
contract in exactly the field under test. The six: the written contract carries
`CONTRACT_SCHEMA_VERSION` at all; that version round-trips; an unknown
**major** raises `ContractError` whose message names both the version and the contract path
; an **unparseable** version (`draft`) is refused rather than assumed current; an unknown
**minor** of the supported major still loads, because a minor bump is additive; and a contract
written before the field existed still loads, because an absent version means 1.0 by definition
— which is why no migration is needed.

The class docstring states why the refusal matters more here than a missing cell would: the front
matter is flat `key: value` lines, so a contract from a future major still **parses**. Without the
check the tools would read every cell and answer questions about a document that means something
else.

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `ContractTask(memory_mode="disabled")`
keeps the fixture free of git/memory setup so the test is a pure contract round-trip; the
module-level `_contract(root, lifecycle_id)` helper is the single place the parameter objects
are assembled.

The version cases derive their inputs rather than hard-coding them:
`test_an_unknown_minor_is_additive_and_still_loads` builds `f"{CONTRACT_SCHEMA_VERSION.split('.')[0]}.99"`,
so it keeps testing "unknown minor of the *current* major" if the major is ever bumped, instead of
silently becoming an unknown-major case.

### Invariants And Boundaries

- One version policy, not two. `worktree_contract` imports `SCHEMA_VERSION` and
  `schema_version_supported` from `controlplane/durable_store.py`; if the contract ever grows its
  own copy of the rule, these tests and the durable-store contract tests stop agreeing about what
  a version means, which is precisely the drift the shared helper exists to prevent.
- An unknown major is refused, an unknown minor is accepted, an unparseable version is refused,
  and an absent version means 1.0. All four arms are asserted; removing any one leaves the policy
  half-specified.
- The refusal must name the contract path. An operator reading it needs to know *which* document
  the tools declined to interpret.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The contract module's lifecycle writer — the `lifecycle:` / `id:` block that `contract_to_text` renders. | `contract_to_text`; `"lifecycle:"`; `"  id: "` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |
| The lifecycle round-trip and pre-2c default behavior exercised by the suite. | `ContractLifecycleAnchorTests` | mcp/tests/test_worktree_contract_lifecycle.py:51-81 |
| The front-matter schema-version writer and the refusal the loader raises, including the exact message text the tests assert. | `contract_to_text`; `"unsupported series contract schemaVersion: "` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |
| The shared rule both artifacts are read under — rejects an unknown major, accepts an unknown minor, refuses an unparseable version. | `schema_version_supported` | mcp/src/agents_remember/controlplane/durable_store.py:224-245 |
| The same policy asserted on the JSONL record side, through the same helper, so the two cannot drift. | `SchemaVersionMajorTests` | mcp/tests/test_durable_store_contract.py:431-517 |

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 5 table citations and 10 prose citation repairs for lifecycle round-trips, schema-version writing/refusal, shared policy, and record-side tests; fixer-generated ranges verified.

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: this suite gained a class,
  cit:([`ContractSchemaVersionTests`], mcp/tests/test_worktree_contract_lifecycle.py:84-145), and the card gained a section for it. It is the
  worktree-contract half of R6: the front matter's `schemaVersion` is read through the **same**
  `schema_version_supported` helper as the control-plane JSONL records, deliberately one policy
  rather than two that drift, and the tests hold all four arms — unknown major refused with the
  version and the contract path in the message, unparseable version refused rather than assumed
  current, unknown minor accepted as additive, absent version treated as 1.0 so existing
  contracts load with no migration. Recorded the fixture technique that makes each case honest
  (`_write_with_version`, cit:([`_write_with_version`], mcp/tests/test_worktree_contract_lifecycle.py:99-110), writes a real contract through `contract_to_text` and rewrites
  or deletes only the `schemaVersion:` line, so a case differs from a valid contract in exactly
  the field under test) and the derived-input convention (`CONTRACT_SCHEMA_VERSION.split('.')[0]`
  keeps the unknown-minor case an unknown-minor case if the major is ever bumped). Recorded the
  class docstring's reason the refusal is load-bearing: the front matter is flat `key: value`
  lines, so a future-major contract still parses and would otherwise answer questions as though
  it meant what this build assumes. **Citations:** the card previously carried a single uncited
  row; it now carries exact anchors for the lifecycle renderer and the lifecycle round-trip tests,
  while the version row cites the writer and refusal message. The lifecycle behavior is covered by
  cit:([`contract_to_text`], mcp/src/agents_remember/worktrees/worktree_contract.py:689-740) and
  cit:([`ContractLifecycleAnchorTests`], mcp/tests/test_worktree_contract_lifecycle.py:51-81); the
  schema-version cases remain under cit:([`ContractSchemaVersionTests`], mcp/tests/test_worktree_contract_lifecycle.py:84-145).
  Added three invariants and a cross-link to
  cit:([`SchemaVersionMajorTests`], mcp/tests/test_durable_store_contract.py:431-517), which asserts the same rule on the record side. Also
  re-pointed `governingOverview` and the Governing Overview backlink from `../overview.md` to the
  route-local `overview.md`, which is the file that exists in this memory tree, and added the
  missing `## Governing Overview` section. The four pre-existing anchor assertions are unchanged.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. `default_contract`
  no longer takes a flat keyword list: the `_contract(...)` fixture now assembles
  `ContractTask(name/repo_name/coordination_root/workflow_kind/memory_mode)`,
  `leaf=LeafIdentity(worktree_name, lifecycle_id)`, and
  `code=RepoBranchPlan(repo_path, source_branch, work_branch, base_commit)`. Rewrote the Logic
  and Conventions paragraphs so they name the parameter objects and place the lifecycle anchor on
  `LeafIdentity.lifecycle_id` instead of describing a `default_contract(..., lifecycle_id=...)`
  keyword that no longer exists. The four assertions and the backward-compatibility case are
  unchanged.
- 2026-06-13T18:45+02:00: Created for slice 2c — contract lifecycle-anchor
  round-trip + backward-compatibility tests. Verification metadata is pinned until
  closeout stamps the 2c code commit.
