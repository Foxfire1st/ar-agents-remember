# mcp/src/agents_remember/providers/cgc/context/constants.py

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
`.cgcignore` generation. `CGC_RUNNER_IMAGE_LAYER_REVISION` ("ar2") is suffixed
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

## Evidence

### Repo-Internal References

- CGC runtime layout uses provider constants and default ignore text from this module. [1]
- CGC Docker runner command/build helpers use runner image and watcher container constants from this module. [2]
- CGC patch application uses marker and snippet constants from this module. [3]
