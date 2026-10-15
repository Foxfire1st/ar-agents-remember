# generated-copies.json

## Governing Overview

[Repository overview](overview.md)

## Purpose

Owns the candidate's declarative mapping from canonical `skills` to generated skill payloads. The declaration is shared input, not a second instruction source or evidence that a sync ran. Code consumers decide parsing, projection and candidate equality; this JSON supplies the source, target and ignore-policy data.

## Construction And Boundaries

Version 1 declares one canonical source, `skills`, with the MCP runtime package target and eight named harness targets. `ignoreNames` and `ignoreSuffixes` are part of that projection contract rather than a separate consumer-maintained census. A declared target is not automatically current or canonical.

The worklist recognizes equal declared copies by actual candidate source/copy equality and rejects symlink equality; ordinary exclusions and divergent copies retain their obligations. A raw nonregular declaration entry is present invalid input, including an empty tree, not an absent declaration. The sync owner consumes the same parsed mapping and validates its projected certification profile before replacing output targets.

This card neither opens nor modifies any generated mirror. It makes no migration, synchronization, test, runtime-delivery or acceptance claim.

## Evidence

- Versioned declaration names canonical skills, package/harness targets and exact ignore-name/suffix policy. [1]
- Candidate recognition compares declared source and copy blobs and keeps present nonregular declarations distinct from absence. [2]
- The common parser validates the declaration and constructs parsed copy projections. [3]
