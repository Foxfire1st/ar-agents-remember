# dashboard/src/panels/review/explainer/ExplanationRequest.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The request form the reviewer sends from, and the door every explainer build goes through.

## Code Commentary

Pressing Explain opens a form tied to that comparison, and a Send goes to the build's own endpoint for that scope; Cancel reaches the build it started. The form does not exist before the reviewer asks, so no page opens a build on its own.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A build is sent for the comparison the reviewer is looking at, with the request body naming that scope. [1]

- Cancelling reaches the build this form started, rather than leaving it running unwatched. [2]
