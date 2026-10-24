# MOC-226025 - Front Suspension with Diff (by MythicalWinter)

Booklet: booklet.pdf (42 pages, 41 steps). Fan MOC - parts list is a direct Rebrickable export (official
part numbers, confirmed), but joins are read from the picture like any other labeling pass, so `~` is
used for hole positions not shown clearly, and some small similar-looking connector parts are a best
reading of the render rather than a certain match.

## Step 1 (page 2)
ADD frame-1 64179 lightgray
WHY Starts with the 5 x 7 open frame that is the heart of the whole suspension assembly.

## Step 2 (page 3)
ADD pin-1 61332 black
ADD pin-2 61332 black
ADD pin-3 61332 black
ADD pin-4 61332 black
CONNECT pin-1.pin1~ -> frame-1.hole1~ STIFF
CONNECT pin-2.pin1~ -> frame-1.hole2~ STIFF
CONNECT pin-3.pin1~ -> frame-1.hole3~ STIFF
CONNECT pin-4.pin1~ -> frame-1.hole4~ STIFF
WHY Pins the four corners of the frame, ready to carry the long side beams.

## Step 3 (page 4)
ADD beam-1 32278 black
ADD beam-2 32278 black
CONNECT beam-1.hole1~ -> pin-1.pin2~ STIFF
CONNECT beam-2.hole1~ -> pin-2.pin2~ STIFF
WHY Adds the two 15-hole beams that form the long sides of the suspension arm.

## Step 4 (page 5)
ADD pin-5 43093 blue
ADD pin-6 43093 blue
CONNECT pin-5.axle1~ -> frame-1.hole5~ STIFF
CONNECT pin-6.axle1~ -> frame-1.hole6~ STIFF
WHY Adds two more pins to the frame, marking where the differential housing will mount.

## Step 5 (page 6)
ADD beam-3 32524 black
ADD beam-4 32524 black
ADD axle-7 4519 lightgray
ADD axle-8 4519 lightgray
CONNECT beam-3.hole1~ -> pin-5.pin1~ STIFF
CONNECT beam-4.hole1~ -> pin-6.pin1~ STIFF
WHY Adds the first two 7-hole beams, starting a second layer above the frame.

## Step 6 (page 7)
ADD pin-7 6558 blue
ADD pin-8 6558 blue
CONNECT pin-7.pin1~ -> beam-3.hole2~ STIFF
CONNECT pin-8.pin1~ -> beam-4.hole2~ STIFF
WHY Extends the second layer with long friction pins for the next beams.

## Step 7 (page 8)
ADD diffbevel-1 6589 tan
ADD diffbevel-2 6589 tan
ADD diffbevel-3 6589 tan
ADD diffhousing-1 62821b darkgray
CONNECT diffbevel-1.axlehole1~ -> diffhousing-1.hole1~ TURNS
CONNECT diffbevel-2.axlehole1~ -> diffhousing-1.hole2~ TURNS
CONNECT diffbevel-3.axlehole1~ -> diffhousing-1.hole3~ TURNS
WHY Builds the differential: three bevel gears free to spin inside the 28-tooth housing.

## Step 8 (page 9)
WHY Drops the finished differential into the frame between the two beam layers.

## Step 9 (page 10)
ADD towpin-1 66906 black
ADD towpin-2 66906 black
CONNECT towpin-1.pin1~ -> beam-1.hole2~ STIFF
CONNECT towpin-2.pin1~ -> beam-2.hole2~ STIFF
WHY Adds two towball pins to the long side beams, for the steering linkage later.

## Step 10 (page 11)
ADD beam-5 32524 black
ADD beam-6 32524 black
ADD axle-9 4519 lightgray
ADD axle-10 4519 lightgray
CONNECT beam-5.hole1~ -> beam-3.hole3~ STIFF
CONNECT beam-6.hole1~ -> beam-4.hole3~ STIFF
WHY Adds the remaining two 7-hole beams, closing out that part count.

## Step 11 (page 12)
ADD pin-9 59443 black
ADD hub-1 10197 darkgray
ADD hub-2 10197 darkgray
WHY Adds a blue pin and two perpendicular-axle hubs, starting the steering tie-rod mounts.

## Step 12 (page 13)
WHY No new parts - fits the differential's pinion gear into mesh with the housing.

## Step 13 (page 14)
ADD bush-1 32123b lightgray
ADD bush-2 32123b lightgray
ADD bush-3 32123b lightgray
ADD bush-4 32123b lightgray
ADD bush-5 32123b lightgray
ADD bush-6 32123b lightgray
ADD bush-7 32123b lightgray
ADD bush-8 32123b lightgray
CONNECT bush-1.hole1~ -> pin-1.pin2~ TURNS
CONNECT bush-2.hole1~ -> pin-2.pin2~ TURNS
CONNECT bush-3.hole1~ -> pin-3.pin2~ TURNS
CONNECT bush-4.hole1~ -> pin-4.pin2~ TURNS
CONNECT bush-5.hole1~ -> pin-5.pin2~ TURNS
CONNECT bush-6.hole1~ -> pin-6.pin2~ TURNS
CONNECT bush-7.hole1~ -> pin-7.pin2~ TURNS
CONNECT bush-8.hole1~ -> pin-8.pin2~ TURNS
WHY Caps all eight corner pins with half bushes so the frame spins freely where it needs to.

## Step 14 (page 15)
ADD conn-1 60483 lightgray
ADD conn-2 60483 lightgray
ADD conn-3 60483 lightgray
ADD conn-4 60483 lightgray
ADD pin-10 66906 black
ADD pin-11 66906 black
ADD pin-12 61332 black
ADD pin-13 61332 black
CONNECT conn-1.hole1~ -> pin-10.pin1~ STIFF
CONNECT conn-2.hole1~ -> pin-11.pin1~ STIFF
CONNECT conn-3.hole1~ -> pin-12.pin1~ STIFF
CONNECT conn-4.hole1~ -> pin-13.pin1~ STIFF
WHY Adds four small pin-and-axle connectors, mounting points for the steering knuckles.

## Step 15 (page 16)
ADD pin-14 6558 blue
ADD pin-15 6558 blue
CONNECT pin-14.pin1~ -> conn-1.axlehole1~ STIFF
CONNECT pin-15.pin1~ -> conn-2.axlehole1~ STIFF
WHY Adds two more blue pins onto the new connectors.

## Step 16 (page 17)
ADD beam-7 11478 black
ADD beam-8 11478 black
ADD beam-9 11478 black
ADD beam-10 11478 black
ADD axle-11 4519 lightgray
ADD axle-12 4519 lightgray
CONNECT beam-7.hole1~ -> pin-14.pin1~ STIFF
CONNECT beam-8.hole1~ -> pin-15.pin1~ STIFF
WHY Boxes the differential in with four 5-hole thin beams.

## Step 17 (page 18)
ADD beam-11 32316 lightgray
ADD pin-16 6558 blue
ADD pin-17 6558 blue
CONNECT beam-11.hole1~ -> pin-16.pin1~ STIFF
WHY Adds the first 5-hole thick beam, closing one end of the box frame.

## Step 18 (page 19)
ADD link-1 32005a black
ADD link-2 32005a black
CONNECT link-1.pin1~ -> beam-7.hole5~ TURNS
CONNECT link-2.pin1~ -> beam-8.hole5~ TURNS
WHY Adds two short links, the start of the steering tie-rod on each side.

## Step 19 (page 20)
ADD pin-18 61332 black
ADD pin-19 61332 black
ADD knuckle-1 64872 darkgray
ADD knuckle-2 64872 darkgray
CONNECT knuckle-1.hole1~ -> link-1.hole1~ TURNS
CONNECT knuckle-2.hole1~ -> link-2.hole1~ TURNS
WHY Adds the first two steering knuckles (towball-socket arms) on each side.

## Step 20 (page 21)
ADD knuckle-3 64872 darkgray
WHY Builds a third steering knuckle as a separate sub-assembly.

## Step 21 (page 22)
ADD pin-20 61332 black
WHY Caps the third knuckle's holes and adds a pin for the shock absorber.

## Step 22 (page 23)
ADD pin-21 61332 black
ADD shock-1 76537 red
CONNECT shock-1.pin1~ -> knuckle-3.hole3~ TURNS
WHY Mounts the first shock absorber onto the third knuckle.

## Step 23 (page 24)
WHY Caps the shock absorber's pivot pins.

## Step 24 (page 25)
WHY No new parts - rotates the finished knuckle/shock sub-assembly for the next step.

## Step 25 (page 26)
WHY Attaches the first knuckle/shock sub-assembly to the left side of the main frame.

## Step 26 (page 27)
ADD knuckle-4 64872 darkgray
WHY Builds the second steering knuckle sub-assembly, mirroring step 20.

## Step 27 (page 28)
ADD pin-22 61332 black
WHY Caps the fourth knuckle's holes and adds a pin for its shock absorber, mirroring step 21.

## Step 28 (page 29)
ADD pin-23 61332 black
ADD shock-2 76537 red
CONNECT shock-2.pin1~ -> knuckle-4.hole3~ TURNS
WHY Mounts the second shock absorber, mirroring step 22.

## Step 29 (page 30)
WHY Caps the second shock absorber's pivot pins, mirroring step 23.

## Step 30 (page 31)
WHY No new parts - rotates the second knuckle/shock sub-assembly.

## Step 31 (page 32)
WHY Attaches the second knuckle/shock sub-assembly to the right side of the main frame.

## Step 32 (page 33)
ADD cv-1 52730 darkgray
ADD cv-2 52730 darkgray
ADD cv-3 52731 lightgray
ADD cv-4 52731 lightgray
ADD cv-5 52731 lightgray
ADD cv-6 52731 lightgray
CONNECT cv-1.axle1~ -> knuckle-1.hole2~ TURNS
CONNECT cv-2.axle1~ -> knuckle-2.hole2~ TURNS
WHY Adds the CV joint female halves and male caps that will carry drive out to the wheels.

## Step 33 (page 34)
ADD hub-3 46490 lightgray
ADD hub-4 46490 lightgray
ADD stud-1 6587 darkgray
ADD stud-2 6587 darkgray
CONNECT hub-3.axle1~ -> cv-1.axle2~ TURNS
CONNECT hub-4.axle1~ -> cv-2.axle2~ TURNS
WHY Mounts the two wheel hubs (with their planetary gear reduction) onto the CV joints.

## Step 34 (page 35)
ADD axle-1 4519 lightgray
ADD axle-2 4519 lightgray
ADD arm-1 41677 black
ADD arm-2 41677 black
ADD arm-3 41677 black
ADD arm-4 41677 black
WHY Adds four short thin beams and two short axles, building the steering arms on both knuckles.

## Step 35 (page 36)
ADD hub-5 6536 lightgray
ADD hub-6 6536 lightgray
ADD ball-1 59443 black
ADD ball-2 59443 black
ADD conn-5 32034 black
ADD conn-6 32034 black
WHY Adds the steering tie-rod end connectors on both wheel hubs.

## Step 36 (page 37)
ADD pin-24 59443 black
ADD pin-25 61332 black
ADD tri-1 60484 black
WHY Adds the 3 x 3 T-shaped beam that anchors the steering linkage's center pivot.

## Step 37 (page 38)
ADD pinion-1 18575 tan
ADD axle-3 44294 lightgray
ADD stud-3 6587 darkgray
ADD stud-4 6587 darkgray
CONNECT pinion-1.axlehole1~ -> axle-3.axle1~ LOCKED
CONNECT axle-3.axle2~ -> diffhousing-1.hole4~ TURNS
WHY Adds the drive input: a 20-tooth bevel gear on a long axle through the differential housing.

## Step 38 (page 39)
ADD cv-7 6587 darkgray
ADD cv-8 6587 darkgray
ADD pin-26 61332 black
ADD pin-27 61332 black
ADD axle-4 4519 lightgray
ADD axle-5 4519 lightgray
WHY Builds the second pair of CV joint links for the steering tie-rod, with their own pins and caps.

## Step 39 (page 40)
ADD pin-28 6632 black
ADD pin-29 6632 black
ADD beam-12 32316 lightgray
WHY Adds one more 5-hole thick beam and two short thin beams, extending the tie-rod linkage frame.

## Step 40 (page 41)
ADD pinion-2 32270 black
ADD axle-6 32062 red
ADD axle-13 32062 red
ADD axle-14 32062 red
ADD axle-15 32062 red
ADD rack-1 87761 black
CONNECT pinion-2.axlehole1~ -> axle-6.axle1~ LOCKED
CONNECT rack-1.hole1~ -> axle-6.axle2~ STIFF
WHY Adds the steering rack and its drive pinion, turning rotation into side-to-side steering motion.

## Step 41 (page 42)
ADD pin-30 32073 lightgray
ADD pin-31 61332 black
ADD beam-14 32316 lightgray
WHY Closes out the frame with the last 5-hole thick beam, finishing the front suspension and differential assembly.
