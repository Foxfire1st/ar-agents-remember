# docs/install/claude-code.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Claude Code install page: what to copy from the repository's `.claude/` starter
package, how to render that copy, where the `SessionStart` hook and skills must sit, and
how to make the MCP registration visible to Claude Code. It closes the install with the
`c-13-install-and-onboard` skill.

## What The Page Establishes

- Claude Code separates always-loaded project instructions from native skills, so the page
  wires both: a `SessionStart` hook for the coordinator first-action directive, and
  `.claude/skills` or `~/.claude/skills` for skills.
- The install is: copy `.claude/` to the workspace root, run the copied
  `.claude/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), and restart Claude Code once. The page also asks for
  `.claude/mcp/mcp.json` to be copied to `<workspace>/.mcp.json`: it states that Claude Code
  will not detect the MCP registration if the file only lives under `.claude/mcp/`.
- The renderer infers the workspace root from the copied folder, fills path and repository
  placeholders, writes the Python hook command and args into `.claude/settings.json`, and
  validates that each named repository exists. The manual alternative is the same
  replacements by hand with no placeholder left behind.
- Package contents the page names: `.claude/settings.json` (`SessionStart` hook
  registration), `.claude/hooks/agents-remember-session-start.py` and `.md` (the Python hook
  that emits the directive as `additionalContext`, and the directive text itself),
  `.claude/mcp/mcp.json`, `.claude/mcp/agents-remember-settings.json`, and `.claude/skills/`.
- The hook is the recommended and, per the page, only reliable surface: an imported
  `CLAUDE.md` is loaded as context carrying a "may or may not be relevant" disclaimer, so
  the doctrine reads as optional. Hook injection is authoritative; the import route is
  described as a degraded fallback.
- The directive the hook emits is entry-only: it addresses a developer-facing free chat and
  says nothing to a role agent that already has a binding.
- Claude Code scans skill folders directly: a skill is discovered only when `SKILL.md` sits
  one level under the skill root in a folder named by the skill's lowercase name, so the
  copied package must stay flat (`c-13-install-and-onboard/SKILL.md`). First-run setup does
  not install skills.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: it does not show that the hook fired, that Claude Code
detected the MCP server, that the renderer ran, or that `runtime_install()` executed. Its
statements about how Claude Code loads context, discovers skills and reads `.mcp.json` are
the page's account of that harness.

## Evidence

- Copy `.claude/`, render with `--repo`, restart once, and copy `mcp/mcp.json` to `<workspace>/.mcp.json` or the registration is not detected. [1]
- Package contents: settings hook registration, Python hook and directive text, MCP registration and authority settings, skills. [2]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [3]
- The hook is the authoritative surface; a `CLAUDE.md` import is described as optional context and a degraded fallback. [4]
- Skills must stay flat because Claude Code discovers only one level under the skill root. [5]
