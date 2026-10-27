# Zetros 42129 source review

The existing transcription is not a one-to-one transcription of the official 388-page booklet. The old draft combined source steps 1 and 2 in one training step and source steps 3 and 4 in another. The first 129 records now follow source steps 1-129 on printed pages 6-94; later source steps still need to be separated and reviewed. The source continues through step 639 on printed page 372. Most training prompts still do not identify their source pages. The source steps, including side builds and repeat counts, must be reviewed and transcribed in order before this set can be considered complete. Inventory reconciliation alone cannot prove coverage.

The duplicate differential names were repaired in the earlier checkpoint. Color names were aligned with the corresponding inventory entries when the part had only one matching intended color in the inventory. On printed page 369, source step 632 calls for two splat plates, two round plates and two three-stud axles, one of each for each front wheel. Two surplus round-plate records were removed from training step 399; the remaining connections have unresolved endpoints. The first 129 steps were checked against printed pages 6-94 and uncertain joints are marked explicitly. Unsupported claims that the differential case outer teeth mesh with its internal bevel gears were removed. These local fixes do not establish the correctness of other steps.

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
