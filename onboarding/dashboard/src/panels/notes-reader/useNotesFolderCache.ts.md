# dashboard/src/panels/notes-reader/useNotesFolderCache.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Adapt one-folder paging and retained cache state to the shared ExplorerTree.

## Code Commentary

Stable store and paging callbacks accumulate folder parts, fill only toward the open note, expose next-part rows, and empty vanished folders with their reason. LRU eviction targets 32 folders while protecting the current insertion and open-note ancestors; if every victim is protected, the target is not an unconditional ceiling. Reader refresh generations invalidate the cache and stale completions cannot repopulate an inactive lifetime.

## Boundaries

Only folder transport and view state: no content, requirements, decisions or report rendering and no second tree. Lifetime belongs to the repo/master-keyed NotesTree.

## Evidence

- useNotesFolderCache is a current owner of the behavior described above. [1]
- useFolderPaging is a current owner of the behavior described above. [2]
- evictFolders is a current owner of the behavior described above. [3]
