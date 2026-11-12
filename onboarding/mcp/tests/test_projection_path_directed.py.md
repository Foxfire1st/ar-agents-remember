# mcp/tests/test_projection_path_directed.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rule 2 (F09): one-change reads ignore unrelated corpus size.

## Code Commentary

The suite checks documentary rewrite, append/delete, task atomic rewrite/delete, declared membership and cross-folder consumers with byte-equal full references and read sets at two corpus sizes. Lifecycle-log inputs and their append/rewrite/delete cases are removed. Reciprocal membership chooses one parent; child entries own their facts, each parent lists the child key once, and all canonical task entries remain reachable. The ordered-sibling regression still breaks a retained dependency cycle, compares the full reference and checks both dependency lists and master frontier. Closure validation ignores unrelated documents. These controlled counts are not installed timing, host-delivery or acceptance proof; retired gate/terminal projection cases are not current coverage.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Task edits match the full reference and reciprocal membership chooses one parent. [2]
- Task-only atomic replacement/deletion read sets stay bounded at both sizes. [3]
- Breaking a cycle updates master frontier and both dependency directions. [4]
