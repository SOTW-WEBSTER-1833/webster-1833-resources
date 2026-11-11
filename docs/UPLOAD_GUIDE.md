# Manual installation | Webster's Bible (1833)

## Target foundation

Recommended separate organization `SOTW-WEBSTER-1833` and repository `webster-1833-resources`. Use a **public**, initially empty repository. Use `main` as the default branch. Do not initialize a competing README, license, or .gitignore if uploading this source package verbatim.

## Install the numbered packs

1. Unzip the outer `SOTW_WEBSTER1833_MANUAL_UPLOAD_KIT_2026-11-10.zip`.
2. Extract `UPLOAD_PART_01_of_19.zip` into a folder; select **the files and folders inside it** (not the wrapper folder or ZIP) and use GitHub's repository root `Add file` / `Upload files` (or `uploading an existing file` on an empty repository).
3. Commit to `main` and repeat in sequence through Pack 19. Every package has at most 95 files; each file is under 25 MiB. The 19 packs have no duplicate repository-root file paths.
4. GitHub does **not** automatically unpack ZIP uploads. The extracted folder hierarchy must be preserved: `books/`, `data/`, `docs/`, `assets/`, `scripts/`, plus root files.
5. Verify all 1,797 repository files, 66 book catalogs, 1,189 chapter files and 31,102 verse records, using `RELEASE_MANIFEST.json` (SHA-256 values) and `UPLOAD_PLAN.json` (partition map).

## Publish the reader separately

After all packs have been installed, open repository `Settings → Pages` and choose `Deploy from a branch`, branch `main`, folder `/(root)`, then Save. Planned website: `https://sotw-webster-1833.github.io/webster-1833-resources/` if those exact names are used.

Test Genesis 1:1, Psalm 23, Matthew 1, Romans 10, and Revelation 22, chapter navigation, `#GEN.1.1`, `?ref=GEN.1.1`, and mobile display. No site deployment or external browser test is claimed by the archive.

Source provenance remains in the technical metadata. The public reader carries only Webster 1833 / Servants of the Way branding. No Strong's data or commentary is included.
