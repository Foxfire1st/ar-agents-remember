# docs/README.md

## Current operative account — MIK-R199

- Under "Core Features", the "Search that finds, not decides" bullet says semantic memory and
  code-graph providers "were optional accelerators for locating relevant files, callers,
  dependencies, and concepts; both are retired now, and verified Markdown and source code remain
  the truth" (`docs/README.md:16`).
- The Start Here entry for Getting Started ends the first-run description at `runtime_install`
  "and set up memory and onboarding": providers are absent from the setup list
  (`docs/README.md:25`).
- The Features entry describes the product tour as covering "by-path memory, drift, the retired
  providers, worktrees, harness setup, and operational guardrails" (`docs/README.md:26`).
- The Guides entry describes the Providers page as "the retired semantic and code-graph
  providers: what an old install leaves behind and how to clean it up" (`docs/README.md:52-53`).
- The paragraph on where durable memory lives sends readers to `features.md` for the full tour,
  a link inside the docs tree (`docs/README.md:21`).
- The opening summary line still advertises retrieval "by path, semantics, and relationsship
  (code-graph)" (`docs/README.md:3`). That sentence is not reworded; it stands beside the feature
  bullet that retires the semantic and code-graph providers.
- The page names no provider id or setting key, gives no provider command, and carries no cleanup
  steps. It states no provider install, prepare, seed, start, query, watch, provider-status or
  provider-lane obligation, and it says nothing about leftover folders, unused keys, a watcher stop
  or a safety check over leftovers (`docs/README.md:1-66`).

### Superseded inventory

- Superseded by MIK-R199: "**Search that finds, not decides:** Optional semantic memory and
  code-graph providers help locate relevant files, callers, dependencies, and concepts, but
  verified Markdown and source code remain the truth." Replaced by the past-tense accelerator
  wording with "both are retired now" (`docs/README.md:16`).
- Superseded by MIK-R199: "then let `c-13-install-and-onboard` run `runtime_install` and set up
  memory, onboarding, and providers." Replaced by the same first-run sentence ending at "memory and
  onboarding" (`docs/README.md:25`).
- Superseded by MIK-R199: "the concentrated product tour: by-path memory, drift, providers,
  worktrees, harness setup, and operational guardrails." Replaced by "the retired providers" in
  the same list (`docs/README.md:26`).
- Superseded by MIK-R199: the bare guides entry "[Providers](guides/providers.md)". Replaced by the
  annotated entry naming retired semantic and code-graph providers and old-install cleanup
  (`docs/README.md:52-53`).
- Superseded by MIK-R199: "For the full tour, see [Features](docs/features.md)." Replaced by the
  same pointer with the link target `features.md` (`docs/README.md:21`).

### Source and authority bounds

- Document read in full: `docs/README.md:1-66`.
- Changed regions read in the current file: `docs/README.md:1-3`, `docs/README.md:14-21`,
  `docs/README.md:23-31`, `docs/README.md:44-53`.
- Superseded wording was read from the supplied diff hunks for this exact path.
- These bounds record what the page states. They supply no build, test, publication, review or
  acceptance claim for the page or the product.

## Evidence

- The core-features bullet retires the semantic and code-graph providers and keeps verified Markdown and source code as the truth. [1]
- The Getting Started entry stops at memory and onboarding, with no provider setup step. [2]
- The Features tour entry names the retired providers. [3]
- The guides entry describes the Providers page as retirement plus old-install cleanup. [4]
- The external-memory paragraph links `features.md` inside the docs tree. [5]
- The opening summary line still lists semantics and code-graph retrieval. [6]
- The page names no provider command, setting key or provider id. [7]
