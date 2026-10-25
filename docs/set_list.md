# Sets to label next

Picked for **variety of mechanisms**, not vehicle types. **3D** = an official 3D model exists in the LDraw Official Model Repository (checked Oct 22, 2026). Those sets give exact part positions for free: every join can be checked against real geometry and the picture check comes almost for free. Prefer them.

Names are from memory: confirm the set number and name on Rebrickable before labeling, and download the instruction PDF from LEGO's building-instructions site.

## Batch 1: small, one or two clear mechanisms each (start here)
| Set | Name | Main mechanisms | 3D |
| --- | --- | --- | --- |
| 42004 | Mini Backhoe Loader | levers, linkages (two tools), no gears | ✅ |
| 42006 | Excavator | linkages, turntable | ✅ |
| 42116 | Skid Steer Loader | lift arm linkage, tilting bucket | ✅ |
| 42101 | Buggy | pull-back motor, simple steering | ✅ |
| 42021 | Snowmobile | suspension, steering | ✅ |
| 42029 | Customised Pick-Up | steering, piston engine, winch | ✅ |
| 42049 | Mine Loader | articulated steering, bucket linkage | ✅ |
| 42061 | Telehandler | telescopic boom, steering | ✅ |
| 42094 | Tracked Loader | tracks, lift linkage | ✅ |
| 8049 | Tractor with Log Loader | crane arm, grab, steering (same era as 8047) | ✅ |
| 8258 | Crane Truck | crane, outriggers, winch, steering | ✅ |

## Batch 2: medium, drivetrain and special systems
| Set | Name | Main mechanisms | 3D |
| --- | --- | --- | --- |
| 42052 | Heavy Lift Helicopter | rotor gearing, winch, folding ramp | ✅ |
| 42056 | Porsche 911 GT3 RS | gearbox, differential, steering, suspension | ✅ |
| 42110 | Land Rover Defender | 4-wheel drive, gearbox, suspension, winch | ✅ |
| 42080 | Forest Machine | pneumatics, crane, grab | ✅ |
| 42095 | Remote-Controlled Stunt Racer | motors and remote control (Power Functions) | ✅ |
| 42063 | BMW R 1200 GS Adventure | motorcycle suspension, engine | ✅ |
| 8275 | Motorized Bulldozer | motors, tracks, blade and ripper | ✅ |
| 8880 | Super Car | classic: 4WD, 4-wheel steering, gearbox, suspension | ✅ |
| 8448 | Super Street Sensation | classic: engine, steering, suspension | ✅ |
| 8862 | Backhoe Grader | classic: pneumatics, linkages | ✅ |

## Batch 3: large, many mechanisms together (after the pipeline is fast)
| Set | Name | Main mechanisms | 3D |
| --- | --- | --- | --- |
| 42054 | Claas Xerion 5000 | 4-wheel steering, rotating cab, drivetrain | ✅ |
| 42082 | Rough Terrain Crane | telescopic boom, outriggers, gearbox-selected functions | ✅ |
| 42083 | Bugatti Chiron | 8-speed gearbox, W16 engine | ✅ |
| 42055 | Bucket Wheel Excavator | motors, conveyors, tracks | ✅ |
| 42100 | Liebherr R 9800 | app-controlled excavator, many motors | ✅ |
| 42131 | Cat D11 Bulldozer | app-controlled, tracks, blade, ripper | ✅ |

## Good sets without a 3D model (label from pictures only)
| Set | Name | Why it's useful |
| --- | --- | --- |
| 8043 | Motorized Excavator | linear actuators + motors, same era as 8047 |
| 8069 | Backhoe Loader | linear actuators, two tools |
| 42009 | Mobile Crane Mk II | large crane, many functions |
| 42030 | Volvo L350F | motorized loader, articulated steering |

## Why this order
- **Mechanism coverage:** across the list the model sees levers, linkages, worm drives, turntables, tracks, steering (normal, articulated, 4-wheel), suspension, gearboxes, differentials, pneumatics, linear actuators, motors, winches and telescopic booms. 8047 only covers worm drives, a turntable, linkages and tracks.
- **Small first:** labeling cost grows with step count, and small sets make the tools faster before tackling 1,000+ piece sets.
- **3D models:** they let us check every label against exact geometry and build the picture-comparison check.
- **Testing:** `training/pack_data.py` combines audited ready sets and holds out one whole set. See `dataset_status.csv` for actual progress; this list is a selection guide.
