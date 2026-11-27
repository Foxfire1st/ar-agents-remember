# mcp/src/agents_remember/application/review_memo_store.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Persists symbol spans, blob-pair diffs, tree search paths and each search's latest-tree origin.

## Code Commentary

Every row retains the complete key its calculation needs. The store namespace binds source, grammars (`_grammar_identity` combines tree-sitter/grammar package digests with `grammars.extractor_version(grammars.default_language_set())`, covering packaged `.scm` query digests), and Git identity. A consumer still reads or probes the required object before using an answer.

Restore admits saved rows through the resident memo and then replays entries already held. Save merges disk and resident rows under that memo's entry and configured byte limits. Encoding keeps the newest rows that fit the separate disk envelope.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- `_grammar_identity` hashes tree-sitter and grammar packages alongside the default `LanguageSet` `extractor_version` so query changes separate memo namespaces. [2]

- _Stored binds a named live memo to its row encoder and decoder. _Rows represents the encoded disk rows, and _question selects a memo by its name. [1]
