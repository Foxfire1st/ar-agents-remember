# dashboard/src/explainer/model.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer column's pure rules: which chat the column selects, the placeholder's words, the form's target and references, the build's steps and percentages, Retire's two lists and the header's menu.

## Code Commentary

- No network, no storage and no DOM: each function takes the state it needs and returns the words or rows to draw.
- A running build takes precedence over an open form. Building, live and closed phases select the explainer. First request, retired and placeholder phases select the placeholder.
- The first-request summary counts references and their nonempty notes. A nonempty message adds “your text”. An empty request labels the explanation as planned or end-to-end and calls for the essay first and the page last.
- A build uses the server's percentage when supplied. Otherwise it averages equal step shares, including partial progress for a counting step. Only a failed build names a failed step and reason.
- The agent menu puts the explainer first when it has an ID. Other seats must match the exact task scope when that scope is available.
- The planned-form placeholders tell the reader to leave the field empty for the requirement and planned effects.

## Evidence

- A running build takes precedence over an open form and a live seat. An observed live or closed seat takes precedence over a stale form. [2]


- Only a failed build names a failed step and a reason [5]

- Building, live and closed phases select the explainer. First request, retired and placeholder select the placeholder. [1]


- An explicit percentage takes precedence over the average of step shares. [4]
- An identified explainer leads the menu and other seats are filtered by task scope. [6]

- The summary chooses the planned or end-to-end line for empty requests and otherwise counts references and nonempty notes and labels the message as “your text”. [3]
- The planned form placeholders name the requirement and planned effects. [7]
