# Defender 42110 transcription

The original 496-page booklet and 2,573-piece inventory are preserved. The source build is transcribed through step 860, page 489, followed by step 861 accounting for the sticker sheet. All 2,573 inventory entries match by part and colour, with no notation errors. The table and JSONL match. There are 869 unknown and 673 estimated endpoints, so the checks do not establish physical geometry or motion.

The booklet takes precedence. Philippe Hurbain's [OMR-compliant reference model](https://forums.ldraw.org/thread-23139.html) is a read-only geometry cross-check, saved outside the repository. Its internal yoke and spider representations are accounted for using complete universal-joint inventory part 61903. Model traversal is ordered with the rear axle first to match the booklet's module order; model order does not determine the source sequence.

The catalog omitted the differential carrier's 28 teeth. The [official LDraw 62821 definition](https://library.ldraw.org/library/official/parts/62821.dat) confirms the tooth count; catalog part 62821b now records it, allowing the pictured input-gear mesh to be checked. Connection uncertainties are not hidden by this metadata correction.

The optional compressed reading copy retains all 496 page sizes and is 78,949,847 bytes, a 48.8% reduction from the 154,116,478-byte original. It uses 160 dpi JPEG quality 75. A rendered preview was checked for readable part callouts, shaft lengths and join arrows. The original SHA256 was verified unchanged.

The [official LDraw 32072 definition](https://library.ldraw.org/library/official/parts/32072.dat) identifies the four-knob gear. Its catalog row previously omitted the driving-lobe count and classified it as other. It now records gear type and four driving lobes in `gear_teeth`, explicitly distinguishing knobs from involute teeth, so the two pictured selector knob wheels can use MESH.

Source steps 152 and 154 introduce the two complete grey soft-spring shocks (76138), which the reference model omits. They are included in the training inventory; the adjacent red hard-spring shock seating follows the booklet and remains estimated. The source also includes two black support pins at step 74 and a mirrored three-piece pivot connector at step 77 that are absent from the reference. The source step 74 inset shows the pins in the outer holes of the first grey connector; their individual left-right naming remains estimated. The step 77 inset calls for two identical assemblies, allowing the second connector to use the same catalog points as the first.

The notation checker now accepts MESH for the existing gear-rack part type without requiring a rotary tooth count. Source step 189 shows the twelve-tooth steering pinion engaging rack 87761. Regression checks cover that valid mesh and a smooth beam that must still be rejected; all eleven checker tests pass.

At source step 283, the booklet specifies two grey 4274 half pins but the geometric reference contains only one at this bracket. The additional instance is retained as steering-bracket-second-half-pin. The enlarged step 283 image shows it in the first round hole beside the L-beam cross hole; the inset also shows it seated against the beam. The bracket and steering-wheel tile clutches also remain explicitly unnamed.

Source steps 352-356 use one black T bracket, four short black 2780 pins and one long black 32054 pin for the right forward side frame. The geometric reference instead mirrors the left bracket with four blue 6558 pins and an extra T bracket. The training follows the booklet, omits reference-only 60484-9 and 6558-56 through 6558-59, and names the five actual black pins explicitly; their seating remains estimated. Source steps 348 and 362 each add a black upright pin absent from the reference model, retained with unresolved receiving-hole labels.

Source step 572 specifies five grey half pins along the front roof trim supports. The reference model omits the centre half pin; it is retained as roof-front-centre-half-pin in the central three-hole beam. Source and inventory take precedence over the geometric model. The rear door latch locating interface at step 496 remains explicitly unresolved in its WHY explanation.

For source step 844, the rear and front rack pins are now linked to the respective rear and front roof panels from source steps 545-546. Their exact panel-hole labels remain unknown. These were previously absent from the attachment record, so recording them increases the count of explicit unknown endpoints by four.

Source step 788 shows the brown gear shaft entering the second roof panel from the front. Tracing the panel sequence back to steps 545-546 identifies that panel as p64782-4; its precise receiving hole and the shaft depth remain unresolved.

The source views at steps 847 and 850 show each short case wall built from a four-stud side brick and a two-stud side brick. The four corner stacks now attach to both wall bricks on each side instead of putting both stacks on the four-stud brick. The stud connection points remain unnamed.

Step 845 places the black accessory bracket on the roof panel under the rack. Comparison with the roof panel assembly at steps 545-546 identifies p64782-3; the two black mounting pins now explicitly connect to that panel, with exact holes unresolved.

Tracing the step 845 bracket forward to steps 857-858 shows that the storage case covers that bracket. The case now attaches to its three half-pin studs; the separately placed traction-board support no longer claims to attach to the bracket beneath the case. Its own mounting point remains unresolved.

Tracing the identical step 77 pivot connector pair into the same-oriented step 114 nine-hole braces resolves the second brace joins to holes 5 and 6, matching the first side.

The enlarged source view at step 194 shows the black friction pins and blue long pins fully seated in their guide blocks. Six pin-depth estimates based only on the geometric reference offset were removed in favor of the booklet.

A source review compared the part callouts, order and selected joins for steps 1-334 (printed pages 6-202), including the rear differential, front axle, gearbox and engine guide. It is not a full geometry proof: unresolved and estimated endpoints remain, and the rest of the booklet has not received the same review.

The source step 258 inset calls for two identical grey and red pin assemblies seated through the matching beam ends. The second pin seating is now specified like the first rather than relying on an offset in the reference model.

Step 261 shows both identical step-258 pins pushed through the matching engine bearing blocks. The right pin-to-bearing seating is no longer estimated.

At step 280 both long side rails fit onto the paired red pins installed at step 258; the illustrated matching seating resolves the second rail connection.

The enlarged step 282-283 insets show the three steering-bracket half pins fully seated in their connector and beam bores. Their tile clutch points remain unnamed.

Step 291 shows the paired half pins fully seated in the engine side connectors introduced at step 197. Their mounting depths are now specified; the open-stud plate clutch points remain unnamed.

The step 303 inset shows the blue axle-pin and capped grey half pin seated in opposite ends of the grey two-length sleeve. Their seating is specified; the catalog names the entire sleeve bore as one point, so the opposite ends are stated in WHY.

The right upright connection at step 320 matches the opposite side shown at step 321 and the paired red pins from step 258; its pin seating is now specified.

The step 314 inset seats the black friction pin and red towball pin from opposite ends of the grey two-length sleeve. These pin depths are now specified; the sleeve has a single cataloged bore, with opposite-end placement described in WHY.

The enlarged steps 352-355 show the five black pins fully seated in the T bracket, beam and upper connector. Ten pin-seating estimates caused by the mismatching geometric reference were removed; the red axle positions in the split connector remain estimated.

Source review of the side-floor assembly in steps 348 and 362 resolves the upright friction pins to the outer round holes of their 42003 connectors. Both booklet insets show the pins opposite the axle socket; split-axle seating remains estimated.

The two identical front seats in steps 370?373 show each stopped brown axle spanning five consecutive components: the two grey end connectors, two tan side beams and central black block. Those axle seating positions are now resolved.

The installation view at step 384 establishes the final seat orientation. Descriptions in steps 370?380 now identify the seat back, headrest end and cushion consistently with that view.
