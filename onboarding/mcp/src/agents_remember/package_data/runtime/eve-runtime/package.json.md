# mcp/src/agents_remember/package_data/runtime/eve-runtime/package.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/eve-runtime/package.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

**Generated file — do not edit.** The package-owned copy of the authored `eve_runtime/package.json`,
produced by `scripts/sync-runtime.py` (the `eve-runtime` target). Edit `eve_runtime/package.json` and
re-run the generator; the read-only `--check` proves currency.

## Code Commentary

### Why this file is load-bearing rather than incidental

`package.json` is one of the two files `install/experiment.py` reads as the
`packaged-eve-application` capability: with `agent/agent.ts` it is what proves a packaged mirror is a
real application, and its dependency block is what the `pinned-eve-dependencies` probe compares
against `PINNED_DEPENDENCIES` (`eve 0.56.0`, `ai 7.0.102`, `@ai-sdk/openai-compatible 3.0.49`,
`zod 4.6.5`). Every dependency must stay **exact** — a range such as `"eve": "^0.56.0"` is reported
by name as a mismatch and **refuses the install before its first write**. The file also carries
`"private": true`, and nothing here publishes a package.

`install_eve_application` copies the mirror into `<coordination_root>/runtime/eve-agent`, and the
record the run returns carries `eveVersion` read from this file rather than from the product's own
output.

### Invariants And Boundaries

- Generated content, never hand-edited; `eve_runtime/package.json` is the authored source.
- The four dependency pins are exact versions with no ranges; a range is a refusal, not a warning.
- `node_modules/` is not committed and not part of the mirror.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pins this file is compared against, and the one-line install command recorded for the operator. | `PINNED_DEPENDENCIES` | mcp/src/agents_remember/install/experiment.py:83-91 |
| The packaged-application probe reads this file together with `agent/agent.ts`. | `probe_capabilities` | mcp/src/agents_remember/install/experiment.py:479-566 |
| The generator declares the `eve-runtime` target with its per-target ignore set. | `TARGETS` | scripts/sync-runtime.py:61-78 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created** for the packaged mirror this leaf
  adds as a generator target. The card records generated content, the exact-pin contract the
  capability probe enforces, and the authored source. Verification metadata names the leaf base
  commit because the candidate is **uncommitted**; the real stamp is closeout-owned.
