# mcp/src/agents_remember/serving/changeset_generation.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Observe the native inputs that determine whether an existing change-set result can be reused, without invoking Git on every unchanged read.

## Code Commentary

Git remains the authority for repository/configuration locations and ignored-directory selection. Layout discovery retains configuration origins, includes, conventional absent configuration paths, ignore/attribute files, environment and alternates. Changes invalidate discovery rather than selecting a guessed repository.

Filesystem identities include link and target inode/mode/size/mtime/ctime. Working manifests skip only directories Git proves ignored as directories, not directories whose present contents merely happen to be ignored; governing directory and .gitignore identities detect late arrivals. Selected references and replacement references participate without invalidating a task for an unrelated sibling ref. Object observations preserve existing content on additions but revoke successful reuse on removal or replacement; absence proofs also change when objects arrive. A failed or inconsistent observation raises to the cache’s uncached fallback, never supplying a successful key.


## Current Behavior

the module now observes Git's own signals. `working_generation(root)` (`:94-135`) runs one `git status --porcelain=v2 -z --untracked-files=all` child and folds each changed path's own identity into the digest, so a same-letter content edit is seen; `count_objects(root)` (`:138-162`) reads Git's loose/packed/alternate census; `RepositoryLayout.object_presence` (`:226-257`) is a direct loose-object stat or a pack `.idx`/`.pack` identity set, never a store walk. `tree_identity` is now only for a named file or small directory. `working_manifest` and `ObjectGeneration` are deleted. This supersedes the Purpose sentence 'without invoking Git on every unchanged read': a working read now runs one status child by design, and a commit pair is keyed by ids rather than observed. The module remains the observation owner, not a diff owner.

## Evidence

- Filesystem generations include directory names, symlinks, ctime and unskipped descendants. [1]
- Object observations distinguish stable existing objects from revoked content and absence proofs. [2]
- Native locations/configuration are discovered through Git and retained with their governing inputs. [3]
- Only directory-level native ignore proof permits skipping a working subtree. [4]