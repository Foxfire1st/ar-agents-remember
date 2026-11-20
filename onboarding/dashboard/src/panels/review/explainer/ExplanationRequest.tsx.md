# dashboard/src/panels/review/explainer/ExplanationRequest.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The review panel's comparison-scoped first-request and build form.

## Code Commentary

Pressing Explain opens a form tied to that comparison. Send goes to the build endpoint for that scope and Cancel targets the displayed running attempt. The form opens on request. A planned binding offers the requirement and planned effects in its placeholder. The recorded placeholder offers the end-to-end explanation. The shared first-request line follows the binding.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A build is sent for the comparison the reviewer is looking at, with the request body naming that scope. [1]

- Cancel targets the displayed build attempt. [2]
- The planned and recorded forms offer distinct empty placeholders and use the shared first-request line. [3]
