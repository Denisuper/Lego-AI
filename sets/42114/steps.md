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
