# Weld-Seam-Finding

Image processing pipeline
* Capture image / geometry acquisition and processing
* Pre-process (normalize lighting, remove noise)
* Segment the objects (using what approach, U-net, yolo3d, etc)
  * Do 2D?  
  *  Do depth approach first with depth camera? 
* Extract boundary line
* Convert to 3d coordinates
* Generate trajectory

Path optimization, focuses on the WHAT and WHEN.  Figuring out where the robot arm needs to move/go
* Layer sequence plan
* Robot kinematic constraints
* Welding process constraints
* Workspace boundaries
* Convert layer plans to waypoints,
* Generate 

Robot motion planning, focuses on the HOW, figuring out what it takes for the robot arm to move there.  
* Inverse dynamics/kinematics solver
