# mcp/src/agents_remember/certification/certificate_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/certificate_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification contract overview](overview.md)

## Purpose

Issuance and finalization authority for gate certificates: publish one green `GateCertificate`
bound to the exact admitted plan, current predecessors, terminal result manifest and consumed
artifacts; validate exact prefixes as chains; and publish/revalidate the transactional
`FinalizationCertificateAuthority` after all five gates are green (CCR-R21@v2).

## Code Commentary

### Logic

`compile_gate_certificate` resolves the admitted gate identity, proves the result manifest is
bound to the exact admitted candidate/gate-plan/registry and is green with certifying
profile/altitude, requires the exact earlier-gate predecessor prefix (each predecessor itself
revalidated against current gate-local inputs), binds consumed artifacts to exactly one earlier
green certificate (`_bind_consumed_artifacts`; Gate 3 must consume a green Gate-2 artifact), and
extracts the canonical rail/artifact/evidence inventories from the manifest. Gate 5 requires
`gate_five_inputs` and folds their identity rows into the certificate.

`validate_certificate_chain` revalidates one exact ordered prefix against current
admission/gate-local inputs. `compile_finalization_authority` validates the complete 5-certificate
chain, then binds code/memory tree pair, admission, certificate identities, candidate-pair,
task-intent, and journal authorities into one content-addressed authority.
`validate_finalization_currentness` rebuilds the exact authority from current inputs and
refuses if any edge drifted, so unchanged recovery starts zero gates.

### Invariants And Boundaries

- Only a complete green certifying result publishes a certificate; diagnostic, partial, or
  report-only results never do.
- Predecessors are always the exact complete earlier-gate prefix; no historical or newest-success
  lookup substitutes for the exact dependency edge.
- Gate 3 binds at least one exact artifact from the green Gate-2 certificate.
- Only Gate 5 may carry memory/coherence inputs.
- Finalization requires exact green Gates 1-5 and revalidates current identities without
  recertifying unchanged gates.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The certificate authority enforces exact predecessor edges, consumed-artifact binding, and finalization currentness. | "def validate_certificate_chain("; "def _bind_consumed_artifacts("; "def validate_finalization_currentness(" | mcp/src/agents_remember/certification/certificate_authority.py:113-132; mcp/src/agents_remember/certification/certificate_authority.py:363-363; mcp/src/agents_remember/certification/certificate_authority.py:198-198 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One green certificate is issued from exact current plans, predecessors, and the result manifest. | `compile_gate_certificate` | mcp/src/agents_remember/certification/certificate_authority.py:39-106 |
| Chains are validated as one exact prefix against current gate-local inputs. | `validate_certificate_chain`; `_require_current_certificate` | mcp/src/agents_remember/certification/certificate_authority.py:109-132; mcp/src/agents_remember/certification/certificate_authority.py:251-294 |
| Consumed artifacts resolve to exactly one earlier green certificate; Gate 3 binds Gate-2 artifacts. | `_bind_consumed_artifacts` | mcp/src/agents_remember/certification/certificate_authority.py:363-402 |
| Finalization binds the memory pair and revalidates authority currentness. | `compile_finalization_authority`; `validate_finalization_currentness` | mcp/src/agents_remember/certification/certificate_authority.py:135-169; mcp/src/agents_remember/certification/certificate_authority.py:198-222 |
| Gate-5 memory inputs become canonical certificate inputs. | `_gate_five_input_identities` | mcp/src/agents_remember/certification/certificate_authority.py:461-494 |

## Cross-Repo References

None; this is the repository-neutral certificate issuance owner.

## Update History

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_bind_consumed_artifacts` repointed to mcp/src/agents_remember/certification/certificate_authority.py:363-402. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_gate_five_input_identities` repointed to mcp/src/agents_remember/certification/certificate_authority.py:461-494. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: replaced the unsupported task-packet citation with behavior-bearing implementation anchors for chain, artifact, and finalization validation. Source hashes: mcp/src/agents_remember/certification/certificate_authority.py=349728f041cffc0a402022c986fd0c973aa00b1bbaa03b9cbb8ae48adece9bac; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=349728f041cffc0a402022c986fd0c973aa00b1bbaa03b9cbb8ae48adece9bac; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new gate
  certificate issuance/finalization authority (exact predecessor chains, artifact binding,
  finalization currentness). Verification is pinned to the owning commit.
