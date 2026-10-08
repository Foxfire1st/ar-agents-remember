# mcp/src/agents_remember/models/knowledge/evidence.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Defines a verification-observation value and its recorded artifact, publication and environment references for readers.

## Code Commentary

`VerificationObservationPayload` requires an exact code or logical knowledge subject and consistent origin; artifact and publication references carry their own identities, while `RunEnvironment` records the environment supplied by the observer. These models do not verify a runtime merely because it was named. EvidenceClaimPayload and the AddEvidenceClaim/AddVerificationObservation canonical write commands were retired. The observation value's survival does not restore a canonical observation collection or writer.

## Evidence

### Repo-Internal References

- `VerificationObservationPayload` owns the current boundary described above. [11]
- `ResultArtifactReference` owns the current boundary described above. [12]
- `PublicationReference` owns the current boundary described above. [13]
- `RunEnvironment` owns the current boundary described above. [14]
