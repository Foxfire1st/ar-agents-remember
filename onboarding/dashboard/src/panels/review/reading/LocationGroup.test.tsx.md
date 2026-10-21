# dashboard/src/panels/review/reading/LocationGroup.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin opened location groups, in-place expansion and full role names.

## Code Commentary

### Logic

Opens the captured fixture's 31-location unchanged group, checks the full-width heading and quiet … 27 more control are excluded from the shared button styling, then expands to all 31 rows without retaining the more button. A second case opens both groups and checks their role cells use full role names, including primary-authority.

### Invariants And Boundaries

The full-role vocabulary and class/selector structure are checked in jsdom. The tests do not measure the group's rendered appearance.

## Evidence

- The group expands from its quiet more control to all 31 rows. [3]
- Opened rows use the full role vocabulary and the first unchanged role is primary-authority. [4]
