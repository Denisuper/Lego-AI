# Set 42175 - Volvo EC230 Electric Excavator

Booklet: booklet.pdf (180 pages, 199 steps). One block per step: parts added, joins, and one line on why. `~` = best reading of the picture, `?` = not shown.

## Step 1 (page 2)
ADD uc-frame-1 64179 black
ADD uc-pin-1 65304 black
ADD uc-pin-2 65304 black
ADD uc-pin-3 65304 black
ADD uc-pin-4 65304 black
CONNECT uc-pin-1.pin1 -> uc-frame-1.hole1~ STIFF
CONNECT uc-pin-2.pin1 -> uc-frame-1.hole5~ STIFF
CONNECT uc-pin-3.pin1 -> uc-frame-1.hole16~ STIFF
CONNECT uc-pin-4.pin1 -> uc-frame-1.hole20~ STIFF
WHY Starts the undercarriage with a stiff rectangular base and four posts to hang the next beams on.

## Step 2 (page 3)
ADD uc-beam9-1 40490 darkgray
ADD uc-beam9-2 40490 darkgray
CONNECT uc-pin-1.pin2 -> uc-beam9-1.hole2~ STIFF
CONNECT uc-pin-3.pin2 -> uc-beam9-1.hole8~ STIFF
CONNECT uc-pin-2.pin2 -> uc-beam9-2.hole2~ STIFF
CONNECT uc-pin-4.pin2 -> uc-beam9-2.hole8~ STIFF
WHY Doubles the thickness of the frame's long sides and gives free end holes for the next pins.

## Step 3 (page 3)
ADD uc-apin-1 18651 black
ADD uc-apin-2 18651 black
ADD uc-apin-3 18651 black
ADD uc-apin-4 18651 black
CONNECT uc-apin-1.pin1 -> uc-beam9-1.hole1~ STIFF
CONNECT uc-apin-2.pin1 -> uc-beam9-1.hole9~ STIFF
CONNECT uc-apin-3.pin1 -> uc-beam9-2.hole1~ STIFF
CONNECT uc-apin-4.pin1 -> uc-beam9-2.hole9~ STIFF
WHY Adds the posts that the long outer beams will sit on.

## Step 4 (page 3)
ADD uc-beam11-1 32525 black
ADD uc-beam11-2 32525 black
CONNECT uc-apin-1.pin1 -> uc-beam11-1.hole1~ STIFF
CONNECT uc-apin-2.pin1 -> uc-beam11-1.hole3~ STIFF
CONNECT uc-apin-3.pin1 -> uc-beam11-2.hole1~ STIFF
CONNECT uc-apin-4.pin1 -> uc-beam11-2.hole3~ STIFF
WHY Widens and lengthens the base so it can carry the track rails later.

## Step 5 (page 4)
ADD uc-lbeam-1 32526 black
ADD uc-lbeam-2 32526 black
ADD uc-lbeam-3 32526 black
ADD uc-lbeam-4 32526 black
ADD uc-beam15-1 32278 black
ADD uc-beam15-2 32278 black
ADD uc-beam5-1 32316 lightgray
ADD uc-beam5-2 32316 lightgray
ADD uc-bpin-1 43093 blue
ADD uc-bpin-2 43093 blue
ADD uc-bpin-3 43093 blue
ADD uc-bpin-4 43093 blue
ADD uc-lpin-1 42924 blue
ADD uc-lpin-2 42924 blue
ADD uc-lpin-3 42924 blue
ADD uc-lpin-4 42924 blue
ADD uc-apin-5 18651 black
ADD uc-apin-6 18651 black
ADD uc-apin-7 18651 black
ADD uc-apin-8 18651 black
CONNECT uc-bpin-1.pin1 -> uc-beam5-1.hole1~ STIFF
CONNECT uc-bpin-2.pin1 -> uc-beam5-1.hole5~ STIFF
CONNECT uc-bpin-3.pin1 -> uc-beam5-2.hole1~ STIFF
CONNECT uc-bpin-4.pin1 -> uc-beam5-2.hole5~ STIFF
WHY Builds the two long side members that will carry the track wheels.

## Step 6 (page 5)
ADD uc-beam7-1 32524 black
ADD uc-beam7-2 32524 black
ADD uc-beam7-3 32524 black
ADD uc-beam7-4 32524 black
ADD uc-apin-9 18651 black
ADD uc-apin-10 18651 black
ADD uc-apin-11 18651 black
ADD uc-apin-12 18651 black
CONNECT uc-apin-9.pin1 -> uc-beam7-1.hole4~ STIFF
CONNECT uc-apin-10.pin1 -> uc-beam7-2.hole4~ STIFF
CONNECT uc-apin-11.pin1 -> uc-beam7-3.hole4~ STIFF
CONNECT uc-apin-12.pin1 -> uc-beam7-4.hole4~ STIFF
WHY Ties the left and right sides together so the base can't spread.

## Step 7 (page 6)
ADD uc-axpin-1 43093 blue
ADD uc-axpin-2 43093 blue
ADD uc-axpin-3 43093 blue
ADD uc-axpin-4 43093 blue
ADD uc-axpin-5 43093 blue
ADD uc-axpin-6 43093 blue
ADD uc-axpin-7 43093 blue
ADD uc-axpin-8 43093 blue
ADD uc-pin-5 65304 black
ADD uc-pin-6 65304 black
ADD uc-pin-7 65304 black
ADD uc-pin-8 65304 black
ADD uc-pin-9 65304 black
ADD uc-pin-10 65304 black
ADD uc-pin-11 65304 black
ADD uc-pin-12 65304 black
CONNECT uc-axpin-1.axle1 -> uc-pin-5.axlehole1 LOCKED
CONNECT uc-axpin-2.axle1 -> uc-pin-6.axlehole1 LOCKED
CONNECT uc-axpin-3.axle1 -> uc-pin-7.axlehole1 LOCKED
CONNECT uc-axpin-4.axle1 -> uc-pin-8.axlehole1 LOCKED
CONNECT uc-axpin-5.axle1 -> uc-pin-9.axlehole1 LOCKED
CONNECT uc-axpin-6.axle1 -> uc-pin-10.axlehole1 LOCKED
CONNECT uc-axpin-7.axle1 -> uc-pin-11.axlehole1 LOCKED
CONNECT uc-axpin-8.axle1 -> uc-pin-12.axlehole1 LOCKED
CONNECT uc-pin-5.pin1 -> uc-beam11-1.hole2~ STIFF
CONNECT uc-pin-6.pin1 -> uc-beam11-1.hole4~ STIFF
CONNECT uc-pin-7.pin1 -> uc-beam11-1.hole8~ STIFF
CONNECT uc-pin-8.pin1 -> uc-beam11-1.hole10~ STIFF
CONNECT uc-pin-9.pin1 -> uc-beam11-2.hole2~ STIFF
CONNECT uc-pin-10.pin1 -> uc-beam11-2.hole4~ STIFF
CONNECT uc-pin-11.pin1 -> uc-beam11-2.hole8~ STIFF
CONNECT uc-pin-12.pin1 -> uc-beam11-2.hole10~ STIFF
WHY Gives the track rollers and wheel carriers something to hang on.

## Step 8 (page 7)
ADD uc-tpin-1 39888 tan
ADD uc-tpin-2 39888 tan
ADD uc-tpin-3 39888 tan
ADD uc-tpin-4 39888 tan
ADD uc-tpin-5 39888 tan
ADD uc-tpin-6 39888 tan
CONNECT uc-tpin-1.pin1 -> uc-beam11-1.hole3~ TURNS
CONNECT uc-tpin-2.pin1 -> uc-beam11-1.hole9~ TURNS
CONNECT uc-tpin-3.pin1 -> uc-beam11-1.hole6~ TURNS
CONNECT uc-tpin-4.pin1 -> uc-beam11-2.hole3~ TURNS
CONNECT uc-tpin-5.pin1 -> uc-beam11-2.hole9~ TURNS
CONNECT uc-tpin-6.pin1 -> uc-beam11-2.hole6~ TURNS
WHY Adds the spindles on which free-turning track rollers will run.

## Step 9 (page 8)
ADD trk-beam5-1 32316 lightgray
ADD trk-beam5-2 32316 lightgray
ADD trk-axpin-1 18651 black
ADD trk-axpin-2 18651 black
ADD trk-axpin-3 18651 black
ADD trk-axpin-4 18651 black
ADD trk-tpin-1 3749 tan
ADD trk-tpin-2 3749 tan
ADD trk-tpin-3 3749 tan
ADD trk-tpin-4 3749 tan
ADD trk-wheel-1 42610 black
ADD trk-wheel-2 42610 black
ADD trk-wheel-3 42610 black
ADD trk-wheel-4 42610 black
ADD trk-tyre-1 50951 black
ADD trk-tyre-2 50951 black
ADD trk-tyre-3 50951 black
ADD trk-tyre-4 50951 black
CONNECT trk-axpin-1.pin1 -> trk-beam5-1.hole1~ STIFF
CONNECT trk-axpin-3.pin1 -> trk-beam5-1.hole5~ STIFF
CONNECT trk-axpin-2.pin1 -> trk-beam5-2.hole1~ STIFF
CONNECT trk-axpin-4.pin1 -> trk-beam5-2.hole5~ STIFF
CONNECT trk-tpin-1.pin1 -> trk-beam5-1.hole2~ TURNS
CONNECT trk-tpin-2.pin1 -> trk-beam5-1.hole4~ TURNS
CONNECT trk-tpin-3.pin1 -> trk-beam5-2.hole2~ TURNS
CONNECT trk-tpin-4.pin1 -> trk-beam5-2.hole4~ TURNS
WHY Adds the small rollers that the track will run on.

## Step 10 (page 9)
ADD trk-axle5-1 32073 lightgray
ADD trk-axle5-2 32073 lightgray
ADD trk-sprocket-1 57520 black
ADD trk-sprocket-2 57520 black
CONNECT trk-axle5-1.axle1 -> uc-beam11-1.hole1~ TURNS
CONNECT trk-axle5-2.axle1 -> uc-beam11-2.hole1~ TURNS
CONNECT trk-axle5-1.axle3 -> trk-sprocket-1.axlehole1~ LOCKED
CONNECT trk-axle5-2.axle3 -> trk-sprocket-2.axlehole1~ LOCKED
WHY Starts the drive end of the track: the sprockets are the wheels whose teeth will grab the track links.

## Step 11 (page 10)
ADD trk-axle4-1 87083 darkgray
ADD trk-axle4-2 87083 darkgray
ADD trk-sprocket-3 57520 black
ADD trk-sprocket-4 57520 black
CONNECT trk-axle4-1.axle1 -> uc-beam11-1.hole11~ TURNS
CONNECT trk-axle4-2.axle1 -> uc-beam11-2.hole11~ TURNS
CONNECT trk-axle4-1.axle3 -> trk-sprocket-3.axlehole1~ LOCKED
CONNECT trk-axle4-2.axle3 -> trk-sprocket-4.axlehole1~ LOCKED
WHY Gives each track loop a sprocket at the front and at the back.

## Step 12 (page 11)
ADD trk-roller-1 55982 lightgray
ADD trk-roller-2 55982 lightgray
ADD trk-roller-3 55982 lightgray
ADD trk-roller-4 55982 lightgray
ADD trk-roller-5 55982 lightgray
ADD trk-roller-6 55982 lightgray
WHY Adds the lower rollers that carry the weight on the track.

## Step 13 (page 12)
ADD trk-beam15-1 32278 black
ADD trk-beam15-2 32278 black
ADD trk-beam9-1 40490 darkgray
ADD trk-beam9-2 40490 darkgray
ADD trk-beam9-3 40490 darkgray
ADD trk-beam9-4 40490 darkgray
ADD trk-pin-1 65304 black
ADD trk-pin-2 65304 black
ADD trk-pin-3 65304 black
ADD trk-pin-4 65304 black
ADD trk-pin-5 65304 black
ADD trk-pin-6 65304 black
ADD trk-pin-7 65304 black
ADD trk-pin-8 65304 black
CONNECT trk-pin-1.pin1 -> trk-beam15-1.hole1 STIFF
CONNECT trk-pin-2.pin1 -> trk-beam15-1.hole8 STIFF
CONNECT trk-pin-3.pin1 -> trk-beam15-1.hole10 STIFF
CONNECT trk-pin-4.pin1 -> trk-beam15-1.hole15 STIFF
CONNECT trk-pin-1.pin2 -> trk-beam9-1.hole1~ STIFF
CONNECT trk-pin-2.pin2 -> trk-beam9-1.hole8~ STIFF
CONNECT trk-pin-3.pin2 -> trk-beam9-2.hole4~ STIFF
CONNECT trk-pin-4.pin2 -> trk-beam9-2.hole9~ STIFF
CONNECT trk-pin-5.pin1 -> trk-beam15-2.hole1 STIFF
CONNECT trk-pin-6.pin1 -> trk-beam15-2.hole8 STIFF
CONNECT trk-pin-7.pin1 -> trk-beam15-2.hole10 STIFF
CONNECT trk-pin-8.pin1 -> trk-beam15-2.hole15 STIFF
CONNECT trk-pin-5.pin2 -> trk-beam9-3.hole1~ STIFF
CONNECT trk-pin-6.pin2 -> trk-beam9-3.hole8~ STIFF
CONNECT trk-pin-7.pin2 -> trk-beam9-4.hole4~ STIFF
CONNECT trk-pin-8.pin2 -> trk-beam9-4.hole9~ STIFF
WHY Builds the long track frames that hold the wheels in line and give the track something to slide on.

## Step 14 (page 13)
ADD trk-capplate-1 2476a lightgray
ADD trk-capplate-2 2476a lightgray
ADD trk-capdisc-1 4032a black
ADD trk-capdisc-2 4032a black
ADD trk-captile-1 15535 black
ADD trk-captile-2 15535 black
WHY Covers the bare axle ends so they look finished and can't catch.

## Step 15 (page 14)
ADD uc-lpin-5 65304 lightgray
ADD uc-lpin-6 65304 lightgray
ADD uc-lpin-7 65304 lightgray
ADD uc-lpin-8 65304 lightgray
CONNECT uc-lpin-5.pin1 -> uc-frame-1.hole?
CONNECT uc-lpin-6.pin1 -> uc-frame-1.hole?
CONNECT uc-lpin-7.pin1 -> uc-frame-1.hole?
CONNECT uc-lpin-8.pin1 -> uc-frame-1.hole?
WHY Adds the posts the next layer (the turntable base) will hang from.

## Step 16 (page 15)
ADD trk-link-1 88323 black
ADD trk-link-2 88323 black
ADD trk-link-3 88323 black
ADD trk-link-4 88323 black
ADD trk-link-5 88323 black
ADD trk-link-6 88323 black
ADD trk-link-7 88323 black
ADD trk-link-8 88323 black
ADD trk-link-9 88323 black
ADD trk-link-10 88323 black
ADD trk-link-11 88323 black
ADD trk-link-12 88323 black
ADD trk-link-13 88323 black
ADD trk-link-14 88323 black
ADD trk-link-15 88323 black
ADD trk-link-16 88323 black
ADD trk-link-17 88323 black
ADD trk-link-18 88323 black
ADD trk-link-19 88323 black
ADD trk-link-20 88323 black
ADD trk-link-21 88323 black
ADD trk-link-22 88323 black
ADD trk-link-23 88323 black
ADD trk-link-24 88323 black
ADD trk-link-25 88323 black
ADD trk-link-26 88323 black
ADD trk-link-27 88323 black
ADD trk-link-28 88323 black
ADD trk-link-29 88323 black
ADD trk-link-30 88323 black
ADD trk-link-31 88323 black
ADD trk-link-32 88323 black
ADD trk-link-33 88323 black
ADD trk-link-34 88323 black
ADD trk-link-35 88323 black
ADD trk-link-36 88323 black
ADD trk-link-37 88323 black
ADD trk-link-38 88323 black
ADD trk-link-39 88323 black
ADD trk-link-40 88323 black
ADD trk-link-41 88323 black
ADD trk-link-42 88323 black
ADD trk-link-43 88323 black
ADD trk-link-44 88323 black
ADD trk-link-45 88323 black
ADD trk-link-46 88323 black
ADD trk-link-47 88323 black
ADD trk-link-48 88323 black
ADD trk-link-49 88323 black
ADD trk-link-50 88323 black
ADD trk-link-51 88323 black
ADD trk-link-52 88323 black
ADD trk-link-53 88323 black
ADD trk-link-54 88323 black
ADD trk-link-55 88323 black
ADD trk-link-56 88323 black
ADD trk-link-57 88323 black
ADD trk-link-58 88323 black
ADD trk-link-59 88323 black
ADD trk-link-60 88323 black
CONNECT trk-link-1.bar1 -> trk-link-2.clip1 TURNS
CONNECT trk-link-2.bar1 -> trk-link-3.clip1 TURNS
CONNECT trk-link-3.bar1 -> trk-link-4.clip1 TURNS
CONNECT trk-link-4.bar1 -> trk-link-5.clip1 TURNS
CONNECT trk-link-5.bar1 -> trk-link-6.clip1 TURNS
CONNECT trk-link-6.bar1 -> trk-link-7.clip1 TURNS
CONNECT trk-link-7.bar1 -> trk-link-8.clip1 TURNS
CONNECT trk-link-8.bar1 -> trk-link-9.clip1 TURNS
CONNECT trk-link-9.bar1 -> trk-link-10.clip1 TURNS
CONNECT trk-link-10.bar1 -> trk-link-11.clip1 TURNS
CONNECT trk-link-11.bar1 -> trk-link-12.clip1 TURNS
CONNECT trk-link-12.bar1 -> trk-link-13.clip1 TURNS
CONNECT trk-link-13.bar1 -> trk-link-14.clip1 TURNS
CONNECT trk-link-14.bar1 -> trk-link-15.clip1 TURNS
CONNECT trk-link-15.bar1 -> trk-link-16.clip1 TURNS
CONNECT trk-link-16.bar1 -> trk-link-17.clip1 TURNS
CONNECT trk-link-17.bar1 -> trk-link-18.clip1 TURNS
CONNECT trk-link-18.bar1 -> trk-link-19.clip1 TURNS
CONNECT trk-link-19.bar1 -> trk-link-20.clip1 TURNS
CONNECT trk-link-20.bar1 -> trk-link-21.clip1 TURNS
CONNECT trk-link-21.bar1 -> trk-link-22.clip1 TURNS
CONNECT trk-link-22.bar1 -> trk-link-23.clip1 TURNS
CONNECT trk-link-23.bar1 -> trk-link-24.clip1 TURNS
CONNECT trk-link-24.bar1 -> trk-link-25.clip1 TURNS
CONNECT trk-link-25.bar1 -> trk-link-26.clip1 TURNS
CONNECT trk-link-26.bar1 -> trk-link-27.clip1 TURNS
CONNECT trk-link-27.bar1 -> trk-link-28.clip1 TURNS
CONNECT trk-link-28.bar1 -> trk-link-29.clip1 TURNS
CONNECT trk-link-29.bar1 -> trk-link-30.clip1 TURNS
CONNECT trk-link-30.bar1 -> trk-link-1.clip1 TURNS
CONNECT trk-link-31.bar1 -> trk-link-32.clip1 TURNS
CONNECT trk-link-32.bar1 -> trk-link-33.clip1 TURNS
CONNECT trk-link-33.bar1 -> trk-link-34.clip1 TURNS
CONNECT trk-link-34.bar1 -> trk-link-35.clip1 TURNS
CONNECT trk-link-35.bar1 -> trk-link-36.clip1 TURNS
CONNECT trk-link-36.bar1 -> trk-link-37.clip1 TURNS
CONNECT trk-link-37.bar1 -> trk-link-38.clip1 TURNS
CONNECT trk-link-38.bar1 -> trk-link-39.clip1 TURNS
CONNECT trk-link-39.bar1 -> trk-link-40.clip1 TURNS
CONNECT trk-link-40.bar1 -> trk-link-41.clip1 TURNS
CONNECT trk-link-41.bar1 -> trk-link-42.clip1 TURNS
CONNECT trk-link-42.bar1 -> trk-link-43.clip1 TURNS
CONNECT trk-link-43.bar1 -> trk-link-44.clip1 TURNS
CONNECT trk-link-44.bar1 -> trk-link-45.clip1 TURNS
CONNECT trk-link-45.bar1 -> trk-link-46.clip1 TURNS
CONNECT trk-link-46.bar1 -> trk-link-47.clip1 TURNS
CONNECT trk-link-47.bar1 -> trk-link-48.clip1 TURNS
CONNECT trk-link-48.bar1 -> trk-link-49.clip1 TURNS
CONNECT trk-link-49.bar1 -> trk-link-50.clip1 TURNS
CONNECT trk-link-50.bar1 -> trk-link-51.clip1 TURNS
CONNECT trk-link-51.bar1 -> trk-link-52.clip1 TURNS
CONNECT trk-link-52.bar1 -> trk-link-53.clip1 TURNS
CONNECT trk-link-53.bar1 -> trk-link-54.clip1 TURNS
CONNECT trk-link-54.bar1 -> trk-link-55.clip1 TURNS
CONNECT trk-link-55.bar1 -> trk-link-56.clip1 TURNS
CONNECT trk-link-56.bar1 -> trk-link-57.clip1 TURNS
CONNECT trk-link-57.bar1 -> trk-link-58.clip1 TURNS
CONNECT trk-link-58.bar1 -> trk-link-59.clip1 TURNS
CONNECT trk-link-59.bar1 -> trk-link-60.clip1 TURNS
CONNECT trk-link-60.bar1 -> trk-link-31.clip1 TURNS
WHY Makes the tracks that the machine rolls on.

## Step 17 (page 17)
ADD sw-top-1 88738 black
ADD sw-base-1 18939 lightgray
ADD sw-bpin-1 42924 blue
ADD sw-bpin-2 42924 blue
ADD sw-bpin-3 42924 blue
ADD sw-bpin-4 42924 blue
CONNECT uc-lpin-1.pin1 -> sw-base-1.hole1~ STIFF
CONNECT uc-lpin-2.pin1 -> sw-base-1.hole2~ STIFF
CONNECT uc-lpin-3.pin1 -> sw-base-1.hole4~ STIFF
CONNECT uc-lpin-4.pin1 -> sw-base-1.hole5~ STIFF
WHY Gives the machine a ring that lets the whole upper body swing round on the tracks.

## Step 18 (page 18)
ADD pm-beam15-1 32278 darkgray
ADD pm-beam15-2 32278 darkgray
ADD pm-lpin-1 42924 blue
ADD pm-lpin-2 42924 blue
ADD pm-lpin-3 42924 blue
ADD pm-lpin-4 42924 blue
ADD pm-apin-1 43093 blue
ADD pm-hub-1 44874 black
ADD pm-conn-1 6536 black
ADD pm-hose-1 5102c04 blue
ADD pm-pump-1 26288 blue
CONNECT pm-lpin-1.pin1 -> pm-beam15-1.hole4 STIFF
CONNECT pm-lpin-2.pin1 -> pm-beam15-1.hole6 STIFF
CONNECT pm-lpin-3.pin1 -> pm-beam15-1.hole8 STIFF
CONNECT pm-lpin-4.pin1 -> pm-beam15-1.hole10 STIFF
CONNECT pm-conn-1.hole1 -> pm-beam15-1.hole?
CONNECT pm-hub-1.pin1 -> pm-beam15-1.hole5~ STIFF
CONNECT pm-apin-1.pin1 -> pm-hub-1.hole1~ STIFF
CONNECT pm-lpin-1.pin3 -> pm-beam15-2.hole4 STIFF
CONNECT pm-lpin-2.pin3 -> pm-beam15-2.hole6 STIFF
CONNECT pm-lpin-3.pin3 -> pm-beam15-2.hole8 STIFF
CONNECT pm-lpin-4.pin3 -> pm-beam15-2.hole10 STIFF
CONNECT sw-bpin-1.pin2 -> pm-beam15-1.hole3~ STIFF
CONNECT sw-bpin-2.pin2 -> pm-beam15-2.hole3~ STIFF
CONNECT sw-bpin-3.pin2 -> pm-beam15-1.hole12~ STIFF
CONNECT sw-bpin-4.pin2 -> pm-beam15-2.hole12~ STIFF
WHY Builds the air pump that will later power the arm's air cylinders.

## Step 19 (page 21)
ADD up-frame-1 64179 black
ADD up-lbeam-1 32526 darkgray
ADD up-lpin-1 65304 lightgray
ADD up-lpin-2 65304 lightgray
ADD up-lpin-3 65304 lightgray
ADD up-lpin-4 65304 lightgray
ADD up-lpin-5 65304 lightgray
ADD up-bpin-1 42924 blue
ADD up-bpin-2 42924 blue
CONNECT up-bpin-1.pin1 -> up-lbeam-1.hole1~ STIFF
CONNECT up-bpin-1.pin3 -> up-frame-1.hole?
CONNECT up-bpin-2.pin1 -> up-lbeam-1.hole5~ STIFF
CONNECT up-bpin-2.pin3 -> up-frame-1.hole?
CONNECT up-lpin-1.pin1 -> up-frame-1.hole?
CONNECT up-lpin-2.pin1 -> up-frame-1.hole?
CONNECT up-lpin-3.pin1 -> up-frame-1.hole?
CONNECT up-lpin-4.pin1 -> up-frame-1.hole?
CONNECT up-lpin-5.pin1 -> sw-top-1.hole?
WHY Starts the walls of the upper body around the pump.

## Step 20 (page 22)
ADD up-frame-2 64179 black
ADD up-lbeam-2 32526 darkgray
ADD up-lpin-6 65304 lightgray
ADD up-lpin-7 65304 lightgray
ADD up-lpin-8 65304 lightgray
ADD up-lpin-9 65304 lightgray
ADD up-bpin-3 42924 blue
ADD up-bpin-4 42924 blue
CONNECT up-bpin-3.pin1 -> up-lbeam-2.hole1~ STIFF
CONNECT up-bpin-3.pin3 -> up-frame-2.hole?
CONNECT up-bpin-4.pin1 -> up-lbeam-2.hole5~ STIFF
CONNECT up-bpin-4.pin3 -> up-frame-2.hole?
CONNECT up-lpin-6.pin1 -> up-frame-2.hole?
CONNECT up-lpin-7.pin1 -> up-frame-2.hole?
CONNECT up-lpin-8.pin1 -> up-frame-2.hole?
CONNECT up-lpin-9.pin1 -> up-frame-2.hole?
WHY Gives the upper body a wall on both sides of the pump.

## Step 21 (page 23)
ADD up-beam15-1 32278 black
ADD up-hub-1 44874 lightgray
ADD up-rpin-1 89678 red
CONNECT up-hub-1.pin1 -> up-beam15-1.hole7 STIFF
CONNECT up-hub-1.pin2 -> up-beam15-1.hole9 STIFF
CONNECT up-rpin-1.pin1 -> up-hub-1.hole1~ STIFF
WHY Ties the two upright frames into one rigid structure over the pump.

## Step 22 (page 24)
ADD hy-tee-1 4697b lightgray
ADD hy-valve-1 19474 lightgray
ADD hy-valve-2 19474 lightgray
ADD hy-hose-1 5102c06 blue
ADD hy-hose-2 5102c06 blue
WHY Starts the air plumbing: this line will carry air from the pump to the two air cylinders.

## Step 23 (page 26)
ADD up-pin-1 4274 lightgray
ADD up-pin-2 4274 lightgray
ADD up-pin-3 4274 lightgray
ADD up-pin-4 4274 lightgray
ADD up-pin-5 4274 lightgray
ADD up-pin-6 4274 lightgray
ADD up-beam5-1 32316 black
ADD up-beam5-2 32316 black
ADD up-lbeam-3 32526 darkgray
ADD up-lbeam-4 32526 darkgray
CONNECT up-pin-1.pin1 -> up-lbeam-3.hole1~ TURNS
CONNECT up-pin-2.pin1 -> up-lbeam-3.hole3~ TURNS
CONNECT up-pin-3.pin1 -> up-lbeam-3.hole5~ TURNS
CONNECT up-pin-4.pin1 -> up-lbeam-4.hole1~ TURNS
CONNECT up-pin-5.pin1 -> up-lbeam-4.hole3~ TURNS
CONNECT up-pin-6.pin1 -> up-lbeam-4.hole5~ TURNS
CONNECT up-pin-1.pin2 -> up-beam5-1.hole1~ TURNS
CONNECT up-pin-2.pin2 -> up-beam5-1.hole3~ TURNS
CONNECT up-pin-3.pin2 -> up-beam5-1.hole5~ TURNS
CONNECT up-pin-4.pin2 -> up-beam5-2.hole1~ TURNS
CONNECT up-pin-5.pin2 -> up-beam5-2.hole3~ TURNS
CONNECT up-pin-6.pin2 -> up-beam5-2.hole5~ TURNS
WHY Builds the two tall supports that the air cylinder will hang between.

## Step 24 (page 27)
ADD hy-cyl-1 19478 darkgray
ADD up-beam2-1 43857 darkgray
ADD up-axle5-1 32073 lightgray
ADD hy-pin-1 77765 lightgray
WHY Adds the first air cylinder.

## Step 25 (page 28)
ADD up-conn-1 59443 black
CONNECT up-conn-1.axlehole? -> up-axle5-1.axle5
WHY Stops the cylinder pivot axle from slipping out.

## Step 26 (page 29)
ADD hy-hose-3 5102c20 lightgray
ADD hy-hose-4 5102c29 black
WHY Brings the two long hoses into the model before they are plugged in.

## Step 27 (page 30)
WHY Connects the pump, switches and cylinder into one air circuit.

## Step 28 (page 31)
ADD up-spin-1 65304 black
ADD up-spin-2 65304 black
CONNECT up-spin-1.pin1 -> up-frame-2.hole?
CONNECT up-spin-2.pin1 -> up-frame-2.hole?
WHY Adds the posts for the next cover panel.

## Step 29 (page 32)
ADD up-panel-1 15458 black
ADD up-spin-3 65304 black
ADD up-spin-4 65304 black
ADD up-spin-5 65304 black
ADD up-spin-6 65304 black
ADD up-spin-7 65304 black
ADD up-spin-8 65304 black
CONNECT up-spin-3.pin1 -> up-panel-1.hole?
CONNECT up-spin-4.pin1 -> up-panel-1.hole?
CONNECT up-spin-5.pin1 -> up-panel-1.hole?
CONNECT up-spin-6.pin1 -> up-panel-1.hole?
WHY Closes the top of the rear section and gives a flat base for the cab.

## Step 30 (page 33)
ADD up-beam11-1 32525 black
ADD up-tbeam-1 41677 black
ADD up-tbeam-2 41677 black
ADD up-bpin-5 43093 blue
ADD up-bpin-6 43093 blue
ADD up-bpin-7 43093 blue
ADD up-bpin-8 43093 blue
ADD fr-fair7-1 2387 black
ADD fr-fair8-1 2389 black
CONNECT up-bpin-5.axle1 -> up-tbeam-1.axlehole1~ LOCKED
CONNECT up-bpin-6.axle1 -> up-tbeam-1.axlehole2~ LOCKED
CONNECT up-bpin-7.axle1 -> up-tbeam-2.axlehole1~ LOCKED
CONNECT up-bpin-8.axle1 -> up-tbeam-2.axlehole2~ LOCKED
CONNECT up-bpin-5.pin1 -> up-beam11-1.hole5~ STIFF
CONNECT up-bpin-6.pin1 -> up-beam11-1.hole7~ STIFF
WHY Builds the first side-body piece with its cosmetic fairings.

## Step 31 (page 35)
ADD sd-panel-1 71709 black
ADD sd-gpin-1 4274 lightgray
ADD sd-gpin-2 4274 lightgray
ADD sd-gbeam-1 32523 darkgray
ADD sd-bpin-1 43093 blue
ADD sd-bpin-2 43093 blue
ADD sd-lbeam-1 32526 black
ADD sd-beam15-1 71710 black
CONNECT sd-gpin-1.pin1 -> sd-panel-1.hole1~ TURNS
CONNECT sd-gpin-2.pin1 -> sd-panel-1.hole2~ TURNS
CONNECT sd-bpin-1.pin1 -> sd-panel-1.hole4~ STIFF
CONNECT sd-bpin-2.pin1 -> sd-panel-1.hole5~ STIFF
CONNECT sd-bpin-1.axle1 -> sd-gbeam-1.hole1 TURNS
CONNECT sd-bpin-2.axle1 -> sd-gbeam-1.hole3 TURNS
CONNECT sd-lbeam-1.hole1 -> sd-bpin-1.axle1?
CONNECT sd-beam15-1.hole1? -> sd-panel-1.hole3?
WHY Builds the long side piece that rides along the cab frame.

## Step 32 (page 37)
ADD sd-fpin-1 43093 blue
CONNECT sd-fpin-1.pin1 -> uc-frame-1.hole?
WHY Adds a post for a part that is fitted in step 33.

## Step 33 (page 38)
ADD sd-hub-1 22961 lightgray
ADD sd-rpin-1 89678 red
ADD sd-ybeam-1 41677 yellow
ADD sd-ybeam-2 41677 yellow
ADD sd-conn-1 42003 black
ADD sd-hub2-1 44874 lightgray
ADD sd-lpin-1 65304 black
CONNECT sd-hub-1.axle1 -> sd-ybeam-1.axlehole1~ LOCKED
CONNECT sd-ybeam-2.axlehole1 -> sd-hub-1.axle1~ LOCKED
CONNECT sd-conn-1.hole1? -> sd-ybeam-1.axlehole2?
CONNECT sd-rpin-1.pin1 -> sd-hub2-1.hole1?
CONNECT sd-conn-1.axlehole1 -> sd-fpin-1.axle1?
WHY Builds the pivot for a moving link at the front.

## Step 34 (page 39)
ADD cb-ybeam-1 32140 yellow
ADD cb-pin-1 4274 lightgray
ADD cb-pin-2 4274 lightgray
ADD cb-pin-3 4274 lightgray
CONNECT cb-pin-1.pin1 -> cb-ybeam-1.hole1~ TURNS
CONNECT cb-pin-2.pin1 -> cb-ybeam-1.hole2~ TURNS
CONNECT cb-pin-3.pin1 -> cb-ybeam-1.hole3~ TURNS
CONNECT sd-fpin-1.pin1 -> cb-ybeam-1.hole4?
WHY Makes three posts for the front hinge parts built next.

## Step 35 (page 40)
ADD cb-bush-1 3713 lightgray
ADD cb-conn-1 63869 black
CONNECT cb-bush-1.axlehole1 -> cb-conn-1.axlehole?
WHY Starts the pivot end of the long arm-like beam in the next step.

## Step 36 (page 40)
ADD cb-beam11-1 32525 black
ADD cb-disc-1 98138 clear
CONNECT cb-conn-1.axlehole1 -> cb-beam11-1.hole?
CONNECT cb-disc-1.stud? -> cb-conn-1.hole?
WHY Gives the long beam a rounded end with a pivot.

## Step 37 (page 40)
ADD cb-axle6-1 3706 black
ADD cb-conn2-1 32013 black
CONNECT cb-axle6-1.axle1 -> cb-conn2-1.axlehole1~ LOCKED
CONNECT cb-conn-1.axlehole1 -> cb-axle6-1.axle6?
WHY Adds the shaft that the beam will turn on.

## Step 38 (page 41)
ADD cb-bpin-1 42924 blue
ADD cb-gbeam-1 41677 lightgray
ADD cb-gbeam-2 41677 lightgray
CONNECT cb-bpin-1.pin1 -> cb-beam11-1.hole2~ STIFF
CONNECT cb-gbeam-1.axlehole1 -> cb-axle6-1.axle5~ LOCKED
CONNECT cb-gbeam-2.axlehole1 -> cb-axle6-1.axle4?
WHY Adds a fixing pin and spacers next to the shaft.

## Step 39 (page 41)
ADD cb-axle5-1 32073 lightgray
ADD cb-conn3-1 60483 black
CONNECT cb-axle5-1.axle1 -> cb-conn3-1.axlehole1~ LOCKED
CONNECT cb-conn3-1.hole1 -> cb-beam11-1.hole1?
WHY Adds a second shaft for the next mechanism.

## Step 40 (page 41)
ADD cb-tbeam-1 11478 black
ADD cb-bp1-1 43093 blue
ADD cb-bp2-1 42924 blue
ADD cb-tb2-1 41677 black
ADD cb-gax-1 18651 black
CONNECT cb-gax-1.axle1 -> cb-tbeam-1.axlehole1~ LOCKED
CONNECT cb-bp1-1.axle1 -> cb-tb2-1.axlehole1~ LOCKED
CONNECT cb-bp2-1.pin1 -> cb-tbeam-1.hole2~ STIFF
CONNECT cb-tbeam-1.hole1 -> cb-beam11-1.hole3?
WHY Adds posts on the beam for linking the next parts.

## Step 41 (page 42)
ADD cb-ll-1 32056 darkgray
ADD cb-ll-2 32056 darkgray
ADD cb-ax5-1 32073 lightgray
ADD cb-ax3-1 4519 yellow
ADD cb-gp-1 4274 lightgray
ADD cb-ob-1 43857 darkgray
CONNECT cb-ax5-1.axle2 -> cb-ll-1.axlehole1~ LOCKED
CONNECT cb-ax5-1.axle4 -> cb-ll-2.axlehole1~ LOCKED
CONNECT cb-ax3-1.axle1 -> cb-ll-1.axlehole2~ LOCKED
CONNECT cb-ax3-1.axle3 -> cb-ll-2.axlehole2~ LOCKED
CONNECT cb-gp-1.pin1 -> cb-ll-2.hole1~ TURNS
CONNECT cb-ob-1.hole1 -> cb-ax3-1.axle3?
WHY Builds the tall double post that will carry the boom later.

## Step 42 (page 43)
ADD cb-lb-1 32526 darkgray
ADD cb-lp-1 4274 lightgray
ADD cb-lp-2 4274 lightgray
ADD cb-lp-3 4274 lightgray
CONNECT cb-lp-1.pin1 -> cb-lb-1.hole1~ TURNS
CONNECT cb-lp-2.pin1 -> cb-lb-1.hole2~ TURNS
CONNECT cb-lp-3.pin1 -> cb-lb-1.hole3~ TURNS
CONNECT cb-lb-1.hole5? -> cb-beam11-1.hole?
WHY Adds a tall rigid post on the beam's end.

## Step 43 (page 43)
ADD cb-b11b-1 32525 black
CONNECT cb-lp-1.pin1 -> cb-b11b-1.hole1?
CONNECT cb-lp-2.pin1 -> cb-b11b-1.hole2?
CONNECT cb-lp-3.pin1 -> cb-b11b-1.hole3?
WHY Doubles the beam so the unit is wide and stiff.

## Step 44 (page 43)
ADD cb-pc-1 60483 black
ADD cb-pc-2 60483 black
ADD cb-gp2-1 4274 lightgray
ADD cb-gp2-2 4274 lightgray
CONNECT cb-gp2-1.pin1 -> cb-pc-1.hole1~ TURNS
CONNECT cb-gp2-2.pin1 -> cb-pc-2.hole1~ TURNS
CONNECT cb-pc-1.axlehole1 -> cb-ax5-1.axle5?
CONNECT cb-pc-2.axlehole1 -> cb-ax5-1.axle1?
WHY Makes anchor points on the underside.

## Step 45 (page 44)
ADD cb-t1-1 60483 black
ADD cb-tp-1 32002 tan
CONNECT cb-tp-1.pin1 -> cb-t1-1.hole1~ STIFF
CONNECT cb-t1-1.axlehole1 -> cb-ax5-1.axle3?
WHY Adds a smooth free-turning pin for a link.

## Step 46 (page 44)
ADD cb-bp-1 43093 blue
ADD cb-tb5-1 11478 black
ADD cb-tb3-1 6632 black
CONNECT cb-bp-1.pin1 -> cb-tb5-1.hole1~ STIFF
CONNECT cb-bp-1.axle1 -> cb-tb3-1.axlehole1~ LOCKED
CONNECT cb-tb5-1.axlehole1 -> cb-ax5-1.axle?
WHY Adds a plate that ties the underside together.

## Step 47 (page 45)
CONNECT cb-beam11-1.hole? -> uc-frame-1.hole?
WHY Joins the new front unit to the machine.

## Step 48 (page 46)
ADD cb-b15-1 71710 black
CONNECT cb-b15-1.hole? -> cb-gp-1.pin1?
CONNECT cb-b15-1.hole? -> cb-bp-1.pin1?
WHY Ties the front unit to the frame along the whole side.

## Step 49 (page 47)
ADD fs-pin-1 43093 blue
CONNECT fs-pin-1.pin1 -> cb-b15-1.hole?
WHY Adds a post for the small build placed in step 50.

## Step 50 (page 48)
ADD fs-bp-1 42924 blue
ADD fs-ax3-1 4519 yellow
ADD fs-yb-1 41677 yellow
ADD fs-yb-2 41677 yellow
ADD fs-yb-3 41677 yellow
ADD fs-yb-4 41677 yellow
ADD fs-gp-1 77765 lightgray
ADD fs-ap-1 18651 black
ADD fs-vb-1 32523 black
ADD fs-gb-1 60483 darkgray
CONNECT fs-ap-1.axle1 -> fs-yb-1.axlehole1~ LOCKED
CONNECT fs-ap-1.axle2 -> fs-yb-2.axlehole1~ LOCKED
CONNECT fs-ax3-1.axle1 -> fs-yb-3.axlehole1~ LOCKED
CONNECT fs-ax3-1.axle3 -> fs-yb-4.axlehole1~ LOCKED
CONNECT fs-bp-1.pin1 -> fs-vb-1.hole2~ STIFF
CONNECT fs-gp-1.pin1 -> fs-gb-1.hole1?
CONNECT fs-ap-1.pin1 -> fs-vb-1.hole1~ STIFF
WHY Builds the pivot block that will carry a link or an arm.

## Step 51 (page 50)
ADD fs-yl-1 32140 yellow
ADD fs-yp-1 4274 lightgray
ADD fs-yp-2 4274 lightgray
ADD fs-yp-3 4274 lightgray
CONNECT fs-yp-1.pin1 -> fs-yl-1.hole1~ TURNS
CONNECT fs-yp-2.pin1 -> fs-yl-1.hole2~ TURNS
CONNECT fs-yp-3.pin1 -> fs-yl-1.hole3~ TURNS
CONNECT fs-yl-1.hole4? -> cb-b15-1.hole?
WHY Adds the yellow L bracket that the next links hang on.

## Step 52 (page 51)
ADD fs-bl-1 32526 black
ADD fs-bp3-1 4274 lightgray
ADD fs-bp3-2 4274 lightgray
ADD fs-bp3-3 4274 lightgray
CONNECT fs-bp3-1.pin1 -> fs-bl-1.hole1~ TURNS
CONNECT fs-bp3-2.pin1 -> fs-bl-1.hole2~ TURNS
CONNECT fs-bp3-3.pin1 -> fs-bl-1.hole3~ TURNS
CONNECT fs-bl-1.hole5? -> cb-b15-1.hole?
WHY Adds a black bracket beside the tall upright.

## Step 53 (page 52)
ADD fs-b5-1 32316 black
CONNECT fs-b5-1.hole1 -> fs-bp3-1.pin1?
CONNECT fs-b5-1.hole3 -> fs-bp3-2.pin1?
WHY Closes the bracket and ties it into the frame.

## Step 54 (page 53)
ADD fs-bp4-1 43093 blue
ADD fs-bp4-2 43093 blue
CONNECT fs-bp4-1.pin1 -> fs-b5-1.hole?
CONNECT fs-bp4-2.pin1 -> fs-b5-1.hole?
WHY Adds posts for the beam fitted in step 55.

## Step 55 (page 54)
ADD fs-bh-1 42003 black
ADD fs-gp5-1 4274 lightgray
ADD fs-gp5-2 4274 lightgray
ADD fs-b7-1 32524 black
ADD fs-rax-1 32062 red
CONNECT fs-gp5-1.pin1 -> fs-bh-1.hole1 TURNS
CONNECT fs-gp5-2.pin1 -> fs-bh-1.hole2 TURNS
CONNECT fs-rax-1.axle1 -> fs-bh-1.axlehole1 LOCKED
CONNECT fs-bh-1.hole? -> fs-b7-1.hole?
CONNECT fs-b7-1.hole1~ -> fs-bp4-1.pin1?
CONNECT fs-b7-1.hole3~ -> fs-bp4-2.pin1?
WHY Builds the seat mount: the red axle will carry the seat.

## Step 56 (page 55)
ADD fs-seat-1 24116 darkgray
CONNECT fs-seat-1.hole1 -> fs-rax-1.axle2?
WHY Adds the operator's seat of the excavator.

## Step 57 (page 56)
ADD fs-sb-1 43857 darkgray
CONNECT fs-sb-1.hole1 -> fs-seat-1.hole?
WHY Holds the seat's foot so it doesn't pop off.

## Step 58 (page 57)
ADD fs-sx-1 3706 black
CONNECT fs-sx-1.axle1 -> fs-sb-1.hole?
WHY Adds the shaft the seat turns or tilts on.

## Step 59 (page 58)
ADD fs-clip-1 3484 black
ADD fs-clip-2 3484 black
CONNECT fs-clip-1.bar? -> fs-sx-1.axle?
CONNECT fs-clip-2.bar? -> fs-sx-1.axle?
WHY Clips will later hold hoses or lines.

## Step 60 (page 59)
ADD hs-hose-1 32580 black
ADD hs-rax-1 32062 red
ADD hs-rax-2 32062 red
ADD hs-conn-1 99021 darkgray
ADD hs-conn-2 99021 darkgray
ADD hs-bp-1 43093 blue
ADD hs-tile-1 3069b black
ADD hs-plate-1 18677 black
CONNECT hs-rax-1.axle1 -> hs-hose-1.axlehole?
CONNECT hs-rax-2.axle1 -> hs-hose-1.axlehole?
CONNECT hs-conn-1.axle? -> hs-rax-1.axle2?
CONNECT hs-bp-1.pin1 -> hs-conn-1.hole?
CONNECT hs-conn-2.hole? -> hs-hose-1.axlehole?
CONNECT hs-tile-1.stud? -> hs-plate-1.stud?
WHY Builds a stiff rod link with end fittings (a Volvo-style label tile).

## Step 61 (page 62)
ADD bm-gp-1 4274 lightgray
ADD bm-lb-1 32140 black
ADD bm-bp-1 43093 blue
CONNECT bm-gp-1.pin1 -> bm-lb-1.hole1~ TURNS
CONNECT bm-bp-1.pin1 -> bm-lb-1.hole2~ STIFF
WHY Starts the arm from its root: an L-beam gives the corner for the first section.

## Step 62 (page 62)
ADD bm-b11-1 32525 black
CONNECT bm-bp-1.pin1 -> bm-b11-1.hole1?
CONNECT bm-lb-1.hole3 -> bm-b11-1.hole2?
WHY Builds the first long section of the arm.

## Step 63 (page 62)
ADD bm-ax5-1 15462 brown
CONNECT bm-ax5-1.axle? -> bm-b11-1.hole?
WHY Adds a shaft for the next link to turn on.

## Step 64 (page 63)
ADD bm-l2-1 32526 black
ADD bm-bp2-1 43093 blue
CONNECT bm-bp2-1.pin1 -> bm-l2-1.hole?
CONNECT bm-l2-1.hole? -> bm-ax5-1.axle?
WHY Doubles the beam at the arm's root so the joint is wide and strong.

## Step 65 (page 63)
ADD bm-ax5b-1 15462 brown
ADD bm-cn-1 6536 lightgray
CONNECT bm-ax5b-1.axle? -> bm-b11-1.hole?
CONNECT bm-cn-1.axlehole1 -> bm-ax5b-1.axle?
WHY Adds the second pivot shaft of the root.

## Step 66 (page 63)
ADD bm-yax-1 4519 yellow
ADD bm-bp3-1 43093 blue
ADD bm-tb-1 41677 black
ADD bm-tb-2 41677 black
CONNECT bm-bp3-1.axle1 -> bm-tb-1.axlehole1~ LOCKED
CONNECT bm-yax-1.axle1 -> bm-tb-2.axlehole1~ LOCKED
CONNECT bm-tb-1.axlehole2 -> bm-yax-1.axle3?
WHY Builds the plate that will carry the cylinder joint.

## Step 67 (page 64)
ADD bm-cn2-1 6536 lightgray
CONNECT bm-cn2-1.axlehole1 -> bm-yax-1.axle?
WHY Adds an attachment point for a later link.

## Step 68 (page 64)
ADD bm-bp4-1 43093 blue
ADD bm-bp4-2 43093 blue
CONNECT bm-bp4-1.pin1 -> bm-b11-1.hole?
CONNECT bm-bp4-2.pin1 -> bm-b11-1.hole?
WHY Adds the posts for the next beam.

## Step 69 (page 64)
ADD bm-b5-1 32316 black
CONNECT bm-bp4-1.pin1 -> bm-b5-1.hole1?
CONNECT bm-bp4-2.pin1 -> bm-b5-1.hole2?
WHY Extends the arm's length.

## Step 70 (page 65)
ADD bm-b11b-1 32525 black
ADD bm-gp2-1 4274 lightgray
CONNECT bm-gp2-1.pin1 -> bm-b11b-1.hole?
CONNECT bm-b11b-1.hole? -> bm-b11-1.hole?
WHY Builds the arm's double beam.

## Step 71 (page 65)
ADD bm-l3-1 32140 black
CONNECT bm-l3-1.hole? -> bm-gp2-1.pin1?
WHY Closes the corner of the root.

## Step 72 (page 65)
ADD bm-l4-1 32526 black
ADD bm-bp5-1 43093 blue
ADD bm-bp5-2 43093 blue
ADD bm-bp5-3 43093 blue
CONNECT bm-bp5-1.pin1 -> bm-l4-1.hole1~ STIFF
CONNECT bm-bp5-2.pin1 -> bm-l4-1.hole2~ STIFF
CONNECT bm-bp5-3.pin1 -> bm-l4-1.hole3~ STIFF
CONNECT bm-l4-1.hole? -> bm-b5-1.hole?
WHY Makes the far end ready for the next piece.

## Step 73 (page 66)
ADD bm-cap-1 98138 clear
ADD bm-gp3-1 4274 lightgray
ADD bm-ac-1 32013 black
CONNECT bm-gp3-1.pin1 -> bm-ac-1.hole1~ TURNS
CONNECT bm-cap-1.stud? -> bm-gp3-1.barhole1?
CONNECT bm-ac-1.axlehole1 -> bm-bp5-1.axle?
WHY Adds a smooth post for a link.

## Step 74 (page 66)
ADD bm-b15-1 32278 black
CONNECT bm-b15-1.hole? -> bm-bp5-1.pin1?
CONNECT bm-b15-1.hole? -> bm-ac-1.hole?
WHY Makes the arm long enough to reach.

## Step 75 (page 67)
ADD bm-gb7-1 32524 darkgray
ADD bm-bp6-1 43093 blue
CONNECT bm-bp6-1.pin1 -> bm-gb7-1.hole1~ STIFF
CONNECT bm-gb7-1.hole? -> bm-b15-1.hole?
WHY Adds the diagonal brace for the middle joint.

## Step 76 (page 67)
ADD bm-l5-1 32526 black
CONNECT bm-l5-1.hole? -> bm-b11-1.hole?
WHY Gives the arm a bracket underneath.

## Step 77 (page 68)
ADD bm-cap2-1 98138 clear
ADD bm-gp4-1 4274 lightgray
ADD bm-ac2-1 32013 black
CONNECT bm-gp4-1.pin1 -> bm-ac2-1.hole1~ TURNS
CONNECT bm-cap2-1.stud? -> bm-gp4-1.barhole1?
CONNECT bm-ac2-1.axlehole1 -> bm-l5-1.hole?
WHY Adds a smooth post below.

## Step 78 (page 68)
ADD bm-bp7-1 42924 blue
ADD bm-ap2-1 18651 black
ADD bm-bc-1 42003 black
CONNECT bm-ap2-1.axle1 -> bm-bc-1.axlehole1~ LOCKED
CONNECT bm-bp7-1.pin1 -> bm-gb7-1.hole?
CONNECT bm-bc-1.hole? -> bm-b11-1.hole?
WHY Adds a joint for the cylinder that lifts the arm.

## Step 79 (page 69)
ADD bm-b11c-1 32525 black
CONNECT bm-b11c-1.hole1 -> bm-bp7-1.pin?
CONNECT bm-b11c-1.hole2? -> bm-gb7-1.hole?
WHY Makes the lower arm section that will swing.

## Step 80 (page 70)
ADD bm-b15b-1 32278 black
CONNECT bm-b15b-1.hole? -> bm-bp5-1.pin?
WHY Adds the upper arm's second layer.

## Step 81 (page 71)
ADD bm-b15c-1 71710 black
ADD bm-bp8-1 43093 blue
ADD bm-bp8-2 43093 blue
ADD bm-bp8-3 43093 blue
ADD bm-bush-1 3713 lightgray
CONNECT bm-bp8-1.pin1 -> bm-b15c-1.hole2~ STIFF
CONNECT bm-bp8-2.pin1 -> bm-b15c-1.hole7~ STIFF
CONNECT bm-bp8-3.pin1 -> bm-b15c-1.hole1~ STIFF
CONNECT bm-bush-1.axlehole1 -> bm-bp8-3.axle1?
WHY Builds the lower arm's second long beam.

## Step 82 (page 72)
ADD bm-b15d-1 71710 black
CONNECT bm-bp8-1.pin1 -> bm-b15d-1.hole?
CONNECT bm-bp8-2.pin1 -> bm-b15d-1.hole?
WHY Closes the lower arm sandwich.

## Step 83 (page 73)
ADD bm-fr21-1 11946 black
ADD bm-fr22-1 11947 black
ADD bm-fp-1 4274 lightgray
ADD bm-fp-2 4274 lightgray
ADD bm-fa-1 32062 red
ADD bm-fa-2 32062 red
ADD bm-ft-1 41677 black
ADD bm-ft-2 41677 black
CONNECT bm-fa-1.axle1 -> bm-ft-1.axlehole1~ LOCKED
CONNECT bm-fa-2.axle1 -> bm-ft-1.axlehole2~ LOCKED
CONNECT bm-fp-1.pin1 -> bm-fr21-1.hole?
CONNECT bm-fp-2.pin1 -> bm-fr22-1.hole?
CONNECT bm-fr21-1.hole? -> bm-fa-1.axle2?
WHY Builds the side cover with the brand print.

## Step 84 (page 74)
ADD bm-l6-1 32526 black
ADD bm-bp9-1 43093 blue
ADD bm-bp9-2 43093 blue
CONNECT bm-bp9-1.pin1 -> bm-l6-1.hole1~ STIFF
CONNECT bm-bp9-2.pin1 -> bm-l6-1.hole2~ STIFF
CONNECT bm-l6-1.hole? -> bm-b15d-1.hole?
WHY Adds the elbow bracket.

## Step 85 (page 75)
ADD bm-b11d-1 32525 black
ADD bm-b5b-1 32316 black
ADD bm-gp5-1 4274 lightgray
ADD bm-bp10-1 43093 blue
ADD bm-bp10-2 43093 blue
ADD bm-bp10-3 43093 blue
ADD bm-bp10-4 43093 blue
ADD bm-tp-1 32002 tan
CONNECT bm-gp5-1.pin1 -> bm-b11d-1.hole1~ TURNS
CONNECT bm-bp10-1.pin1 -> bm-b11d-1.hole3~ STIFF
CONNECT bm-bp10-2.pin1 -> bm-b11d-1.hole8~ STIFF
CONNECT bm-bp10-3.pin1 -> bm-b11d-1.hole11~ STIFF
CONNECT bm-bp10-4.pin1 -> bm-b5b-1.hole2~ STIFF
CONNECT bm-tp-1.pin1 -> bm-b5b-1.hole1~ STIFF
WHY Builds the elbow beam that the upper arm hangs on.

## Step 86 (page 77)
ADD bm-ax5c-1 32073 lightgray
ADD bm-tbk-1 41677 black
CONNECT bm-ax5c-1.axle3 -> bm-tbk-1.axlehole1~ LOCKED
CONNECT bm-ax5c-1.axle1 -> bm-tp-1.pin2?
WHY Adds the elbow shaft.

## Step 87 (page 78)
ADD bm-b13-1 41239 darkgray
CONNECT bm-b13-1.hole1 -> bm-ax5c-1.axle?
WHY Adds the upper arm beam.

## Step 88 (page 79)
ADD bm-b15e-1 32278 black
CONNECT bm-bp10-1.pin1 -> bm-b15e-1.hole?
CONNECT bm-bp10-2.pin1 -> bm-b15e-1.hole?
WHY Adds the second upper beam.

## Step 89 (page 80)
ADD bm-b3-1 32523 black
ADD bm-bp11-1 43093 blue
ADD bm-bp11-2 43093 blue
ADD bm-bp11-3 43093 blue
CONNECT bm-bp11-1.pin1 -> bm-b3-1.hole1~ STIFF
CONNECT bm-bp11-2.pin1 -> bm-b3-1.hole3~ STIFF
CONNECT bm-bp11-3.pin1 -> bm-b15e-1.hole?
CONNECT bm-b3-1.hole2 -> bm-tp-1.pin2?
WHY Adds posts for the cylinder mounts.

## Step 90 (page 81)
ADD bm-cyl-1 19478 darkgray
ADD bm-tpin-1 39888 tan
ADD bm-tpin-2 39888 tan
CONNECT bm-tpin-1.pin1 -> bm-cyl-1.hole?
CONNECT bm-tpin-2.pin1 -> bm-cyl-1.hole?
CONNECT bm-tpin-1.pin2 -> bm-b15e-1.hole?
CONNECT bm-tpin-2.pin2 -> bm-b3-1.hole?
WHY Adds the cylinder that bends the arm at the elbow.

## Step 91 (page 82)
ADD bm-b11e-1 32525 black
ADD bm-gp6-1 4274 lightgray
ADD bm-l7-1 32526 black
CONNECT bm-gp6-1.pin1 -> bm-b11e-1.hole11~ TURNS
CONNECT bm-b11e-1.hole? -> bm-bp10-1.pin1?
CONNECT bm-l7-1.hole? -> bm-b11-1.hole?
WHY Holds the cylinder's pin in place from above.

## Step 92 (page 83)
ADD bm-tb2-1 41677 black
CONNECT bm-tb2-1.axlehole1 -> bm-gp6-1.pin?
WHY Locks the grey pin so it stays.

## Step 93 (page 84)
ADD bm-tbk2-1 11478 black
ADD bm-tbk2-2 11478 black
ADD bm-bp12-1 43093 blue
ADD bm-b5c-1 32316 black
ADD bm-ap3-1 18651 black
CONNECT bm-ap3-1.axle1 -> bm-tbk2-1.axlehole1~ LOCKED
CONNECT bm-ap3-1.axle2 -> bm-tbk2-2.axlehole1~ LOCKED
CONNECT bm-bp12-1.pin1 -> bm-b5c-1.hole1~ STIFF
CONNECT bm-tbk2-1.hole1 -> bm-b5c-1.hole?
WHY Builds the link at the elbow.

## Step 94 (page 85)
ADD bm-b15f-1 32278 black
CONNECT bm-b15f-1.hole? -> bm-bp12-1.pin?
WHY Lengthens the arm's lower section.

## Step 95 (page 86)
ADD bm-b11f-1 32525 black
ADD bm-b11f-2 32525 black
ADD bm-gp7-1 4274 lightgray
ADD bm-gp7-2 4274 lightgray
ADD bm-rp-1 89678 red
ADD bm-rp-2 89678 red
ADD bm-rp-3 89678 red
ADD bm-rp-4 89678 red
CONNECT bm-gp7-1.pin1 -> bm-b11f-1.hole11~ TURNS
CONNECT bm-gp7-2.pin1 -> bm-b11f-2.hole11~ TURNS
CONNECT bm-rp-1.pin1 -> bm-b11f-1.hole3~ STIFF
CONNECT bm-rp-2.pin1 -> bm-b11f-1.hole7~ STIFF
CONNECT bm-rp-3.pin1 -> bm-b11f-2.hole3~ STIFF
CONNECT bm-rp-4.pin1 -> bm-b11f-2.hole7~ STIFF
WHY Builds the side plates for the next hinge.

## Step 96 (page 87)
ADD bm-ax5d-1 32073 lightgray
ADD bm-tb3-1 41677 black
CONNECT bm-ax5d-1.axle1 -> bm-tb3-1.axlehole1~ LOCKED
CONNECT bm-ax5d-1.axle5 -> bm-b11f-1.hole?
WHY Adds a cross shaft that ties the two side beams.

## Step 97 (page 88)
ADD bm-tb4-1 41677 black
CONNECT bm-tb4-1.axlehole1 -> bm-ax5d-1.axle1?
WHY Locks the cross shaft from the other side.

## Step 98 (page 89)
ADD bm-tile-1 6636 black
ADD bm-tile-2 6636 black
CONNECT bm-tile-1.stud? -> bm-b11f-1.hole?
CONNECT bm-tile-2.stud? -> bm-b11f-2.hole?
WHY Adds the warning stripe that real excavator arms show.

## Step 99 (page 90)
ADD bm-ax6-1 3706 black
ADD bm-tb5-1 41677 black
ADD bm-tb5-2 41677 black
CONNECT bm-ax6-1.axle1 -> bm-tb5-1.axlehole1~ LOCKED
CONNECT bm-ax6-1.axle6 -> bm-tb5-2.axlehole1~ LOCKED
WHY Adds the second cross shaft at the bottom.

## Step 100 (page 91)
ADD bm-b5d-1 32316 black
CONNECT bm-b5d-1.hole? -> bm-ax6-1.axle?
WHY Strengthens the lower end.

## Step 101 (page 92)
ADD bm-rax-1 3705 red
ADD bm-b5e-1 32316 black
ADD bm-ax6b-1 3706 black
ADD bm-gb4-1 32449 darkgray
ADD bm-go-1 41677 darkgray
ADD bm-bu-1 3713 lightgray
CONNECT bm-ax6b-1.axle1 -> bm-gb4-1.axlehole?
CONNECT bm-bu-1.axlehole1 -> bm-ax6b-1.axle6 LOCKED
CONNECT bm-go-1.axlehole1 -> bm-ax6b-1.axle?
CONNECT bm-rax-1.axle1 -> bm-gb4-1.axlehole?
CONNECT bm-b5e-1.hole? -> bm-rax-1.axle?
WHY Builds the bucket link bracket.

## Step 102 (page 94)
ADD bm-b5f-1 32316 black
ADD bm-go2-1 41677 darkgray
CONNECT bm-go2-1.axlehole1 -> bm-ax6-1.axle6?
CONNECT bm-b5f-1.hole? -> bm-rax-1.axle?
WHY Locks the shaft end.

## Step 103 (page 95)
ADD bm-bu2-1 3713 lightgray
ADD bm-go3-1 41677 darkgray
CONNECT bm-bu2-1.axlehole1 -> bm-rax-1.axle4?
CONNECT bm-go3-1.axlehole1 -> bm-ax6b-1.axle?
WHY Locks the bucket hinge shafts.

## Step 104 (page 96)
ADD bm-ax6c-1 3706 black
CONNECT bm-ax6c-1.axle? -> bm-go3-1.axlehole?
WHY Adds the shaft the bucket will hang on.

## Step 105 (page 97)
ADD bk-bucket-1 24120 darkgray
ADD bk-bucket-2 24120 darkgray
ADD bk-tpin-1 32002 tan
ADD bk-tpin-2 32002 tan
ADD bk-tb-1 41677 black
ADD bk-tb-2 41677 black
CONNECT bk-tpin-1.pin1 -> bk-tb-1.axlehole?
CONNECT bk-tpin-2.pin1 -> bk-tb-2.axlehole?
CONNECT bk-tpin-1.pin2 -> bk-bucket-1.hole?
CONNECT bk-tpin-2.pin2 -> bk-bucket-2.hole?
WHY Adds the digging bucket(s).

## Step 106 (page 98)
ADD hy-hose-5 5102c32 black
WHY Brings the arm cylinder's long hose in.

## Step 107 (page 99)
ADD hy-hose-6 5102c25 lightgray
WHY Brings the second arm hose in.

## Step 108 (page 100)
ADD cb-rax10-1 3737 red
ADD cb-rbush-1 3713 red
CONNECT cb-rax10-1.axle1 -> cb-lb-1.axlehole?
CONNECT cb-rbush-1.axlehole1 -> cb-rax10-1.axle10?
WHY Adds the axle that the arm's root hinge sits on.

## Step 109 (page 101)
ADD cb-gpin-1 77765 lightgray
CONNECT cb-gpin-1.pin? -> bm-lb-1.hole?
WHY Locks the arm to the machine.

## Step 110 (page 102)
ADD hy-hose-7 5102c13 lightgray
ADD hy-hose-8 5102c18 black
WHY Brings the hoses that run from the switches to the arm in.

## Step 111 (page 103)
CONNECT hy-hose-7.end? -> hy-tee-1.nozzle?
CONNECT hy-hose-8.end? -> hy-valve-2.nozzle?
WHY Connects the cab-side hoses to the switches.

## Step 112 (page 105)
ADD up-gb13-1 41239 darkgray
CONNECT up-gb13-1.hole? -> up-lbeam-1.hole?
CONNECT up-gb13-1.hole? -> up-lbeam-2.hole?
WHY Adds a rear cross beam on which the counterweight will sit.

## Step 113 (page 106)
ADD cw-panel-1 15458 black
ADD cw-gp-1 61332 black
ADD cw-gp-2 61332 black
ADD cw-gp-3 61332 black
ADD cw-gp-4 61332 black
CONNECT cw-gp-1.pin1 -> cw-panel-1.hole?
CONNECT cw-gp-2.pin1 -> cw-panel-1.hole?
CONNECT cw-gp-3.pin1 -> cw-panel-1.hole?
CONNECT cw-gp-4.pin1 -> cw-panel-1.hole?
WHY Starts the rear counterweight: a stack of panels and beams.

## Step 114 (page 106)
ADD cw-b7-1 32524 black
CONNECT cw-gp-1.pin1 -> cw-b7-1.hole2~ STIFF
CONNECT cw-gp-2.pin1 -> cw-b7-1.hole6~ STIFF
WHY Adds a layer to the stack.

## Step 115 (page 106)
ADD cw-bp-1 43093 blue
ADD cw-bp-2 43093 blue
CONNECT cw-bp-1.pin1 -> cw-b7-1.hole1 STIFF
CONNECT cw-bp-2.pin1 -> cw-b7-1.hole7 STIFF
WHY Adds posts for the next beam.

## Step 116 (page 106)
ADD cw-b7b-1 32524 black
ADD cw-b7b-2 32524 black
CONNECT cw-bp-1.pin1 -> cw-b7b-1.hole1~ STIFF
CONNECT cw-bp-2.pin1 -> cw-b7b-1.hole7~ STIFF
WHY Builds up the counterweight's height.

## Step 117 (page 107)
ADD cw-gp2-1 61332 black
ADD cw-gp2-2 61332 black
CONNECT cw-gp2-1.pin1 -> cw-b7b-1.hole2~ STIFF
CONNECT cw-gp2-2.pin1 -> cw-b7b-1.hole6~ STIFF
WHY Posts for the top panel.

## Step 118 (page 107)
ADD cw-panel2-1 15458 black
CONNECT cw-gp2-1.pin1 -> cw-panel2-1.hole?
CONNECT cw-gp2-2.pin1 -> cw-panel2-1.hole?
WHY Closes the sandwich.

## Step 119 (page 107)
ADD cw-gp3-1 61332 black
ADD cw-gp3-2 61332 black
ADD cw-bp2-1 43093 blue
ADD cw-bp2-2 43093 blue
CONNECT cw-gp3-1.pin1 -> cw-panel-1.hole?
CONNECT cw-gp3-2.pin1 -> cw-panel2-1.hole?
CONNECT cw-bp2-1.pin1 -> cw-panel-1.hole?
CONNECT cw-bp2-2.pin1 -> cw-panel2-1.hole?
WHY Adds the mounting points that attach it to the frame.

## Step 120 (page 107)
ADD cw-bp3-1 43093 blue
ADD cw-bp3-2 43093 blue
ADD cw-conn-1 42003 black
ADD cw-conn-2 42003 black
CONNECT cw-bp3-1.pin1 -> cw-conn-1.hole1~ STIFF
CONNECT cw-bp3-2.pin1 -> cw-conn-2.hole1~ STIFF
CONNECT cw-conn-1.hole2 -> cw-panel-1.hole?
CONNECT cw-conn-2.hole2 -> cw-panel-1.hole?
WHY Adds the corner locks.

## Step 121 (page 108)
CONNECT cw-panel-1.hole? -> up-gb13-1.hole?
WHY Balances the arm.

## Step 122 (page 109)
ADD cw-b7c-1 32524 black
ADD cw-bp4-1 43093 blue
ADD cw-bp4-2 43093 blue
CONNECT cw-bp4-1.pin1 -> cw-b7c-1.hole1~ STIFF
CONNECT cw-bp4-2.pin1 -> cw-b7c-1.hole5~ STIFF
CONNECT cw-b7c-1.hole? -> up-gb13-1.hole?
WHY Adds a side beam beside the cab.

## Step 123 (page 110)
ADD cw-b7d-1 32524 black
ADD cw-bp5-1 43093 blue
CONNECT cw-bp5-1.pin1 -> cw-b7d-1.hole1~ STIFF
CONNECT cw-b7d-1.hole? -> up-gb13-1.hole?
WHY Adds a second side post beside the cab.

## Step 124 (page 111)
ADD cw-bp6-1 43093 blue
ADD cw-bp6-2 43093 blue
ADD cw-bp6-3 43093 blue
ADD cw-bp6-4 43093 blue
CONNECT cw-bp6-1.pin1 -> cw-panel-1.hole?
CONNECT cw-bp6-2.pin1 -> cw-panel-1.hole?
CONNECT cw-bp6-3.pin1 -> cw-panel2-1.hole?
CONNECT cw-bp6-4.pin1 -> cw-panel2-1.hole?
WHY Adds the posts for the top cover.

## Step 125 (page 112)
WHY Tells the builder to put the four stickers on the counterweight top.

## Step 126 (page 113)
ADD hd-fair-1 71682 black
ADD hd-rpin-1 11214 red
ADD hd-rpin-2 11214 red
CONNECT hd-rpin-1.axle1 -> hd-fair-1.axlehole1~ LOCKED
CONNECT hd-rpin-2.axle1 -> hd-fair-1.axlehole3~ LOCKED
WHY Starts the hood piece.

## Step 127 (page 113)
ADD hd-f8-1 2389 black
ADD hd-f7-1 2387 black
WHY Gives the hood its long curved shape.

## Step 128 (page 113)
ADD hd-rpin2-1 11214 red
ADD hd-rpin2-2 11214 red
CONNECT hd-rpin2-1.axle1 -> hd-f7-1.axlehole?
CONNECT hd-rpin2-2.axle1 -> hd-f8-1.axlehole?
WHY Adds the pins that the beam in step 129 sits on.

## Step 129 (page 113)
ADD hd-b9-1 40490 black
CONNECT hd-rpin2-1.pin1 -> hd-b9-1.hole1~ STIFF
CONNECT hd-rpin2-2.pin1 -> hd-b9-1.hole9~ STIFF
WHY Adds the brand beam on the front of the hood.

## Step 130 (page 114)
ADD hd-gp-1 61332 black
ADD hd-gp-2 61332 black
ADD hd-gp-3 61332 black
ADD hd-gp-4 61332 black
CONNECT hd-gp-1.pin1 -> hd-b9-1.hole3~ STIFF
CONNECT hd-gp-2.pin1 -> hd-b9-1.hole4~ STIFF
CONNECT hd-gp-3.pin1 -> hd-b9-1.hole5~ STIFF
CONNECT hd-gp-4.pin1 -> hd-b9-1.hole7~ STIFF
WHY Adds posts for the next beam.

## Step 131 (page 114)
ADD hd-b3-1 32523 black
CONNECT hd-b3-1.hole1 -> hd-gp-1.pin2~ STIFF
CONNECT hd-b3-1.hole3 -> hd-gp-3.pin2~ STIFF
WHY Adds the middle spacer.

## Step 132 (page 114)
ADD hd-rp-1 11214 red
ADD hd-rp-2 11214 red
ADD hd-cb-1 60483 black
ADD hd-cb-2 60483 black
CONNECT hd-rp-1.axle1 -> hd-cb-1.axlehole1 LOCKED
CONNECT hd-rp-2.axle1 -> hd-cb-2.axlehole1 LOCKED
CONNECT hd-cb-1.hole1 -> hd-b9-1.pin?
CONNECT hd-cb-2.hole1 -> hd-b9-1.pin?
WHY Makes the hood's mounting pins.

## Step 133 (page 114)
ADD hd-b7-1 32524 black
CONNECT hd-rp-1.pin1 -> hd-b7-1.hole2~ STIFF
CONNECT hd-rp-2.pin1 -> hd-b7-1.hole6~ STIFF
WHY Ties the hood together underneath.

## Step 134 (page 115)
CONNECT hd-rp-1.pin2 -> cw-panel-1.hole?
CONNECT hd-rp-2.pin2 -> cw-panel-1.hole?
WHY Gives the machine its rear cover.

## Step 135 (page 116)
ADD rf-b11-1 73507 black
ADD rf-b7-1 32524 black
ADD rf-bp-1 43093 blue
ADD rf-bp-2 43093 blue
ADD rf-bp-3 43093 blue
ADD rf-b5-1 32316 black
ADD rf-b5-2 32316 black
ADD rf-b4-1 32449 black
ADD rf-gp-1 61332 black
ADD rf-gp-2 61332 black
ADD rf-gp-3 61332 black
CONNECT rf-bp-1.pin1 -> rf-b11-1.hole2~ STIFF
CONNECT rf-bp-2.pin1 -> rf-b11-1.hole5~ STIFF
CONNECT rf-bp-3.pin1 -> rf-b11-1.hole8~ STIFF
CONNECT rf-gp-1.pin1 -> rf-b11-1.hole10~ STIFF
CONNECT rf-gp-2.pin1 -> rf-b11-1.hole11~ STIFF
CONNECT rf-bp-1.axle1 -> rf-b7-1.hole?
WHY Builds the roof support: layered beams make a stiff bar.

## Step 136 (page 119)
ADD rf-b5b-1 32316 black
CONNECT rf-b5b-1.hole? -> rf-bp-1.pin?
WHY Fixes the roof stack to the frame.

## Step 137 (page 120)
ADD cb-yb3-1 32523 yellow
ADD cb-bp7-1 43093 blue
ADD cb-dp-1 61332 black
CONNECT cb-bp7-1.pin1 -> cb-yb3-1.hole1~ STIFF
CONNECT cb-dp-1.pin1 -> cb-yb3-1.hole3~ STIFF
CONNECT cb-yb3-1.hole2 -> cb-bp-1.pin?
WHY Adds the yellow trim beam that matches the yellow beam already there.

## Step 138 (page 121)
ADD cr-tb-1 41677 black
ADD cr-tb-2 41677 black
ADD cr-tb-3 41677 black
ADD cr-tb-4 41677 black
ADD cr-conn-1 42003 black
ADD cr-rax-1 32062 red
ADD cr-hub-1 44874 black
ADD cr-fair-1 2395 black
ADD cr-yax-1 4519 yellow
ADD cr-yax-2 4519 yellow
CONNECT cr-yax-1.axle1 -> cr-tb-1.axlehole1~ LOCKED
CONNECT cr-yax-1.axle3 -> cr-tb-2.axlehole1~ LOCKED
CONNECT cr-yax-2.axle1 -> cr-tb-3.axlehole1~ LOCKED
CONNECT cr-yax-2.axle3 -> cr-tb-4.axlehole1~ LOCKED
CONNECT cr-rax-1.axle1 -> cr-fair-1.axlehole?
CONNECT cr-hub-1.hole? -> cr-yax-1.axle2?
WHY Builds the front-left corner cover/hinge.

## Step 139 (page 123)
ADD cb-yb5-1 32316 yellow
ADD cb-bp8-1 43093 blue
ADD cb-dp2-1 61332 black
CONNECT cb-bp8-1.pin1 -> cb-yb5-1.hole1~ STIFF
CONNECT cb-dp2-1.pin1 -> cb-yb5-1.hole3~ STIFF
CONNECT cb-yb5-1.hole? -> cb-yb3-1.hole?
WHY Extends the yellow trim along the frame side.

## Step 140 (page 124)
ADD cb-dp3-1 61332 black
ADD cb-dp3-2 61332 black
CONNECT cb-dp3-1.pin1 -> hd-b7-1.hole?
CONNECT cb-dp3-2.pin1 -> hd-b7-1.hole?
WHY Adds posts for the next yellow beam.

## Step 141 (page 125)
ADD cb-yb5b-1 32316 yellow
CONNECT cb-dp3-1.pin2 -> cb-yb5b-1.hole2~ STIFF
CONNECT cb-dp3-2.pin2 -> cb-yb5b-1.hole4~ STIFF
WHY Finishes the yellow trim line.

## Step 142 (page 126)
ADD sc-bp-1 43093 blue
ADD sc-bp-2 43093 blue
ADD sc-yax-1 4519 yellow
ADD sc-lb-1 32140 black
ADD sc-lb-2 32140 black
ADD sc-lb-3 32140 black
ADD sc-dp-1 61332 black
CONNECT sc-yax-1.axle1 -> sc-lb-1.axlehole1~ LOCKED
CONNECT sc-dp-1.pin1 -> sc-lb-2.hole1~ STIFF
CONNECT sc-bp-1.pin1 -> sc-lb-3.hole2~ STIFF
CONNECT sc-bp-2.pin1 -> sc-lb-3.hole3~ STIFF
WHY Builds the left side cover with the machine's ELECTRIC label.

## Step 143 (page 128)
ADD hd2-bp-1 43093 blue
ADD hd2-rp-1 32062 red
ADD hd2-f8-1 2389 yellow
ADD hd2-panel-1 71709 yellow
CONNECT hd2-rp-1.axle1 -> hd2-f8-1.axlehole?
CONNECT hd2-bp-1.pin1 -> hd2-f8-1.hole?
CONNECT hd2-f8-1.hole? -> hd2-panel-1.hole?
WHY Adds the yellow cover with the model name.

## Step 144 (page 129)
ADD rs-b11-1 73507 black
ADD rs-bp-1 43093 blue
ADD rs-bp-2 43093 blue
ADD rs-bp-3 43093 blue
CONNECT rs-bp-1.pin1 -> rs-b11-1.hole2~ STIFF
CONNECT rs-bp-2.pin1 -> rs-b11-1.hole5~ STIFF
CONNECT rs-bp-3.pin1 -> rs-b11-1.hole8~ STIFF
WHY Starts the right side beam.

## Step 145 (page 129)
ADD rs-lb-1 32526 black
CONNECT rs-lb-1.hole1 -> rs-bp-1.pin1~ STIFF
CONNECT rs-lb-1.hole2 -> rs-bp-2.pin1~ STIFF
WHY Adds the upright end of the side beam.

## Step 146 (page 129)
ADD rs-dp-1 61332 black
ADD rs-dp-2 61332 black
ADD rs-dp-3 61332 black
CONNECT rs-dp-1.pin1 -> rs-b11-1.hole10~ STIFF
CONNECT rs-dp-2.pin1 -> rs-b11-1.hole11~ STIFF
CONNECT rs-dp-3.pin1 -> rs-b11-1.hole9~ STIFF
WHY Adds posts for the next beams.

## Step 147 (page 130)
ADD rs-b3-1 32523 black
ADD rs-b7-1 32524 black
CONNECT rs-b7-1.hole? -> rs-bp-1.pin?
CONNECT rs-b3-1.hole? -> rs-dp-1.pin2?
WHY Thickens the side beam.

## Step 148 (page 130)
ADD rs-b5-1 32316 black
CONNECT rs-dp-2.pin2 -> rs-b5-1.hole?
WHY Closes the right beam's far end.

## Step 149 (page 130)
ADD rs-bp2-1 43093 blue
ADD rs-dp2-1 61332 black
ADD rs-tb-1 11478 black
ADD rs-tb-2 11478 black
CONNECT rs-bp2-1.axle1 -> rs-tb-1.axlehole1~ LOCKED
CONNECT rs-bp2-1.pin1 -> rs-tb-2.hole1~ STIFF
CONNECT rs-dp2-1.pin1 -> rs-tb-1.hole3~ STIFF
WHY Adds the tall end plate.

## Step 150 (page 131)
CONNECT rs-bp-3.pin1 -> up-frame-2.hole?
CONNECT rs-b11-1.hole? -> up-frame-2.hole?
WHY Closes the right side of the cab box.

## Step 151 (page 132)
ADD rs-b5c-1 32316 black
CONNECT rs-b5c-1.hole? -> rs-dp-1.pin?
WHY Finishes the top rail of the right side.

## Step 152 (page 133)
ADD cn-ax6-1 3706 black
ADD cn-conn-1 42003 black
CONNECT cn-ax6-1.axle1 -> cn-conn-1.axlehole1 LOCKED
WHY Starts the corner pivot.

## Step 153 (page 133)
ADD cn-tb-1 41677 black
ADD cn-tb-2 41677 black
CONNECT cn-tb-1.axlehole1 -> cn-ax6-1.axle5~ LOCKED
WHY Adds a spacer beside the connector.

## Step 154 (page 133)
ADD cn-tb2-1 41677 black
ADD cn-tb2-2 41677 black
CONNECT cn-tb2-1.axlehole1 -> cn-ax6-1.axle4~ LOCKED
CONNECT cn-tb2-2.axlehole1 -> cn-ax6-1.axle3~ LOCKED
WHY Adds the second spacer.

## Step 155 (page 133)
ADD cn-yc-1 6536 yellow
CONNECT cn-yc-1.axlehole1 -> cn-ax6-1.axle2~ LOCKED
WHY Adds the yellow end of the cab corner.

## Step 156 (page 134)
ADD cn-tb3-1 41677 black
ADD cn-tb3-2 41677 black
CONNECT cn-tb3-1.axlehole1 -> cn-ax6-1.axle1~ LOCKED
CONNECT cn-tb3-2.axlehole1 -> cn-ax6-1.axle2?
WHY Locks the axle's free end.

## Step 157 (page 134)
ADD cn-yax-1 4519 yellow
CONNECT cn-yax-1.axle1 -> cn-yc-1.axlehole?
WHY Adds the second pivot shaft.

## Step 158 (page 134)
ADD cn-u-1 69819 black
CONNECT cn-u-1.axlehole? -> cn-yax-1.axle2?
WHY Closes the pivot with a U clamp.

## Step 159 (page 134)
ADD cn-rax-1 32062 red
CONNECT cn-rax-1.axle1 -> cn-u-1.axlehole?
WHY Adds a red mount axle.

## Step 160 (page 135)
ADD cn-yc2-1 6536 yellow
ADD cn-yc2-2 6536 yellow
CONNECT cn-yc2-1.axlehole1 -> cn-rax-1.axle2~ LOCKED
CONNECT cn-yc2-2.hole? -> cn-yc2-1.hole?
WHY Gives the corner its yellow end.

## Step 161 (page 135)
ADD cn-dp-1 61332 black
CONNECT cn-dp-1.pin1 -> cn-yc2-1.hole?
WHY Locks the yellow corner.

## Step 162 (page 135)
ADD cn-fair-1 2403 black
ADD cn-rax2-1 32062 red
CONNECT cn-rax2-1.axle1 -> cn-fair-1.axlehole?
CONNECT cn-rax2-1.axle2 -> cn-yc2-2.axlehole?
WHY Adds the rounded corner of the cab.

## Step 163 (page 136)
CONNECT cn-ax6-1.axle6 -> rs-b5c-1.hole?
CONNECT cn-yc-1.hole? -> rs-b5c-1.hole?
WHY Adds the yellow-black corner that closes the cab box.

## Step 164 (page 137)
ADD cn-dp4-1 61332 black
ADD cn-dp4-2 61332 black
ADD cn-dp4-3 61332 black
ADD cn-dp4-4 61332 black
CONNECT cn-dp4-1.pin1 -> cn-fair-1.hole?
CONNECT cn-dp4-2.pin1 -> cn-fair-1.hole?
CONNECT cn-dp4-3.pin1 -> rs-b11-1.hole?
CONNECT cn-dp4-4.pin1 -> rs-b11-1.hole?
WHY Adds the posts for the corner covers.

## Step 165 (page 138)
ADD cv-f1-1 87080 black
ADD cv-f2-1 87086 black
CONNECT cv-f1-1.hole? -> cn-dp4-1.pin2?
CONNECT cv-f2-1.hole? -> cn-dp4-3.pin2?
WHY Gives the corner its finished shape and warning marks.

## Step 166 (page 139)
ADD yb-b9-1 40490 yellow
ADD yb-hub-1 65487 blue
ADD yb-dp-1 61332 black
ADD yb-dp-2 61332 black
ADD yb-gp-1 3673 lightgray
CONNECT yb-dp-1.pin1 -> yb-b9-1.hole2~ STIFF
CONNECT yb-dp-2.pin1 -> yb-b9-1.hole3~ STIFF
CONNECT yb-hub-1.pin1 -> yb-b9-1.hole9~ STIFF
CONNECT yb-gp-1.pin1 -> yb-hub-1.hole1~ TURNS
WHY Adds the long yellow trim on the right side, matching the left.

## Step 167 (page 140)
ADD sc2-bp-1 43093 blue
ADD sc2-bp-2 43093 blue
ADD sc2-yax-1 4519 yellow
ADD sc2-lb-1 32140 black
ADD sc2-lb-2 32140 black
ADD sc2-lb-3 32140 black
ADD sc2-dp-1 61332 black
CONNECT sc2-yax-1.axle1 -> sc2-lb-1.axlehole1~ LOCKED
CONNECT sc2-dp-1.pin1 -> sc2-lb-2.hole1~ STIFF
CONNECT sc2-bp-1.pin1 -> sc2-lb-3.hole2~ STIFF
CONNECT sc2-bp-2.pin1 -> sc2-lb-3.hole3~ STIFF
WHY Builds the right side cover with the machine's ELECTRIC label.

## Step 168 (page 142)
ADD yc-bp-1 43093 blue
ADD yc-bp-2 43093 blue
ADD yc-panel-1 71709 yellow
ADD yc-tb-1 41677 yellow
ADD yc-tb-2 41677 yellow
CONNECT yc-bp-1.axle1 -> yc-tb-1.axlehole1~ LOCKED
CONNECT yc-bp-2.axle1 -> yc-tb-2.axlehole1~ LOCKED
CONNECT yc-bp-1.pin1 -> yc-panel-1.hole?
CONNECT yc-bp-2.pin1 -> yc-panel-1.hole?
WHY Matches the left yellow cover with the model name.

## Step 169 (page 144)
ADD ca-yl-1 32526 yellow
ADD ca-bp-1 43093 blue
ADD ca-bp-2 43093 blue
ADD ca-bp-3 43093 blue
ADD ca-dp-1 61332 black
CONNECT ca-bp-1.pin1 -> ca-yl-1.hole1~ STIFF
CONNECT ca-bp-2.pin1 -> ca-yl-1.hole2~ STIFF
CONNECT ca-bp-3.pin1 -> ca-yl-1.hole5~ STIFF
CONNECT ca-dp-1.pin1 -> ca-yl-1.hole4~ STIFF
WHY Builds the yellow upright (roof pillar) for the cab.

## Step 170 (page 145)
ADD ca-yb9-1 40490 yellow
ADD ca-ytb-1 32017 yellow
ADD ca-ytb-2 32017 yellow
ADD ca-dp2-1 61332 black
ADD ca-dp2-2 61332 black
ADD ca-dp2-3 61332 black
CONNECT ca-dp2-1.pin1 -> ca-yb9-1.hole2~ STIFF
CONNECT ca-dp2-2.pin1 -> ca-yb9-1.hole3~ STIFF
CONNECT ca-dp2-3.pin1 -> ca-yb9-1.hole7~ STIFF
CONNECT ca-ytb-1.hole1 -> ca-dp2-1.pin2?
CONNECT ca-ytb-2.hole1 -> ca-dp2-3.pin2?
WHY Builds the yellow roof rail.

## Step 171 (page 146)
ADD ca-ax10-1 3737 black
ADD ca-yc-1 6536 yellow
CONNECT ca-ax10-1.axle10 -> ca-yc-1.axlehole1 LOCKED
CONNECT ca-yc-1.hole1 -> ca-yb9-1.hole?
WHY Adds the long rod the roof leans on.

## Step 172 (page 147)
ADD ca-b7-1 32524 black
CONNECT ca-b7-1.hole? -> ca-bp-1.pin1?
CONNECT ca-b7-1.hole? -> ca-bp-2.pin1?
WHY Ties the pillar's pins.

## Step 173 (page 148)
ADD cp-b7-1 32524 black
ADD cp-bp-1 43093 blue
ADD cp-dp-1 61332 black
ADD cp-dp-2 61332 black
ADD cp-rax-1 32062 red
ADD cp-f8-1 2389 yellow
ADD cp-yax-1 4519 yellow
CONNECT cp-dp-1.pin1 -> cp-b7-1.hole2~ STIFF
CONNECT cp-dp-2.pin1 -> cp-b7-1.hole4~ STIFF
CONNECT cp-rax-1.axle1 -> cp-yax-1.axle?
CONNECT cp-yax-1.axle3 -> cp-b7-1.hole?
CONNECT cp-bp-1.pin1 -> cp-f8-1.hole?
WHY Builds the front corner pillar of the roof.

## Step 174 (page 150)
ADD ca-ec-1 6536 black
ADD ca-ec-2 6536 black
CONNECT ca-ec-1.axlehole1 -> cp-yax-1.axle3?
CONNECT ca-ec-2.axlehole1 -> cp-rax-1.axle2?
WHY Adds the connectors that the roof tube plugs into.

## Step 175 (page 151)
ADD rt-rax-1 32062 red
ADD rt-rax-2 32062 red
ADD rt-ax5-1 32073 lightgray
ADD rt-cyl-1 59443 black
ADD rt-end-1 32291 darkgray
ADD rt-end-2 32291 darkgray
CONNECT rt-rax-1.axle1 -> rt-cyl-1.axlehole1~ LOCKED
CONNECT rt-ax5-1.axle1 -> rt-end-1.axlehole1~ LOCKED
CONNECT rt-ax5-1.axle5 -> rt-end-2.axlehole1~ LOCKED
WHY Builds the roof tube / cab handle.

## Step 176 (page 152)
ADD bt-hose-1 32199 black
ADD bt-ang-1 32014 black
ADD bt-ball-1 52730 darkgray
ADD bt-rax-1 32062 red
ADD bt-yax-1 4519 yellow
ADD bt-cyl-1 59443 black
ADD bt-tb-1 41677 black
CONNECT bt-rax-1.axle1 -> bt-cyl-1.axlehole1~ LOCKED
CONNECT bt-yax-1.axle1 -> bt-cyl-1.axlehole1~ LOCKED
CONNECT bt-tb-1.axlehole1 -> bt-yax-1.axle?
CONNECT bt-ang-1.axlehole1 -> bt-cyl-1.axlehole1?
WHY Builds the bent roof tube that holds the hose handle.

## Step 177 (page 154)
ADD bt-ax6-1 3706 black
ADD bt-tb2-1 41677 black
CONNECT bt-tb2-1.axlehole1 -> bt-ax6-1.axlehole?
WHY Adds the second roof handle rod.

## Step 178 (page 155)
ADD sb-bush-1 32123b yellow
ADD sb-bush-2 32123b yellow
CONNECT sb-bush-1.axlehole1 -> ca-dp2-1.pin?
CONNECT sb-bush-2.axlehole1 -> ca-dp2-3.pin?
WHY Stops the thin roof beams from sliding off.

## Step 179 (page 156)
ADD rb-tb-1 11478 black
ADD rb-conn-1 42003 black
ADD rb-ax-1 87083 darkgray
ADD rb-tp-1 32002 tan
ADD rb-tp-2 32002 tan
CONNECT rb-tp-1.pin1 -> rb-tb-1.hole1~ STIFF
CONNECT rb-tp-2.pin1 -> rb-tb-1.hole3~ STIFF
CONNECT rb-conn-1.hole1 -> rb-tp-1.pin2?
CONNECT rb-ax-1.axle1 -> rb-conn-1.axlehole1?
WHY Builds a hinge bracket for the roof.

## Step 180 (page 157)
ADD rf2-b9-1 40490 yellow
ADD rf2-tb-1 32017 yellow
ADD rf2-tb-2 32017 yellow
ADD rf2-dp-1 61332 black
ADD rf2-dp-2 61332 black
ADD rf2-dp-3 61332 black
CONNECT rf2-dp-1.pin1 -> rf2-b9-1.hole2~ STIFF
CONNECT rf2-dp-2.pin1 -> rf2-b9-1.hole3~ STIFF
CONNECT rf2-dp-3.pin1 -> rf2-b9-1.hole7~ STIFF
CONNECT rf2-tb-1.hole1 -> rf2-dp-1.pin2?
CONNECT rf2-tb-2.hole1 -> rf2-dp-3.pin2?
WHY Doubles the yellow roof beam so the roof is wide.

## Step 181 (page 158)
ADD ca-ax10b-1 3706 black
ADD ca-yc2-1 6536 yellow
CONNECT ca-ax10b-1.axle6 -> ca-yc2-1.axlehole1 LOCKED
CONNECT ca-yc2-1.hole1 -> rf2-b9-1.hole?
WHY Adds the front roof rod that mirrors the one in step 171.

## Step 182 (page 159)
ADD or-hose-1 75c11 orange
WHY Adds an orange line as a decoration and window-brace.

## Step 183 (page 160)
ADD fl-bp-1 43093 blue
ADD fl-tile-1 3069b black
ADD fl-pl-1 18677 black
ADD fl-cn-1 32014 black
CONNECT fl-bp-1.pin1 -> fl-cn-1.hole1~ STIFF
CONNECT fl-pl-1.hole? -> fl-bp-1.axle1?
WHY Adds a small panel to the pillar top.

## Step 184 (page 161)
ADD ag-rax-1 32062 red
ADD ag-bp-1 43093 blue
ADD ag-cap-1 98138 black
ADD ag-ang-1 32015 black
ADD ag-ball-1 32291 darkgray
CONNECT ag-rax-1.axle1 -> ag-ang-1.axlehole1~ LOCKED
CONNECT ag-bp-1.pin1 -> ag-ang-1.hole1~ STIFF
CONNECT ag-ang-1.axlehole2 -> ag-ball-1.axlehole1?
CONNECT ag-cap-1.stud? -> ag-bp-1.pin?
WHY Builds the rear-right roof corner fitting.

## Step 185 (page 162)
ADD ao-dp-1 61332 black
ADD ao-cn-1 6536 black
ADD ao-bar-1 63965 orange
ADD ao-tile-1 98138 clear
CONNECT ao-dp-1.pin1 -> ao-cn-1.hole1 STIFF
CONNECT ao-tile-1.stud? -> ao-cn-1.hole?
CONNECT ao-bar-1.bar? -> ao-cn-1.hole?
WHY Adds the orange rail (the real machine's rear handle) on the roof.

## Step 186 (page 163)
ADD ao-tb-1 41677 black
CONNECT ao-tb-1.axlehole1 -> ao-cn-1.axlehole?
WHY Locks the orange rail in its connector.

## Step 187 (page 164)
ADD ar-plate-1 6141 transorange
ADD ar-dome-1 85861 black
ADD ar-clip-1 3484 black
CONNECT ar-plate-1.stud? -> ar-dome-1.stud?
CONNECT ar-clip-1.clip? -> ar-dome-1.stud?
WHY Adds the amber warning beacon.

## Step 188 (page 165)
ADD ah-tile-1 98138 clear
ADD ah-dp-1 61332 black
ADD ah-cn-1 6536 black
CONNECT ah-dp-1.pin1 -> ah-cn-1.hole1 STIFF
CONNECT ah-tile-1.stud? -> ah-dp-1.barhole?
WHY Adds a small light fitting at the rear.

## Step 189 (page 166)
ADD of-ball-1 52730 darkgray
ADD of-rax-1 32062 red
ADD of-rax-2 32062 red
ADD of-rax-3 32062 red
ADD of-rax-4 32062 red
ADD of-rax-5 32062 red
ADD of-bp-1 43093 blue
ADD of-bp-2 43093 blue
ADD of-ang-1 32014 orange
ADD of-ang-2 32014 orange
ADD of-cyl-1 59443 orange
ADD of-cyl-2 59443 orange
ADD of-cyl-3 59443 orange
ADD of-cyl-4 59443 orange
ADD of-tb-1 41677 black
ADD of-tb-2 41677 black
CONNECT of-rax-1.axle1 -> of-ang-1.axlehole1~ LOCKED
CONNECT of-rax-2.axle1 -> of-ang-1.axlehole2~ LOCKED
CONNECT of-rax-3.axle1 -> of-ang-2.axlehole1~ LOCKED
CONNECT of-ang-2.axlehole2 -> of-ball-1.axle1?
CONNECT of-rax-4.axle1 -> of-cyl-1.axlehole1~ LOCKED
CONNECT of-rax-5.axle1 -> of-cyl-2.axlehole1~ LOCKED
WHY Builds the orange hose-end fitting used as the engine breather on the model.

## Step 190 (page 169)
ADD of2-pl-1 18677 black
ADD of2-tile-1 3069b black
ADD of2-dp-1 61332 black
CONNECT of2-dp-1.pin1 -> of2-pl-1.hole?
CONNECT of2-tile-1.stud? -> of2-pl-1.stud?
WHY Adds a label tile on the machine's rear-left.

## Step 191 (page 170)
ADD of3-yax-1 4519 yellow
ADD of3-ang-1 32013 orange
CONNECT of3-yax-1.axle1 -> of3-ang-1.axlehole1~ LOCKED
WHY Starts the second orange fitting.

## Step 192 (page 170)
ADD of3-cyl-1 59443 orange
ADD of3-rc-1 18654 orange
CONNECT of3-cyl-1.axlehole1 -> of3-yax-1.axle2~ LOCKED
WHY Builds the orange outer tube.

## Step 193 (page 170)
ADD of3-ax6-1 3706 black
CONNECT of3-ax6-1.axle6 -> of3-cyl-1.axlehole2?
WHY Adds the piston rod of the fitting.

## Step 194 (page 171)
ADD of3-bp-1 43093 blue
ADD of3-bush-1 32123b yellow
CONNECT of3-bp-1.pin1 -> of3-ang-1.hole?
CONNECT of3-bush-1.axlehole1 -> of3-ax6-1.axle?
WHY Stops the rod from sliding out.

## Step 195 (page 171)
ADD of3-ang2-1 32015 orange
CONNECT of3-ang2-1.axlehole1 -> of3-bp-1.pin?
WHY Builds the bend of the fitting.

## Step 196 (page 171)
ADD of3-hose-1 32580 orange
CONNECT of3-hose-1.axlehole? -> of3-ang2-1.axlehole?
WHY Adds the long orange arm of the fitting.

## Step 197 (page 172)
ADD of3-ang3-1 32016 orange
CONNECT of3-ang3-1.axlehole1 -> of3-hose-1.axlehole?
WHY Finishes the arm with a foot.

## Step 198 (page 172)
ADD of3-rax-1 32062 red
ADD of3-ro-1 18654 orange
CONNECT of3-rax-1.axle1 -> of3-ang3-1.axlehole?
CONNECT of3-ro-1.axlehole? -> of3-rax-1.axle2?
WHY Finishes the second orange fitting.

## Step 199 (page 173)
CONNECT of3-ang-1.hole? -> uc-frame-1.hole?
WHY Finishes the model.
