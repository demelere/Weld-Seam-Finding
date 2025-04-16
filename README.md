# Weld Seam Finding

## Real-time fine-tuned seam finding
Starting with adapting a 2D model for 3D before going full 3D.  I started with FastSAM as a baseline, since it claims to be 50x faster than SAM.  It's based on YOLOv8-seg.  Some alternatives include YOLOv8-seg, YOLOv9-seg, YOLACT++, U-Net, BiSeNet.

## Autonomous Programming Workflow
### Image processing pipeline
* Capture image/video and geometry
* Pre-process (normalize lighting, remove noise)
* Segment the objects
* Extract boundary line
* Convert to 3D coordinates
* Generate trajectory

### Path optimization
Focuses on the WHAT and WHEN, figure out where the robot arm needs to move/go
* Layer sequence plan
* Robot kinematic constraints
* Welding process constraints
* Workspace boundaries
* Convert layer plans to waypoints
* Generate 

### Robot motion planning
Focuses on the HOW, figure out what it takes for the robot arm to move there
* Inverse dynamics/kinematics solver