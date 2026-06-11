# Human-Facing Installer Design

Date: 2026-06-03

This note captures the current requirements and design direction for an Agents
Remember installer aimed at humans, not agents. The installer should make the
happy path boring: run one shell command from the folder that contains the
developer's projects, answer a small number of prompts, start the harness once,
and have Agents Remember already wired in.

## Product Stance

Agents Remember should not rely on a model reading PyPI text, cloning a repo,
discovering harness-specific config paths, installing an MCP server, restarting,
installing runtime assets, restarting again, then installing hooks.

The install experience should be a product installer, not a scavenger hunt.

The shell installer is human-facing. It can print instructions that an agent can
follow later, but the primary user is a developer at a terminal. This matters
because the installer should be explicit, conservative, and understandable even
for developers who are competent software engineers but new to agentic coding
toolchains.

## Core Decision

Install `ar-coordination` into the folder that holds the user's projects.

Example:

```text
~/Projects/
  ar-coordination/
  project-a/
  project-b/
```

The coordinator is intentionally not installed inside a code repository and is
not meant to be checked into the user's project. That separation keeps project
repositories clean and preserves the cross-repo knowledge model.

The software may technically support other coordinator locations, but the MVP
installer should not advertise them. The happy path is the product path.

## MVP Scope

The MVP installer supports:

- Linux, WSL, and macOS-style developer environments.
- A shell bootstrap that can be run from the projects parent folder.
- Codex harness setup.
- Claude Code harness setup.
- Existing Python installation through either `uv`/`uvx` or `pip`.
- Existing Node installation for JSONC-safe config edits.
- Direct config mutation for MCP and hook registration.
- Runtime, skills, and providers installation through existing Python internals.
- Idempotent re-runs.

The MVP explicitly does not support:

- Installing `ar-coordination` inside a repository.
- Advertising arbitrary coordinator locations.
- IDE-specific integrations beyond the harness config files they already use.
- VS Code, Cursor, JetBrains, Eclipse, or Copilot as first-class setup targets.
- Solving machines that lack basic Python and Node developer tooling.
- Guessing through unknown config formats.

## User Flow

The intended flow:

```text
cd ~/Projects
curl -fsSL <installer-url> | sh
```

The installer asks:

```text
Where should Agents Remember be installed?
Default: /home/alex/Projects
```

The installer then asks which harnesses to configure:

```text
Configure harnesses:
1. Codex
2. Claude Code
3. Both
4. Other / show manual instructions
```

The default should favor the detected harness when only one is present. If both
are present, default to both.

The final message should be simple:

```text
Done.
Start Codex or Claude from /home/alex/Projects.
Agents Remember will load at session start.
```

## Installer Architecture

The shell script should stay small. It should:

- Detect platform basics.
- Check for Python.
- Check for Node.
- Prefer `uv`/`uvx` when available.
- Fall back to `pip` when reasonable.
- Explain missing prerequisites clearly.
- Download or invoke the Python installer core.
- Pass the chosen install root and harness choices to Python.

The Python installer core owns:

- Install plan construction.
- Existing install discovery.
- Coordinator creation or adoption.
- Runtime and skills installation.
- Provider setup.
- MCP config installation.
- Hook file installation.
- Safe config mutation.
- Verification.
- Final summary.

## Config Mutation Libraries

Use these libraries for config edits:

- `tomlkit` for Codex TOML config.
- `jsonc-parser` through Node for Claude JSON/JSONC config.
- `filelock` for cross-platform file locking.

Use Python standard library support for:

- Temporary files.
- Atomic replacement with `os.replace`.
- Path handling.
- Subprocess calls to Node when applying JSONC edits.

Do not mutate structured config through raw string appends except for generated
files that the installer fully owns.

## Transaction Model

Every installer step should classify state before acting:

- `absent`: create the file, directory, or config entry.
- `already-correct`: do nothing.
- `mergeable`: merge a missing entry into existing user config.
- `conflict`: stop and print the manual action needed.

Existing user files should be handled with:

- A lock file near the target config.
- A backup before the first modification.
- A parse check before editing.
- A semantic check after editing.
- Atomic write.
- A summary entry in the final report.

The installer must never overwrite:

- Existing memory folders.
- Existing `ar-coordination` content.
- Existing harness settings.
- Existing hook scripts that are not byte-for-byte installer-owned.
- Existing MCP server entries with a different command or name collision.

## Idempotency Requirements

The installer must be safe to run repeatedly.

Re-running should:

- Adopt an existing `ar-coordination` folder when it has the expected shape.
- Leave existing memory repositories intact.
- Leave already-correct MCP entries unchanged.
- Leave already-correct hook entries unchanged.
- Refresh installer-owned hook scripts only when the installed version is known
  to be owned by Agents Remember.
- Report drift between expected and installed config instead of silently
  overwriting.

The final summary should distinguish:

- Created
- Updated
- Adopted
- Already present
- Skipped
- Conflicts

## Codex Setup

Codex MVP setup targets project-local config under:

```text
<projects-root>/.codex/config.toml
<projects-root>/.codex/hooks/
```

The installer should add:

- The Agents Remember MCP server entry.
- A `SessionStart` hook entry.
- The hook script.
- The hook directive Markdown.

Codex config mutation should use `tomlkit` so comments, ordering, and user
formatting survive as much as possible.

If the local `.codex/config.toml` does not exist, create it. If it exists but
cannot be parsed, stop and print manual instructions. If a global Codex config
exists, do not mutate it by default for the MVP.

The hook should push the model toward:

- Reading the workspace `ar-coordination/AGENTS.md`.
- Entering `l-01-session-job-lifecycle`.
- Running `context_packet(repo_id="<repo-id>", include_providers=true,
  include_drift=true)` before trusting memory, providers, task files,
  onboarding, or source.
- Avoiding startup use of `include_drift=false`.

## Claude Code Setup

Claude MVP setup should target the relevant Claude settings JSON/JSONC file.

The installer should add:

- The Agents Remember MCP server entry.
- A session/startup equivalent if supported by the target Claude settings model,
  or the strongest available always-on instruction/hook surface.
- A generated Agents Remember instruction file when the harness config can point
  to one safely.

Claude config mutation should use `jsonc-parser` through Node so edits preserve
comments and formatting where possible.

The installer should not rely on `claude mcp add` as the primary path. Harness
CLI commands often imply a restart-driven flow. The product installer should
prepare the files directly before the human starts the harness.

If the target Claude config cannot be found or safely edited, the installer
should stop for that harness and print exact manual instructions.

## MCP Setup

The installer should configure MCP directly in the harness config files.

The MCP command should prefer an invocation that does not depend on an activated
virtual environment. Candidate order:

1. `uvx agents-remember` when `uvx` is available.
2. A managed Python environment created by the installer.
3. A pip-installed console script when clearly available.

The final written command must be stable across new terminal sessions.

The installer should verify that the configured command can start far enough to
respond to an MCP startup or version probe when such a probe is practical. If no
probe is practical before harness launch, it should at least verify that the
command exists and the Python package can import.

## Runtime, Skills, And Providers

Runtime and skills installation should reuse the existing Python internals
already encoded in the MCP package.

Provider setup should:

- Detect Docker before offering Docker-backed providers.
- Explain clearly when Docker is missing.
- Install provider config only when prerequisites are satisfied.
- Avoid starting long-running provider work unless the installer explicitly says
  it is doing so.
- Prefer a final "ready for first harness start" state over a partially running
  hidden background state.

## Failure Behavior

The installer should fail in a way that preserves trust.

It should stop on:

- Running from inside a Git repository.
- Existing `ar-coordination` with an unknown or unsafe shape.
- Unparseable target config.
- Config name collisions.
- Missing Python.
- Missing Node when Claude JSONC mutation is requested.
- Missing Docker when Docker-backed providers are requested.

It should not stop on:

- Harness not selected.
- Harness not installed.
- Provider setup skipped by user choice.
- Already-correct existing config.
- Existing memory repositories.

Every failure should include:

- What was detected.
- What was left untouched.
- The exact next command or manual edit when available.

## Security And Trust

The `curl | sh` path is familiar but trust-sensitive.

The README should offer both:

```text
curl -fsSL <installer-url> | sh
```

and:

```text
curl -fsSLO <installer-url>
less install.sh
sh install.sh
```

The installer should print the install root, selected harnesses, and files it
plans to modify before making changes. For existing configs, it should say that
backups will be created.

## Open Questions

- Exact Claude config paths and hook/instruction surfaces need to be verified
  against the current Claude Code docs before implementation.
- The installer-owned file marker format needs a decision. A small header comment
  plus version string is likely enough for generated hook files.
- The MCP command name and package invocation should be finalized around the
  published PyPI package shape.
- Provider startup should be decided separately: install-only versus install and
  start.
- Whether global Codex/Claude config support is a post-MVP feature or an
  advanced flag.

## MVP Acceptance Criteria

The MVP is good enough when:

- A developer can run one command from a projects parent folder.
- The installer refuses to install inside a Git repository.
- `ar-coordination` is created or safely adopted.
- Codex config is safely created or merged with `tomlkit`.
- Claude config is safely created or merged with `jsonc-parser`.
- Config files are locked while edited.
- Existing config files are backed up before modification.
- Writes are atomic.
- Existing memory folders are never overwritten.
- Re-running the installer produces no duplicate config entries.
- The final summary tells the user exactly what changed and how to start the
  harness.
