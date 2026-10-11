# dashboard/src/cockpit/role-launcher/RoleLauncher.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The extracted role launcher: one row of controls that fills or accepts a selection, reports preparation progress and one failure line, and dispatches a start.

## Code Commentary

`RoleLauncher` renders accessible selectors without visible titles, information chips and action buttons from its admitted selection and options. Selectors use `launcherSelect` from `grammar/viewTabLook`; chips and buttons take their look from the same shared tab definition. Start uses the selected-tab look and Refresh the unselected look. Role, agent, model, effort and selectable-feature hovers retain their complete chosen-or-default label, purpose and applicable default provenance. A document selector whose reference matches a selected option retains its complete document label, purpose and canonical identity in hover. When no option matches (`optionIndex` is empty), its hover names only the purpose — Sprint, Master or Task — not the visible empty placeholder or a document identity. Long selected values may ellipsize, but their recovered hover text does not.

The ordinary task-needing role/sprint/master/task/agent/model/effort/one-feature/mode/Start/Refresh composition fits one line at 1440px. Extra controls or narrower space wrap by whole controls, without an overflow menu; the strip is not an unconditional fixed-height or wide-nowrap container. Reply length still cannot grow it because execution/reply prose is absent. During preparation, the Start label carries the shared progress phase; failures retain the existing single actionable line. The mode and optional Instructions are chips, permission-bearing features are settings-owned chips, and selectable features share the row's selector. Service-tier disclosure keeps its existing meaning and test id as a shared chip.

The Chats pane and document rail share this extracted owner. Bound callers hide references already determined by their selection and retain uncertainty/retry identity. Ordinary singleton and Projects rows prohibit a second open-request start; selected sprint/master Investigator rows retain their backend-admitted per-request exception. Choices, ordering, disabled branches and start/options payloads are unchanged. Model and effort changes retain explicit feature values; an invalid explicit agent id still clears the override. No second workspace list, report navigation or execution-prose surface is introduced.

## Evidence

- A bound row decides startability from the bound role, the live occupant and the canStart answer. [1]
- Bound mode omits the reference fields the selection already determines. [2]
- Preparation is carried by the Start label rather than an extra ordinary status line. [3]
- Whole-control wrapping replaces unconditional fixed-height/wide-nowrap presentation. [6]

- The complete selected document label and identity survive truncation in hover; an empty or unmatched document selector instead names only its purpose. [7]

## Investigator scope and request identity

Ordinary singleton and Projects bound rows still adopt an open request and disable a second start. Selected sprint/master Investigator rows may start another per-request execution under backend capacity admission; existing uncertainty still preserves the exact request for Retry. The exception changes receipt cardinality without adding controls, execution prose, report navigation or primary-chat replacement.


- The current source preserves singleton/Projects gating and the selected Investigator exception. [5]


## Refreshed current evidence

- The shared owner renders selectors, chips, progress-labelled actions and the existing failure line for both hosts. [4]
