# dashboard/index.html

## Governing Overview

[repository overview](../overview.md)

## Purpose

The dashboard's single HTML entry page. Vite serves and builds it; it holds the `root` element and loads `/src/main.tsx` as a module script.

## Code Commentary

The page sets `<meta name="referrer" content="no-referrer">` in its head, before any asset loads. That page policy makes the browser omit the referrer for the images, video sources, posters and nested sources that repository documents load inside the dashboard. The root element also carries `data-effects="on"` and the page title.

## Relationships

`dashboard/vite.config.ts` builds the dashboard from this entry. The referrer policy here is the page-level half of the repository-document media rules; the media filtering itself lives in the dashboard's document rendering code.

## Evidence

- The page sets a no-referrer policy before any asset loads. [1]
- The page holds the root element and loads the module entry. [2]
- The dashboard HTML mounts the application at `#root`, loads `/src/main.tsx` as a module and sets the referrer policy to `no-referrer`. [3]
