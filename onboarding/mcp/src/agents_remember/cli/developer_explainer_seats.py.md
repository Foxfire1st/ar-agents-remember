# mcp/src/agents_remember/cli/developer_explainer_seats.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The tray's second recipient class: a leaf explainer's live seat.

## Code Commentary

A leaf's explainer seat is addressed as its own recipient class rather than as a developer, so a message for a live seat cannot land in a developer's tray and a developer's reply cannot be read as a seat's.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- explainer_recipient resolves a leaf explainer's seat as its own recipient class. [1]
