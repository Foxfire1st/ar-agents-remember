# CGC Context Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/providers/cgc/context/` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`cgc/context/` defines the CodeGraphContext provider's runtime layout, materializes its directories and configuration, detects source-repository artifacts, removes stale runtime artifacts, and supplies constants and upstream patch helpers. These retained implementation and settings facilities describe CGC context construction; they do not establish a public provider provisioning route. The current runtime installer no longer installs provider dependencies from enabled provider settings.

## Hot Path Summary

Use `core.py` for `CgcRuntimeLayout`, layout construction, settings interpretation, and `cgc_runner_image()`. Use `materialize.py` for `ensure_cgc_runtime_layout`, managed directories, and configuration files. Use `cleanup.py` for source-artifact checks and stale runtime cleanup. Use `constants.py` for dependency pins, backend names, environment exclusions, ignore patterns, and patch snippets. Use `patches.py` for marker-based application of patches to supplied upstream file paths. `__init__.py` re-exports these modules as the context facade.

## How It Is Built

`cgc_runtime_layout(repo, *, instance=, watcher=, backend=)` separates construction into four frozen dataclasses:

| Bundle | What it describes | Defaults |
| --- | --- | --- |
| `CgcRepo` | The owning `coordination_root`, `repo_id`, indexed `code_repo_root`, and repository-specific `cgcignore_patterns`. Ignore patterns describe graph coverage for this repository. | Required positional bundle; ignore patterns default to an empty tuple. |
| `CgcInstance` | Instance placement and pins: `runtime_root`, `requirements_file`, `patches_root`, `state_file`. | All fields are optional overrides. |
| `CgcWatcher` | One watcher process: runner `image`, `build_root`, `lock_file`, `container_name`, `process_env_template`, `watch_cwd`, `watch_log_file`. | All fields are optional overrides. |
| `CgcBackend` | The managed FalkorDB backend: `root`, `data_root`, `state_file`, `container_name`, `network_name`. | All fields are optional overrides. |

The empty keyword bundles select conventional placement. `DEFAULT_CGC_INSTANCE`, `DEFAULT_CGC_WATCHER`, and `DEFAULT_CGC_BACKEND` are module-level frozen defaults. The instance normally lives under `providers/runners/codegraphcontext/<repoId>`; shared requirements and patches live under `providers/requirements/` and `providers/patches/codegraphcontext`, while backend storage defaults to `providers/data/codegraphcontext/falkordb`. New placement overrides belong to the bundle describing their subject. Construction returns `CgcRuntimeLayout`, which contains the resolved paths, image and container names, ignore patterns, and process-environment template consumed by context and lifecycle helpers.

`cgc_runtime_layout_from_provider_settings` assembles the same bundles from settings. Its `_cgc_instance` helper expands `requirementsFile` and `patchesRoot` through `_unresolved_template_path`, preserving template spelling at that intermediate step. Their defaults are `<coordination_root>/providers/requirements/codegraphcontext.txt` and `<coordination_root>/providers/patches/codegraphcontext`. The final `cgc_runtime_layout` construction resolves these paths through `_resolve_optional_path`.

Materialization combines the default ignore patterns, nonempty lines from the repository's top-level `.gitignore`, and configured repository-specific exclusions. It writes identical ignore content to the instance `.cgcignore` and the HOME-scoped `.codegraphcontext/global/.cgcignore` that the retained watcher integration expects to read. `CGC_REPO_CGCIGNORE_EXTRAS` contributes the `agents-remember` package-data exclusion through generated root settings. Materialization also writes the FalkorDB configuration and filtered `.env`, and creates the pinned requirements file only when it is absent.

`cgc_runner_image()` constructs the runner tag as `repository:version-layerrevision` from the pinned CGC requirement and image constants. `providers/settings.py` imports this function for its runner setting, keeping settings and layout defaults consistent. The current CGC pin is `0.4.10` and the layer revision is `ar2`.

## Invariants And Boundaries

The runner layer revision must change when Docker-layer content changes without a CGC version change: the retained `cgc_runner_image_build` helper reuses an existing tag unless `no_cache` is requested. This cache behavior belongs to that helper; the current runtime installer does not provision provider dependencies. Enabled provider keys are reported as unused, and the installer attempts to stop old watchers before refreshing runtime assets.

Settings-derived layouts reject `venvRoot`, require an existing repository directory with no unresolved path placeholders, and require a concrete runner image tag. Process environments keep CGC's HOME and logs in the runtime layout; host-only Windows variables are omitted from container defaults. A supplied process-environment template replaces the defaults after expansion. `.env` materialization excludes the keys listed in `CGC_ENV_FILE_EXCLUDED_KEYS`.

Source-repository checks detect `.cgcignore`, `.codegraphcontext`, and `CGC_REPORT.md`. Cleanup considers unconfigured runtime directories and obsolete embedded `db`, `global`, `kuzu`, and `kuzu.wal` artifacts; resolved-path containment checks refuse removals outside the provider or instance root, and dry-run behavior is delegated to the removal helper.

Patch helpers return false for an already-applied patch and reject an unexpected unpatched snippet. The timer-pop patch removes a fired debounce timer's entry while protecting a replacement timer through an identity check. Other retained snippets cover explicit ignore-file preservation, Windows deletion prefixes, C++ and TableGen discovery, and visualizer query and routing changes. Their presence does not prove that an installed upstream module has been patched.

These construction and resolution rules describe the current returned layout. They do not assert historical equivalence for every upstream version or reader. Retained patch helpers and generated settings must not be mistaken for proof of installation or an available public provisioning route.

## Evidence

- The context facade re-exports layout, materialization, cleanup, constants, and patch helpers; patch helpers operate on supplied paths rather than discovering upstream modules. \[1] [1]
- Four frozen construction bundles feed a resolved `CgcRuntimeLayout`; empty keyword bundles select defaults with distinct instance, shared-resource, and backend placements. \[2] [2]
- Settings construction preserves requirement and patch template spelling in an intermediate bundle, then resolves those paths during final layout construction; it validates repository and image inputs and rejects venvRoot. \[3] [3]
- Materialization writes matching enriched instance and HOME-scoped global ignore files, retains an existing requirements file, and filters persisted environment keys; generated root settings carry managed repository exclusions. \[4] [4]
- Settings and layout defaults share the version-and-layer image tag, currently using CGC 0.4.10 and ar2; the retained image builder skips an existing tag unless no_cache is requested, while runtime installation no longer installs provider dependencies. \[5] [5]
- Runtime environments, source-artifact detection, cleanup containment, and expected-snippet patch checks constrain these helpers; timer-pop identity checks preserve replacement timers. \[6] [6]
