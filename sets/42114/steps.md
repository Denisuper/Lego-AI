# Set 42114 - 6x6 Volvo Articulated Hauler

Booklet: booklet.pdf (456 pages). One block per step: parts added, joins, and one line on why. `~` = best reading of the picture, `?` = not shown.

## Step 1 (page 6)
ADD frame-1 64179 darkgray
ADD pin-1 2780 black
ADD pin-2 2780 black
CONNECT pin-1.pin1 -> frame-1.hole?~ STIFF
CONNECT pin-2.pin1 -> frame-1.hole?~ STIFF
WHY Starts the rear gearbox core with a 5x7 open frame and two friction pins through the short sides.

## Step 2 (page 6)
ADD lpin-1 6558 blue
ADD lpin-2 6558 blue
ADD lpin-3 6558 blue
ADD lpin-4 6558 blue
CONNECT lpin-1.pin1 -> frame-1.hole?~ STIFF
CONNECT lpin-2.pin1 -> frame-1.hole?~ STIFF
CONNECT lpin-3.pin1 -> frame-1.hole?~ STIFF
CONNECT lpin-4.pin1 -> frame-1.hole?~ STIFF
WHY Adds four long blue pins standing up at the corners so the next frame can stack on them.

## Step 3 (page 7)
ADD frame-2 64179 darkgray
ADD frame-3 64179 darkgray
CONNECT lpin-1.pin2 -> frame-2.hole?~ STIFF
CONNECT lpin-2.pin2 -> frame-2.hole?~ STIFF
CONNECT lpin-3.pin2 -> frame-2.hole?~ STIFF
CONNECT lpin-4.pin2 -> frame-2.hole?~ STIFF
WHY Stacks the second and third 5x7 frames on the long pins to make a thick sandwich for the gearbox.

## Step 4 (page 7)
ADD pin-3 2780 black
ADD pin-4 2780 black
ADD pin-5 2780 black
ADD pin-6 2780 black
ADD pin-7 2780 black
ADD pin-8 2780 black
CONNECT pin-3.pin1 -> frame-1.hole?~ STIFF
CONNECT pin-4.pin1 -> frame-1.hole?~ STIFF
CONNECT pin-5.pin1 -> frame-2.hole?~ STIFF
CONNECT pin-6.pin1 -> frame-2.hole?~ STIFF
CONNECT pin-7.pin1 -> frame-3.hole?~ STIFF
CONNECT pin-8.pin1 -> frame-3.hole?~ STIFF
WHY Locks the stacked frames together with more friction pins so the sandwich cannot come apart.

## Step 5 (page 7)
ADD beam11-1 32525 yellow
ADD beam11-2 32525 yellow
CONNECT beam11-1.hole?~ -> pin-?.pin2 STIFF
CONNECT beam11-2.hole?~ -> pin-?.pin2 STIFF
WHY Attaches the two long yellow 11-hole beams along the sides of the stacked frames to stiffen the core and give mounting holes for later gears.

## Step 6 (page 8)
ADD frame-4 64179 lightgray
ADD pin-9 2780 black
ADD pin-10 2780 black
CONNECT pin-9.pin1 -> frame-4.hole?~ STIFF
CONNECT pin-10.pin1 -> frame-4.hole?~ STIFF
WHY Builds a separate light-gray 5x7 frame with two pins for a side pocket of the gearbox.

## Step 7 (page 8)
ADD plate-1 60484 yellow
ADD axpin-1 43093 blue
ADD axpin-2 43093 blue
CONNECT axpin-1.pin1 -> frame-4.hole?~ STIFF
CONNECT axpin-2.pin1 -> frame-4.hole?~ STIFF
CONNECT plate-1.hole?~ -> axpin-1.axle1 LOCKED
CONNECT plate-1.hole?~ -> axpin-2.axle1 LOCKED
WHY Puts a yellow 2x4 plate with holes into the centre of the side frame and locks it with axle-pins.

## Step 8 (page 8)
ADD redpin-1 32054 red
ADD redpin-2 32054 red
ADD bush-1 3713 lightgray
ADD bush-2 3713 lightgray
CONNECT redpin-1.pin1 -> frame-4.hole?~ STIFF
CONNECT redpin-2.pin1 -> frame-4.hole?~ STIFF
CONNECT bush-1.axlehole1 -> redpin-1.axle1 LOCKED
CONNECT bush-2.axlehole1 -> redpin-2.axle1 LOCKED
WHY Adds red axle-pins with bushes on the sides of the frame to give free axle ends for later shafts.

## Step 9 (page 9)
ADD pin-11 2780 black
CONNECT pin-11.pin1 -> frame-4.hole?~ STIFF
WHY Inserts one more friction pin after rotating the side assembly so it can join the main stack.

## Step 10 (page 9)
CONNECT frame-4.hole?~ -> pin-?.pin2 STIFF
WHY Seats the side frame assembly onto the main stacked frames (arrow down in the booklet).

## Step 11 (page 9)
ADD pin-12 2780 black
ADD axpin-3 43093 blue
CONNECT pin-12.pin1 -> frame-4.hole?~ STIFF
CONNECT axpin-3.pin1 -> frame-4.hole?~ STIFF
WHY Locks the joined frames with the remaining pin and axle-pin so the side pocket is solid.

## Step 12 (page 10)
ADD beam7-1 32524 yellow
ADD axpin-4 43093 blue
ADD axpin-5 43093 blue
CONNECT axpin-4.pin1 -> beam7-1.hole1~ STIFF
CONNECT axpin-5.pin1 -> beam7-1.hole7~ STIFF
CONNECT beam7-1.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a yellow 7-hole beam with two blue axle-pins as a side carrier for the next layer.

## Step 13 (page 10)
ADD beam9-1 40490 lightgray
ADD axpin-6 43093 blue
ADD axpin-7 43093 blue
CONNECT axpin-6.pin1 -> beam9-1.hole1~ STIFF
CONNECT axpin-7.pin1 -> beam9-1.hole9~ STIFF
CONNECT beam9-1.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a light-gray 9-hole beam with axle-pins on the opposite side to balance the structure.

## Step 14 (page 11)
ADD lbeam-1 32526 yellow
ADD pin-13 2780 black
ADD pin-14 2780 black
CONNECT pin-13.pin1 -> lbeam-1.hole?~ STIFF
CONNECT pin-14.pin1 -> lbeam-1.hole?~ STIFF
CONNECT lbeam-1.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a yellow L-shaped 3x5 beam as a corner brace that will support the first gear carriers.

## Step 15 (page 12)
ADD beam9-2 40490 lightgray
ADD beam9-3 40490 lightgray
ADD axpin-8 43093 blue
ADD axpin-9 43093 blue
ADD axpin-10 43093 blue
ADD axpin-11 43093 blue
CONNECT axpin-8.pin1 -> beam9-2.hole1~ STIFF
CONNECT axpin-9.pin1 -> beam9-2.hole9~ STIFF
CONNECT axpin-10.pin1 -> beam9-3.hole1~ STIFF
CONNECT axpin-11.pin1 -> beam9-3.hole9~ STIFF
CONNECT beam9-2.hole?~ -> frame-?.hole?~ STIFF
CONNECT beam9-3.hole?~ -> frame-?.hole?~ STIFF
WHY Adds two more 9-hole beams with axle-pins after rotating the assembly, giving mounting points for the gear stacks.

## Step 16 (page 12)
ADD lbeam-2 32526 yellow
ADD pin-15 2780 black
ADD pin-16 2780 black
CONNECT pin-15.pin1 -> lbeam-2.hole?~ STIFF
CONNECT pin-16.pin1 -> lbeam-2.hole?~ STIFF
CONNECT lbeam-2.hole?~ -> frame-?.hole?~ STIFF
WHY Adds the second yellow L-beam on the opposite corner so both sides of the gearbox core are braced the same way.

## Step 17 (page 13)
ADD lbeam-3 32526 yellow
ADD axle5-1 15462 reddishbrown
ADD axle5-2 15462 reddishbrown
ADD gear16-1 94925 lightgray
ADD gear16c-1 18946 red
ADD bush-3 3713 yellow
ADD bush-4 3713 lightgray
CONNECT axle5-1.axle1 -> lbeam-3.hole?~ TURNS
CONNECT axle5-2.axle1 -> lbeam-3.hole?~ TURNS
CONNECT gear16-1.axlehole1 -> axle5-1.axle2 LOCKED
CONNECT gear16c-1.axlehole1 -> axle5-2.axle2 LOCKED
CONNECT bush-3.axlehole1 -> axle5-1.axle3 LOCKED
CONNECT bush-4.axlehole1 -> axle5-2.axle3 LOCKED
WHY Builds the first gear carrier: a yellow L-beam holding two 5.5 axles with a plain 16-tooth gear and a red clutch gear ready to mesh inside the frame.

## Step 18 (page 14)
ADD lbeam-4 32526 yellow
ADD axpin-12 43093 blue
ADD axle4-1 3705 black
CONNECT axpin-12.pin1 -> lbeam-4.hole?~ STIFF
CONNECT axle4-1.axle1 -> lbeam-4.hole?~ TURNS
WHY Makes a second short carrier with a blue axle-pin and a 4L axle that will hold the next gear pair.

## Step 19 (page 14)
ADD gear16-2 94925 lightgray
ADD gear8-1 3647 lightgray
CONNECT gear16-2.axlehole1 -> axle4-1.axle2 LOCKED
CONNECT gear8-1.axlehole1 -> axle4-1.axle3 LOCKED
WHY Puts a 16-tooth and an 8-tooth gear on the 4L axle so they turn together as a reduction stage.

## Step 20 (page 14)
ADD gear16-3 94925 lightgray
ADD axle5-3 15462 reddishbrown
CONNECT gear16-3.axlehole1 -> axle5-3.axle2 LOCKED
CONNECT axle5-3.axle1 -> lbeam-4.hole?~ TURNS
WHY Adds another 16-tooth gear on a 5.5 axle that will mesh with the previous stage and carry drive out of the carrier.

## Step 21 (page 15)
ADD beam7-2 32524 yellow
ADD axpin-13 43093 blue
CONNECT axpin-13.pin1 -> beam7-2.hole1~ STIFF
CONNECT beam7-2.hole?~ -> lbeam-4.hole?~ STIFF
WHY Adds a yellow 7-hole beam as an upright that will support the outer end of the gear shafts.

## Step 22 (page 15)
ADD gear16-4 94925 lightgray
ADD axle3-1 4519 tan
CONNECT gear16-4.axlehole1 -> axle3-1.axle1 LOCKED
CONNECT axle3-1.axle2 -> beam7-2.hole?~ TURNS
WHY Mounts a 16-tooth gear on a short tan axle that meshes with the previous gear and sits in the upright beam.

## Step 23 (page 15)
ADD lbeam-5 32526 yellow
CONNECT lbeam-5.hole?~ -> beam7-2.hole?~ STIFF
WHY Caps the gear sub-assembly with another yellow L-beam so the shafts are held at both ends and the unit can be dropped into the main frame.

## Step 24 (page 16)
ADD axle3-2 4519 yellow
ADD bush-5 3713 yellow
ADD bush-6 3713 yellow
ADD gear16-5 94925 lightgray
ADD pin-17 2780 red
CONNECT gear16-5.axlehole1 -> axle3-2.axle1 LOCKED
CONNECT bush-5.axlehole1 -> axle3-2.axle2 LOCKED
CONNECT bush-6.axlehole1 -> axle3-2.axle3 LOCKED
CONNECT pin-17.pin1 -> bush-6.hole1~ STIFF
WHY Builds a short output shaft with a 16-tooth gear, two yellow bushes and a red pin that will later drive the differential.

## Step 25 (page 17)
ADD axle4-2 3705 yellow
ADD axle3-3 4519 tan
CONNECT axle4-2.axle1 -> lbeam-5.hole?~ TURNS
CONNECT axle3-3.axle1 -> beam7-2.hole?~ TURNS
WHY Adds two more short axles through the upright beams to carry additional gears.

## Step 26 (page 17)
ADD gear16c-2 18946 red
ADD bush-7 3713 lightgray
CONNECT gear16c-2.axlehole1 -> axle4-2.axle2 LOCKED
CONNECT bush-7.axlehole1 -> axle4-2.axle3 LOCKED
WHY Puts a red clutch gear and a bush on the yellow axle so it can engage or freewheel depending on the drive path.

## Step 27 (page 18)
ADD beam11-3 32525 yellow
ADD gear16-6 94925 lightgray
CONNECT gear16-6.axlehole1 -> beam11-3.hole1~ LOCKED
CONNECT beam11-3.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a long yellow 11-hole beam with a 16-tooth gear on the end that will mesh with the clutch gear and span the gearbox.

## Step 28 (page 18)
ADD gear16-7 94925 lightgray
CONNECT gear16-7.axlehole1 -> beam11-3.hole?~ LOCKED
WHY Adds a second 16-tooth gear on the long beam so both ends of the beam drive parallel shafts.

## Step 29 (page 19)
CONNECT lbeam-3.hole?~ -> frame-?.hole?~ STIFF
CONNECT lbeam-4.hole?~ -> frame-?.hole?~ STIFF
CONNECT lbeam-5.hole?~ -> frame-?.hole?~ STIFF
WHY Inserts the completed gear carrier sub-assembly into the main stacked frames (rotate and drop in as shown by the arrow).

## Step 30 (page 20)
ADD gear16-8 94925 lightgray
CONNECT gear16-8.axlehole1 -> axle5-1.axle?~ LOCKED
WHY Adds one more 16-tooth gear deep inside the frame that meshes with the first carrier gears.

## Step 31 (page 21)
ADD diff-1 62821 lightgray
ADD gear24-1 3649 red
ADD axle3-4 4519 tan
ADD axle3-5 4519 tan
ADD gear8-2 3647 lightgray
ADD gear8-3 3647 lightgray
ADD gear8-4 3647 lightgray
ADD gear8-5 3647 lightgray
ADD gear8-6 3647 lightgray
CONNECT gear8-2.axlehole1 -> diff-1.axlehole?~ LOCKED
CONNECT gear8-3.axlehole1 -> diff-1.axlehole?~ LOCKED
CONNECT gear8-4.axlehole1 -> diff-1.axlehole?~ LOCKED
CONNECT gear8-5.axlehole1 -> diff-1.axlehole?~ LOCKED
CONNECT gear24-1.axlehole1 -> diff-1.axlehole?~ LOCKED
CONNECT axle3-4.axle1 -> diff-1.axlehole?~ TURNS
CONNECT axle3-5.axle1 -> diff-1.axlehole?~ TURNS
WHY Builds the first differential: housing, four small bevels, a large red crown gear and two output axles that will drive the left and right rear wheels.

## Step 32 (page 22)
ADD connector-1 6536 black
ADD connector-2 6536 black
ADD connector-3 6536 black
ADD connector-4 6536 black
ADD axpin-14 43093 blue
ADD axpin-15 43093 blue
ADD axpin-16 43093 blue
ADD axpin-17 43093 blue
CONNECT axpin-14.pin1 -> connector-1.hole1 STIFF
CONNECT axpin-15.pin1 -> connector-2.hole1 STIFF
CONNECT axpin-16.pin1 -> connector-3.hole1 STIFF
CONNECT axpin-17.pin1 -> connector-4.hole1 STIFF
CONNECT connector-1.hole2 -> frame-?.hole?~ STIFF
CONNECT connector-2.hole2 -> frame-?.hole?~ STIFF
CONNECT connector-3.hole2 -> frame-?.hole?~ STIFF
CONNECT connector-4.hole2 -> frame-?.hole?~ STIFF
WHY Adds four perpendicular connectors with blue axle-pins that will hold the differential shafts and keep the gears aligned.

## Step 33 (page 23)
ADD axle9-1 22961 lightgray
ADD axle9-2 22961 lightgray
ADD gear16c-3 18946 red
ADD beam7-3 32524 yellow
CONNECT gear16c-3.axlehole1 -> axle9-1.axle2 LOCKED
CONNECT beam7-3.hole?~ -> axle9-1.axle3 TURNS
CONNECT axle9-1.axle1 -> connector-?.hole?~ TURNS
CONNECT axle9-2.axle1 -> connector-?.hole?~ TURNS
WHY Adds two long output shafts with a red clutch gear and a yellow beam that will later connect to the wheel hubs.

## Step 34 (page 24)
ADD beam5-1 32316 lightgray
ADD gear16-9 94925 lightgray
CONNECT gear16-9.axlehole1 -> beam5-1.hole?~ LOCKED
CONNECT beam5-1.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a short light-gray beam with a 16-tooth gear that meshes with the differential crown and transfers drive sideways.

## Step 35 (page 25)
ADD axle8-1 3707 black
ADD gear16-10 94925 lightgray
CONNECT gear16-10.axlehole1 -> axle8-1.axle2 LOCKED
CONNECT axle8-1.axle1 -> frame-?.hole?~ TURNS
WHY Inserts a long black 8L axle with a 16-tooth gear that will carry drive toward the second differential or intermediate shaft.

## Step 36 (page 26)
ADD beam9-4 40490 lightgray
ADD axpin-18 43093 blue
ADD axpin-19 43093 blue
CONNECT axpin-18.pin1 -> beam9-4.hole1~ STIFF
CONNECT axpin-19.pin1 -> beam9-4.hole9~ STIFF
CONNECT beam9-4.hole?~ -> frame-?.hole?~ STIFF
WHY Adds another 9-hole beam with blue pins across the top of the gearbox to close the structure and support more gears.

## Step 37 (page 26)
ADD gear16-11 94925 lightgray
ADD gear16-12 94925 lightgray
ADD gear16c-4 18946 red
ADD axle3-6 4519 tan
CONNECT gear16-11.axlehole1 -> axle3-6.axle1 LOCKED
CONNECT gear16-12.axlehole1 -> axle3-6.axle2 LOCKED
CONNECT gear16c-4.axlehole1 -> axle3-6.axle3 LOCKED
CONNECT axle3-6.axle?~ -> beam9-4.hole?~ TURNS
WHY Builds a triple-gear stack (two plain 16s + one clutch) on a short axle that sits in the new top beam.

## Step 38 (page 27)
ADD beam9-5 40490 lightgray
CONNECT beam9-5.hole?~ -> frame-?.hole?~ STIFF
WHY Adds the matching 9-hole beam on the other side so the top of the gearbox is fully closed and rigid.

## Step 39 (page 28)
ADD beam5-2 32316 lightgray
ADD gear16-13 94925 lightgray
ADD gear16-14 94925 lightgray
ADD axle4-3 3705 black
ADD axpin-20 43093 blue
ADD axpin-21 43093 blue
ADD lbeam-6 32526 yellow
CONNECT axpin-20.pin1 -> beam5-2.hole1~ STIFF
CONNECT axpin-21.pin1 -> beam5-2.hole5~ STIFF
CONNECT gear16-13.axlehole1 -> axle4-3.axle1 LOCKED
CONNECT gear16-14.axlehole1 -> axle4-3.axle2 LOCKED
CONNECT axle4-3.axle3 -> beam5-2.hole?~ TURNS
CONNECT lbeam-6.hole?~ -> beam5-2.hole?~ STIFF
WHY Builds a side gear carrier with two 16-tooth gears on a 4L axle that will mesh with the main drive train and sit outside the frame.

## Step 40 (page 29)
ADD gear16-15 94925 lightgray
CONNECT gear16-15.axlehole1 -> axle4-3.axle?~ LOCKED
WHY Adds one more 16-tooth gear on the outer shaft so it can drive the next stage or a wheel hub.

## Step 41 (page 29)
ADD bush-8 3713 lightgray
ADD bush-9 3713 lightgray
ADD bush-10 3713 lightgray
CONNECT bush-8.axlehole1 -> axle8-1.axle?~ LOCKED
CONNECT bush-9.axlehole1 -> axle9-1.axle?~ LOCKED
CONNECT bush-10.axlehole1 -> axle9-2.axle?~ LOCKED
WHY Caps three free axle ends with bushes so the shafts cannot slide out of the frames.

## Step 42 (page 30)
ADD axle3-7 4519 yellow
ADD axle3-8 4519 yellow
ADD axle3-9 4519 yellow
ADD bush-11 3713 yellow
ADD connector-5 32013 purple
ADD gear24-2 3650a orange
ADD pin-18 2780 red
CONNECT gear24-2.axlehole1 -> axle3-7.axle1 LOCKED
CONNECT bush-11.axlehole1 -> axle3-7.axle2 LOCKED
CONNECT pin-18.pin1 -> bush-11.hole1~ STIFF
CONNECT connector-5.hole1 -> axle3-8.axle1 LOCKED
CONNECT axle3-9.axle1 -> connector-5.hole2 LOCKED
WHY Builds a short orange-crowned shaft with a purple angle connector that will later link to the motor or an intermediate drive.

## Step 43 (page 32)
ADD axle5-4 15462 lightgray
ADD axle3-10 4519 yellow
ADD axle3-11 4519 yellow
CONNECT axle5-4.axle1 -> frame-?.hole?~ TURNS
CONNECT axle3-10.axle1 -> connector-5.hole?~ LOCKED
CONNECT axle3-11.axle1 -> gear24-2.axlehole?~ LOCKED
WHY Extends the orange crown shaft and adds a longer axle that will carry drive further into the gearbox.

## Step 44 (page 33)
ADD gear24-3 3650a lightgray
ADD gear16-16 94925 lightgray
ADD axle3-12 4519 yellow
CONNECT gear24-3.axlehole1 -> axle3-12.axle1 LOCKED
CONNECT gear16-16.axlehole1 -> axle3-12.axle2 LOCKED
WHY Builds a free-spinning gear pair (24-tooth + 16-tooth) that will later mesh with the main train.

## Step 45 (page 33)
CONNECT axle3-12.axle3 -> lbeam-6.hole?~ TURNS
WHY Mounts the free gear pair onto the side carrier so it can transfer rotation.

## Step 46 (page 33)
ADD redpin-3 32054 red
ADD bush-12 3713 lightgray
CONNECT redpin-3.pin1 -> lbeam-6.hole?~ STIFF
CONNECT bush-12.axlehole1 -> redpin-3.axle1 LOCKED
WHY Adds a red axle-pin with bush on the side carrier to give a free axle end for later attachment.

## Step 47 (page 33)
ADD lbeam-7 32526 yellow
CONNECT lbeam-7.hole?~ -> redpin-3.pin2 STIFF
WHY Caps the side carrier with another yellow L-beam so the free gear pair is fully supported.

## Step 48 (page 34)
ADD redpin-4 32054 red
ADD bush-13 3713 lightgray
CONNECT redpin-4.pin1 -> lbeam-7.hole?~ STIFF
CONNECT bush-13.axlehole1 -> redpin-4.axle1 LOCKED
WHY Adds another red axle-pin and bush on the opposite side of the new L-beam.

## Step 49 (page 34)
CONNECT lbeam-7.hole?~ -> frame-?.hole?~ STIFF
WHY Attaches the completed side gear carrier to the main gearbox frame (rotate and seat as shown).

## Step 50 (page 34)
ADD gear16c-5 18946 red
ADD gear16c-6 18946 red
ADD gear16c-7 18946 red
ADD bush-14 3713 lightgray
CONNECT gear16c-5.axlehole1 -> axle8-1.axle?~ LOCKED
CONNECT gear16c-6.axlehole1 -> axle9-1.axle?~ LOCKED
CONNECT gear16c-7.axlehole1 -> axle9-2.axle?~ LOCKED
CONNECT bush-14.axlehole1 -> axle8-1.axle?~ LOCKED
WHY Adds three more red clutch gears and a bush on the long output shafts so they can selectively engage drive.

## Step 51 (page 35)
ADD frame-5 64179 darkgray
ADD axpin-22 43093 blue
ADD axpin-23 43093 blue
CONNECT axpin-22.pin1 -> frame-5.hole?~ STIFF
CONNECT axpin-23.pin1 -> frame-5.hole?~ STIFF
WHY Starts a new 5x7 frame that will become the motor mount / second stage housing.

## Step 52 (page 35)
ADD plate-2 60484 yellow
CONNECT plate-2.hole?~ -> axpin-22.axle1 LOCKED
CONNECT plate-2.hole?~ -> axpin-23.axle1 LOCKED
WHY Puts a yellow 2x4 plate into the centre of the new frame, locked by the axle-pins.

## Step 53 (page 35)
ADD redpin-5 32054 red
ADD redpin-6 32054 red
ADD bush-15 3713 lightgray
ADD bush-16 3713 lightgray
ADD connector-6 6536 black
ADD connector-7 6536 black
CONNECT redpin-5.pin1 -> frame-5.hole?~ STIFF
CONNECT redpin-6.pin1 -> frame-5.hole?~ STIFF
CONNECT bush-15.axlehole1 -> redpin-5.axle1 LOCKED
CONNECT bush-16.axlehole1 -> redpin-6.axle1 LOCKED
CONNECT connector-6.hole1 -> frame-5.hole?~ STIFF
CONNECT connector-7.hole1 -> frame-5.hole?~ STIFF
WHY Adds red axle-pins with bushes and two perpendicular connectors on the new frame for later shaft support.

## Step 54 (page 36)
ADD beam11-4 32525 yellow
ADD pin-19 2780 black
ADD pin-20 2780 black
ADD pin-21 2780 black
ADD pin-22 2780 black
ADD pin-23 2780 black
ADD pin-24 2780 black
ADD connector-8 6536 black
ADD bush-17 3713 lightgray
ADD bush-18 3713 lightgray
CONNECT pin-19.pin1 -> beam11-4.hole?~ STIFF
CONNECT pin-20.pin1 -> beam11-4.hole?~ STIFF
CONNECT pin-21.pin1 -> beam11-4.hole?~ STIFF
CONNECT pin-22.pin1 -> beam11-4.hole?~ STIFF
CONNECT pin-23.pin1 -> beam11-4.hole?~ STIFF
CONNECT pin-24.pin1 -> beam11-4.hole?~ STIFF
CONNECT connector-8.hole1 -> beam11-4.hole?~ STIFF
CONNECT bush-17.axlehole1 -> pin-?.axle1 LOCKED
CONNECT bush-18.axlehole1 -> pin-?.axle1 LOCKED
WHY Builds a long yellow 11-hole beam with six pins and a connector that will later hold the motor drive gears.

## Step 55 (page 37)
ADD axle5-5 15462 reddishbrown
ADD axle5-6 15462 reddishbrown
ADD gear16c-8 18946 red
ADD gear16-17 94925 lightgray
ADD axpin-24 43093 blue
CONNECT axle5-5.axle1 -> beam11-4.hole?~ TURNS
CONNECT axle5-6.axle1 -> beam11-4.hole?~ TURNS
CONNECT gear16c-8.axlehole1 -> axle5-5.axle2 LOCKED
CONNECT gear16-17.axlehole1 -> axle5-6.axle2 LOCKED
CONNECT axpin-24.pin1 -> beam11-4.hole?~ STIFF
WHY Adds two 5.5 axles with a clutch gear and a plain 16-tooth gear into the long beam, ready to mesh with the motor.

## Step 56 (page 38)
ADD axle7-1 44294 yellow
ADD axle6-1 3706 red
ADD gear16-18 94925 lightgray
ADD gear16-19 94925 lightgray
CONNECT axle7-1.axle1 -> beam11-4.hole?~ TURNS
CONNECT axle6-1.axle1 -> axle7-1.axle2 LOCKED
CONNECT gear16-18.axlehole1 -> axle6-1.axle2 LOCKED
CONNECT gear16-19.axlehole1 -> axle6-1.axle3 LOCKED
WHY Builds a longer compound shaft (7L yellow + 6L red) with two 16-tooth gears that will carry drive from the motor into the gearbox.

## Step 57 (page 39)
ADD bush-19 3713 lightgray
ADD axpin-25 43093 blue
CONNECT bush-19.axlehole1 -> axle6-1.axle?~ LOCKED
CONNECT axpin-25.pin1 -> beam11-4.hole?~ STIFF
WHY Caps the long shaft with a bush and adds one more axle-pin for stability.

## Step 58 (page 39)
ADD beam11-5 32525 yellow
CONNECT beam11-5.hole?~ -> pin-?.pin2 STIFF
WHY Adds a second long yellow 11-hole beam parallel to the first, forming a sandwich that holds the motor gears.

## Step 59 (page 39)
ADD bush-20 3713 lightgray
ADD axle3-13 4519 tan
CONNECT bush-20.axlehole1 -> axle5-5.axle?~ LOCKED
CONNECT axle3-13.axle1 -> beam11-5.hole?~ TURNS
WHY Caps another free axle and inserts a short tan axle through the new beam.

## Step 60 (page 40)
CONNECT beam11-4.hole?~ -> frame-5.hole?~ STIFF
CONNECT beam11-5.hole?~ -> frame-5.hole?~ STIFF
WHY Attaches the completed motor-drive beam sandwich onto the new 5x7 frame (arrow shows seating direction).

## Step 61 (page 41)
ADD lbeam-8 32526 yellow
ADD pin-25 2780 black
ADD pin-26 2780 black
CONNECT pin-25.pin1 -> lbeam-8.hole?~ STIFF
CONNECT pin-26.pin1 -> lbeam-8.hole?~ STIFF
WHY Builds a yellow L-beam with two pins that will become a motor support bracket.

## Step 62 (page 41)
ADD axpin-26 43093 blue
ADD axpin-27 43093 blue
CONNECT axpin-26.pin1 -> lbeam-8.hole?~ STIFF
CONNECT axpin-27.pin1 -> lbeam-8.hole?~ STIFF
WHY Adds two blue axle-pins to the L-beam so it can lock into the motor mount frame.

## Step 63 (page 41)
ADD beam11-6 32525 yellow
CONNECT beam11-6.hole?~ -> pin-25.pin2 STIFF
CONNECT beam11-6.hole?~ -> pin-26.pin2 STIFF
WHY Attaches a long yellow 11-hole beam to the L-beam, forming an extended motor support arm.

## Step 64 (page 41)
ADD connector-9 6536 black
ADD pin-27 2780 black
ADD pin-28 2780 black
CONNECT pin-27.pin1 -> connector-9.hole1 STIFF
CONNECT pin-28.pin1 -> connector-9.hole2 STIFF
CONNECT connector-9.hole?~ -> beam11-6.hole?~ STIFF
WHY Adds a perpendicular connector with two pins on the end of the long beam for later attachment.

## Step 65 (page 42)
CONNECT beam11-6.hole?~ -> frame-5.hole?~ STIFF
WHY Seats the motor support arm onto the motor mount frame.

## Step 66 (page 42)
ADD axle5-7 15462 lightgray
ADD bush-21 3713 yellow
ADD bush-22 3713 yellow
CONNECT axle5-7.axle1 -> beam11-6.hole?~ TURNS
CONNECT bush-21.axlehole1 -> axle5-7.axle2 LOCKED
CONNECT bush-22.axlehole1 -> axle5-7.axle3 LOCKED
WHY Adds a 5.5 axle with two yellow bushes through the motor support arm that will later hold a gear or coupler.

## Step 67 (page 43)
ADD frame-6 64179 darkgray
ADD pin-29 2780 black
ADD pin-30 2780 black
ADD pin-31 2780 black
ADD pin-32 2780 black
ADD pin-33 2780 black
ADD pin-34 2780 black
CONNECT pin-29.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-30.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-31.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-32.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-33.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-34.pin1 -> frame-6.hole?~ STIFF
WHY Starts another 5x7 frame with six pins that will form the next stage of the chassis.

## Step 68 (page 43)
ADD axpin-28 43093 blue
ADD axpin-29 43093 blue
CONNECT axpin-28.pin1 -> frame-6.hole?~ STIFF
CONNECT axpin-29.pin1 -> frame-6.hole?~ STIFF
WHY Adds two blue axle-pins standing up on the new frame for stacking.

## Step 69 (page 43)
ADD frame-7 64179 darkgray
ADD pin-35 2780 black
ADD pin-36 2780 black
CONNECT pin-35.pin1 -> frame-7.hole?~ STIFF
CONNECT pin-36.pin1 -> frame-7.hole?~ STIFF
CONNECT frame-7.hole?~ -> axpin-28.pin2 STIFF
CONNECT frame-7.hole?~ -> axpin-29.pin2 STIFF
WHY Stacks a second 5x7 frame on the blue axle-pins and locks it with two more pins.

## Step 70 (page 44)
ADD frame-8 64179 darkgray
CONNECT frame-8.hole?~ -> pin-?.pin2 STIFF
WHY Adds a third 5x7 frame to the stack, thickening the chassis core.

## Step 71 (page 44)
ADD lbeam-9 32526 yellow
ADD pin-37 2780 black
ADD pin-38 2780 black
ADD pin-39 2780 black
ADD pin-40 2780 black
CONNECT pin-37.pin1 -> lbeam-9.hole?~ STIFF
CONNECT pin-38.pin1 -> lbeam-9.hole?~ STIFF
CONNECT pin-39.pin1 -> lbeam-9.hole?~ STIFF
CONNECT pin-40.pin1 -> lbeam-9.hole?~ STIFF
CONNECT lbeam-9.hole?~ -> frame-6.hole?~ STIFF
WHY Adds a yellow L-beam with four pins as a side brace on the stacked frames.

## Step 72 (page 44)
ADD axpin-30 43093 blue
ADD axpin-31 43093 blue
ADD axpin-32 43093 blue
ADD pin-41 2780 black
CONNECT axpin-30.pin1 -> frame-6.hole?~ STIFF
CONNECT axpin-31.pin1 -> frame-6.hole?~ STIFF
CONNECT axpin-32.pin1 -> frame-6.hole?~ STIFF
CONNECT pin-41.pin1 -> frame-6.hole?~ STIFF
WHY Adds more axle-pins and a friction pin after rotating the stack so more beams can attach.

## Step 73 (page 45)
ADD beam15-1 32278 yellow
ADD axpin-33 43093 blue
ADD axpin-34 43093 blue
ADD axpin-35 43093 blue
CONNECT axpin-33.pin1 -> beam15-1.hole1~ STIFF
CONNECT axpin-34.pin1 -> beam15-1.hole8~ STIFF
CONNECT axpin-35.pin1 -> beam15-1.hole15~ STIFF
CONNECT beam15-1.hole?~ -> frame-6.hole?~ STIFF
WHY Adds a long yellow 15-hole beam with three blue axle-pins that will become a main chassis rail.

## Step 74 (page 45)
ADD beam11-7 32525 yellow
CONNECT beam11-7.hole?~ -> frame-6.hole?~ STIFF
WHY Adds a parallel yellow 11-hole beam on the other side of the stacked frames to balance the rail.

## Step 75 (page 46)
CONNECT frame-5.hole?~ -> beam15-1.hole?~ STIFF
CONNECT frame-5.hole?~ -> beam11-7.hole?~ STIFF
WHY Joins the motor mount assembly to the new chassis rails (rotate and seat as shown).

## Step 76 (page 46)
CONNECT beam15-1.hole?~ -> frame-1.hole?~ STIFF
CONNECT beam11-7.hole?~ -> frame-1.hole?~ STIFF
WHY Connects the chassis rails to the original gearbox core so the whole rear section is now one rigid unit.

## Step 77 (page 47)
ADD beam13-1 41239 lightgray
ADD pin-42 2780 black
CONNECT pin-42.pin1 -> beam13-1.hole?~ STIFF
CONNECT beam13-1.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a long light-gray 13-hole beam across the top of the joined assemblies to stiffen the structure.

## Step 78 (page 48)
ADD gear16-20 94925 lightgray
CONNECT gear16-20.axlehole1 -> axle5-4.axle?~ LOCKED
WHY Adds one more 16-tooth gear on the intermediate shaft that meshes with the motor drive train.

## Step 79 (page 49)
ADD beam7-4 32524 yellow
ADD connector-10 6536 black
ADD pin-43 2780 black
ADD pin-44 2780 black
CONNECT pin-43.pin1 -> connector-10.hole1 STIFF
CONNECT pin-44.pin1 -> connector-10.hole2 STIFF
CONNECT connector-10.hole?~ -> beam7-4.hole?~ STIFF
CONNECT beam7-4.hole?~ -> frame-?.hole?~ STIFF
WHY Builds a short yellow beam with a perpendicular connector that will support an intermediate gear or shaft.

## Step 80 (page 50)
ADD beam5-3 32316 lightgray
ADD axpin-36 43093 blue
ADD axpin-37 43093 blue
CONNECT axpin-36.pin1 -> beam5-3.hole1~ STIFF
CONNECT axpin-37.pin1 -> beam5-3.hole5~ STIFF
CONNECT beam5-3.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a short light-gray beam with two blue axle-pins as a side support for the next stage.

## Step 81 (page 51)
ADD beam7-5 32524 yellow
ADD connector-11 6536 black
CONNECT connector-11.hole1 -> beam7-5.hole?~ STIFF
CONNECT beam7-5.hole?~ -> frame-?.hole?~ STIFF
WHY Adds another yellow 7-hole beam with a connector that will hold a vertical support.

## Step 82 (page 52)
ADD beam13-2 41239 lightgray
ADD pin-45 2780 black
CONNECT pin-45.pin1 -> beam13-2.hole?~ STIFF
CONNECT beam13-2.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a second long light-gray 13-hole beam parallel to the first, closing the top of the chassis.

## Step 83 (page 53)
ADD beam15-2 32278 yellow
ADD axpin-38 43093 blue
ADD axpin-39 43093 blue
ADD axpin-40 43093 blue
CONNECT axpin-38.pin1 -> beam15-2.hole1~ STIFF
CONNECT axpin-39.pin1 -> beam15-2.hole8~ STIFF
CONNECT axpin-40.pin1 -> beam15-2.hole15~ STIFF
CONNECT beam15-2.hole?~ -> frame-?.hole?~ STIFF
WHY Adds the matching long yellow 15-hole beam on the opposite side, completing the main chassis rails.

## Step 84 (page 54)
ADD beam15-3 32278 yellow
ADD axpin-41 43093 blue
ADD axpin-42 43093 blue
ADD axpin-43 43093 blue
ADD connector-12 6536 black
ADD connector-13 6536 black
ADD pin-46 2780 black
ADD pin-47 2780 black
ADD pin-48 2780 black
CONNECT axpin-41.pin1 -> beam15-3.hole1~ STIFF
CONNECT axpin-42.pin1 -> beam15-3.hole8~ STIFF
CONNECT axpin-43.pin1 -> beam15-3.hole15~ STIFF
CONNECT connector-12.hole1 -> beam15-3.hole?~ STIFF
CONNECT connector-13.hole1 -> beam15-3.hole?~ STIFF
CONNECT pin-46.pin1 -> connector-12.hole2 STIFF
CONNECT pin-47.pin1 -> connector-13.hole2 STIFF
CONNECT pin-48.pin1 -> beam15-3.hole?~ STIFF
CONNECT beam15-3.hole?~ -> frame-?.hole?~ STIFF
WHY Adds a third long yellow 15-hole beam with connectors and pins that will support the next sub-assembly.

## Step 85 (page 55)
ADD beam15-4 32278 yellow
ADD axpin-44 43093 blue
ADD axpin-45 43093 blue
ADD connector-14 6536 black
ADD connector-15 6536 black
ADD pin-49 2780 black
ADD pin-50 2780 black
ADD pin-51 2780 black
ADD pin-52 2780 black
CONNECT axpin-44.pin1 -> beam15-4.hole1~ STIFF
CONNECT axpin-45.pin1 -> beam15-4.hole15~ STIFF
CONNECT connector-14.hole1 -> beam15-4.hole?~ STIFF
CONNECT connector-15.hole1 -> beam15-4.hole?~ STIFF
CONNECT pin-49.pin1 -> connector-14.hole2 STIFF
CONNECT pin-50.pin1 -> connector-15.hole2 STIFF
CONNECT pin-51.pin1 -> beam15-4.hole?~ STIFF
CONNECT pin-52.pin1 -> beam15-4.hole?~ STIFF
CONNECT beam15-4.hole?~ -> frame-?.hole?~ STIFF
WHY Adds the fourth long yellow 15-hole beam with connectors, completing the lower chassis rail structure.
