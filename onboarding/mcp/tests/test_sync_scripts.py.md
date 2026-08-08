# mcp/tests/test_sync_scripts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_sync_scripts.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T10:45+02:00                     |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187`|
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Two different jobs, in two classes, and the module docstring cit:(["Two different jobs live here"], mcp/tests/test_sync_scripts.py:3-3) says so.
`ReplaceTreeTests` exercises the crash-safe copy-then-swap (`replace_tree`) and
the Windows extended-length path helper (`extended_length`) shared by
`scripts/sync-skills.py` and `scripts/sync-runtime.py`, over throwaway trees.
`RealTreeDriftTests` (260731-EFA-L4) reads the **actual mirrored trees in this
checkout** and fails if any generated copy disagrees with its canonical source.

## Code Commentary

### Logic

The scripts have dashed filenames, so cit:([`load_script`], mcp/tests/test_sync_scripts.py:23-33) loads them via
`importlib.util.spec_from_file_location`, registering each module in
`sys.modules` first (`@dataclass` resolves its defining module there at class
creation).

cit:([`ReplaceTreeTests`], mcp/tests/test_sync_scripts.py:57-156) has six tests and they are **unchanged by
260731-EFA-L4 and still load-bearing**: target replaced with source content and
stale files removed, a crash during `copytree` leaving the live target untouched
(the crash-safety contract), re-runs healing stale `.ar-sync-new`/`.ar-sync-old`
leftovers, sync-skills/sync-runtime parity, `extended_length` idempotence and
platform behavior, and cache-name copy ignores. They test `replace_tree`'s
*semantics*, which is a different property from real-tree drift; nothing here
replaced them.

### 260731-EFA-L4 The Enforcing Half

cit:([`drifted_files`], mcp/tests/test_sync_scripts.py:36-54) is a module-level reader shared by both
scripts. It works for both because both publish the same reading surface — a
`diff_target(target)` returning `missing` / `extra` / `changed` tuples of
tree-relative paths, plus `repo_relative` — so one reader serves both. Each entry
is rebased onto the target (`repo_relative(target.path / rel_path)`), so a
failure names the copy that has to be fixed rather than the path it shares with
eight others.

cit:([`RealTreeDriftTests`], mcp/tests/test_sync_scripts.py:159-207) holds two tests, each iterating the script's own
`TARGETS` tuple:

- `test_every_skill_copy_matches_the_canonical_tree` — all **9** entries of
  `sync-skills.TARGETS`: the packaged runtime copy
  (`mcp/src/agents_remember/package_data/runtime/skills`) plus the eight
  per-harness mirrors (`.claude`, `.codex`, `.cursor`, `.github-vscode`,
  `.hermes`, `.openclaw/workspace`, `.pi`, `.agents`). With the canonical
  `skills/` tree that is ten byte-identical copies of each skill.
- `test_every_runtime_package_asset_matches_its_source` — all **4** entries of
  `sync-runtime.TARGETS` (`agents-md-files`, `benchmarks`, `providers`,
  `system`).

Both failure messages name the exact repair command
(`python3 scripts/sync-skills.py` / `python3 scripts/sync-runtime.py`), the shape
`test_sync_harness.py::test_every_generated_harness_file_matches_its_source`
already used.

`maxDiff = None` cit:([`maxDiff`], mcp/tests/test_sync_scripts.py:177-177) is deliberate, not tidiness. `diff_target` on a wholly
absent mirror returns every source path as `missing` — 65 entries today
(`find skills -type f | wc -l` = 65) — and unittest's 640-character truncation
would elide exactly the filenames the test exists to print.

**The gap this closed, and it was real.** Nothing in CI checked that the ten
copies were in step. Verified at this revision: no workflow under
`.github/workflows/` (`quality-checks.yml`, `integration-gated.yml`,
`publish-mcp-to-pypi.yml`) mentions `sync-skills.py`, `sync-runtime.py` or
`.githooks/_gate.sh`; `code_quality/check.py` mentions none of them either; and
all six pre-existing tests run inside a `tempfile.TemporaryDirectory()` over
synthetic trees, so a hand-edited `.claude/skills/.../SKILL.md` passed every one
of them. The only thing that caught drift was `.githooks/_gate.sh`, which does
call both scripts with `--check` (`sync-skills.py` L81, `sync-runtime.py` L83;
L85 is the third script, `sync-harness.py`, already enforced by
`test_sync_harness.py`) — and that gate runs only for a contributor who has run
`setup-hooks.sh` to point `core.hooksPath` at `.githooks`. No CI run executes it.

### Invariants And Boundaries

- The crash-simulation test is the regression guard for the 2026-06-09
  incident where delete-then-copy gutted `package_data` mid-crash; the live
  target must survive any failure before the swap renames.
- Both scripts must keep exposing `replace_tree`, `extended_length`, `shutil`,
  and `os` as module attributes for these tests to patch and inspect. Since L4
  they must also keep exposing `TARGETS`, `diff_target` and `repo_relative`, or
  `drifted_files` breaks for both classes at once.
- **These tests close the gap through the pytest step CI already runs, not by
  arming `--check`.** `[tool.pytest.ini_options] testpaths = ["mcp/tests"]`
  (root `pyproject.toml`) is what `code_quality/check.py` reads to build its
  pytest step, and the `quality` job runs
  `python -m agents_remember.code_quality.check`. So drift now fails CI. CI still
  does **not** invoke `sync-skills.py --check` or `sync-runtime.py --check`
  directly; do not read a green pipeline as evidence that it does.
- **The reach of both tests is exactly `TARGETS`, and nothing asserts `TARGETS`
  is complete.** A tenth skill mirror added to the repository without being
  registered in `sync-skills.TARGETS` is invisible to
  `test_every_skill_copy_matches_the_canonical_tree` — it would report an empty
  drift list, which is also what a healthy tree reports. The runtime side has the
  guard this side lacks:
  `test_sync_runtime.py::test_default_targets_only_write_to_mcp_package_data`
  pins the runtime label set with an exact `assertEqual`, so a fifth runtime
  target fails until it is acknowledged. There is no equivalent assertion for the
  skill targets. That is a real, open limit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scripts under test. | "class SkillTarget", "class RuntimeTarget" | scripts/sync-runtime.py:27-27; scripts/sync-skills.py:27-27 |
| `TARGETS` (9 skill copies) with `repo_relative` / `file_digests` / `diff_target` — the reading surface `drifted_files` consumes, including `file_digests` returning `{}` for an absent tree so every source path reports `missing`. | `TARGETS`, `repo_relative`, `file_digests`, `diff_target` | scripts/sync-skills.py:43-56; scripts/sync-skills.py:79-80; scripts/sync-skills.py:103-114; scripts/sync-skills.py:117-129 |
| `TARGETS` (4 runtime asset targets) and the matching `repo_relative` / `diff_target`. | `TARGETS`, `repo_relative`, `diff_target` | scripts/sync-runtime.py:44-53; scripts/sync-runtime.py:73-74; scripts/sync-runtime.py:111-123 |
| The completeness assertion the runtime side has and the skill side does not — an exact `assertEqual` over the runtime target labels. | `test_default_targets_only_write_to_mcp_package_data` | mcp/tests/test_sync_runtime.py:72-84 |
| The model for this class, including naming the repair command in the failure message. | `test_every_generated_harness_file_matches_its_source` | mcp/tests/test_sync_harness.py:40-51 |
| The only pre-L4 drift check: the locally installed hook gate calling both scripts with `--check` (installed by `setup-hooks.sh` L36, which sets `core.hooksPath`). | "scripts/sync-skills.py", "scripts/sync-runtime.py" | .githooks/_gate.sh:79-79; .githooks/_gate.sh:80-80 |
| Why CI reaches these tests: `testpaths` is the single declaration the quality wrapper reads to build its pytest step. | `testpaths` | pyproject.toml:119-119 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: converted the reference rows to
  exact `path:start-end` sources with anchors, rebased `testpaths` to `pyproject.toml:112`, and
  converted the history `(L…)` citations; exact non-fixing check returns zero findings.

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator: this card described a file that tested only
  `replace_tree` semantics; the module now has a second, enforcing class and the card said nothing
  about it. Recorded cit:([`drifted_files`], mcp/tests/test_sync_scripts.py:36-54), the shared reader that works for both scripts
  because both publish `diff_target` (`missing`/`extra`/`changed`) plus `repo_relative`, and
  cit:([`RealTreeDriftTests`], mcp/tests/test_sync_scripts.py:159-207) with its two tests over all 9 `sync-skills.TARGETS` and all 4
  `sync-runtime.TARGETS`. Recorded why `maxDiff = None` cit:([`maxDiff`], mcp/tests/test_sync_scripts.py:177-177) is load-bearing rather than tidy:
  an absent mirror reports every source path as `missing`, 65 today, and unittest truncates at 640
  characters. Stated explicitly that the six `ReplaceTreeTests` are **unchanged and still
  valuable** — they pin `replace_tree`'s semantics, a different property from real-tree drift —
  because the new class reads as a replacement otherwise. Verified the enforcement gap at this
  revision rather than restating it: none of the three files in `.github/workflows/` names
  `sync-skills.py`, `sync-runtime.py` or `.githooks/_gate.sh`; `code_quality/check.py` names none
  of them; and `.githooks/_gate.sh` L81/L83/L85 (the `--check` calls) runs only for a clone whose
  `core.hooksPath` was set by `setup-hooks.sh`. Added the two invariants that keep this honest: the
  gap is closed **through the pytest step CI already runs** (`testpaths = ["mcp/tests"]`, root
  `pyproject.toml` L187-L196, which the quality wrapper reads) and **not** by arming `--check` in
  CI; and the reach of both tests is exactly `TARGETS`, with **no completeness assertion on the
  skill target tuple** — a tenth mirror added without registering it reports an empty drift list,
  indistinguishable from a healthy tree — in contrast to
  `test_sync_runtime.py::test_default_targets_only_write_to_mcp_package_data` cit:([`test_default_targets_only_write_to_mcp_package_data`], mcp/tests/test_sync_runtime.py:72-84), which pins
  the runtime label set with an exact `assertEqual`. Ran the suite to confirm the description:
  8 tests, all pass. Added six reference rows; the pre-existing row was re-checked and still lands.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-10T00:40+02:00: Created with the S7 crash-safe sync rework.
