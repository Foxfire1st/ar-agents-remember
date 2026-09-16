# mcp/src/agents_remember/kernel/_agentic_settings_harness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/_agentic_settings_harness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

`orchestration.harnesses` parser: the effective harness registry. Entries merge over the builtin table
by id; the strict merged pass enforces completeness and delivery-vehicle pairing, while the per-file
pass checks shapes and unknown keys only.

Its load-bearing job beyond shape checking is deciding **what an override is allowed to lose**. A
settings entry that customizes a builtin's launch mapping must not silently discard properties of the
builtin that describe its *runtime* rather than its command line — which is why the readiness probe is
carried across an override explicitly.

## Code Commentary

### Logic

The parser is split so each pass can be strict about one thing:

- `_parse_harnesses` reads the `harnesses` mapping and `_HarnessEntry` is its typed row;
  `_entry_string` and `_entry_string_list` are the scalar/list shape checks that name the offending
  key and its owner.
- `_parse_harness_entry` builds the declared half (name, flags, effort policy) and
  `_resolved_launch` resolves the launch mapping; `_merged_harness` merges a declared entry over its
  builtin row and produces the effective `Harness`.
- `_refuse_unpaired_vehicles` and `_refuse_bad_effort_template` are the strict merged-pass refusals
  for a delivery-vehicle pair that cannot work and for an effort template that cannot be formatted.

**`_merged_harness` carries a builtin's readiness probe across an override.** When the entry merges
over a builtin (`base is not None`), it sets `overrides["runtime_probe"] = base.runtime_probe` before
applying the declared fields. The comment in the code states the reason and is the claim to preserve:
a builtin's readiness probe is a property of its **runtime**, not of the launch mapping an override
customizes, so dropping it would silently downgrade a runtime-probed harness back to a `which` lookup
over a command that was never a PATH program — reporting a missing runtime as a generic not-installed
harness. It has to be carried here rather than declared by the user because
`orchestration.harnesses` has **no probe key** for a settings entry to set.

A settings entry with a **new** id has no builtin to inherit from, so it declares no probe — the
correct outcome, since the parser cannot know a new id's runtime.

### Conventions

- Every refusal names the key, the owner and the source file, so a malformed settings edit is
  diagnosable without reading the parser.
- The two passes stay separate on purpose: the per-file pass checks shapes and unknown keys only, and
  the merged pass is where completeness and pairing are enforced.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_harness.py`.
- **An override must not strip a builtin's `runtime_probe`.** This is the module's one
  behaviour-carrying rule, and it is asserted by
  `test_a_builtin_override_keeps_its_runtime_readiness_probe`.
- **A settings-defined id declares no probe.** There is no key for one, and the parser must not
  invent one from the id or the command.
- Builtin id ordering is preserved and new ids append; the assertion derives the expected builtin
  prefix from `HARNESSES` rather than transcribing it, so a silent reorder cannot pass.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the settings surface this parser implements is documented in-repo. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The merge that carries a builtin's readiness probe across an override, so customizing a launch mapping cannot downgrade detection. | `_merged_harness` | mcp/src/agents_remember/kernel/_agentic_settings_harness.py:133-182 |
| The row type the merge produces, including the `runtime_probe` field it must preserve. | `Harness` | mcp/src/agents_remember/kernel/harnesses.py:149-184 |
| The curated table the merge reads its builtin half from, and the `eve` row whose probe is the one at stake. | `HARNESSES`; `EVE_RUNTIME_PROBE` | mcp/src/agents_remember/kernel/harnesses.py:144-144; mcp/src/agents_remember/kernel/harnesses.py:187-212 |
| The consumers that would be misled by a dropped probe: detection detail and the capability catalog's install gate. | `harness_detection_detail`; `HarnessCapabilityCatalog` | mcp/src/agents_remember/serving/harnesses.py:110-124; mcp/src/agents_remember/serving/harness_capability_catalog.py:84-212 |
| The case asserting the probe survives an override and that a settings-defined id has none to inherit. | `test_a_builtin_override_keeps_its_runtime_readiness_probe`; `test_new_id_adds_a_harness_with_defaults_derived` | mcp/tests/test_agentic_settings.py:268-278; mcp/tests/test_agentic_settings.py:280-294 |

## Cross-Repo References

No external repository boundary is implemented by this parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **an override may no longer strip a builtin's
  readiness probe.** `_merged_harness` now sets `overrides["runtime_probe"] = base.runtime_probe` when
  the entry merges over a builtin, because a probe is a property of a harness's *runtime* rather than of
  the launch mapping a settings override customizes — dropping it would silently downgrade a
  runtime-probed harness back to a `which` lookup over a command that was never a PATH program. The
  carry is explicit precisely because `orchestration.harnesses` has no probe key for a settings entry to
  declare. Replaced the bare symbol list in Code Commentary with a real body (the parser split, the two
  strict refusals, the carry rule and its stated reason, and the new-id case), added the invariant, and
  gave the card its first reference table rows. Verification metadata moves to the leaf's synced base
  `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
