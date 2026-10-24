# docs/design/canvas-host.md

## Governing Overview

[governing route overview](overview.md)

## Purpose

The design of record for the generated review page's host and the review presenter (MIK-R104 at v2, MIK-R105 at v1). It states the two surfaces, how the dashboard's origin arrangement holds, how scripts are gated on the browser proof, what the browser does not contain, the readiness rule before a revision becomes ready, the host protocol, sessions and their limits, the presenter's admission and publication path, the panel, and the boundaries that remain.

## Code Commentary

- It opens on the two surfaces the document names: the frame route serving one admitted revision's bytes, and the trusted API route serving the panel; its changed API row says the old authoring POSTs are retired and refuse by name.
- It records the origin arrangement and the policy: the dashboard is local and unauthenticated as a deployment posture, which is why a request guard — not authentication — is what refuses a foreign writer, and why header-less CLI calls pass.
- Scripts are gated on the browser proof: the served policy digest, the enforcement bindings and the recorded checks must all cover what is being served, and a page whose proof does not cover it is served with no script at all.
- The protocol, session and presenter sections state the bounds once: a closed operation set, a host-created session bound to the exact frame and revision, and a presenter that admits an explicit attempt, confines its runner and publishes only after one model-free load.
- The closing section names the limits the document actually states: the kit is not a container, the frame's own navigation is an accepted channel, and a host that cannot confine the presenter's writes refuses with `presenter-confinement-unavailable` rather than running unconfined.

## Evidence

- The design states the two surfaces and the origin/policy arrangement. [1]
- Scripts are gated on the browser proof, and an uncovered page is served with no script. [2]
- The presenter, protocol and session bounds are stated once in one design document. [3]
- The remaining limits are named instead of being implied away. [4]

## Current authoring-path account

The changed API row documents retirement of the old authoring POSTs. The changed presenter section describes an injected confined runner receiving one attempt's prepared folder, and `UnconfiguredPresenterRunner` refusing by name when no runner is wired. It identifies the retired native presenter-tools launch and the explainer seat on the normal task server as the authoring path; the kept tools retain immutable packet/source reads and writes confined to the attempt's own assets. This card describes the design document's changed seams; it introduces no independent runtime guarantee or fresh execution evidence.

- The trusted API row documents retirement and named refusal of the old authoring POSTs. [5]
- The authoring section documents the injected-runner boundary, unconfigured refusal and retired standalone-native entry, while retaining the kept tools' bounded evidence/assets account. [6]
