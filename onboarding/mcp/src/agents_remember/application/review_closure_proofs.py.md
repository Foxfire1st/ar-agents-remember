# mcp/src/agents_remember/application/review_closure_proofs.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Keeps closure proofs for object bodies read in a recorded comparison.

## Code Commentary

The request and process memo owners each hold up to 64 exact-root proofs and 16 latest-repository proofs. Native calls use the request owner. When supplied, the disk store keeps up to 64 proof files by default. Each envelope records the complete object-ID list, witness digest, reference stamp and layout digest. The answer owner re-observes the current layout, references and object presence before it relies on a proof.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence


- The disk store keeps up to 64 proof files by default. Each proof file holds the complete object-ID list and its witness, reference and layout stamps. [1]
