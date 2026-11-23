# mcp/tests/test_object_census_witness.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for object census witness.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

The native cases verify within-request reuse and release for small and large alternate populations. The shared history test checks the fixed-size alternate fingerprint and the different revision transitions under strict and tolerant addition policy.

Two identical unscoped change-set snapshots run one census, as checked by `test_two_identical_requests_run_one_census`.

## Evidence

- Two identical requests run one census, witnessed by test_two_identical_requests_run_one_census [1]
