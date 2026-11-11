# Stable Scripture identity and cross-foundation compatibility

- `GEN.1.1` identifies a Scripture reference independently of its translation.
- `WEBSTER1833:GEN.1.1` identifies this Webster Bible verse's edition record.
- The English text appears only in `data/webster1833/{slug}/chapters/{NN}.json` using ASV/KJV-compatible `verses[]` and `spans[]`.
- Separate original-language repositories already index `WEBSTER1833` for accepted word-link evidence. That data is not Scripture text and is not imported here.
- An English verse reference is NOT proof of word-by-word correspondence across translations. Do not infer Strong's alignments, token offsets, or original-language meanings from the English spans.
- Historical-commentary passages can be joined by shared canonical references, but no API, commentary text, or UI integration is asserted as operational.
- The existing ASV, KJV, original-language repositories, and CGBC player remain unmodified by this standalone release.
