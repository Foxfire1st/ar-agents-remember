# mcp/tests/test_held_delivery_tick_cost.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

What one held-delivery tick costs when nothing has changed.

## Code Commentary

The tick reads the host's publication and the role record for two decisions, and the finding this file guards was a second reader that parsed both files on every tick even when the host had written nothing. The cases count the reads, the stats and any bridge process for one seat and for a fleet.

**L184 — INV-1ZKP4R.** The cost bound is measured by this case, which is where a regression would show. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

A closed event can recheck held delivery once by its event stamp. That case ignores stale helper work and performs no usage read because no stored report is due; a due report adds one claimed read to the tick, two due reports and a stamped end share one batch, and an unchanged quiet tick starts none.

`test_two_due_reports_and_a_stamped_end_share_one_usage_batch` holds the shared batch; `test_a_failed_periodic_read_retains_the_fact_and_mapping` and `test_due_report_without_a_registered_seat_logs_once_per_period` hold the failure and no-seat paths; `test_a_due_provider_clear_releases_held_work_without_a_turn_end` holds the delivery order. `test_unchanged_quiet_ticks_parse_both_inputs_once` remains the zero-cost case.
