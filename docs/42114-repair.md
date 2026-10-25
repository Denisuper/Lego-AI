# 42114 repair — 2026-10-25

The old 54-step draft did not follow the official booklet. Its first step introduced six blue pins and two red bushes; source step 1 introduces a black frame and two black pins. Renaming its invalid connection points would have preserved the wrong build.

The repair replaces all 54 existing steps directly from `sets/42114/booklet.pdf`, source pages 6–36, and rebuilds the matching chat examples with the shared system prompt, previous four steps and source page numbers. The original 456-page PDF remains unchanged. Step 42 spans pages 30–31. Step 54 ends during an unfinished outer-frame side build; its GROUP deliberately remains open for the continuation at step 55, page 37.

| Check | Before | After |
| --- | ---: | ---: |
| Numbered steps | 54 | 54 |
| Missing catalog point errors | 562 | 0 |
| Incompatible connection errors | 10 | 0 |
| Inventory pieces | 44 | 2,193 |
| Introduced pieces | Incorrect draft | 174 |
| Introduced pieces exceeding inventory by part and colour | Not reliable | 0 |

Inventory restored from Rebrickable's non-spare 42114-1 inventory version 1 (inventory ID 67064), matching the original 2020 booklet edition. It has 237 part/colour rows. Its catalog numbers include 42924 for blue long friction pins, 46189 for the black three-length two-pin connectors and 65489 for the grey four-pin connector. Older OMR design references use 6558, 15461 and 48989 for those positions; the training ADD records use the inventory numbers and their corresponding catalog points.

The official booklet determines part introduction and assembly order. The LDraw OMR [42114 model](https://library.ldraw.org/omr/sets/1225) was used as a read-only geometry cross-check for named holes and shaft positions. It does not resolve every interface and omits the assembled torque-limiter submodel from its main hierarchy; it is not a substitute for the booklet.

There are 21 explicitly unknown endpoints and 11 estimated endpoints. The catalog does not name the differential's internal carrier posts and crown retaining clips, the driving rings' sliding splines, the selector-to-ring interfaces, or the torque limiter's internal slipping interface. The three-length clutch connectors have only one named cross-bore point, so their shaft positions are estimated. The torque-limiter bracket's attachment-hole orientation is also estimated. These uncertainties are preserved rather than turned into fictitious exact point names.

Zero notation errors means the named connections fit the current catalog. It does not prove the complete physical build. The set remains `needs review`, is excluded from ready-only training packs, and still has 2,019 inventory pieces outside this 54-step transcription. Generic unreferenced-part warnings remain because the checker's motion verbs do not model structural load paths.
