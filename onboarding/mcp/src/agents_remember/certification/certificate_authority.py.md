# mcp/src/agents_remember/certification/certificate_authority.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

- The certificate authority enforces exact predecessor edges, consumed-artifact binding, and finalization currentness. [1]

### Repo-Internal References

- One green certificate is issued from exact current plans, predecessors, and the result manifest. [2]
- Chains are validated as one exact prefix against current gate-local inputs. [3]
- Consumed artifacts resolve to exactly one earlier green certificate; Gate 3 binds Gate-2 artifacts. [4]
- Finalization binds the memory pair and revalidates authority currentness. [5]
- Gate-5 memory inputs become canonical certificate inputs. [6]

### Cross-Repo References

None; this is the repository-neutral certificate issuance owner.
