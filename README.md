# Servants of the Way Digital Library | Webster's Bible (1833)

Independent, text-only **Webster's Bible (1833)** translation foundation following the established ASV 1901 / KJV 1769 book, chapter, and verse data layout.

**Coverage:** 66 books, 1,189 chapters and 31,102 verses. Canonical IDs are shared (`GEN.1.1`); edition IDs are independent (`WEBSTER1833:GEN.1.1`).

- `index.html`: public Bible book selector.
- `books/<slug>/site/index.html`: book/chapter/verse readers.
- `data/webster1833/<slug>/chapters/NN.json`: English verse text, with printed supplied-word italics as `spans`.
- `data/webster1833/catalog-<slug>.json`: per-book metadata and navigation structure.
- `data/webster1833/route-map.json`: logical future cross-foundation reference hooks.
- `docs/EDITION.json` and `docs/SOURCE_LOCK.json`: digital source identity, rights, per-file provenance and SHA-256 locks (source data retained in metadata, **not displayed** in reader).
- `docs/UPLOAD_GUIDE.md`: owner installation and GitHub Pages setup.

Presented by the **Servants of the Way Digital Library**. No scans, embedded Strong's data, dictionary content or historical commentaries; future verse-click study information belongs to the existing independent foundations. This package does not alter any other repository or deploy a site.
