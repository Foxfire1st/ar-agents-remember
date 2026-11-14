# dashboard/e2e/sidebar-chat-stays-loaded.spec.ts

## Governing Overview

[agents-remember root overview](../../overview.md)

The repository root overview governs this fixture, alongside the cockpit browser spec.

## Purpose

Defines a browser walk through the development document-chat harness to check retention of the Role chats iframe across eight navigation legs.

## Code Commentary

The fixture redirects `/h/` requests to the development fake host. Its observer increments a counter when the iframe element changes or its `src` changes, including element disappearance. This is a lossy element/address mutation census; it does not count network document loads. The walk visits master chat, river, chat, a task, another task, the master, an agentless document and the first task. Agent checks compare the fake host's label text rather than native screen visibility. The agentless leg checks the launcher's visible no-role notice. Draft, scroll, composer and banner content are not asserted.

The case records the counter after every leg and asserts a final value of one. This card describes the executable assertions and fixture boundaries; it records no browser run or measurement of the developer's browser.

## References

- Counts changes to the iframe element or its src attribute. [2]
- Defines the eight navigation legs and the final mutation-count assertion. [3]
