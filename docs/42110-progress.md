# Defender 42110 transcription

The original 496-page booklet and 2,573-piece inventory are preserved. The source build is transcribed through step 860, page 489, followed by step 861 accounting for the sticker sheet. All 2,573 inventory entries match by part and colour, with no notation errors. The table and JSONL match. There are 874 unknown and 536 estimated endpoints, so the checks do not establish physical geometry or motion.

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

Steps 392?393 show the seated, symmetric rear headrest rail pin sleeves and adjoining axle segments. Steps 408?409 show the stopped axles spanning the new L supports and the two receiving connectors installed in steps 68?69; those twelve seating positions are resolved. The unlisted stud and plate interfaces remain unknown.

The step 423 rear bumper view shows four half pins fully seated in the outer black-beam holes before the tiles are pressed over them; those pin seating estimates are resolved.

Steps 441 and 457 now record the four previously omitted sill-to-floor joins. The long blue pins were installed through the sill and bent beam in steps 435?436 and 451?452; the source installation arrows show the floor attachments. Exact floor-hole labels are left unknown.

Steps 525 and 532 show ten wheel-arch trim half pins seated by their long pin ends in the beams, leaving the small studs outside for the trim. The erroneous pin1 beam endpoints are corrected to pin2, and the fully seated positions no longer carry estimates.

The same reversed half-pin endpoint appeared in steps 540, 572, 592 and 628. Booklet views on pages 315, 337, 350 and 366 confirm all nineteen pins seat by their long ends with studs outside. Window hinge joints also use the stop ends as pivot interfaces; their orientations require separate source review.

Step 494 also had the rear latch half pin reversed. Its inset shows the long end entering the cross connector and the stud retaining the white round plate. The plate clutch surface is not named by the catalog, so it remains unknown rather than being confused with its round through-hole.

Further source insets confirm nineteen named half-pin endpoints were also reversed in the bumper, headlights, fenders, windshield uprights, ladder caps and roof-load bracket (steps 675, 680, 692, 745, 755, 771, 783, 834 and 845). Their long pin ends enter the receiving holes, with studs outward; roof bracket hole labels remain estimated.

Sequential comparison of selected part callouts, order and visible attachments has continued through the roof-rack frame at step 807, page 465. This is not a complete proof of every hidden connection or motion; unresolved catalog interfaces and half-stud stacks remain marked.

The inset at step 649 shows both second-door window half pins inserted into the sloping-rail ends first. Their long ends and their stud pivot contacts in steps 649?650 were reversed in the dataset and are now corrected; the hinge seating remains estimated.

The mirrored step 666?667 bumper-end insets show both friction pins through the short leg of each L beam and the blue axle-pin through its long leg. Six estimated beam contacts are resolved; the corner-panel holes remain unknown because the catalog geometry is ambiguous.

Steps 668?670 show the central bumper mount and both mirrored layered lamp blocks in enlarged subassembly insets, resolving twelve previous pin and axle contact estimates.

The enlarged source inset at step 583 shows the two stopped brown shafts keyed into the flexible black connectors and passing through the pivot links introduced at step 582. Those four axle contacts are now specified; the flexible connectors can still bend as the roof moves.

Source steps 612-614 show the window hinge half pins seated and the six-stud axle keyed into both hinge ends; step 616 shows the mirror axle-pin keyed into the thin lever introduced at step 598. Six previously estimated contacts are specified.

The mirrored window frame and mirror at steps 649-652 show the six-stud axle, two half-pin pivots and mirror axle-pin fully seated. These six contacts are specified; the half-pin ends retain their corrected orientation.

The paired latch-rail insets at steps 598-599 and 634-635 show each thin lever seated on its stopped axle and each red axle seated in its angled connector. Steps 604 and 640 similarly show each grey axle seated in the thin lever. The deeper panel and articulated stack positions remain estimated.

The headlight insets at steps 680 and 692 show each assembled lamp crossbar seated on the black axle introduced at steps 677 and 689. Those two contacts are specified; the adjacent half-stud stack positions remain estimated.

The hood-support steps 705-706 and mirrored steps 712-713 show each olive L beam seated on the earlier black and blue pins, with the blue pin in its short leg. Four estimated pin contacts are specified.

The step-727 inset shows both hood fastener half pins inserted by their long ends, with black tiles on their exposed studs. The two pin ends were reversed in the data and are corrected; the panel hole labels and tile clutch surfaces remain unknown.

The enlarged fender-rail insets at steps 742-745 and mirrored steps 768-771 show the second seven-hole beam bridging the first: its inner pins occupy holes 5 and 7, while the two blue cross-connector pins occupy holes 2 and 4 and the half pins occupy holes 3 and 6. The old data put a second pin into an already occupied bridge hole and used the wrong beam positions. Both sides are corrected, and the forward bar pin at steps 748/774 uses the remaining end hole 1. Hole numbering runs from the free front end of the second beam toward the overlap.

At steps 761 and 784, the previously estimated windshield support axle target was the seventh fender-rail beam hole, which is occupied by the rail bridge pin. The source arrows point toward an engine-bay attachment, but do not resolve its receiving part in the reviewed views. The two unsupported joins were removed and the missing receiving interfaces are stated in WHY; the lower estimate count does not mean they have been resolved.

The cargo-box source views at steps 810-813 show two long axles passing horizontally through the frame and six pins entering its upward-facing holes. The draft assigned some axles to vertical holes and some vertical pins to horizontal holes. The frame interfaces and U-shaped rim positions are corrected; two axle-depth endpoints at the far frame side remain unknown.
