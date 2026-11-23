# Host-free adapter test for parent wakes

## Governing Overview

[Area overview](../overview.md)

## Purpose

Drive the contributed `registerParentWakeEvents` handler against a mock host, so the host-state read that decides whether a seat may be woken is exercised where it is installed rather than only in the pure decision.

## Contract

The test registers the real adapter on a mock event registry and host sender, with `PASEO_HOME` pointing at a temporary directory and both a seat and its parent in the role records. It fires one completed silent turn end and then advances the 60-second wait. A complete listing — a page that reports no further pages — is read once at the end and once at delivery, sends the seat one message and writes one `seat-message` row with count 1. Three incomplete walks — a missing continuation cursor, a repeated cursor and the eight-page cap — admit no timer and no delivery, write one `left-alone` row with the reason `host-state-unavailable` and count 0, and still give the parent MIK-R172's ordinary line. The cleanup the registration returns is called in every arm. A further case keeps a seat that left the role record from receiving its deferred resume, and three cases drive the Paseo 0.16.2 hook shape, with mock events that omit the `timeline` field: the ended turn read through `timeline.refetch` still shows a hand-over, the rows read that way keep their turn id so an earlier turn's hand-over does not count, and a refetch that throws gives an unreadable last line rather than an empty one. This is a mock host, not a live SDK adapter or a plugin-load proof.

The ordinary adapter cases exercise a new line to a closed parent, held lines owed to a closed parent and held lines about a closed child. Archive learned by hook or listing selects an alternate. The separate registry-backed reopened-child case is registered only when AR_TEST_REOPENED_ROLE_REGISTRY is set. It reads Worker-generated role registry bytes and injects the surviving child's next turn and end. The Worker owns repair-parent/reopened-registry-proof.py and w2-f03-verification/after-registration.json in W2-evidence.tar. The W4 supervisor uses that retained fixture. From the W4 plug-in root with the provisioned Node 22.23.2 and dependencies, set fixture to the extracted after-registration.json and run:

```sh
AR_TEST_REOPENED_ROLE_REGISTRY="$fixture" node --experimental-strip-types --experimental-test-isolation=none --test --test-name-pattern='a reopened child from the product registry' server/turn_events.test.ts
```

## Evidence


- The contributed adapter admits a seat wake only from an exhausted host listing. An incomplete walk leaves the seat alone and preserves the parent's line. [1]

- A turn event without a timeline exercises whole-tail refetch, recognition of a hand-over, turn-ID scoping and unreadable history. [2]

- The reopened-child case is registered only with the supplied registry fixture. Its adapter injects the next turn and its end. [3]
