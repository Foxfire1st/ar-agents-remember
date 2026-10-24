# skills/c-13-install-and-onboard/SKILL.md

## Governing Overview

[governing lifecycle or repository overview](../../overview.md)

## Purpose

This setup orchestrator starts after the Agents Remember MCP tool server is installed and registered with the harness. Installation no longer distributes the canonical skills: the server serves them from its own packaged copy as MCP resources, so nothing is copied into a harness, project or coordination-root skill folder and no skill-rendering or skill-sync step belongs to a user's install. The user starts the path with one call from their own chat, `role_start(role="bootstrap", request_id=<UUID>)`, which prepares a missing runtime scaffold and host, verifies the plug-in and starts one instructed Bootstrap seat whose dashboard chat carries setup onward. The skill is the setup reference for the path as a whole: how installation works, the order of the stages, which skill owns each one, and the handover the first run ends on.

Its stages run the runtime scaffold, obtain user-owned settings decisions and delegate memory initialization to `c-00-initialize-memory-repo` and the first baseline to `c-10-adopt-memory-baseline`. It installs no missing harness files, authors no onboarding and no knowledge record, runs no citation fixer, and creates no skill folder. `runtime_install()` keeps its deterministic maintenance surface, and its scaffold carries no skills copy, so a missing skill folder is not a scaffold defect.

The knowledge foundation is a handover rather than a production step: setup reads `memory_init`'s `knowledge` block (`not-recorded`, `recorded` at an identity, `unusable`, or a refused admission with its own `nextAction`), reports that state, and names the next step — start the Architect, which organises optional onboarding and the foundation as regular task work through `c-14-knowledge-bootstrap`'s Curator route. A repository whose memory has a commit may still read `not-recorded` when setup ends, and that is the honest result rather than a gap to fill in setup. Existing memory still needs its foundation state read. The first-conversion procedure distinguishes an unattributed root converted in place from an official line converted inside a new leaf and landed normally. Certification is a separately requested operation, not routine closeout.

Authored migration prose uses the shared STE-inspired writing profile. Assessment procedures link it before their waves; later statements, family guarantees and history reasons preserve semantic scope, exact evidence identities and frozen history. Proposed rewrites receive independent meaning review before ordinary writer publication. This authoring addition does not make conversion a cosmetic rewrite or authorize bulk rewriting.

The source retains older provider-indexing phrases in its description, early stages and report inventory, while Stage 6 explicitly retires provider install/start/watch. These residual phrases are source inconsistency, not a restored provider route. User permission choices stay user-owned, host provisioning is runtime_install's operation, and the final dashboard command must use the actual serving installation.

## Evidence

- Adds migration-author use of the shared writing profile and independent meaning review; it changes authoring guidance, not converter admission or publication authority. [1]
- Adds migration-author use of the shared writing profile and independent meaning review; it changes authoring guidance, not converter admission or publication authority. [2]
- Adds migration-author use of the shared writing profile and independent meaning review; it changes authoring guidance, not converter admission or publication authority. [3]
- Adds migration-author use of the shared writing profile and independent meaning review; it changes authoring guidance, not converter admission or publication authority. [4]
- Adds migration-author use of the shared writing profile and independent meaning review; it changes authoring guidance, not converter admission or publication authority. [5]
