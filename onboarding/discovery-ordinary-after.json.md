# discovery-ordinary-after.json

## Governing Overview

[repository overview](overview.md)

## Purpose

A persisted ordinary-mode `tools/list` answer captured as the after operand of a historical discovery-contract comparison. This file is comparison data, not the executable tool registry or a fresh capture of the current W9 server.

## Source Commentary

The JSON has one `tools` array containing 42 complete tool declarations, including their ordered names, descriptions, schemas and annotations. Its bytes equal the companion `discovery-ordinary-before.json`; the checked historical comparison artifact records their canonical JSON identity. Those bytes describe that capture's source epoch. The current W9 source conformance pin is 43, so the retained 42-entry fixture must not be read as today's live advertised population.

The comparison producer is `scripts/compare-discovery-contract.py`. A persisted raw answer locates what that historical comparison used; it supplies neither a new server invocation, current installed-host proof, passing test result nor a timing guarantee.

## Evidence

- The stored ordinary-mode after answer contains the retained 42 declarations; it is historical capture data rather than a current live-server witness. [1]
