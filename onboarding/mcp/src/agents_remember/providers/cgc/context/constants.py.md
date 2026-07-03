# mcp/src/agents_remember/providers/cgc/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T01:55+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/constants.py` owns CGC provider identifiers, pins, Docker runner image,
watcher naming defaults, shared Docker network name, backend defaults, source
artifact names, env exclusion keys, default `.cgcignore` text, per-repo managed
exclusions (`CGC_REPO_CGCIGNORE_EXTRAS` — L12: agents-remember excludes its committed
package_data bundle from watch/index work), the watcher timer-pop patch snippets, and upstream
patch snippets.

## Code Commentary

### Logic

CGC runtime, runner, and patch modules import this file for stable names and
marker text. It also reads source `.gitignore` patterns for managed
`.cgcignore` generation. `CGC_RUNNER_IMAGE_LAYER_REVISION` ("ar1") is suffixed
onto the runner image tag (`<repo>:<cgc-version>-<revision>`) so changes to
the runner Docker layer alone — entrypoint scripts, baked patches — produce a
new tag.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.
- Bump `CGC_RUNNER_IMAGE_LAYER_REVISION` whenever the runner Docker layer
  changes without a cgc version change: `runtime_install` skips building image
  tags that already exist, so an unbumped revision leaves upgraded hosts on the
  cached old image (the GitHub #50 failure mode).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC runtime layout uses provider constants and default ignore text from this module. | [core.py](core.py.md) |
| CGC Docker runner command/build helpers use runner image and watcher container constants from this module. | [runner.py](../lifecycle/runner.py.md) |
| CGC patch application uses marker and snippet constants from this module. | [patches.py](patches.py.md) |

## Update History

- 2026-07-03T01:55+02:00 — L12: adds CGC_REPO_CGCIGNORE_EXTRAS (feeds per-root cgcignorePatterns in generated settings), the watcher timer-pop patch id/marker/snippets, and bumps CGC_RUNNER_IMAGE_LAYER_REVISION ar1->ar2 so hosts rebuild the runner image with the new patch.
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the layer-revision tag mechanics into Logic and promoted the bump-on-layer-change rule to Invariants (documentation only).
- 2026-06-09T22:10+02:00 — Added `CGC_RUNNER_IMAGE_LAYER_REVISION` ("ar1"), suffixed onto the runner image tag (`<repo>:<cgc-version>-<revision>`); bump it whenever the runner Docker layer changes without a cgc version change, because `runtime_install` skips building image tags that already exist.
- 2026-05-26T13:58+02:00: Updated after adding the shared CGC Docker network constant.
- 2026-05-26T12:51+02:00: Updated after adding CGC Docker runner image and watcher naming constants.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
