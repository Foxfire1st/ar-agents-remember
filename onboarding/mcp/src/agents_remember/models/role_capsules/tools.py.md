# mcp/src/agents_remember/models/role_capsules/tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

Requested tool identities, narrowed against the admitted permission policy. **A capsule
*requests* capabilities; it never grants them.** This module is the whole of that boundary.

## Code Commentary

### Logic

cit:([`narrow_tool_requests`], mcp/src/agents_remember/models/role_capsules/tools.py:24-58) turns the tool identities the compiled sources
declare into cit:([`CapsuleToolRequest`], mcp/src/agents_remember/models/role_capsules/types.py:435-450) values, deduplicated and returned in
**stable tool-id order**, and refuses (`tool-request-not-permitted`) rather than silently
widening when a request falls outside the snapshot an existing AR owner admitted
(cit:([`CapsuleToolPolicy`], mcp/src/agents_remember/models/role_capsules/types.py:181-194)).

The declared identities come from the canonical manifest's per-role `tools` array, read through
the compiled sources and handed here as `(tool_id, authority)` pairs. Nothing in this module can
add a tool the policy did not already permit, *which is why the check is a subset test and not a
merge.*

### Conventions

Order is by tool id, not by declaration order — the capsule's requested-tool list must be
reproducible from the same admitted facts regardless of how the manifest lists them.

### Invariants And Boundaries

- **A request is not a grant.** This module narrows; it never widens, and it never mutates the
  policy snapshot.
- A request outside the admitted policy is a typed refusal, not a dropped entry. Silently
  dropping a declared request would make the capsule differ from its own sources.
- The returned tuple is deduplicated and in stable tool-id order; the semantic digest lists
  these ids in that order.
- The manifest declares *what a role asks for*; the admitted `CapsuleToolPolicy` decides *what is
  permitted*. Do not merge those two authorities into one table.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted policy snapshot and the request/`ToolId` shapes this module works with. | `CapsuleToolPolicy`; `CapsuleToolRequest`; `CapsuleToolId` | mcp/src/agents_remember/models/role_capsules/types.py:182-197; mcp/src/agents_remember/models/role_capsules/types.py:435-450 |
| The refusal code for a request outside the admitted snapshot. | `STATUS_TOOL_REQUEST_NOT_PERMITTED` | mcp/src/agents_remember/models/role_capsules/statuses.py:22-23 |
| The compiler step that narrows requests before sealing the digest. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:89-145 |
| The architect seat's declared tool requests in the canonical manifest, including the child-seat messaging tool that supplies a declared identity. | `message_child` | skills/l-01-agent-lifecycles/composition-manifest.json:165-174 |
| A request inside the policy is carried but not granted; one outside it is refused; every declared id exists in the public tool roster. | `test_a_tool_request_inside_the_policy_is_carried_but_not_granted`; `test_a_tool_request_outside_the_admitted_policy_is_refused`; `test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` | mcp/tests/test_role_capsule_compiler.py:819-828; mcp/tests/test_role_capsule_compiler.py:831-838; mcp/tests/test_role_capsule_admission.py:223-230 |

## Cross-Repo References

No sibling-repository contract defines this narrowing rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `compile_role_capsule` repointed to mcp/src/agents_remember/models/role_capsules/compiler.py:89-145. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the tool-request
  narrowing boundary added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records
  the request-versus-grant distinction, the subset-test (not merge) rule, the stable tool-id
  ordering, and the refusal-rather-than-drop behavior. Verification metadata is left at the leaf
  base commit because the source is uncommitted — the governed closeout stamps the real code
  commit.
