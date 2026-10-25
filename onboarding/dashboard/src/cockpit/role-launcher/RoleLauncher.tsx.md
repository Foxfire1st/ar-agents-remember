# dashboard/src/cockpit/role-launcher/RoleLauncher.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The extracted role launcher: one row of controls that fills or accepts a selection, reports preparation progress and one failure line, and dispatches a start.

## Code Commentary

`RoleLauncher` follows TaskEntry children for its reference options, without reconstructing document/series joins, and composes document fields, override fields and the action bar. roleLauncherDisplay owns pure chosen/default labels, roleLauncherReadiness owns readiness predicates, and useLauncherSelectionRepair owns the document-then-override repair effects. The local field components render accessible selectors without visible titles, information chips and action buttons from the admitted selection and options. Selectors use `launcherSelect` from `grammar/viewTabLook`; chips and buttons take their look from the same shared tab definition. Start uses the selected-tab look and Refresh the unselected look. Role, agent, model, effort and selectable-feature hovers retain their complete chosen-or-default label, purpose and applicable default provenance. A document selector whose reference matches a selected option retains its complete document label, purpose and canonical identity in hover. When no option matches (`optionIndex` is empty), its hover names only the purpose — Sprint, Master or Task — not the visible empty placeholder or a document identity. Long selected values may ellipsize, but their recovered hover text does not.

The earlier ordinary task-needing role/sprint/master/task/agent/model/effort/one-feature/mode/Start/Refresh composition was measured as fitting one line at 1440px; that is retained layout evidence, not a new guarantee for the added step-up/status controls. Extra controls or narrower space wrap by whole controls, without an overflow menu; the strip is not an unconditional fixed-height or wide-nowrap container. Reply length still cannot grow it because execution/reply prose is absent. During preparation, the Start label carries the shared progress phase; failures retain the existing single actionable line. The mode and optional Instructions are chips, permission-bearing features are settings-owned chips, and selectable features share the row's selector. Service-tier disclosure keeps its test id as a shared chip; while the selected execution is stepped up, its Base label and hover explicitly deny that it is the applied tier.

The Chats pane and document rail share this extracted owner. Bound callers hide references already determined by their selection and retain uncertainty/retry identity. Ordinary singleton and Projects bound rows prohibit a second open-request start; selected sprint/master Investigator rows retain their backend-admitted per-request exception. Choice ordering and start/options payloads retain their existing owners. A selected bound seat with status `held` is labeled “(held)” and counts as a live occupant, disabling another ordinary bound Start. That state extension does not change the shared visual authority or add execution prose. Explicit model and effort UI changes retain feature values; inherited invalid-catalog model/effort repair drops them, and an invalid explicit agent id clears the override. No second workspace list, report navigation or execution-prose surface is introduced.

## Current Contract

The same shared `roleLauncherGrid` composes the launcher. Its action row adds one configured Step up control and shared receipt-derived StepUpStatus beside Start/Retry/Revive/Result/Refresh. Step up is disabled for incomplete selection, unavailable options, busy/loading state or an offered retry. Ordinary Start still uses its existing readiness/occupancy guard. A truthy current execution stepUp switches mode/instruction/features and service tier to explicitly non-applied Base previews; applied mode/features remain unreported. The failure component receives showStepUp=false to avoid duplicate status. Existing whole-control wrapping is retained; no unconditional single-visual-line promise follows from these additions.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence




- The final Start guard joins backend startability, preparation and bound-seat occupancy. [1]

- Bound mode omits the reference fields the selection already determines. [2]

- Preparation is carried by the Start label rather than an extra ordinary status line. [3]


- The visual grid keeps whole-control wrapping. [6]



- The complete selected document label and identity survive truncation in hover; an empty or unmatched document selector instead names only its purpose. [7]


## Investigator scope and request identity

Ordinary singleton and Projects bound rows still adopt an open request and disable a second start. Selected sprint/master Investigator rows may start another per-request execution under backend capacity admission; existing uncertainty still preserves the exact request for Retry. The exception changes receipt cardinality without adding controls, execution prose, report navigation or primary-chat replacement.


- Readiness retains ordinary singleton gating and the request-scoped exception. [5]


## Refreshed current evidence


- The shared composition wires field sections, repair effects and the action bar. [4]


- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [8]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [9]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [10]

- Worker/Curator typed review census, record-only exclusion and unknown history. [11]

- Reason admission, threshold and differing-harness/model inheritance boundary. [12]
