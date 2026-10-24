# mcp/tests/test_l192_retired_start_progress.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Keep a retired provider gate out of both surfaces that read the durable pre-contract progress file.

## Code Commentary

One owning boundary, `read_start_progress`, feeds two surfaces: the attention queue
(`build_attention_queue`) and the Engine Room process map (`build_engine_processes`). A file
written before the search providers were retired carries `phase: provider-blocked`, which no
surviving producer writes, so it is an obsolete record and must reach neither surface — while real
pre-contract blocks (stale base, source lineage, memory compatibility) still arrive, with the
actionable-drift alarm still ranked above them. The cases check both surfaces together for each
payload, and the last two set the bounds of the rule: retirement names the provider phase rather
than filtering broadly, and a future gate phase the producer does not write yet still reaches both
surfaces as an unknown process.

## Evidence

- A persisted provider gate reaches neither the queue nor the process map.
  `test_a_persisted_provider_gate_reaches_neither_attention_nor_the_process_map`
- Real pre-contract blocks still reach both surfaces, below drift.
  `test_real_pre_contract_blocks_still_reach_both_surfaces`
- A beat is progress, not an alarm; an unwritten phase is not suppressed.
  `test_a_happy_path_beat_is_progress_not_an_alarm`,
  `test_a_future_gate_phase_the_producer_does_not_write_is_not_suppressed`
