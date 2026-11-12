# mcp/src/agents_remember/application/review_closure_proofs.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Consumed object closures, kept on disk under the storage witnesses they were proven with.

## Code Commentary

A consumed object's closure is stored beside the digest of the witnesses it was proven under, so a later read can tell a proof that still applies from one whose witnesses moved. The store answers with the stored closure only while that digest matches.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- ClosureProofStore keeps each closure with its witnesses and layout digests rather than alone. [1]
