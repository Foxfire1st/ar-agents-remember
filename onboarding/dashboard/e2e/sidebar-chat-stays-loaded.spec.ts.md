# dashboard/e2e/sidebar-chat-stays-loaded.spec.ts

## Governing Overview

[agents-remember root overview](../../overview.md)

There is no route-local overview for `dashboard/e2e/`, so the repository root
overview is the nearest governing ancestor (same resolution as the
`dashboard/e2e/cockpit.spec.ts` sidecar).

## Purpose

The MIK-R122 rule-8 browser walk over the Projects/Leaf/Master/Ghost fixtures, sampling iframe-element/`src` transitions as a DOM proxy for loads; unexecuted in the leaf, and its labels are fake-host text, not native screens.
Written for Dagger-path execution on the Owner's evidence path; unexecuted in the leaf.

## Code Commentary

The spec redirects the frame host to the fake Paseo host, samples iframe replacement and `src` changes with a MutationObserver (samples include element disappearance, so the proxy is lossy), checks fake-agent label text equality per leg (text, not screen visibility; only the ghost launcher's visibility is asserted), logs per-leg LOAD-CENSUS values, and asserts only the final sampled total is one. Load counting is element-identity based; draft, scroll, composer and banner content are not asserted.

## Evidence

- The fixture walk samples iframe/src transitions per leg and asserts only the final sampled total is one. [1]
