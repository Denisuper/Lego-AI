# Zetros 42129 source review

The transcription now follows all 640 numbered source steps on printed pages 6-373 of the official booklet. Source-order coverage and inventory reconciliation alone cannot prove mechanical correctness: many connection endpoints remain uncertain, and inventory differences still need investigation.

The duplicate differential names were repaired in the earlier checkpoint. Color names were aligned with the corresponding inventory entries when the part had only one matching intended color in the inventory. On printed page 369, source step 632 calls for two splat plates, two round plates and two three-stud axles, one of each for each front wheel. Two surplus round-plate records were removed from training step 399; the remaining connections have unresolved endpoints. The 640 source steps were checked against printed pages 6-373 and uncertain joints are marked explicitly. Unsupported claims that the differential case outer teeth mesh with its internal bevel gears were removed. These local fixes do not establish the correctness of other steps.

At this checkpoint, run `python tools/audit_dataset.py` for the exact current inventory counts. Keep 42129 in the audit's incomplete set list until its source sequence and inventory are fully reconciled. The existing notation check does not prove geometry or source coverage.

A second source check found that the frame assembled in source steps 611-618 was recorded twice in the old data, once as a side build and again when attached. Source page 363 shows one completed frame being attached, not a second set of parts. The duplicate ADDs and joins were replaced by one attachment step, and the later extinguisher references now use the original frame parts. The frame's interfaces to the truck remain unresolved. The transcription is still not one-to-one with all 639 numbered source steps.

Printed page 117, source step 196, calls for four axle-pin hubs in two paired rear-axle link assemblies. The draft introduced five: the old `ra-conn-8` and `ra-conn-11` occupied the same place in the same link. The duplicate was removed and its later references now use `ra-conn-11`. The links remain represented as two training steps and still need to be split or renumbered as part of a source-order rewrite.

On printed page 100, source step 148 uses a grey three-stud axle in the second wheel reduction hub; the draft incorrectly recorded a red four-stud axle. The inventory and training were corrected, and the unsupported connection from that axle to the earlier differential was replaced with unresolved hub and joint endpoints. Its surrounding source-step order still needs review.

Printed page 37, source step 53, shows two light-grey single-pin connectors on the chassis floor panel. The old draft called both dark grey and assigned some pin ends to two panel holes at once. Their color now matches the booklet, and the uncertain panel hole positions are explicit.

Source step 23 on printed page 19 specifies one red half bush. The draft had added a second one at this location; it was removed, and any remaining inventory shortfall must be traced to its actual source step.

Printed page 20, source steps 24 and 25 add a red half bush and turn the axle. Both are now represented separately.

Printed pages 21-23, source steps 26-28, assemble the gearbox support and install the two seven-stud axles separately. Their unresolved joins are explicit. Continue at source step 29, page 23.

Printed pages 23-28, source steps 29-36, separate the support beam, gears, two clutch assemblies, lock motor and shafts into their numbered source steps. The motor side build is attached separately; uncertain mounting points remain explicit. Continue at source step 37, page 29.

Printed pages 29-35, source steps 37-50, separate the upper crossbeam and stop pins, the paired side panels, and the numbered build and attachment of the second chassis subassembly. Earlier source pages 16-17 were used to locate the receiving crossbar and pins; exact unresolved interfaces remain marked. Continue at source step 51, page 36.

Printed pages 36-42, source steps 51-60, separate the shaft and gears, floor panel subassembly, motor beams and two side frames. Refer back to the floor and side-panel build views to locate their joins; unresolved pin positions remain explicit. Continue at source step 61.

Printed pages 44-49, source steps 61-70, split the front crossbar into its five component steps, then its two mounting steps, and review the following motor pins and L-beams. The crossbar mounting was compared with the side-frame build on pages 40-43; unknown pin hole positions remain explicit. Continue at source step 71.

Printed pages 50-61, source steps 71-82, separate the upright beams, long pins, paired L-brackets, cable clips and black side panels. Earlier motor-support steps 69-70 establish where the uprights fit. The formerly combined records are now in source order; exact unresolved pin positions remain marked. Continue at source step 83.

Printed pages 62-68, source steps 83-94, separate the bent beam and brown axle, the numbered side-frame build and attachment, and its two braces. Earlier side-panel views on pages 60-61 establish the receiving panel; unresolved interfaces stay marked. Continue at source step 95.

Printed pages 69-72, source steps 95-98, separate the axle and connector, support bracket, opposite bent beam and its stop axle. Source step 95 explicitly specifies a red six-stud axle: the draft incorrectly recorded a yellow five-stud axle, now corrected and renamed throughout. This resolves one missing and one extra inventory entry. Continue at source step 99.

Printed pages 73-76, source steps 99-105, separate the frame build, its attachment, the blue mounting pin and the fan assembly. The frame mounts to side beams built on pages 64-68; exact endpoints remain unknown where the booklet view does not resolve them. Continue at source step 106.

Printed pages 77-86, source steps 106-115, review the opposite side-frame and steering supports against the earlier frame build. Source step 107 includes a red towball pin omitted by the draft, now restored. Source step 114 explicitly calls for a red six-stud axle, correcting a yellow five-stud draft entry. The four motor-bracket pins belong to step 115. Continue at source step 116.

Printed pages 87-94, source steps 116-129, separate the central upright support, its attachment, cable routing, and the paired panel extensions. The receiving upright beams and mounting pins are traced to source steps 71-74 and 115; uncertain interfaces remain marked. Continue at source step 130.

Printed pages 95-98, source steps 130-142, separate the first wheel-reduction support, axle links, driving ring and differential. The receiving pins and axles are traced through the preceding illustrations; the internal differential interfaces remain uncertain where not visible. Continue at source step 143.

Printed pages 99-101, source steps 143-154, separate the second hub support, three-stud axles, thin links and attachment. Source step 145 adds a dark-grey three-hole connector, red axle-pin and blue axle-pin omitted by the draft; source step 146 adds only one black friction pin, so the extra draft pin was removed. The original first-hub view on pages 95-98 helped identify the mirrored structure, but source step 145 is asymmetric and takes precedence. Continue at source step 155.

Printed pages 102-104, source steps 155-164, separate the differential-lock support build and attachment. The receiving axle links and driving ring are traced to source steps 139-142 and 152-154; exact interfaces remain uncertain where not shown. Continue at source step 165.

Printed pages 105-107, source steps 165-170, separate the lock-support pins, central bracket, paired thin links and bevel-gear shaft. Earlier source steps 155-164 identify the receiving lock-support beam; uncertain holes remain explicit. Continue at source step 171.

Printed pages 108-111, source steps 171-180, separate the drive support into its numbered subassembly steps and then its attachment. The earlier draft described it as already attached while it was being built; the source shows a separate assembly until step 178. Continue at source step 181.

Printed pages 112-114, source steps 181-187, separate the axle-frame connectors, geared five-hole beams and the two red clutch gears. Page 113 shows the yellow shaft receiving the second red gear on page 114. Continue at source step 188.

Printed pages 115-117, source steps 188-196, separate the rear axle housing build, its attachment and the two matching upper links. The housing attaches to the earlier frame from steps 171-180; unresolved interfaces stay marked. Continue at source step 197.

Printed pages 118-123, source steps 197-205, separate the grey pin stacks, thin links, paired suspension supports, axle pins and shocks. Earlier housing and upper-link views identify the assemblies receiving them; hole positions remain uncertain where hidden. Continue at source step 206.

Printed pages 124-129, source steps 206-212, separate the axle crossbeam and shafts, panel, axle-to-chassis attachment, shock seating and side-panel pins. Earlier shaft and shock views were compared, but exact shaft pairing and shock receiving holes remain unresolved. Continue at source step 213.

Printed pages 130-135, source steps 213-224, separate the upper-frame subassembly, its attachment and pin seating. Source step 223 includes a black five-hole beam omitted from the draft; it is now restored. Continue at source step 225.

Printed pages 136-144, source steps 225-240, separate the rear frame panels and the beginning of the front axle. Source step 228 builds and attaches both matching panel extensions together, while steps 229-240 separately build the front differential frame, shafts and supports. Continue at source step 241.

Printed pages 144-149, source steps 241-255, separate the front wheel hubs, steering arms, supports, shocks and steering rack. The source views of the front differential and frame on pages 140-144 identify the earlier parts receiving them; hidden endpoints remain uncertain. Continue at source step 256.

Printed pages 150-157, source steps 256-265, recombine the front axle support side builds as pictured and separate each subsequent L-bracket installation. The receiving supports can be followed back to the front axle frame and steering rack on pages 140-149; hidden endpoints remain uncertain. Continue at source step 266.

Printed pages 158-164, source steps 266-280, separate the paired connector stacks, cross-shaft, steering motor subassembly and attachment, and steering link. Source pages 161-163 show that the motor remains a separate build until step 277. Continue at source step 281.

Printed pages 165-177, source steps 281-293, separate the steering motor brackets, shock-end mounts and front drivetrain shaft, then restore the previously omitted front axle-to-chassis installation and steering cable routing. Exact mounting interfaces remain unresolved. Continue at source step 294.

Printed pages 178-184, source steps 294-300, restore the shock/link positioning, cross-shaft, two side beams and cable clips. The draft had added an unsupported red two-stud axle in step 294; the source shows no new piece and the earlier receiving assembly already has its own axle, so the extra record was removed. Continue at source step 301.

Printed pages 185-193, source steps 301-317, separate the bumper side build, stickers, headlight assemblies, grille and duck ornament, and restore the bumper attachment step. Bumper mounting interfaces remain unresolved. Continue at source step 318.

Printed pages 194-200, source steps 318-331, restore the tan mounting pin before the separate engine-detail build, sticker, installation and pin seating. The earlier draft omitted a black round plate shown in the step 330 callout; it has been restored. Continue at source step 332.

Printed pages 201-209, source steps 332-345, separate the three-seat side build, its attachment, Control+ hub preparation and the two motor lead connection steps. The seat assembly fits the earlier central upright support; precise mounting interfaces remain unresolved. Continue at source step 346.

Printed pages 210-216, source steps 346-352, restore the previously omitted hub-clip positioning step, the paired side brackets and braces, and steering wheel. Their earlier receiving uprights are visible in source steps 71-74 and 123-125. Continue at source step 353.

Printed pages 217-219, source steps 353-363, separate the cabin side panel, pins, links, beams and two numbered stickers in source order. The panel and beam receiving points are traced to the preceding substeps; unresolved holes remain marked. Continue at source step 364.

Printed pages 220-224, source steps 364-380, separate the first cabin door linkage, tile stickers, linkage attachment and remaining cabin-side brace. Earlier cabin panel steps 353-363 establish the receiving assembly; exact interface holes remain uncertain. Continue at source step 381.

Printed pages 225-227, source steps 381-391, separate the opposite cabin side panel, links, connector and beams. Earlier steps 381-388 establish the receiving parts for the later beams; exact hole positions remain uncertain. Continue at source step 392.

Printed pages 228-233, source steps 392-408, separate the opposite door linkage and tiles, its attachment, stickers and joining of the two cabin sides. The previous cabin side beam in step 380 identifies the receiving assembly; exact mounting holes remain uncertain. Continue at source step 409.

Printed pages 234-240, source steps 409-415, separate the cabin crossbeam connectors, cabin mounting and hinge positioning, stickered engine tile, paired linkages and side panels. The cabin side and crossbeam steps establish the receiving assembly; hidden mounting holes remain uncertain. Continue at source step 416.

Printed pages 241-244, source steps 416-423, separate the cabin roof panels, connecting beams, pins, curved panels, stickers and handles. The preceding roof panel build locates the receiving pins; hidden holes remain uncertain. Continue at source step 424.

Printed pages 245-248, source steps 424-427, review the roof cross-axle, beam, antenna and roof installation. The roof pins and cabin side panels are traced to earlier steps; exact attachment holes remain uncertain. Continue at source step 428.

Printed pages 249-252, source steps 428-434, separate the roof-side connector pairs and axles, then the start of the separate roof frame. Earlier roof-end connectors from step 424 identify the receiving assemblies; hidden holes remain uncertain. Continue at source step 435.

Printed pages 252-256, source steps 435-440, separate the roof-frame extensions, closing crossbar, round details, frame installation and amber lights. Earlier roof and frame steps identify the receiving parts; mounting holes remain uncertain. Continue at source step 441.

Printed pages 257-259, source steps 441-448, separate the roof connectors, upright tube build and its installation on the cabin side. Earlier roof pins and side panel locate the receiving assembly; exact mounting interfaces remain uncertain. Continue at source step 449.

Printed pages 260-262, source steps 449-457, separate the hood support build, turning and installation. Step 454 calls for a black axle-pin rather than the draft blue axle-pin; corrected. The front chassis receives the support but exact mounting holes remain uncertain. Continue at source step 458.

Printed pages 263-264, source steps 458-464, separate the opposite tube upright and its installation. Earlier roof connector and side panel identify the receiving assembly; exact mounting interfaces remain uncertain. Continue at source step 465.

Printed pages 265-267, source steps 465-472, separate the opposite hood support build, turning and installation. Step 469 calls for a black axle-pin rather than the draft blue axle-pin; corrected. The chassis receives the support but exact mounting holes remain uncertain. Continue at source step 473.

Printed pages 268-270, source steps 473-480, separate the paired hood beams, half pins, decorative details, sticker and connector pairs. Earlier beam and half-pin steps locate the receiving structure; hidden interfaces remain uncertain. Continue at source step 481.

Printed pages 271-274, source steps 481-489, separate the hood crossbeam, its attachment to the earlier hood connector pairs, clip details, and hood installation. Hood supports from steps 449-457 and 465-472 identify the receiving assembly; exact mounting holes remain uncertain. Continue at source step 490.

Printed pages 275-276, source steps 490-497, restore two omitted grey bars and connectors beside the hood, then separate the side detail and sticker. The bars match the inventory three-stud grey bar; the two axle connectors are black, consistent with the source view and the remaining matching inventory. Continue at source step 498.

Printed pages 277-278, source steps 498-500, combine the round side detail as shown, turn it and install it next to the hood. The receiving cabin-side assembly is traced to earlier pages; exact mounting holes remain uncertain. Continue at source step 501.

Printed pages 279-280, source steps 501-506, separate the front body connector, axles, links and long beam with four grey bars. The bars are distinct from the shorter pair in step 490; exact attachment holes remain uncertain. Continue at source step 507.

Printed pages 281-282, source steps 507-513, separate the matching front-body side build, its turning and attachment to the long beam from step 506. The exact receiving hole remains uncertain. Continue at source step 514.

Printed pages 283-284, source steps 514-519, separate the front cross-frame L-beams, thin links, axle and connectors. Earlier substeps locate the receiving axle; exact hidden interfaces remain uncertain. Continue at source step 520.

Printed pages 285-288, source steps 520-529, separate joining the cross-frame, the stop axles, emblem and central link. Restored the orange plate and grey round tile omitted in step 525, and corrected step 529 to two thin two-hole links and one thin three-hole link. Exact hidden interfaces remain uncertain. Continue at source step 530.

Printed pages 289-290, source steps 530-533, separate the stickered beam and seven-hole beam and recombine each layered side detail as the booklet shows. Earlier front-body connectors identify the receiving assemblies; exact hidden holes remain uncertain. Continue at source step 534.

Printed pages 291-292, source steps 534-540, separate the hood panels, paired wedge details, pins, stickers and grille attachment. The earlier grille beams identify the receiving assembly; exact holes remain uncertain. Continue at source step 541.

Printed pages 293-296, source steps 541-544, recombine the hood corner and stickered side builds as shown. The draft added an unsupported extra blue long pin to each side build; those two entries were removed. Earlier hood panels identify the receiving assemblies; exact holes remain uncertain. Continue at source step 545.

Printed pages 297-300, source steps 545-550, recombine the side supports and paired lights, then restore the turning and installation of the finished front body. Earlier hood supports identify the receiving assembly; exact mounting holes remain uncertain. Continue at source step 551.

Printed pages 301-307, source steps 551-557, separate the side beams and restore the paired connector stacks, light-grey links and hood closing. The four-hole links match the inventory light-grey beam with end studs; connector colour and any overlap with later legacy entries need reconciliation. Continue at source step 558.

Printed pages 308-311, source steps 558-567, separate the two rear-side plate builds, their turning and installation. The rear chassis is the receiving assembly; exact mounting holes remain uncertain. Continue at source step 568.

Printed pages 312-315, source steps 568-570, recombine the rear panel, green crossbar and matching rear lights in booklet order. The preceding panel and crossbar views locate the receiving assemblies; exact holes remain uncertain. Continue at source step 571.

Printed pages 316-320, source steps 571-579, recombine the paired black rails and separately transcribe the floor panels, hubs, pins and beam. The earlier floor substeps establish the receiving parts; exact hole positions remain uncertain. Continue at source step 580.

Printed pages 321-324, source steps 580-583, restore the bed-floor installation and separate the green connector, fourteen long pins and six green rail beams. Earlier chassis rails locate the receiving assembly; exact holes remain uncertain. Continue at source step 584.

Printed pages 325-328, source steps 584-587, review the black rail pins, second green rail layer, and restore both stickering steps. Earlier green beams locate the receiving rails; exact holes remain uncertain. Continue at source step 588.

Printed pages 329-334, source steps 588-592, separate the marker lights, side bracket, curved panels, mounting beam and paired cylindrical details. Earlier chassis and panel builds identify the receiving assemblies; exact holes remain uncertain. Continue at source step 593.

Printed pages 335-340, source steps 593-595, recombine the ladder and first wheel-arch support in source order. Restored a black pin omitted from step 594. The chassis receives these builds; exact holes remain uncertain. Continue at source step 596.

Printed pages 341-347, source steps 596-599, recombine the opposite side markers, wheel-arch support and ladder in source order. Restored the missing black pin in step 597. The chassis receives these builds; exact holes remain uncertain. Continue at source step 600.

Printed pages 348-356, source steps 600-608, recombine the opposite side panels and separate the grey mounting block, its installation, curved connector and grille box. Earlier side chassis views locate the receiving assembly; exact mounting holes remain uncertain. Continue at source step 609.

Printed pages 357-363, source steps 609-620, separate the bed pins, two T-brackets and support-frame steps, turning and attachment. Earlier cab and bed pins locate the receiving assemblies; exact mounting holes remain uncertain. Continue at source step 621.

Printed pages 364-368, source steps 621-631, separate the exhaust stack and restore its omitted seventh ribbed cylinder, then recombine the two extinguishers and four wheels. The support frame identifies the receiving assembly; exact holes remain uncertain. Continue at source step 632.

Printed pages 369-372, source steps 632-639, review both sets of wheel hubs and recombine the paired white and red marker flags. Removed the artificial final sticker-sheet step; the sheet is instead accounted for at its first use in source step 312, following the project inventory convention. Continue with inventory reconciliation and unresolved connection review.

Inventory reconciliation after source coverage: source step 490 supplies the two previously missing black 42135 connectors; the initially transcribed dark-grey colour was corrected. The remaining differences are two black 41677 thin beams. Do not assume the beams are unused or spare until source counts are independently verified.

Printed page 373 contains a numbered completion illustration, source step 640, with no added parts; it is now recorded explicitly. The black two-hole thin-beam callouts located in the booklet total 24 across steps 356, 357, 378, 384, 385, 407, 503-505, 509-511, 529, 532 and 533; the inventory lists 26. The two-piece difference remains unresolved rather than placing parts without a source location.

A targeted comparison with the checked-in `model.mpd` locates the two-link discrepancy at source step 529. The booklet callout and inset on printed page 288 show two black 41677 two-hole thin beams and one black 6632 three-hole thin beam, with two tan axle-pins. In contrast, the authored LDraw model section `42129 - front.ldr`, lines 2801-2808, uses four black 41677 beams and no black 6632 beam for that assembly. Flattening the reachable truck model gives 26 black 41677 and 13 black 6632; this transcription gives 24 and 14 respectively, while the provided inventory lists 26 and 14. The model is a separate authored reconstruction, so the evidence does not establish whether its construction represents another version or an error, or whether the inventory has a mismatch. Keep the booklet construction at step 529 and the two missing inventory entries unresolved.

Drivetrain interface review: source step 13, printed page 10, shows three tan bevel gears inside the red differential. The draft omitted the third gear?s housing support and its engagement with the two output bevel gears. Those relations are recorded; the internal mounting point remains uncertain.

Front drivetrain interface review: source steps 231-233 on printed pages 141-142 show the black input bevel gear engaging the red outer ring gear of the front differential. That drive mesh is now recorded; the exact axle and bearing endpoints remain uncertain.

Rear drivetrain interface review: printed pages 106-107 trace the blue gear to step 141 and show the black bevel gear added in step 170 engaging it. That mesh is now recorded; the axle and support endpoints remain uncertain.

Motor differential interface review: source step 16 on printed page 13 shows both grey 24-tooth motor gears engaging the red differential?s exterior teeth. These meshes are recorded separately from the internal bevel-gear contacts.

Rear-drive shaft review: comparing source steps 168, 177, 184 and 187 on pages 106, 110, 113 and 114, then checking the authored model geometry, places the second red clutch gear on the yellow shaft from step 168, not on either of the two later yellow shafts. The shaft reference is corrected and its visible mesh with the adjacent grey gear is recorded.

Axle differential review: source step 142 page 98 and step 231 page 141 show the two output bevel gears with three intermediate bevel gears in each case. In each numbered group, the first and last bevel names represent the two outputs and the three middle names represent the intermediates; their six internal gear contacts are now recorded. Mounting points remain uncertain.

Motor support review: source steps 1-6 on pages 6-7 show paired triangular beams with the black pins in the two inner base holes, the yellow axle through one cross-shaped end and the grey hub through the opposite cross-shaped end. The black pin hub passes through the apex. Receiving holes are now identified using the catalog geometry; hidden shaft and pin end positions remain uncertain.

Gearbox support review: source step 26 inset sequence on page 21 shows the long blue pins in the ends of the white three-hole beam and black pins securing the olive beams to the white supports. The two white-beam receiving holes are identified, and the olive beam connections now name the actual intervening pins rather than claiming direct beam-to-beam joints. Hidden pin and hole positions remain uncertain.

Gearbox drive review: the subassembly on page 21 and its installation on pages 22-24 establish which gears share the brown shaft and which flank it. The step 27 grey gear meshes with its 16-tooth gear, the step 28 small gear with its 24-tooth gear, and the grey gear added in step 30 meshes with the adjacent red clutch gear. These visible contacts are now recorded; axle-bearing points remain uncertain.

Lock-motor gearing review: printed pages 25-28 show the prepared motor shaft and the adjacent seven-stud shaft from step 28. The two grey sixteen-tooth gears installed in step 36 engage each other; that mesh is now recorded. The shaft bearing points remain uncertain.

Upper crossbar review: source step 37 inset on page 29 shows the four-pin hub seated in the white three-hole beam?s ends and holes 3 and 5 of the eleven-hole beam. Those four receiving holes are now explicit; which hub pin faces each end remains uncertain.

Side-panel interface review: page 32 shows the white three-hole beams and round connectors joined to each new panel by its blue long pins; earlier pages 14-15 show the grey stop pins receiving the round connectors. Step 40 now records those intervening pins instead of direct panel-to-panel and panel-to-beam joins. Pin-end positions remain uncertain.

Second chassis interface review: printed pages 33-35 show the black pins in the round holes of the two short axle connectors, with white sleeves over their exposed ends. Step 47 previously assigned its pin to the L-beam; it belongs in the round hole of the short connector added in step 46. The four-pin hub seats in two holes of each L-beam, and step 49 inserts its red pin into the middle hole of the earlier grey perpendicular connector. Hidden pin-end positions remain uncertain.

- Source pages 36?38, steps 51?56: the gray and tan gears mesh; their axle holes and the ball-ended shaft socket are identifiable. The two gray floor connectors insert their integral pins. The paired black pins and blue axle-pins at each floor edge are distributed across both panels, not all in the narrow panel. Individual panel holes remain uncertain.

- Source pages 40?43, steps 59?60: the side frames? four black friction pins fit the round holes of the gray pin hubs, rather than directly into the frames. Each hub?s integral pin fits the frame. Each dark connector is held to the frame by the blue axle-pin; the remaining axle hole takes the later stop axle in step 61. The corresponding ball-ended socket in step 62 is also identified.

- Source page 45, steps 63?64: the ball-joint axle passes through the L-beam?s short leg, the black pin occupies the corner, and the blue axle-pin occupies its cross hole at the far end.

- Source pages 49?50, steps 70?71: the two blue axle-pins were listed but their placement was omitted. Their axle ends lock into the L-beams? cross holes, and their pin ends receive the fifteen-hole beams in the next step.

- Source pages 52?56, steps 73?78: the L-bracket blue axle-pins occupy their cross holes. The gray cable-support hubs use their integral pins in the earlier motor-support short-leg holes and hold the round ends of the blue axle-pins; the cable clip in step 77 fits the projecting axle, rather than the hub directly.

- Source pages 57?59, steps 78?80: the red cable clip in step 79 fits the other support axle-pin, matching its blue counterpart. The black cable-clip axle-pins enter the panels using their round pin ends.

- Source pages 62?63, steps 83?84: the blue pin occupies the second round hole on the short angled arm of the bent beam; the brown axle enters the cross hole at the opposite long end.

- Source pages 64?65, steps 85?86 and 91: the blue and red axle ends pass through both thin L-beams, including the previously omitted second red connection. The triangular panel is held to the later L-beam by a friction pin rather than a direct panel-to-beam connection; the red axle-pin locks into the panel cross hole.

- Source pages 67 and the mirrored steps 97?98: the side brace in step 93 is held to the eleven-hole beam by its two blue pins, not by a direct beam-to-beam connection. Their positions and the gray axle?s short-end cross hole follow the enlarged inset. The opposite side bent-beam pin and axle mirror steps 83?84.

- Source page 73, step 102: the tan frictionless pin passes through the steering lever and is held by two gray pin hubs; the hubs? integral pins attach to the frame. The two additional black pins go into the frame, not the lever. The original direct lever-to-frame and hub-to-lever claims skipped the intermediary pin.

- Source pages 77 and 80, steps 106 and 109: mirrored thin L-beams are held by the axle ends of the blue and red pins; the red axle connection to the second beam was omitted. The opposite bent brace attaches through two long pins, and its hole positions mirror the source step 93 brace.

- Source pages 79 and 84, steps 108 and 113: the paired steering arms attach to the earlier end L-brackets via their brown stop axles; they do not attach directly to the small 2-hole beams introduced in step 112. Exact axle positions remain uncertain.

- Source page 83, step 112: each black pin fits the round hole of its two-hole beam and joins it to the gray connector, replacing direct beam-to-connector claims.

- Source pages 87?88, steps 116 and 120: the two gray axles enter the two separate cross holes of the central connector, and each black long axle-pin enters the cross hole of its triangular panel.

- Source pages 86, 90, and 92, steps 115, 125 and 127: the upright support attaches to the earlier beams on the four previously fitted friction pins. The green cable clip sits above the earlier blue clip on the black axle-pin from step 78; it is not connected directly to the newly added L-beam.

- Source pages 94?95, steps 129?130: both chassis panel extensions fit the earlier panels through their paired black pins. The rear-axle support begins with pins in holes 2 and 4 of the five-hole beam.

- Source pages 95?96, steps 132 and 135: the gray axles pass through the cross holes at the ends of the thin three-hole beams and the gray connectors. The red drive axle enters the wheel joint?s axle socket.

- Source pages 95?97, steps 132, 136?138: each outer thin three-hole beam spans a pair of gray axles and the intervening blue pin, rather than connecting only to the newly inserted axle. Its two end cross holes and center round hole are recorded; left/right beam orientation is symmetric.

- Source page 97, steps 139?141: the dark 2-hole link is stacked on the red axle-pin through the adjoining thin 4-hole link; each link also uses its second round hole on the earlier blue hub pin. The red drive axle runs through the blue gear?s round center and the red connector?s cross hole.

- Source page 99, steps 143?145, and the mirrored second-hub assembly: the second five-hole support uses holes 2 and 4. Its blue axle-pin fastens the dark center connector to the gray hub support, while the red axle-pin occupies the other cross hole. The second hub joint socket and thin-beam cross holes mirror the earlier hub.

- Source page 101, steps 151?153: the second hub?s two thin beams span both gray axles and the center blue pins, and the dark two-hole link shares a red axle-pin with the adjacent four-hole link. These mirror the earlier hub?s documented corrections.

- Source pages 102?103, steps 155?160: the lock shaft passes through the round holes of the perpendicular end connectors; its bushings, orange selector and black gear use their cross holes. Blue axle-pins enter the connectors? cross holes and their round ends hold positions 5 and 11 of the 11-hole support beam.

- Source pages 103?104, steps 161?163: the red and blue pins above the lock shaft enter the upper cross holes of its existing connectors, not the lower support beam. The previously omitted blue pin also fastens hole 5 of the upper beam; its two end pins occupy holes 1 and 11.

- Source pages 106?107, steps 167?170: each red pin enters the thick end cross hole of its light-gray link. The yellow axle in step 168 and red axle-pin in step 169 each pass through the stacked dark links; the small bevel gear in step 170 uses its cross hole.

- Source pages 108?109, steps 171?177: the rear-drive support uses its lower beam?s holes 1, 3 and 5, and upper beam?s holes 1, 3, 5 and 9. The red connector bridges the exposed blue and red axle ends; the new gear uses its cross hole on the yellow axle.

- Source pages 111?112, steps 180?182: the white 3-hole beam attaches to the black frame through the two previously inserted pins, and the red towball occupies its center hole. The black spacer uses the third pin, and the gray stop-pin and blue axle-pin meet through the stop-pin?s cross socket. The gray gear?s shaft hole is explicit.

- Source pages 113?114, steps 183?185: the red axle-pin occupies the second hole of its five-hole beam and passes through the black spacer. The yellow gear shaft passes through the other five-hole beam?s center hole and the two gear cross holes; the red clutch gear fits the tan pin through its round center.

- Source pages 114?115, steps 186?191: the paired joint shafts and gray gears use their cross sockets; the second red clutch gear uses its round center. Each end of the housing link has a red axle-pin and pin hub axle inserted in the two cross holes of its three-hole connector, and the yellow shaft enters the black connectors? end sockets.

- Source pages 115?118, steps 188?194 and 197?198: the first housing beam receives the two earlier red axle-pins, and both end pin hubs bridge the two parallel beams. The two red axle-pins enter gray stop-pin cross sockets before the spacer or white 3-hole beam is fitted.

- Source pages 120?121, steps 201?202: each suspension linkage sandwiches two thin six-hole beams on shared black pins and the integral pins of two gray hubs; the two central pins also secure the perpendicular connector. The steering lever fits the ball-ended pin added in the inset, rather than directly to that connector. Exact individual hole numbers remain uncertain.

- Source pages 123?124, steps 205?206: the gray shock-end hubs insert their integral pins in the shocks. The two light-gray crossbeam links connect to the seven-hole beam via their black pins and blue axle-pins; the blue axle ends occupy the thick-end cross holes and the black pins occupy the second round holes from the thin ends.

- Source pages 36, 45, 114 and 125, steps 52, 62, 186 and 207: correction to earlier hole identification: the joint?s ball end engages the cup, while its free cross socket receives the later red or yellow axle. The ball/cup endpoints have no catalog point and remain uncertain. In step 208 the curved panel fits the two blue axle-pins from step 206.

- Source pages 94, 129?130, steps 129 and 212?215: each chassis side receives one blue pin in the earlier panel and one in its step 129 extension. Both pins on each side of the upper-frame subassembly pass through the eleven-hole beam and the end holes of the three-hole beam; the second contact was omitted for each part.

- Source pages 132?133, steps 220?221: the upright steering lever pivots on the tan pin held between two gray connectors; black axle-pins fasten those to the frame and bridge the dark connector. The next crossbar is attached through four blue pins: two axle-pins join its central connector, while the two long pins in its end holes join the frame.

- Source pages 129 and 134?135, steps 212 and 223?224: the completed upper frame seats on the four blue side-panel pins placed earlier, with two pins entering each eleven-hole side beam. The draft had represented the mounting as a direct frame-to-panel connection.

- Source pages 123, 136, 139?140, steps 205, 225, 228?230: the four-stud shafts enter the round holes of the earlier shock-end hubs. Each paired panel extension is joined by its two friction pins. The red front-frame piece is held by its integral pin and the blue axle-pin rather than a direct part-to-frame connection. Step 233?s bevel gear axle hole is identified.

- Source pages 98, 100?101 and 141, steps 142, 148, 154 and 232: the rear and front differential half-shafts pass through the case?s round center and engage the cross holes of the two output bevel gears. The second rear hub joins via its shaft, rather than by a direct housing-to-housing contact; left/right identical axle naming is symmetric.

- Source pages 142?143, steps 234?238: the first seven-hole beams attach through blue pins in their end holes; the five-hole crossbar fits both black pins and the gray hubs mount on the side beams. On the reverse side, both blue pins pass through each seven-hole beam, and the nine-hole crossbar shares one on each side.

- Source pages 143?144, steps 239?241: the two stop axles run through the cross holes of both pairs of gray connectors and their red bushings; blue pins use the outer round holes. The differential output extensions engage opposite ends of their two dark axle couplers.

- Source pages 143?146, steps 239?248: front wheel hubs connect to differential output extensions through their joint sockets. Both long pins secure each upright L-beam; the stop pins enter the lower gray connectors installed in step 239. Each blue axle-pin passes through the paired thin two-hole links.

- Source pages 147?148, steps 251?254: shocks attach through their stop axles; each pair of thin links shares both red and gray axles. The blue axle-pins fasten the black connectors to two-hole supports, and the white crossbeam joins the black nine-hole beam through two black pins.

- Source pages 148?150, steps 252 and 255?256: the steering rack?s blue pins and tan axle-pins each pass through both stacked thin links; the tan pin ends attach those links to the earlier paired hub links. The following support?s four integral hub pins and yellow axle hold both five-hole beams, rather than the previously recorded partial contacts.
