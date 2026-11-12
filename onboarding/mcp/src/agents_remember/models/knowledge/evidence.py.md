# mcp/src/agents_remember/models/knowledge/evidence.py

## Governing Overview

[models route overview](../overview.md)

## Retirement

The verification-observation payload, artifact/publication/environment helpers and execution-result vocabulary are deleted whole. There is no current observation constructor/collection here and no equivalent replacement in the judgment proof model: proof currentness is not a recorded run result.

The source is deleted. The preserved account below is historical only; none of its constructor, route, writer or reference claims is a present implementation promise. The surviving current boundary is documented separately.

## Historical prior account — retired, not relocated

> # mcp/src/agents_remember/models/knowledge/evidence.py
>
> ## Governing Overview
> [models route overview](../overview.md)
>
> ## Purpose
> Defines a verification-observation value and its recorded artifact, publication and environment references for readers.
>
> ## Code Commentary
> `VerificationObservationPayload` requires an exact code or logical knowledge subject and consistent origin; artifact and publication references carry their own identities, while `RunEnvironment` records the environment supplied by the observer. These models do not verify a runtime merely because it was named. EvidenceClaimPayload and the AddEvidenceClaim/AddVerificationObservation canonical write commands were retired. The observation value's survival does not restore a canonical observation collection or writer.
>
> ### Logic
>
> `ResultArtifactReference` is a reference, never the bytes: a confined repository-relative POSIX path, the
> sha256 of the artifact's bytes, and the byte size. `PublicationReference` is the sibling for the
> interpretable manifest, naming a durable destination, the sha256 of the published bytes and the recorded
> instant; its presence or absence is how the record states which retention route it relies on.
>
> ### Conventions
>
> A vocabulary module declares the typed shape and the closed sets; the write path resolves links and the row
> codecs convert. Frozen and extra-forbidden is the default for every payload, so an undeclared field is a
> shape error rather than stored data.
>
> - **No semantic conclusion anywhere.** Nothing in either payload asks or answers whether evidence is
>   adequate, sufficient, convincing or relevant; nothing grades, ranks, scores or summarises. The absence is
>   structural — there is no field for a well-meaning writer to fill in.
> - **No second identity authority.** Neither record carries a content address, a logical digest or a
>   fingerprint of its own. A revision's seal is `record_revision.content_digest`; the one digest here is the
>   sha256 of an external artifact's bytes.
> - **The artifact reference never becomes a content store.** There is no bytes column and no BLOB in the
>   vocabulary or in generation 7, and the confinement validator refuses an absolute, drive, UNC, backslash,
>   NUL, `..` or pathspec spelling.
> - **Assessment references are explicit and opaque.** `ReviewAssessment` belongs to a later leaf, so
>   this module carries no `assessment_refs` field — the observation payload has none, only a
>   forward-reference docstring names it; a claim with none is served as unassessed rather than as compatible.
> - **Evidence results are facts, not verdicts.** `passed` and `failed` are equally facts; nothing in this
>   module converts either into a finding, a gate or a lifecycle change.
>
> ## Evidence
> ### Repo-Internal References
>
> - `VerificationObservationPayload` owns the current boundary described above. (historical reference 11; no current anchor)
> - `ResultArtifactReference` owns the current boundary described above. (historical reference 12; no current anchor)
> - `PublicationReference` owns the current boundary described above. (historical reference 13; no current anchor)
> - `RunEnvironment` owns the current boundary described above. (historical reference 14; no current anchor)
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Cross-Repo References
>
> No cross-repository behavior is implemented in this file.
>
> No meaningful cross-repo references found.
>
> - The artifact reference: a confined path, the bytes' sha256 and size — a reference, never a content store. (historical reference 19; no current anchor)
> - The publication reference whose presence states which retention route the record relies on. (historical reference 20; no current anchor)
> - The run's own toolchain, recorded at write time and bounded. (historical reference 21; no current anchor)
> - The observation aggregate: recorded candidate, command identity, artifact, execution result, environment, publication. (historical reference 22; no current anchor)

## Evidence

- The surviving response requires judgment, source and knowledge panes; it carries no old evidence pane or multi-class channel. [23]
