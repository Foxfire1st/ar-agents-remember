# Host-free adapter test for parent wakes

## Governing Overview

[Area overview](../overview.md)

## Purpose

Drive the contributed `registerParentWakeEvents` handler against a mock host, so the host-state read that decides whether a seat may be woken is exercised where it is installed rather than only in the pure decision.

## Contract

The test registers the real adapter on a mock event registry and host sender, with `PASEO_HOME` pointing at a temporary directory and both a seat and its parent in the role records. It fires one completed silent turn end and then advances the 60-second wait. A complete listing — a page that reports no further pages — is read once at the end and once at delivery, sends the seat one message and writes one `seat-message` row with count 1. Three incomplete walks — a missing continuation cursor, a repeated cursor and the eight-page cap — admit no timer and no delivery, write one `left-alone` row with the reason `host-state-unavailable` and count 0, and still give the parent MIK-R172's ordinary line. The cleanup the registration returns is called in every arm. This is a mock host, not a live SDK adapter or a plugin-load proof.

## Evidence

- The contributed adapter admits a seat wake only from an exhausted host listing; every incomplete walk leaves the seat alone and preserves the parent's line. [1]
