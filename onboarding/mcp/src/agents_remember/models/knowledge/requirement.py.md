# mcp/src/agents_remember/models/knowledge/requirement.py

## Governing Overview
[models route overview](../overview.md)

## Purpose
Carries the exact task-document identity that owns a requirement and the result of resolving that owner.

## Code Commentary
`RequirementOwnerRef` names the task-relative path, stable requirement ID and version under their declared patterns. `RequirementOwnerResolution` carries the resolved owner or its refusal. These are frozen values, not filesystem admission or a durable requirement revision. RequirementRevisionPayload and its canonical writer/read graph were retired; ownership resolution cannot silently substitute another requirement version.

### Logic

- **Three components, spelled the owner's way.** `RequirementOwnerRef` (116-137) carries exactly
  `path`, `stableId` and `version` — `ApprovedRequirementPacketRef`'s own field names, so the two
  planes compare literally rather than through a translation that could disagree. `extra="forbid"` is
  what refuses a fourth addressing scheme: there is no field for a UUID or a content address to arrive
  in. **The payload does not police the reference**: it bounds the three components and does not
  confine the path to a task root, require a `.md` suffix, or read the packet's metadata rows. Those
  are the owner's refusals, and a substrate that pre-refused them would substitute its own answer for
  the owner's, which requirement 2.3 forbids in terms.
- **The version spelling is the task plane's own.** `REQUIREMENT_PACKET_VERSION_PATTERN` (90) is the
  same `^v[1-9][0-9]*$` the owner's reference declares, written once here as the same pattern rather
  than a second, wider one — two admitted spellings for one version is exactly the drift requirement
  2.2 forbids.
- **The resolution is consumed, never re-derived.** `RequirementOwnerResolution` (140-169) holds one
  outcome: `resolved` carries no refusal fields, `unresolved` carries the owner's own `refusal_code`
  and `refusal_detail` verbatim. Nothing in this record group constructs either value, so a store can
  never report an owner's refusal the owner did not give. The resolution carries **no components of
  its own** — the reference it is about is the record's one `owner` field, which is never rewritten by
  a resolution, so a resolution cannot disagree with the reference it resolves.

## Evidence
### Repo-Internal References

- `RequirementOwnerRef` owns the current boundary described above. [23]
- `RequirementOwnerResolution` owns the current boundary described above. [24]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The version spelling taken from the task plane's own pattern rather than widened into a second admitted form. [28]
- **The owner reference in the task plane's own three components, with `extra="forbid"` as the fourth-addressing-scheme refusal.** [29]
- The resolution consumed rather than re-derived: one outcome, and the owner's own refusal fields verbatim. [30]
