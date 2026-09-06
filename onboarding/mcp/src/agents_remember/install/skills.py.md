# mcp/src/agents_remember/install/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/install/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5` |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`skills.py` implements the MCP-owned `skills_install` service. It copies
packaged Agents Remember skills into the configured harness skill root.

## Code Commentary

### 260731-EFA-L2 Skills Install Request

**`SkillsInstallRequest(install_root, dry_run=False, overwrite=False, archive_existing=False)`**
is what one skills install is asked to do: where the packaged skills land, whether it writes at
all, and how it treats a skill directory that is already there. **The collision rule rides with
the destination** because every per-skill copy has to consult both.

`request.validated()` replaces the old `_validate_install_skills_args` helper and raises the same
two `ValueError`s — a non-absolute `install_root`, and `overwrite` together with
`archive_existing` (mutually exclusive). `install_skills(*, install_root, dry_run=False,
overwrite=False, archive_existing=False)` keeps its fully keyword-only public signature and builds
the validated request internally; `_copy_skill_tree(request, summary, *, source, destination)`
takes it. `dry_run` still defaults to `False` (act-by-default).

### Logic

The service finds the packaged runtime skills through `packaged_source_root`. The
packaged skills tree is flat — one folder per skill directly under `skills/` — so
the service simply copies each skill directory under the install root, named by its
frontmatter `name` (validated as `[a-z0-9][a-z0-9-]*`). There is no layout
branching or namespace folder: the source is already flat, so the script just
copies the skills across. Existing targets are either archived or replaced
depending on the request. Replacement handles normal directories, file links,
directory symlinks, and Windows junction/reparse-point directories so legacy
symlink installs can be migrated to the copy.

### Invariants And Boundaries

- This service must copy skill directories; it must not create symlinks.
- `overwrite` and `archive_existing` are mutually exclusive.
- Existing non-archived/non-overwritten targets are errors so stale local skill
  copies are not silently merged.
- Replacing an old symlink or junction target must remove only the link itself,
  not the linked target tree.
- `install_skills`'s `dry_run` defaults to `False` (act-by-default); `dry_run=true`
  reports the planned copy/replace without writing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `skills_install` is exposed as an MCP payload. | `skills_install` | mcp/src/agents_remember/mcp/tools/core.py:156-156 |
| Runtime package discovery is shared with runtime install. | "class RuntimeTreeSync" | mcp/src/agents_remember/install/runtime.py:72-72 |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `_validate_install_skills_args` became `SkillsInstallRequest.validated()`, and
  `_copy_skill_tree` was re-signed onto the request. `install_skills`'s public signature and both
  refusals are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-06T12:28+02:00: Corrected the MCP payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-02T04:40+02:00: Simplified to a single flat copy — dropped the `layout` param, the `tree` branch, and the `agents-remember` namespace now that the packaged skills tree is flat (U-01-core-skills dissolved). `install_skills` copies each skill by frontmatter name; callers + the `skills_install` tool dropped `layout`. `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-05-29T18:35+02:00: Added `sys.platform` narrowing in `_is_link` for the Windows-only `st_file_attributes` and extracted `_validate_install_skills_args` from `install_skills`; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-23T17:34+02:00: Documented overwrite handling for legacy symlink and Windows junction skill installs.
- 2026-05-23T13:09+02:00: Created for copy-only MCP skill installation.
