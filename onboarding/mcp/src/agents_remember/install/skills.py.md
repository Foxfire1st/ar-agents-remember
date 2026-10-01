# mcp/src/agents_remember/install/skills.py

## Governing Overview

[overview.md](../../../overview.md)

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

## Evidence

### Repo-Internal References

- `skills_install` is exposed as an MCP payload. [1]
- Runtime package discovery is shared with runtime install. [2]
