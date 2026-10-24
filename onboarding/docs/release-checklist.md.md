# docs/release-checklist.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The pre-tag checklist for a public `agents-remember-mcp` release: which gates are not rerun,
which version strings must match, what the shipped-host lock needs, what the install and
first-run smoke run must show, what the docs must match, and how the tag is landed and
published.

## What The Page Establishes

- Release notes live in GitHub Releases; there is no `CHANGELOG.md`; the canonical tag is
  `mcp-vX.Y.Z`.
- Quality: every leaf was accepted once by the lifecycle-owned Dagger `mode=targeted` gate
  before its commit and the master once by `mode=full` at integration, and neither gate is
  rerun for release. The pull-request-only deterministic check validates generated copies,
  lint, formatting and types, and does not run acceptance tests.
- Version sync: `mcp/pyproject.toml` `version`, the `SERVER_VERSION` fallback in
  `mcp/src/agents_remember/mcp/__init__.py`, and the `README.md` Status line must all match.
- Shipped host contract: an intentional host release moves `paseo_host/contract.json`, the
  exact `paseo_host/package.json` dependency and the plugin development SDK pin together; the
  whole `package-lock.json` is regenerated with the contract's checked Node/npm in an isolated
  staging directory and copied in, because production installs use `npm ci`; a Node change
  updates the exact version, the Linux-x64 archive URL and its SHA-256 together, and no other
  platform is claimed. `scripts/check-host-contract.py` plus the focused host-release tests
  bind the installed lock entry, manifest, plugin SDK, locked integrity/resolution and Node
  version/platform URL.
- Install and first-run smoke: a fresh `uvx agents-remember-mcp==<version>` starts and serves
  the tool list; `runtime_install(dry_run=true)` previews cleanly and
  `runtime_install(dry_run=false, install_provider_deps=false)` applies; `python3
  scripts/sync-skills.py --check` confirms root `skills/`, MCP package data and harness package
  skill folders are in sync.
- The two provider items are stated as setup properties, not provider features: setup works
  with no provider configuration at all, and an older settings file carrying retired provider
  keys loads, reports them once as unused (`unusedProviderKeys`), with leftover provider
  folders reported with their sizes. Neither item asks a releaser to install, enable or start
  anything.
- Docs: no stale references to removed APIs or arguments remain, and quickstart, install pages
  and the MCP tool reference match the shipped tool surface.
- Tag and publish: the release lands on `main` through a PR, the `mcp-vX.Y.Z` tag is pushed at
  the merged commit, the publish workflow proves the tag is reachable from `origin/main` before
  building and publishing without rerunning acceptance, and a GitHub Release is created on the
  tag.

## Boundaries

A checklist for a person releasing, not a record of a release. It does not state that any item
was performed, that a gate was accepted, that the smoke run passed, or that a tag was pushed.
Every checkbox is an obligation to satisfy and evidence elsewhere.

The two provider items describe what a release must show about a configuration-free setup and
about an older file's unused keys. They do not describe provider behaviour, and they carry no
provider install, status, query or cleanup procedure.

## Evidence

- Release notes live in GitHub Releases with no changelog file; the canonical tag is `mcp-vX.Y.Z`. [1]
- The targeted/full Dagger gates are consumed once and not rerun; the PR-only check is deterministic and not acceptance. [2]
- Version sync covers the package version, the `SERVER_VERSION` fallback and the README status line. [3]
- Host contract, whole-lock regeneration, Node pin and the host-contract check. [4]
- Fresh `uvx` start, dry-run then apply of `runtime_install`, and the skill-sync check. [5]
- Setup works with no provider configuration; an older file's retired keys are reported once as unused and leftover folders are reported with sizes. [6]
- Docs must match the shipped tool surface; the release lands by PR, the tag is proven reachable before publishing, and a GitHub Release is created. [7]
