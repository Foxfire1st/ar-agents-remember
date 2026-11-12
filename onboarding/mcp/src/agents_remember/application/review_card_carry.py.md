# mcp/src/agents_remember/application/review_card_carry.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

An invariant's cards carried to a newer comparison only while everything they were made from still holds.

## Code Commentary

A card is carried to a newer comparison rather than re-authored, and only while every input it was made from still holds: the same memory trees and the same blobs. When one of them moved the carry does not happen, so a carried card never describes inputs it was not made from.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- carried_entries carries only the entries whose inputs still hold, and CardCarry is the shape a caller receives. [1]
