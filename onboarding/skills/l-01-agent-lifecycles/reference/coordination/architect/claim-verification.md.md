# skills/l-01-agent-lifecycles/reference/coordination/architect/claim-verification.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The Architect's rules for checking a reported claim before ruling on it. It grants no additional authority.

## Code Commentary

Five short rules, each under its own heading: claimed sends are checked in the message log and ruled on from recorded facts without waiting for a resend; a behaviour-preservation requirement needs a same-day run, and an unrun behaviour claim is not stated; the existing design and its origin are established before an observation is called a defect; the complete code path is read before a ruling, read once more before ruling against an agreed Worker, Reviewer and Manager reading, and a wrong ruling is withdrawn plainly; and a claim about a file's origin or handling outside scratch is accepted only after reading the file, its creation time and the session record. The Architect role points here before ruling on a reported claim.

## Evidence

- Sends are verified in the message log; preservation claims need a same-day run; a design's origin is established before calling it defective. [1]
- The complete code path is read before ruling, re-read before overruling an agreed reading, and a wrong ruling is withdrawn plainly. [2]
- Claims about files outside scratch are checked against the file, its creation time and the session record. [3]
- The Architect role points here before ruling on a reported claim. [4]
