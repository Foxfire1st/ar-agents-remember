# dashboard/src/panels/lifecycle-list/columnPresentation.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Own the task column’s local typography/layout and controlled grouping controls. Removed pickup-warning dismissal is not part of this owner.

## Code Commentary

The extracted styles retain bounded one-line row cells, state-tone variants, indentation, wrapping head tools and focus-visible treatments. The controlled React Aria pivot accepts only repo/phase and mounts the shared AttentionQueue; row/tree/state derivation remains with the existing data/presentation owners.

TaskPivotBar renders the task count, controlled repo/phase toggles and the shared AttentionQueue without writing task state. The module exports no PickupDismiss and calls no operator-inbox dismissal adapter: incoming L113 removal remains effective after the L162 extraction. The row word is task-own state, not a composite gate/chat/pickup priority. Local typography and control source alone establish no assembled narrow-column browser proof for the L162 major-step lane.

## Evidence


- Extracted column styling and controlled grouping pivot preserve separate row derivation and task-own state; there is no pickup dismissal control. [1]

