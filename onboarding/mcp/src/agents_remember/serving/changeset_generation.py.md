# mcp/src/agents_remember/serving/changeset_generation.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Observes the Git inputs that determine whether an existing change-set result can be reused.

## Code Commentary

Git remains the authority for repository/configuration locations and ignored-directory selection. Layout discovery retains configuration origins, includes, conventional absent configuration paths, ignore/attribute files, environment and alternates. Changes invalidate discovery rather than selecting a guessed repository.

Working generations fold Git status and current path identities into the key. Object presence checks use a direct loose-object stat or a pack index and pack identity set for the selected object. Layout and witness failures prevent successful reuse where the route requires those observations.


## Current Behavior

`working_generation` runs Git status and observes the actual changed paths, including edits that keep the same status letter. `count_objects` reads loose, packed and alternate counts. An unchanged observation can reuse a saved census. A native request owns that census and its witness until the request exits. Dashboard reads use a separate count-bounded process memo. An unavailable or changed witness leads to a current observation.

## Evidence



- A small named-input generation includes file and directory identities for the admitted subtree. [1]




- A named-object observation checks its loose file or the identities of the applicable pack files and indexes. [2]


- Native locations/configuration are discovered through Git and retained with their governing inputs. [3]


- The working generation uses Git's porcelain-v2 status and folds in each changed path's file identity. [4]
