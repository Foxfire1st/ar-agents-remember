# mcp/src/agents_remember/application/memory_quality/census.py

## Purpose
Memory census module for complete affected-memory census in the closeout pipeline.

## Key Classes/Functions
- MemoryCensus - Main census class for tracking affected memory artifacts
- CensusRow - Individual row in the census representing an affected artifact
- CensusResult - Result of running the census

## Dependencies
- Used by closeout pipeline for memory quality checks
- Integrates with curator checklist and quality gates

## Update History
- 2026-09-08T14:45:44+00:00 — CCR-L24 preparation normalized the inherited date-only history bullet to an offset-bearing ISO timestamp while preserving its date and text.
- 2026-09-08T00:00:00+00:00 — Initial creation for MCAR L04
