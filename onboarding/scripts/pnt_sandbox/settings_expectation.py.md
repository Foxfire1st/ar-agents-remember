# scripts/pnt_sandbox/settings_expectation.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

Prepare a PNT sandbox's settings and prove they hold only the sandbox's own values. The sandbox is a disposable
installation of this checkout, so its settings file is one real installation's settings file — the same
coordination root, transcript folder, dashboard port and one repository — and this module owns that file and the
receipt that proves what it wrote.

It owns the sandbox's values only. The block a cold host needs and the one user settings location are product
behaviour, so the module asks the product instead of spelling its own: `fresh_host_block` supplies the
`paseoRuntime` block and `require_user_settings_path` resolves the developer user-settings input separately from the MCP host authority. A sandbox that
spelled either one itself could drift from the build under test and still report success.

Two properties are checked, and both are about the sandbox being ordinary rather than special: the settings file
differs from the product's own default only in the recorded root, the transcript folder and the dashboard port,
with an existing native authority block preserved and only an absent block receiving the product's fresh defaults;
and an existing developer user-settings file is an input byte for byte, so the sandbox never rewrites the developer's
configured file and its receipt records the same digest before and after.

The surface is `check(settings, workspace, coordination, dashboard_port, repo)`. It resolves the one repository
folder (`repository_ids`), digests the input, reads the file, selects the host block (`host_authority`) and the
user-settings path's digest, builds the prepared document (`settings_payload`) and the template's own default, then
compares both. `difference_keys` names every differing top-level key, `unapproved` refuses a key outside the recorded
reason map, and only then is the file written and read back. `SETTINGS_DIFFERENCE_REASONS` names the coordination
root, transcript root and dashboard; `HOST_DIFFERENCE_REASONS` names install prefix, home, listen, embed and
providers; `DEFAULT_DASHBOARD_PORT` is the port a template names before an installation records its own. An
existing `paseoRuntime` is parsed by `parse_paseo_runtime_settings` before any write — invalid or null content
refuses rather than being replaced — and absence alone selects the fresh block. The sandbox's settings file is the
host authority, so the block lives in it, while the developer's user settings file is an input the sandbox never
writes and never creates: an absent one stays absent, and a changed user-settings digest is refused before the sandbox file is written. The receipt also records a digest read after that write.

The receipt is inert data: the settings owner's path and digest, the product owners, the input and prepared paths
and digests, the user-settings path's before and after digests, the arguments, the two documents with provider entries
omitted by `receipt_settings`, the difference keys, the provider ids and the per-key host difference reasons
(an existing block is recorded as preserved unchanged). No provider value is printed or copied into it.

## Conventions

`main` is the command line over the same `check`: `--settings`, `--workspace`, `--coordination`,
`--dashboard-port` and `--repo`, printing the receipt as JSON. A repository id is one folder name under the
workspace root, must exist there, and is refused if it carries a path separator; a repeated id is
configured once rather than refused.

## Evidence

- The sandbox settings owner prepares its file and returns the receipt that proves what it holds.
- The host block and the shared user settings location come from the product's own functions, not from a local
  spelling.
- Only the recorded root, transcript folder and dashboard port may differ from the template default, and an
  existing authority block is preserved rather than replaced.
- The developer's shared settings file is an input: never written, never created, and digest-checked before and
  after the write.
- The receipt carries digests, difference keys and reasons, with both provider maps omitted.

## Current source evidence

- The sandbox MCP file owns host authority; developer user settings are input-only, checked for change before the sandbox write and recorded by before/after receipt digests. [1]
