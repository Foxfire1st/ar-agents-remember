# dashboard/src/cockpit/paseoFrameModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Validate frame descriptors, native execution targets and normalized plugin navigation and tray messages.

## Code Commentary

Available descriptors require an HTTP(S) serving origin and server ID. Only native `paseo-agent` host fields supply an execution target, and rejected receipts supply none. Frame URLs encode agent/workspace identities. The descriptor carries the backend's provisioning command; when it names none, the existing command-template notice identifies that omission. [1]

Source-tagged messages distinguish readiness/pong abilities, host navigation, on-chat, drawn/failed chat, plural native selection, nullable shown chat and source-scoped Parent errors. An absent ability list means an older plugin, not inability to open agents; only an explicit list without `open-agent` requires URL navigation. Capability notices name missing abilities, the provisioning command and an earlier drawing-answer boundary. Wait text distinguishes host lookup, application drawing and an undifferentiated older chat wait; a late answer is described as slow. [2] [3] [4] [5]

Chat picks require nonempty text, an agent ID, a parseable message time and either a nonempty message ID or its absent/null value. Invalid IDs and missing/invalid time are refused rather than becoming provenance. Composer reports require finite top/height/frameHeight, nonnegative height and positive frame height; the message box's own left and width are admitted only together, as finite numbers with a width greater than 0, and a partial, non-finite or non-positive pair is dropped while the vertical report stays valid. Unavailable pick/composer reports require a reason. An explicit shown-chat report must carry an agent ID or `null`; an omitted value is invalid.

Both sides name `pick` for tray negotiation. The dashboard also advertises `showing`; its general missing-ability notice includes `pick`, while older shown-chat inference remains the controller's responsibility.

## Invariants And Boundaries

These are pure shape and value checks. Source tagging does not establish event origin/window trust; the controller supplies that boundary. Parsed native identifiers do not establish canonical task scope or whether an agent can be contacted.

Native web route spellings are version-sensitive. The model consumes no hierarchy snapshot; it keeps native selected rows, a pending navigation answer and the nullable chat actually shown as separate message forms.


## Evidence

- Non-rejected native execution fields supply frame targets. [1]
- Only supported source-tagged forms are normalized. [2]
- Explicit lack of open-agent differs from an absent capability list. [3]
- Plugin notices name missing abilities and provisioning. [4]
- Request text retains host/drawing/older wait distinctions and lateness. [5]
- Descriptor and route handling validate the serving origin and encode native identities. [6]
- Pick text, optional message identity and required message time are validated together. [7]
- Composer coordinates must be finite with valid heights. [8]
- The box's left and width are admitted only together, as finite numbers with a positive width. [11]
- Explicit null shown chat differs from an absent agent field. [9]
- The dashboard's advertised abilities include pick and showing. [10]
