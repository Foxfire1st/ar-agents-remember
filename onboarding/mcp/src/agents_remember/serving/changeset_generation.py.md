# mcp/src/agents_remember/serving/changeset_generation.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Observe the native inputs that determine whether an existing change-set result can be reused, without invoking Git on every unchanged read.

## Code Commentary

Git remains the authority for repository/configuration locations and ignored-directory selection. Layout discovery retains configuration origins, includes, conventional absent configuration paths, ignore/attribute files, environment and alternates. Changes invalidate discovery rather than selecting a guessed repository.

Filesystem identities include link and target inode/mode/size/mtime/ctime. Working manifests skip only directories Git proves ignored as directories, not directories whose present contents merely happen to be ignored; governing directory and .gitignore identities detect late arrivals. Selected references and replacement references participate without invalidating a task for an unrelated sibling ref. Object observations preserve existing content on additions but revoke successful reuse on removal or replacement; absence proofs also change when objects arrive. A failed or inconsistent observation raises to the cache’s uncached fallback, never supplying a successful key.

## Evidence

- Filesystem generations include directory names, symlinks, ctime and unskipped descendants. [1]
- Object observations distinguish stable existing objects from revoked content and absence proofs. [2]
- Native locations/configuration are discovered through Git and retained with their governing inputs. [3]
- Only directory-level native ignore proof permits skipping a working subtree. [4]
