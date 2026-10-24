# MOC-266362 - DIY Differential (by Totte77)

Booklet: booklet.pdf (14 pages: cover, 12 steps, closing parts-list page). Fan MOC - parts list is a
direct Rebrickable export (official part numbers, confirmed), but joins are read from the picture like
any other labeling pass, so `~` is used for hole positions not shown clearly.

## Step 1 (page 2)
ADD base-1 32184 lightgray
ADD hub-1 87082 lightgray
ADD arm-1 32140 lightgray
CONNECT hub-1.pin1~ -> base-1.hole1~ STIFF
CONNECT arm-1.hole1~ -> hub-1.pin2~ STIFF
WHY Starts the input-side bracket: a perpendicular connector carrying a pin hub, with an L-shaped arm for the turntable housing.

## Step 2 (page 3)
ADD pin-1 32054 lightgray
ADD top-1 99009 lightgray
ADD base-2 99010 black
CONNECT top-1.hole1~ -> base-2.hole1~ TURNS
CONNECT pin-1.pin1~ -> arm-1.hole2~ STIFF
WHY Builds the first turntable housing (small base + top) that will carry the satellite gears, mounted on the input bracket.

## Step 3 (page 4)
ADD pin-2 43093 blue
ADD pin-3 43093 blue
ADD hub-2 87082 lightgray
ADD arm-2 32140 lightgray
CONNECT hub-2.pin1~ -> base-1.hole2~ STIFF
CONNECT arm-2.hole1~ -> hub-2.pin2~ STIFF
WHY Mirrors step 1 on the opposite side of the base connector, with blue pins marking the turntable's rotation axle.

## Step 4 (page 5)
ADD pin-4 3749 tan
ADD gear-1 32270 black
CONNECT gear-1.axlehole1~ -> pin-4.pin1~ LOCKED
CONNECT pin-4.axle1~ -> base-2.hole2~ STIFF
WHY Mounts the first 12-tooth bevel gear onto the turntable housing on a tan axle-pin.

## Step 5 (page 6)
ADD pin-5 32054 lightgray
ADD axle-1 4519 lightgray
ADD gear-2 32270 black
CONNECT gear-2.axlehole1~ -> axle-1.axle1~ LOCKED
CONNECT axle-1.axle2~ -> base-2.hole3~ TURNS
WHY Adds the second bevel gear, meshing with the first, on its own short axle inside the turntable housing.

## Step 6 (page 7)
ADD axle-2 4519 lightgray
CONNECT axle-2.axle1~ -> base-2.hole4~ TURNS
WHY Adds the input shaft that will drive the turntable housing from outside.

## Step 7 (page 8)
ADD pin-6 32054 lightgray
ADD pin-7 32054 lightgray
ADD beam-1 32316 lightgray
CONNECT pin-6.pin1~ -> arm-1.hole3~ STIFF
CONNECT pin-7.pin1~ -> beam-1.hole1~ STIFF
CONNECT beam-1.hole5~ -> arm-2.hole3~ STIFF
WHY Closes the frame around the turntable with a 5-hole beam pinned to both side arms.

## Step 8 (page 9)
ADD pin-8 11214 darkgray
ADD pin-9 11214 darkgray
ADD arm-3 32140 lightgray
CONNECT pin-8.pin1~ -> beam-1.hole2~ STIFF
CONNECT arm-3.hole1~ -> pin-9.pin1~ STIFF
WHY Starts the output-side bracket, mirroring steps 1 and 3 for the second turntable housing.

## Step 9 (page 10)
ADD bush-1 6538c darkgray
ADD hub-3 11214 darkgray
CONNECT bush-1.hole1~ -> arm-3.hole2~ TURNS
CONNECT hub-3.pin1~ -> beam-1.hole3~ STIFF
WHY Adds a bushing and a second pin hub to carry the output-side turntable's axle.

## Step 10 (page 11)
ADD pin-10 11214 darkgray
ADD top-2 99009 lightgray
ADD base-3 99010 black
CONNECT top-2.hole1~ -> base-3.hole1~ TURNS
CONNECT pin-10.pin1~ -> arm-3.hole3~ STIFF
WHY Builds the second turntable housing for the output side, matching step 2.

## Step 11 (page 12)
ADD bush-2 6538c darkgray
ADD axle-3 4519 lightgray
ADD gear-3 32270 black
ADD arm-4 32140 lightgray
CONNECT gear-3.axlehole1~ -> axle-3.axle1~ LOCKED
CONNECT axle-3.axle2~ -> base-3.hole2~ TURNS
CONNECT arm-4.hole1~ -> base-3.hole3~ STIFF
WHY Adds the third bevel gear into the output turntable and a matching arm, joining the two turntable halves into one frame.

## Step 12 (page 13)
ADD axle-4 4519 lightgray
CONNECT axle-4.axle1~ -> base-3.hole4~ TURNS
WHY Adds the output shaft, finishing the differential - power goes in on one turntable's axle and out the other, with the turntables free to counter-rotate for the diff action.
