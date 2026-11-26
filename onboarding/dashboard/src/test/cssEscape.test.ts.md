# dashboard/src/test/cssEscape.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Verifies that the jsdom `CSS.escape` stand-in installed by `dashboard/src/test/setup.ts` serializes CSS identifiers according to CSSOM rules and produces valid `querySelector` attribute selectors.

## Code Commentary

Five Vitest cases exercise the global `CSS.escape` stand-in loaded via `vitest.config.ts`:

- Leading ASCII digits (`"0"`, `"1abc"`, `"9-tail"`) serialize as a hex code point followed by a trailing space (`"\\30 "`, `"\\31 abc"`, `"\\39 -tail"`).
- A hyphen followed by an ASCII digit (`"-0"`, `"-1foo"`, `"-9"`) serializes as `-` plus the escaped digit (`"-\\30 "`, `"-\\31 foo"`, `"-\\39 "`).
- A standalone hyphen (`"-"`) escapes to `"\\-"`, while double-hyphen custom properties (`"--custom-prop"`) and hyphen-letter identifiers (`"-foo"`) remain unchanged.
- Empty strings stay empty, `NULL` (`"\0"`) becomes `"\uFFFD"`, ASCII control characters (`0x01`–`0x1f`, `0x7f`) escape as hex plus space, punctuation (`"a:b.c[0]"`) is backslash-escaped, and plain identifiers (`"plain_ident-2"`) stay intact.
- DOM lookup exercises both unquoted (`[data-key=${CSS.escape(key)}]`) and quoted (`[data-key="${CSS.escape(key)}"]`) attribute selectors via `root.querySelector` for leading-digit, hyphen-digit, standalone-hyphen, and punctuated keys.

The DOM case checks attribute selectors (matching React Aria's lookup pattern) rather than `#id` shorthand, because jsdom 25's `nwsapi` selector engine mishandles hex-escaped `#\30 ` ID shorthand.

## Relationships

Tests the `globalThis.CSS.escape` stand-in (`escapeCssIdent`) defined in `dashboard/src/test/setup.ts`, which Vitest loads before every test through `dashboard/vitest.config.ts` `setupFiles`. It does not import `setup.ts` directly and asserts no React Aria component rendering.

## Evidence

- Five Vitest cases check leading digits, hyphen-digit pairs, standalone hyphen vs custom properties, NULL/controls/punctuation, and `querySelector` attribute selectors against `CSS.escape`. [1]
- The stand-in under test implements CSSOM identifier serialization in the shared Vitest jsdom bootstrap. [2]
- Vitest loads `setup.ts` via `setupFiles` before running this suite. [3]
