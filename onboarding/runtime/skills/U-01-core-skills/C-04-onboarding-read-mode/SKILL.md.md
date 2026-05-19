# C-04-onboarding-read-mode/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-19T03:58+02:00                                 |
| lastVerifiedCommitHash | `9aec8cf67dd5693d80ae6b3f69158a48ec144798`             |
| lastVerifiedCommitDate | 2026-05-19T04:35:33+02:00|

## Purpose

C-04 is the onboarding-first read protocol for source work. It is deliberately
short because its job is routing efficiency: discover likely routes, then
confirm only the resulting candidate packet.

## Code Commentary

### Logic

The skill has two modes. `fast-memory-discovery` reads the root route index
first, using root `hotPath`, child routes, and routing terms before falling back
to root overview prose. It then reads selected route indexes and only necessary
route overviews to produce a candidate packet. `bounded-source-confirmation`
starts from that packet and does not repeat discovery reads.

### Conventions

Route indexes are availability metadata. `coveredFiles` means a sidecar exists;
a source path inside `sourceScope` but absent from `coveredFiles` means skip the
sidecar probe and read source first. Full route overviews are fallback-only
after discovery; `hotPath` fields are generated hints for cheap discovery, not
proof.

### Invariants And Boundaries

Discovery may run one capped route-scoped `rg` only when index/overview evidence
does not produce candidate sources. Confirmation may run one capped `rg` only
for a named unresolved source question, over candidate files first, and over a
selected route only after filename narrowing. Missing sidecars or sparse memory
stay in confirmation and drive targeted source reads/searches, not a second
overview pass. Before source `rg`, confirmation converts the packet into source
anchors that are more specific than route labels or broad domain words.
Confirmation stops when source proves the subsystem boundary, immediate cause,
user-facing consequence, and next fix direction, and returns to discovery only
when no route/source target exists or targeted source evidence proves the
selected route/files irrelevant. Confirmation commands carry an operational
80-line output budget using shell-level caps for route-scoped searches, and
triage tasks stop at likely cause plus next direction instead of searching
implementation mechanisms unless explicitly asked.

### Todos

None.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-04 fits under 120 lines and defines only discovery plus bounded confirmation. | L1-L20 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Discovery produces the candidate packet, reads root index before root overview, uses route-index `hotPath` hints, and avoids sidecar probing, repository-root search, and multi-subsystem search. | L22-L57 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Confirmation consumes the packet, starts source-anchor narrowing from `hotPath.anchorHints`, narrows filenames before printing route-wide matches, and enforces an 80-line shell-capped command-output budget. | L60-L84 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Confirmation makes route overviews fallback-only after discovery, stops once source evidence is sufficient, and keeps triage out of implementation-mechanism searches unless asked. | L85-L108 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |
| Route indexes distinguish covered sidecars from indexed absence and expose cheap `hotPath` summary/anchors without blocking source reads. | L110-L118 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-onboarding-read-mode/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

## Update History

- 2026-05-19T04:05+02:00: Clarified that the 80-line confirmation output budget requires shell-level output caps and that `rg -m` alone is not enough across many files. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:58+02:00: Added a general confirmation command-output budget and triage-scope limit so C-04 does not enter implementation-mechanism search unless the prompt asks for it. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:40+02:00: Tightened bounded confirmation with filename-first narrowing, route-overview fallback rules, and a hard stop once source evidence is sufficient. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:12+02:00: Changed fast discovery to read root `overview.index.json` before root `overview.md`, making full root overview prose a fallback when the index is insufficient.
- 2026-05-19T02:45+02:00: Added route-index `hotPath` consumption so discovery can use generated summary, candidate hints, and source-anchor hints before reading full overview prose.
- 2026-05-19T02:21+02:00: Added the generalized source-anchor narrowing step before confirmation-mode `rg`, so route labels and broad domain terms are not reused as source queries after they already selected the route.
- 2026-05-19T02:03+02:00: Clarified that missing sidecars or sparse memory are not packet failures; they stay in bounded source confirmation and use targeted source reads/searches.
- 2026-05-19T01:50+02:00: Condensed the source skill to 98 lines and corrected the bounded confirmation handoff so it consumes the discovery candidate packet instead of replaying overview/index reads.
- 2026-05-19T01:37+02:00: Replaced the normal `deterministic-walkthrough` handoff with `bounded-source-confirmation`.
- 2026-05-19T01:11+02:00: Split read behavior into `fast-memory-discovery` and `deterministic-walkthrough` modes.
- 2026-05-18T21:44+02:00: Created onboarding for the renamed and hardened C-04 onboarding read-mode skill after pulling `origin/main`.
