# robot_arm_ros_client
ROS package which does:

1. **Forward Kinmatics**: Sends control commands from an xbox controller to a raspberry pi server controlling the servo motors.
2. **Inverse Kinematics**: Provide a desired end effector position, computes robot servo angles, sends angles to the raspberry pi server.  

The server code which controls the motors can be found: https://github.com/NateGyory/raspberry_pi_server.git

# Robot Arm
The robot is composed of:

1. 3D Printed Body
2. 9g Micro Servos
3. Raspberry Pi 4
4. 16 Pin PWM Driver

![IMG_5978](https://user-images.githubusercontent.com/45575958/232506312-c384d7f3-181b-42a8-8464-7c98c9fdc5c4.JPG)

## Xbox Controller Demo

https://user-images.githubusercontent.com/45575958/232511461-8255df1f-5332-4522-a536-d11fe38cad67.MOV

## Inverse Kinematics Demo

https://user-images.githubusercontent.com/45575958/232512142-1b0855ac-ea05-4ff5-b2cb-cad3f4b8ac69.MOV

## Requirements
ROS noetic, ubuntu 20.04, python3.

## How to run
Clone the repo into your ROS src director:

```console
foo@bar:~$ git clone https://github.com/NateGyory/robot_arm_ros_client.git
```

Build the new ros package:

```console
foo@bar:~$ catkin build robot_arm_ros_client
```

Source the new ROS package:

```console
foo@bar:~$ source ../devel/setup.zsh
```

Launch the client code:

```console
foo@bar:~$ roslaunch robot_arm_ros_client bringup.launch
```
