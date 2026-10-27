# Defender 42110 transcription

The original 496-page booklet and 2,573-piece inventory are preserved. The source build is transcribed through step 860, page 489, followed by step 861 accounting for the sticker sheet. All 2,573 inventory entries match by part and colour, with no notation errors. The table and JSONL match. There are 868 unknown and 715 estimated endpoints, so the checks do not establish physical geometry or motion.

The booklet takes precedence. Philippe Hurbain's [OMR-compliant reference model](https://forums.ldraw.org/thread-23139.html) is a read-only geometry cross-check, saved outside the repository. Its internal yoke and spider representations are accounted for using complete universal-joint inventory part 61903. Model traversal is ordered with the rear axle first to match the booklet's module order; model order does not determine the source sequence.

The catalog omitted the differential carrier's 28 teeth. The [official LDraw 62821 definition](https://library.ldraw.org/library/official/parts/62821.dat) confirms the tooth count; catalog part 62821b now records it, allowing the pictured input-gear mesh to be checked. Connection uncertainties are not hidden by this metadata correction.

The optional compressed reading copy retains all 496 page sizes and is 78,949,847 bytes, a 48.8% reduction from the 154,116,478-byte original. It uses 160 dpi JPEG quality 75. A rendered preview was checked for readable part callouts, shaft lengths and join arrows. The original SHA256 was verified unchanged.

The [official LDraw 32072 definition](https://library.ldraw.org/library/official/parts/32072.dat) identifies the four-knob gear. Its catalog row previously omitted the driving-lobe count and classified it as other. It now records gear type and four driving lobes in `gear_teeth`, explicitly distinguishing knobs from involute teeth, so the two pictured selector knob wheels can use MESH.

Source steps 152 and 154 introduce the two complete grey soft-spring shocks (76138), which the reference model omits. They are included in the training inventory; the adjacent red hard-spring shock seating follows the booklet and remains estimated. The source also includes two black support pins at step 74 and a mirrored three-piece pivot connector at step 77 that are absent from the reference. Those pieces are retained with explicit uncertain endpoints.

The notation checker now accepts MESH for the existing gear-rack part type without requiring a rotary tooth count. Source step 189 shows the twelve-tooth steering pinion engaging rack 87761. Regression checks cover that valid mesh and a smooth beam that must still be rejected; all eleven checker tests pass.

At source step 283, the booklet specifies two grey 4274 half pins but the geometric reference contains only one at this bracket. The additional instance is retained as steering-bracket-second-half-pin, with its receiving hole unresolved instead of omitted or assigned an invented exact hole. The bracket and steering-wheel tile clutches also remain explicitly unnamed.

Source steps 352-356 use one black T bracket, four short black 2780 pins and one long black 32054 pin for the right forward side frame. The geometric reference instead mirrors the left bracket with four blue 6558 pins and an extra T bracket. The training follows the booklet, omits reference-only 60484-9 and 6558-56 through 6558-59, and names the five actual black pins explicitly; their seating remains estimated. Source steps 348 and 362 each add a black upright pin absent from the reference model, retained with unresolved receiving-hole labels.

Source step 572 specifies five grey half pins along the front roof trim supports. The reference model omits the centre half pin; it is retained as roof-front-centre-half-pin in the central three-hole beam. Source and inventory take precedence over the geometric model. The rear door latch locating interface at step 496 remains explicitly unresolved in its WHY explanation.

For source step 844, the rear and front rack pins are now linked to the respective rear and front roof panels from source steps 545-546. Their exact panel-hole labels remain unknown. These were previously absent from the attachment record, so recording them increases the count of explicit unknown endpoints by four.

Source step 788 shows the brown gear shaft entering the second roof panel from the front. Tracing the panel sequence back to steps 545-546 identifies that panel as p64782-4; its precise receiving hole and the shaft depth remain unresolved.

The source views at steps 847 and 850 show each short case wall built from a four-stud side brick and a two-stud side brick. The four corner stacks now attach to both wall bricks on each side instead of putting both stacks on the four-stud brick. The stud connection points remain unnamed.
