# install-skills.sh

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `scripts/install-skills.sh`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-12T18:21+02:00                     |
| lastVerifiedCommitHash | `d2f8072bb43a197c193b99405056e720adc34b1b` |
| lastVerifiedCommitDate | 2026-05-12T19:22:12+02:00|

## Purpose

`install-skills.sh` installs Agents Remember skills into a harness-specific skills directory by creating symlinks back to the canonical `agents-remember-md/skills` tree.

## Code Commentary

### Logic

The script parses an explicit `--install-root` destination, optional `--source`, optional `--layout tree|flat`, and optional `--archive-local-copies`. It derives its default source from the checkout that owns the script, validates that the resolved source contains `SKILL.md` files, creates the destination folder, and then installs one of two symlink layouts. The default tree layout creates or refreshes `<install-root>/agents-remember-md` as a symlink to the canonical skills tree. The flat layout reads each skill's frontmatter `name`, validates lowercase skill names, rejects duplicates, and creates direct `<install-root>/<skill-name>` symlinks to each canonical skill directory for harnesses that expect direct skill folders.

### Conventions

The install destination is explicit so the script can be used with workspace-local, user-wide, or harness-specific skills folders without hard-coded path assumptions. The `--skills-dir` alias is accepted for callers that name the destination as a skills directory. `--source` accepts either an `agents-remember-md` checkout or a direct `skills` directory, but normal checkout-owned use does not need it. The `tree` layout is the default and `namespace` is accepted as an alias; `flat` is accepted with `direct` as an alias.

### Invariants And Boundaries

The script must not copy skill sources because resolver-relative paths inside the skill bundle depend on the canonical checkout layout. Both layouts preserve canonical directories through symlinks. Tree mode manages the `agents-remember-md` namespace symlink in the install root; flat mode manages one symlink per frontmatter skill name. The script does not configure `AR_COORDINATION_ROOT` or edit the target harness. Archive mode is non-destructive: it moves conflicting local copies aside rather than deleting them.

### Todos

Refresh verification metadata after the installer script is committed so this onboarding record points at the commit that first includes the file.

### Docs References

No external documentation is needed for this small shell installer.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                           | Citations        | Source Path                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------- |
| The installer CLI requires `--install-root`, documents recursive and direct-folder examples, and describes tree versus flat symlink shapes. | L7-L47 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| Argument parsing accepts `--layout tree|flat`, `--source`, `--archive-local-copies`, and aliases for legacy callers. | L51-L111 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| Source resolution defaults to the checkout that owns the script but can accept a checkout or direct `skills` directory. | L113-L158; L324-L338 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| Flat layout reads CRLF-tolerant frontmatter names, validates lowercase names, rejects duplicates, and creates direct skill-name symlinks. | L160-L175; L261-L316 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| Tree layout creates or refreshes the `agents-remember-md` namespace symlink to the canonical skills tree. | L246-L258 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| Archive mode moves conflicting local folders into timestamped `.archived-local-copies/` directories instead of deleting them. | L177-L244 | [skills installer](agents-remember-md/scripts/install-skills.sh) |
| The active Agents Remember memory settings include shell scripts under `scripts/**`, making this installer eligible for onboarding. | L7-L21 | [memory settings](ar-coordination/memory-repos/ar-agents-remember-md/system/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed for this installer.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T18:21+02:00: Updated after adding `--layout flat` for harnesses that require direct lowercase skill folders while preserving canonical source paths through symlinks.
- 2026-05-12T17:31+02:00: Created onboarding after adding the checkout-owned installer script and making `scripts/**` plus `.sh` eligible in the active memory settings.
