# dashboard/src/cockpit/role-launcher/RoleCatalogStatus.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Show the provenance of launcher choices while fresh options are pending or a catalog part is saved or unknown.

## Code Commentary

### Logic

Fresh parts add no notice. Saved parts show their read time and any recorded error. Unknown parts explain that configured values will be sent unchecked. Notices distinguish agents, models, permission modes, tool-server support, effort, features and speed tiers.

While options load, the component labels displayed choices as saved and shows their origin. It lists at most three model labels per provider and reports the remaining count. A settled catalog with no notices renders nothing.

### Invariants And Boundaries

This component presents supplied discovery state. It does not fetch choices, enable Start, invent a failed request, validate settings or grant permissions.

## Repo-Internal References

- Saved and unknown parts get distinct notices; fresh parts add none. [1]
- Saved previews show at most three model labels and the remaining count. [2]
- Pending state and per-part provenance are shown without deciding a launch. [3]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
