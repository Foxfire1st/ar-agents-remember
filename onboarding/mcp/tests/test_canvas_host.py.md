# mcp/tests/test_canvas_host.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The host's HTTP and protocol boundary: what a page may load, what a session may ask, and which evidence reference opens — one case per host rule, against the real policy, validator and a published revision.

## Code Commentary

- Script enablement is decided by the proof record and the served policy, so an unproven policy serves no script at all.
- Every response carries its policy headers; a session serves its own document and assets and refuses anything else.
- Protocol messages are bound, bounded and replay-safe before an effect.

- Proof-consumer cases use the fabricated frontend fixture and real binding functions. Changing its frontend bytes must invalidate the bound proof; these fixtures do not produce browser evidence.

## Evidence

- The case `test_an_unproven_policy_serves_no_script_at_all` protects this behaviour. 

- The case `test_a_proof_is_bound_to_the_exact_policy_digest` protects this behaviour. 
- The case `test_every_response_carries_its_policy_headers` protects this behaviour. [3]

- Changing the consumer frontend invalidates its bound proof. 

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_host.py::test_an_unproven_policy_serves_no_script_at_all - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/tests/test_canvas_host.py::test_a_proof_is_bound_to_the_exact_policy_digest - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/tests/test_canvas_host.py::test_a_consumer_frontend_change_invalidates_its_bound_proof - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
