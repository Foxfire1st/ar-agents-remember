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
- 2026-09-08: Initial creation for MCAR L04
