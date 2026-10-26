# Defender 42110 transcription

The original 496-page booklet and 2,573-piece inventory are preserved. Source transcription currently reaches step 408, page 240, with 1244 introduced pieces, no excess by part and colour and zero notation errors. The table and JSONL match; the remaining 1,329 inventory pieces are not yet transcribed. 245 unknown and 394 estimated endpoints remain explicit, including differential carrier posts, complete universal-joint orientation and suspension ball sockets. Continue at source step 409, page 241.

The booklet takes precedence. Philippe Hurbain's [OMR-compliant reference model](https://forums.ldraw.org/thread-23139.html) is a read-only geometry cross-check, saved outside the repository. Its internal yoke and spider representations are accounted for using complete universal-joint inventory part 61903. Model traversal is ordered with the rear axle first to match the booklet's module order; model order does not determine the source sequence.

The catalog omitted the differential carrier's 28 teeth. The [official LDraw 62821 definition](https://library.ldraw.org/library/official/parts/62821.dat) confirms the tooth count; catalog part 62821b now records it, allowing the pictured input-gear mesh to be checked. Connection uncertainties are not hidden by this metadata correction.

The optional compressed reading copy retains all 496 page sizes and is 78,949,847 bytes, a 48.8% reduction from the 154,116,478-byte original. It uses 160 dpi JPEG quality 75. A rendered preview was checked for readable part callouts, shaft lengths and join arrows. The original SHA256 was verified unchanged.

The [official LDraw 32072 definition](https://library.ldraw.org/library/official/parts/32072.dat) identifies the four-knob gear. Its catalog row previously omitted the driving-lobe count and classified it as other. It now records gear type and four driving lobes in `gear_teeth`, explicitly distinguishing knobs from involute teeth, so the two pictured selector knob wheels can use MESH.

Source steps 152 and 154 introduce the two complete grey soft-spring shocks (76138), which the reference model omits. They are included in the training inventory; the adjacent red hard-spring shock seating follows the booklet and remains estimated. The source also includes two black support pins at step 74 and a mirrored three-piece pivot connector at step 77 that are absent from the reference. Those pieces are retained with explicit uncertain endpoints.

The notation checker now accepts MESH for the existing gear-rack part type without requiring a rotary tooth count. Source step 189 shows the twelve-tooth steering pinion engaging rack 87761. Regression checks cover that valid mesh and a smooth beam that must still be rejected; all eleven checker tests pass.

At source step 283, the booklet specifies two grey 4274 half pins but the geometric reference contains only one at this bracket. The additional instance is retained as steering-bracket-second-half-pin, with its receiving hole unresolved instead of omitted or assigned an invented exact hole. The bracket and steering-wheel tile clutches also remain explicitly unnamed.

Source steps 352-356 use one black T bracket, four short black 2780 pins and one long black 32054 pin for the right forward side frame. The geometric reference instead mirrors the left bracket with four blue 6558 pins and an extra T bracket. The training follows the booklet, omits reference-only 60484-9 and 6558-56 through 6558-59, and names the five actual black pins explicitly; their seating remains estimated. Source steps 348 and 362 each add a black upright pin absent from the reference model, retained with unresolved receiving-hole labels.
