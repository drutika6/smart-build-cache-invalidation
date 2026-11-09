# Smart Build-Cache Invalidation

## Objective
Reuse a build when its inputs have not changed, and rebuild when an input changes.

## Steps
1. Created `cache_demo.py`.
2. Used Python’s SHA-256 hash to create a fingerprint from the build inputs.
3. Saved the fingerprint in `.build_cache.json`.
4. Ran the program twice with the same inputs. The second run reported a cache hit and reused the build.
5. Changed the version from 1 to 2 and ran it again. The program reported a cache miss and rebuilt.

## What I learned
A build cache avoids repeating work when inputs stay the same. When an input changes, its fingerprint changes, so the old cached build is not reused.

## How to run
Run `python3 cache_demo.py` in the project folder.

## GitHub repository
Add the GitHub repository link here after publishing the project.