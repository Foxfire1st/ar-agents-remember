# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:20:31+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` (synced onto L14's landing) |
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-17T10:20 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Declares shared test-support/fixture ownership, fidelity, lifetime, replacement contracts, and
exact consumers. The catalog currently contains **54 artifact records** and four executable replacement
contracts; those declarations are not records that a test ran. 260915-CAPS-L9 adds **two consumer
rows and no artifact row**: `mcp/tests/test_capsule_experiment_install.py` and
`mcp/tests/test_install_runtime.py` join the `mcp/tests/fixtures/repository_profiles/node/package-lock.json`
artifact's `consumers` list, because the new module reads the pinned application's committed
lockfile through the installer it drives and `test_install_runtime.py` inherits the same reach
through the module it imports. The artifact set has moved since (L14 and L17 land into the same
file, and the merged pin is re-derived on the merged catalog — never restored from another
leaf's figure).

The count is re-derived from the file rather than carried: it stood at 43 when an earlier version of
this paragraph was written, measures **50 at this leaf's synced base `23cc7a72`**, and measures 51 with
this leaf's one added row.

## Code Commentary

### Logic

Contract records bind a production owner to a retained executable node. Artifact records describe
category, authority, fidelity, cadence, source/generator provenance, lifetime and permanence/expiry
rationale, replacement evidence, and consumers. `large_fixture_bytes=25000` remains the catalog's
large-fixture discovery setting.

The closeout fixture and closeout-input support records now name
`test_public_closeout_commits_code_and_memory_without_acceptance_tools` as their replacement node.
That matches the current two-output transaction behavior and does not require a ledger publication.
The closeout-input and curator-coherence support records also declare
`test_post_integration_cleanup_guidance.py` as an exact consumer.

Other artifact categories and ownership declarations retain their own scopes. Consumer rows are
accounting for source-observed support use, including transitive use where declared; they do not
establish acceptance, installed-executor fidelity, or a production run.

**260915-CAPS-L15 added consumer rows only, and that is what moved the byte pin.** The new
`mcp/tests/test_capsule_launch_wiring.py` reaches three governed artifacts through the shared test
support it imports, so three `consumers` lists gained one entry each
(`mcp/tests/evidence-lifecycle.toml:351`, `:624`, `:1257`) — the same shape 260915-CAPS-L7 used. **No
artifact was registered, no row was removed, and no artifact's identity moved**: the populations are
unchanged at **4 contracts / 51 artifacts**, while the byte pin in
`mcp/tests/test_dependency_ownership_ast_helpers.py` moved `812211e9… → 3342a249…` because the file's
bytes changed. A consumer row is a catalog change; the pin is re-derived from the file, never maintained
by hand.

**`consumers` is a derived test population, and the loader enforces it.** For `consumer_scope = "exact"`
the loader re-derives the test modules that reach the artifact from the source graph and reports any
difference from the declared list, so a row's `consumers` cell is a checkable claim rather than prose.
The eve capsule row added by this leaf lists exactly the four test modules the loader derives for it —
one of which reaches the support only **transitively** through another support module. That transitivity
is why a row's `consumers` and its `permanence_rationale` can describe different things without either
being wrong: the list is the mechanical test population, the rationale is the artifact's semantic role.

Because the rows are derived from the graph, they are also what a base move invalidates. The merge that
produced this leaf's base re-derived every catalog consumer proof it touched, and **verifying that
re-derivation is a separate leaf's obligation**; a row that disagrees with the graph is a loader finding
to be repaired by its owner, not a tolerated inconsistency.

### Conventions

The catalog is a policy/configuration input and is not counted as an artifact inside itself.
Fidelity, lifetime, and test grouping answer different questions. Current source declarations
supersede historical per-leaf consumer positions and population counts retained below.

### Invariants And Boundaries

- Replacement node references must name the retained real test definition.
- Exact consumer declarations must correspond to actual support use; stale counts are not authority.
- Registry consistency and permanent-support rationale do not claim execution or certification.
- Ledger retirement changes the closeout replacement node, not unrelated artifact ownership.
- **A consumer row is a catalog change.** Adding an importer to a `consumers` list moves the file's
  bytes and therefore the pin in `test_dependency_ownership_ast_helpers.py`, even when no artifact is
  registered or removed. The pin is re-derived at the changing leaf's own tip.
- **Consumer rows are accounting, never acceptance.** A row states that a test module reaches a
  support artifact; it does not claim the artifact's fidelity, that a test ran, or that a boundary was
  exercised in production.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| None | "ar-test-evidence-lifecycle/v3"; "large_fixture_bytes = 25000" | mcp/tests/evidence-lifecycle.toml:1-2 |
| None | "mcp/tests/closeout_fixture_test_support.py" | mcp/tests/evidence-lifecycle.toml:265-276 |
| Closeout-input support names the same retained code/memory transaction replacement node. | "mcp/tests/closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:283-294 |
| None | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/test_post_integration_cleanup_guidance.py" | mcp/tests/evidence-lifecycle.toml:330-373 |
| None | `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## 260915-CAPS-L9 Consumer Rows

The two added rows state reach that is real rather than decorative: the experiment module installs
and probes the pinned application by reading `package.json` and `package-lock.json`, and the
pre-existing `test_install_runtime.py` inherits the reach because it imports the installer module
that now does. Nothing was registered, no row was removed, and the populations are unchanged by
this leaf apart from its own two consumers. The byte pin over this file is re-derived **at this
leaf's tip** by the runbook recipe (`31c6983d…`, 4 contracts / 54 artifacts at the merged tip)
and never restored from a historical figure.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **consumer rows only** — `mcp/tests/test_capsule_experiment_install.py`
  and `mcp/tests/test_install_runtime.py` join the
  `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact's `consumers` list, because the
  new module reads the pinned application's committed lockfile through the installer it drives and the
  pre-existing `test_install_runtime.py` inherits the same reach through the module it imports. Nothing was
  registered and no row was removed; the catalog's population delta on this leaf's own branch is zero rows
  at the artifact level. The byte pin over this file is re-derived at this leaf's tip (`31c6983d…`,
  4 contracts / 54 artifacts on the merged catalog) and never restored from a historical figure. The
  section above records what the two rows mean rather than only that they exist. Verification metadata
  remains closeout-owned: the candidate is uncommitted.
- 2026-09-17T10:50+02:00 — 260915-CAPS-L15 curator: **consumer rows only, and the byte pin moved for
  that alone.** This leaf's new acceptance module reaches three governed artifacts through the shared
  test support it imports, so three `consumers` lists each gained one entry; nothing was registered,
  removed or re-identified, and the populations stayed at 4 contracts / 51 artifacts while the pin went
  `812211e9… → 3342a249…`. The body states that shape and adds two invariants — a consumer row is a
  catalog change, and consumer rows are accounting rather than acceptance. Verification metadata moves
  to this leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout
  stamps the real code commit and no hash or fingerprint was invented here.


- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: **consumer rows only again, and the pin re-derived
  against the MERGED catalog — which is this leaf's own obligation.** The leaf's new test module
  `mcp/tests/test_eve_effort_runtime.py` starts the shipped runtime, so it consumes three
  already-governed artifacts and each `consumers` list gained one entry:
  `mcp/tests/fixtures/repository_profiles/node/package-lock.json` (L649),
  `mcp/tests/eve_capsule_test_support.py` (L736) and `mcp/tests/test_eve_adapter_test_support.py`
  (L1186). **Nothing was registered, no row was removed and no artifact's identity moved**, so the
  populations stay at **4 contracts / 51 artifacts**. The pin is **`563582a0…`**, and it is neither
  L15's `3342a249…` nor the `22ce7027…` this leaf measured before L15 landed: L15 landed first, so this
  value covers the **merged** artifact set. Re-derived and independently recomputed this pass —
  `sha256sum mcp/tests/evidence-lifecycle.toml` = `563582a0542f4a8721d1f717a48e92440c53fdf63a26b68fb43624c56ad90506`,
  matching the constant at `mcp/tests/test_dependency_ownership_ast_helpers.py:46` (counts 51 / 4 at
  `:44-:45`). The card's Purpose sentence attributing 51 to "this leaf's one added row" describes the
  L15 pass and is left as history; **the value, not the sentence, is the claim**, and the rule that a
  consumer row is a catalog change is what makes this re-derivation mandatory at each changing leaf.
  **Checker result (post-sync, verbatim).** The refusal this entry first recorded was resolved
  by the leaf's `worktree_sync`: the pair is now `leaf-candidate` / `acceptanceEligible:true` on
  code base `d8ed8c21`, and the contract-scoped `memory_quality_check` ran against this
  worktree. Headline: `ok:false`, `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `onboarding_drift_drifted` finding and one
  `style.update_history.history_order` "not newest-first" finding, the latter caused by the
  future-dated `10:50` stamp on the L15 entry below this one and not by this entry's content
  (see the `serving/overview.md` entry for the same attribution). The pin above was additionally
  recomputed directly and independently — it is `e3651d6f…` at **4 contracts / 54 artifacts**
  after L14 landed its fifty-fourth artifact, not the `563582a0…` this leaf measured pre-sync at
  51. Verification metadata moves to the synced base `d8ed8c21`; the candidate is deliberately
  uncommitted, so the governed closeout stamps the real code commit and no hash or fingerprint
  was invented here.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **one artifact row added, one shared-support row
  extended, population re-measured.** The leaf's new `mcp/tests/eve_capsule_test_support.py` is
  registered as `shared-support` / `unit-regression`, owned by
  `mcp/src/agents_remember/application/eve_capsule/__init__.py`, with `consumer_scope = "exact"` and
  exactly the four consumers the loader derives for it; the two new L7 suites were added as exact
  consumers of the existing `mcp/tests/test_eve_adapter.py`-adjacent shared-support row. The declared
  population is corrected in the Purpose paragraph: **51 artifacts** at the candidate, of which 50 are
  the synced base `23cc7a72` and one is this leaf's — the previous 43 was stale and is now stated with
  the measurement it came from rather than silently replaced. A new paragraph records that `consumers`
  is a graph-derived population the loader enforces, which is why a transitively-derived consumer can
  appear in a list whose rationale describes a different role, and that verifying the merge's
  re-derivation of every touched consumer proof belongs to a separate leaf. Verification metadata moves
  to the leaf's synced base `23cc7a72`; the candidate is deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-15T01:02 UTC — Updated the documented replacement-node spelling for code/memory-only closeout and the two cleanup-guidance consumer declarations; retained registry ownership/fidelity/lifetime semantics and separated them from execution evidence. Working candidate verified by source inspection; commit metadata records real committed history only.

### Preserved earlier registry notes

The following earlier-card notes retain their historical scope. Their uses of “current”, counts, and source-line positions describe those earlier passes; the working-source references above supersede them.

### CCR-L42 current candidate

The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

### 260831-LOCR-L32 Three Consumer Rows

The leaf's new `mcp/tests/test_worktree_status_terminal_next_tool.py` was added as an exact
consumer of three existing shared-support artifacts — no artifact row was added, removed or
re-categorised, so the catalog's population is unchanged:

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:336` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:395` |
| `mcp/tests/lifecycle_enclosure_test_support.py` | `publish_test_enclosure` — the suite's terminal-archive fixture is a real published enclosure | `mcp/tests/evidence-lifecycle.toml:471` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
The L4 producer-census insertion shifted all three rows by one line (from `:330`/`:383`/`:461`), and this
card names the current positions.

### 260831-LOCR-L34 Two More Consumer Rows

The leaf's new `mcp/tests/test_checkpoint_landing_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts the L32 suite consumes, again through `QueueFixture`'s transitive
composition. No artifact row was added, removed or re-categorised, so the declared population is
unchanged; the insertion did shift the later consumer rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:305` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:364` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
The L4 producer-census insertion moved all of these rows by one line: the L32 rows now resolve at `:334`,
`:391` and `:467`, the L34 rows at `:304` and `:361`, and this card names the current positions. The L32
rows' own shift history is recorded in the L32 section above.

### 260831-LOCR-L37 Two More Consumer Rows

The leaf's new `mcp/tests/test_pause_stop_only_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts every other `QueueFixture`-based boundary suite consumes, reached
transitively through that fixture's composition. No artifact row was added, removed or re-categorised,
so the declared population is unchanged; the insertion did shift the later consumer rows, which are
re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:322` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:380` |

The leaf's other new module, `mcp/tests/test_pause_is_not_publication.py`, is deliberately **not** a
consumer of any artifact here: it parses the source tree with `ast` and resolves module paths, so it
composes no fixture and installs no support. Consumer declarations are ownership accounting only; they
are not execution or acceptance evidence.

The L4 producer-census insertion moved these two rows by one line (from `:319` and `:376`), and this
card's references now name the current lines. The L36 rows moved with the earlier insertions
(`closeout_input_test_support.py` artifact row resolves at `:283` unchanged, `curator_coherence_test_support.py` at `:340`, the
`lifecycle_enclosure_test_support.py` artifact row at `:452` with the L32 suite's consumer entry at
`:467`), and this card's references now name the current lines.

### 260831-LOCR Seal Removal — Two More Consumer Rows

The change set's new `mcp/tests/test_lifecycle_playthrough_end_to_end.py` was added as an exact
consumer of the same two shared-support artifacts every other `QueueFixture`-based boundary suite
consumes, reached transitively through that fixture's composition. No artifact row was added, removed
or re-categorised, so the declared population is unchanged; the insertion did shift the later consumer
rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:322` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:375` |

The L4 producer-census insertion did **not** move these two rows: it was added after them in both lists,
so their positions are unchanged. Consumer
declarations are ownership accounting only; they are not execution or acceptance evidence.

### 260913-LCA-L4 Two More Consumer Rows

The leaf's new `mcp/tests/test_memory_attribution_producers.py` was added as an exact consumer of two
existing shared-support artifacts, both reached transitively through the `QueueFixture` composition its
carryover case builds. No artifact row was added, removed or re-categorised, so the declared population
stays 42 shared-support artifacts and four executable replacement contracts:

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_fixture_test_support.py` | transitive closeout/lifecycle fixture composition the carryover case's `QueueFixture` relies on | `mcp/tests/evidence-lifecycle.toml:319` |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition, same fixture | `mcp/tests/evidence-lifecycle.toml:378` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.

### 260913-LCA-L5 Two More Consumer Rows

The leaf's new `mcp/tests/test_leaf_doc_master_link_binding.py` was added as an exact consumer of the
same two shared-support artifacts, reached transitively through `test_worktree_support` —
`initialized_memory_repo` imports both. No artifact row was added, removed or re-categorised, so the
declared population stays 42 shared-support artifacts and four executable replacement contracts
(measured: 42 `[[artifact]]` and 4 `[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition `test_worktree_support` imports | `mcp/tests/evidence-lifecycle.toml:316` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same import | `mcp/tests/evidence-lifecycle.toml:375` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Two insertions — one in each consumer list — shift everything after them, so the current positions,
measured by line number in the current file, are: the closeout-input `path` cell `:283` (unchanged) with
its block now `282-338`, the curator-coherence `path` cell `:341` with its block now `340-396`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:454`. The earlier per-leaf sections above record
their own as-of positions and should be read that way; the reference table above names the current ones.

### 260913-LCA-L7 Two More Consumer Rows

The leaf's new `mcp/tests/test_closeout_projection_source_classification.py` was added as an exact
consumer of the same two shared-support artifacts every other closeout boundary suite consumes. The
module imports `QueueFixture`, `REPO` and `SPRINT` from the sibling `test_closeout_queue` fixture
rather than rebuilding the world, and that fixture's own imports carry both supports —
`curator_coherence_test_support` directly and `closeout_input_test_support` through
`test_worktree_support`, whose `initialized_memory_repo` imports it. No artifact row was added, removed
or re-categorised, so the declared population is unchanged (measured: 42 `[[artifact]]` and 4
`[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the shared `QueueFixture` relies on | `mcp/tests/evidence-lifecycle.toml:307` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same fixture | `mcp/tests/evidence-lifecycle.toml:366` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Two insertions — one in each consumer list — shift everything after them, so the current positions,
measured by line number in the current file, are: the closeout-input `path` cell `:283` (unchanged) with
its block now `282-339`, the curator-coherence `path` cell `:342` with its block now `341-398`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:456`. Every later row moved by one line: the L5
entries `:315` → `:316` and `:373` → `:375`; the L4 census `:318` → `:319` and `:376` → `:378`; the
playthrough `:317` → `:318` and `:376` → `:377`; the pause suite `:321` → `:322` and `:380` → `:381`;
the L32 suite `:335` → `:336`, `:394` → `:395` and `:470` → `:471`; the L36 suite `:308` → `:309` and
`:367` → `:368`; and the L34 suite `:304` → `:305` and `:363` → `:364`. The earlier per-leaf sections
above record their own as-of positions and should be read that way; the reference table above names the
current ones.

### 260913-LCA-L8 Nine More Consumer Rows

The leaf's new `mcp/tests/test_terminal_blocker_reasons.py` was added as an exact consumer of nine
existing shared-support artifacts. No artifact row was added, removed or re-categorised, so the
declared population stays 42 shared-support artifacts and four executable replacement contracts
(measured: 42 `[[artifact]]` and 4 `[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | imported directly by `integration_branch_authority_test_support`, whose landing fixture builds the whole-tool world | `mcp/tests/evidence-lifecycle.toml:331` |
| `mcp/tests/curator_coherence_test_support.py` | reached through `selected_lifecycle_test_support`, whose closeout-operation input composes it | `mcp/tests/evidence-lifecycle.toml:391` |
| `mcp/tests/integration_branch_authority_test_support.py` | imported directly: `_authority_fixture` and `_closed_external_leaf_worktrees` build the real landed leaf each whole-tool case starts from | `mcp/tests/evidence-lifecycle.toml:435` |
| `mcp/tests/repository_profile_test_support.py` | imported directly by the landing fixture (`AGENTS_REMEMBER_PROFILE_REFERENCE`) | `mcp/tests/evidence-lifecycle.toml:565` |
| `mcp/tests/fixtures/repository_profiles/node/package.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:604` |
| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:643` |
| `mcp/tests/gate_certification_test_support.py` | reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint` | `mcp/tests/evidence-lifecycle.toml:955` |
| `mcp/tests/source_selection_test_support.py` | reached through `repository_profile_test_support`, which imports `source_selection_fixture` | `mcp/tests/evidence-lifecycle.toml:1012` |
| `mcp/tests/selected_lifecycle_test_support.py` | imported directly by the landing fixture (`selected_closeout_operation_input`) | `mcp/tests/evidence-lifecycle.toml:1038` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Each insertion shifts everything after it, so the current positions, measured by line number in the
current file, are: the closeout-input `path` cell `:283` (unchanged) with its block now `282-341`, the
curator-coherence `path` cell `:343` with its block now `342-401`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:459`. Every later row moved: the L5 entries
`:316` → `:315` and `:375` → `:375` (up one and unchanged — `test_cross_master_concurrency.py` moved
after it in the same list); the L4 census `:319` → `:320` and `:378` → `:380`; the playthrough
`:318` → `:318` and `:377` → `:378`; the pause suite `:322` → `:322` and `:381` → `:382`; the L32 suite
`:336` → `:337`, `:395` → `:397` and `:471` → `:474`; the L36 suite `:309` → `:312` and `:368` →
`:372`; the L7 suite `:307` → `:307` and `:366` → `:367`; and the L34 suite `:304` → `:304` and
`:364` → `:364` (unchanged). The earlier per-leaf sections above record their own as-of positions and
should be read that way; the reference table above names the current ones.




- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the frozen catalog gained
  the `checkpoint_landing_test_support.py` artifact, so the declared population is 43
  shared-support/fixture artifacts plus four replacement contracts. Corrected the Purpose population
  count; the artifact blocks and every cited row were re-read. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the leaf's new `mcp/tests/test_terminal_blocker_reasons.py` as an exact consumer of nine
  existing shared-support artifacts — `closeout_input_test_support.py` (`:331`),
  `curator_coherence_test_support.py` (`:391`), `integration_branch_authority_test_support.py`
  (`:435`), `repository_profile_test_support.py` (`:565`), the two `repository_profiles/node` fixture
  files (`:604`, `:643`), `gate_certification_test_support.py` (`:955`),
  `source_selection_test_support.py` (`:1012`) and `selected_lifecycle_test_support.py` (`:1038`) —
  the first two through the shared closeout/worktree fixture composition and the landing/authority
  fixture, the rest through the repository-authority and certification-profile composition the landed
  fixture carries. No artifact row was added, removed or re-categorised, so the declared population is
  unchanged (measured: 42 `[[artifact]]`, 4 `[[contract]]`). Re-derived every position this card
  cites against the current file: the closeout-input `path` cell stays `:283` with its block
  `282-341`, the curator-coherence `path` cell is `:343` with its block `342-401`, and
  `lifecycle_enclosure_test_support.py` is `:459`; among consumer rows the L5 suite is
  `:315`/`:375`, the L4 census `:320`/`:380`, the playthrough `:318`/`:378`, the pause suite
  `:322`/`:382`, the L7 suite `:307`/`:367`, the L32 suite `:337`/`:397`/`:474` and the L36 suite
  `:312`/`:372`. Corrected the reference rows that named pre-insertion values (the two artifact block
  ranges `282-339`/`341-398` → `282-341`/`342-401`, the curator-coherence `path` cell `:341` → `:343`,
  the enclosure fixture `:456` → `:459`, the L32/L34/L37/L5/L4/playthrough/L36/L7 consumer entries)
  and added the row for the nine new consumer edges. Verification metadata is **not** advanced: the
  code commit does not exist and closeout owns the stamp; no acceptance claim.
- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the leaf's new `mcp/tests/test_closeout_projection_source_classification.py` as an exact
  consumer of `closeout_input_test_support.py` (row 307) and `curator_coherence_test_support.py` (row
  366), both reached transitively through the sibling `test_closeout_queue` fixture it imports its
  world from. No artifact row was added, removed or re-categorised, so the declared population is
  unchanged (measured: 42 `[[artifact]]`, 4 `[[contract]]`). Re-derived every position this card cites
  against the current file: the closeout-input `path` cell stays `:283` with its block `282-339`, the
  curator-coherence `path` cell is `:342` with its block `341-398`, and
  `lifecycle_enclosure_test_support.py` is `:456`; among consumer rows the L5 suite moved to
  `:316`/`:375`, the L4 census to `:319`/`:378`, the playthrough to `:318`/`:377`, the pause suite to
  `:322`/`:381`, the L32 suite to `:336`/`:395`/`:471` and the L36 suite to `:309`/`:368`. Corrected
  four reference rows that named pre-insertion values (the two artifact block ranges
  `282-338`/`340-396` → `282-339`/`341-398`, the L5 consumer entries `:315`/`:373` → `:316`/`:375`, the
  L4 census `:318`/`:376` → `:319`/`:378`, and the playthrough `:317`/`:375` → `:318`/`:377`) and added
  the row for the new consumer edge. Verification metadata is **not** advanced: the code commit does
  not exist and closeout owns the stamp; no acceptance claim.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): registered the leaf's new `mcp/tests/test_leaf_doc_master_link_binding.py` as an exact
  consumer of `closeout_input_test_support.py` (row 315) and `curator_coherence_test_support.py`
  (row 373), both reached transitively through `test_worktree_support`, whose `initialized_memory_repo`
  imports both — measured, not inferred from the fixture name. No artifact row was added, removed or
  re-categorised, so the declared population is unchanged (measured: 42 `[[artifact]]`, 4
  `[[contract]]`). Re-derived every position this card cites, by line number in the current file: the
  closeout-input `path` cell stays `:283` with its block `282-338`, the curator-coherence `path` cell is
  `:341` with its block `340-396`, `lifecycle_enclosure_test_support.py` is `:454`; among consumer rows
  the pause suite moved to `:321`/`:379`, the L4 census to `:318`/`:376`, the playthrough to
  `:317`/`:375`, the L32 suite to `:335`/`:393`/`:469`, the L34 suite to `:304`/`:362` and the L36
  suite to `:308`/`:366`. Corrected four reference rows that named pre-insertion values (the
  curator-coherence `path` cell `:340` → `:341`, the enclosure fixture `:452` → `:454`, the two artifact
  block ranges `283-337`/`340-394` → `282-338`/`340-396`, and the pause/L4/playthrough consumer rows).
  Verification metadata is **not** advanced: the code commit does not exist and closeout owns the stamp;
  no acceptance claim.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): registered the leaf's new `mcp/tests/test_memory_attribution_producers.py` as an
  exact consumer of `closeout_fixture_test_support.py` (row 317) and `closeout_input_test_support.py`
  (row 374), both reached transitively through the `QueueFixture` its carryover case composes. No
  artifact row was added or re-categorised, so the declared population is unchanged. Corrected the two
  inline citations that named the *pre-insertion* block ranges
  (`closeout_input_test_support.py` 282-336 → 282-338 from its `path` cell at `:282`,
  `curator_coherence_test_support.py` 338-392 → 339-393 from its `path` cell at `:339`), which is the
  same shift this leaf's insertion causes. Verification metadata is **not** advanced: the registry's
  `lastVerifiedCommitHash` (`9c8a7a42`) predates this change set and the code commit does not exist yet,
  so closeout owns the stamp; no acceptance claim.
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 316) and `curator_coherence_test_support.py` (row 372), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; re-derived every shifted consumer row this card cites (the pause
  suite's entries 318 → 319 and 373 → 374, `curator_coherence_test_support.py` path 338 → 339,
  `lifecycle_enclosure_test_support.py` path 449 → 450 with the L32 entry 464 → 465) and corrected the
  three shared artifact-block ranges in the reference table to `282-336` and `338-392`. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: registered the new boundary suite
  `mcp/tests/test_pause_stop_only_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 318) and `curator_coherence_test_support.py` (row 373), reached
  transitively through `QueueFixture`, and recorded that the leaf's other new module
  (`test_pause_is_not_publication.py`) consumes no artifact because it is AST-only. No artifact row was
  added or re-categorised, so the declared population is unchanged; re-derived the shifted consumer
  rows (`curator_coherence_test_support.py` 338, `lifecycle_enclosure_test_support.py` 448, L32 entry
  463). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T18:09+02:00 — 260831-LOCR-L36: rebound two citation ranges shifted by this leaf's two
  additions to the manifest (`mcp/tests/test_cross_master_concurrency.py` in both consumer lists): the
  curator-coherence support artifact resolves at `:337` and the enclosure/worktree fixture's `path`
  cell at `:446`. Ranges only; the artifact and consumer claims are unchanged and no verification
  stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: recorded
  `mcp/tests/test_checkpoint_landing_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 304) and `curator_coherence_test_support.py` (row 357), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; the insertion shifted three later consumer rows, which are
  re-derived and re-cited here (330, 383, 459). Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:336-336. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: recorded the new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` as an exact consumer of three existing
  shared-support artifacts (`closeout_input_test_support.py` at row 329,
  `curator_coherence_test_support.py` at row 381, and `lifecycle_enclosure_test_support.py` at row 457,
  the last because the suite publishes a real enclosure through `publish_test_enclosure`). No artifact
  row was added or re-categorised, so the declared population is unchanged; added three reference rows
  and a section naming each artifact's reason for the edge. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:335-335. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:334-334. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ02 preparation recorded the exact two R25/R26 consumers added to both shared support rows. Registry SHA `15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are preserved as source/diagnostic evidence only; the source is uncommitted and no acceptance claim is made.
- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Registered the extracted gate fixture and publication-suite consumers in durable memory; reconciled exact-source runner ownership with the distinct pytest closure.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 registration of
  `test_gate_certificate_authority.py` as an exact consumer of the shared certification and
  closeout-input support rows whose builders its forcing suite imports. Verification is pinned
  to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 expanded the certification shared-support row to
  the complete five-consumer set exposed by the source graph. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Registered the portable certification composition owner with its two
  exact focused-suite consumers. Verification remains closeout-owned.

- 2026-08-31T12:39+02:00 — Added `test_dispatch_agent_ambient_reviewer.py` to both exact transitive
  consumer sets after the L5 closeout fast hook identified the previously undeclared ownership
  edges.

- 2026-08-30T16:32+02:00 — Added `test_public_surface_conformance.py` to both exact transitive
  consumer sets after the L4 staged fast hook exposed the source-derived ownership edges; the
  focused lifecycle validator passes with 35 governed artifacts.

- 2026-08-29T23:04+02:00 — Added `test_memory_candidate_pair.py` to the exact source-derived
  consumer sets for the closeout-input and curator-coherence test composition roots after the
  A002 lifecycle fast hook exposed both missing edges.

- 2026-08-29T12:27+02:00 — Reconciled the curator-coherence helper's declared consumers with the
  source-derived transitive ownership graph after generation 7 rejected the direct-import-only
  catalog row. Verification remains closeout-owned.

- 2026-08-29T12:10+02:00 — Registered the shared curator-coherence fixture-input owner and its
  three exact importers after the generation-6 fast hook rejected the uncatalogued helper.
  Verification remains closeout-owned.

- 2026-08-29T09:58+02:00 — Added the curator-coherence suite to the exact source-derived consumer
  set for the shared closeout-input test support after the targeted closeout gate exposed the
  missing edge.
- 2026-08-28T05:10+02:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.
- 2026-08-27T13:32+02:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.
