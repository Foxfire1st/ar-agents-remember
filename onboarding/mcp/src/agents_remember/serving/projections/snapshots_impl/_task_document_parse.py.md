# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_document_parse.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Tolerate addressed future-version extra fields in read-only task projection while withholding genuinely invalid known content.

## Code Commentary

Projection validation retries on a deep copy with a fixed four-attempt bound. Only extra_forbidden locations may be removed; after removal the complete model is validated again. Known-field errors or exhausted attempts return None rather than manufacturing a document. Authoring remains strict.

Dict/list locations can be pruned, but synthesized union/ref locations that cannot address the raw payload do not justify deleting unrelated data. An unaddressable extra can exhaust the bounded retries and remain withheld. Successful model validation does not itself prove that the raw JSON carried a schema key: caller admission checks are a separate boundary.

## Evidence

- Read-side extra-field pruning is bounded, location-specific and distinct from raw-schema admission and strict authoring. [1]
