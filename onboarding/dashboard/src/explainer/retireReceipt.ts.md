# dashboard/src/explainer/retireReceipt.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The receipt a retirement leaves, and which seat may show it.

## Code Commentary

A retirement receipt belongs to its generation and never to the seat that replaces it: a new seat opening after a retirement shows no receipt from the retired one. That is what keeps a receipt from reading as a live explanation's own note.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A receipt is shown only for the generation that retired, never for the seat that replaced it. [1]
