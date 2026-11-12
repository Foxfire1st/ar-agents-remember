# dashboard/src/panels/review/ReviewHeader.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Compose the review page’s responsive top line: Back, task title and record label, status/comparison controls, refresh and keyboard reference.

## Code Commentary

`shortLeafId` reduces a dated uppercase leaf identifier to its `L<n>` suffix and otherwise keeps the identifier whole. The heading retains the complete identifier in its tooltip when shortened. The task projection supplies the title; absent titles display the leaf identifier.

`ReviewHeader` takes caller-owned `chip`, `comparison` and `refresh` nodes. Back calls `onBack`; the optional `record` label distinguishes historical or reconstructed content as supplied by the owner. `ReviewKeys` closes the line. This component neither derives read state nor changes selected subjects.

The title box gives width to the controls; title and record labels ellipsize with complete tooltips. At 40rem and narrower the title box and labels wrap within the top line. The refresh notice can occupy its own full-width flex row. The page owner determines whether this header is outside an independent scroller or part of the stacked page.

## Invariants And Boundaries

Caller components own task resolution, comparison state and reads. This module renders the provided controls and labels; it does not write judgments or certify browser geometry.

## Evidence

- Task/title/record controls and supplied owner nodes compose one top line. [3]
- Dated leaf ids shorten without changing their underlying identity. [4]
- Responsive title and record styling releases width without dropping complete tooltip text. [5]
