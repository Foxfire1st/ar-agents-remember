# Managed-sync Git implementation

## Governing Overview

[Worktree lifecycle](../overview.md)

## What This Area Is

Exact Git reading, carrying, parking, reapply proof and cancellation support for resumable code and memory-content sync. The compatibility facade preserves the previous import surface; the qualified modules own implementation and evidence.

## Hot Path Summary

`_read` supplies exact refs and complete stash inventory; `_proof` constructs the native expected reapply; `_stash` parks/reapplies work; `_cancel` assesses ownership and preserves unattributable bytes before discard; `_merge` owns converted-memory carry/validation; `_base` supplies shared result vocabulary.

## Operating Model

The driver journals authority and orders code before memory. These helpers prove actual Git state; a status label, sample, cached row or another merge algorithm cannot substitute for that proof. Converted memory merges are structurally planned and validated against both parents and paired code; incoming fast-forwards validate before refs move. Content, validator and repository-hook stops retain different recovery meanings.

Restoration and cancellation ownership are distinct. Full parked inventory and native reapply equality establish restoration; exact index/stash or retained fingerprints establish attribution. Failed attribution never blesses owner work. Cancellation first saves later/unproved bytes with verified manifests and binary patches, then discards and rolls back. The original stash remains authority until terminal recovery. Only the memory root memory.md is disposable cache; a code file with that name remains ordinary content.

## Invariants And Boundaries

- Expected-value pins and typed side identity prevent destructive action on an unrelated ref or checkout.
- Native merge configuration and carried attributes govern expected content; merge-file or alternative-algorithm output is not a fallback.
- Diagnostic samples never establish complete restoration; renamed carried paths require explicit supported matching.
- Structural validation is not semantic approval, and a repository hook is not task acceptance.
- Saving unattributable bytes does not make them owned transaction output; failure to save retains recovery authority rather than authorizing loss.
- This package owns no task acceptance, final integration decision or Git closeout authority.

## Evidence

- Compatibility exports preserve qualified implementation boundaries. [1]
- Complete stash inventory is distinct from its display sample. [2]
- Native expected reapply has one configured merge owner. [3]
- Saved unproved state is written before destructive cancellation. [4]
- Incoming memory fast-forwards validate before moving refs. [5]
