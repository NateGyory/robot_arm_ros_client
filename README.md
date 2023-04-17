# robot_arm_ros_client
ROS package which does:

1. **Forward Kinmatics**: Sends control commands from an xbox controller to a raspberry pi server controlling the servo motors.
2. **Inverse Kinematics**: Provide a desired end effector position, computes robot servo angles, sends angles to the raspberry pi server.  

The server code which controls the motors can be found: https://github.com/NateGyory/raspberry_pi_server.git

## Xbox Controller Demo

https://user-images.githubusercontent.com/45575958/232519944-8e0900b1-7683-47f6-a9d9-4791cea931b2.mp4

## Inverse Kinematics Demo
To run the IK functionality, type the desired end effector 3D coordinates into the terminal. Once the solver computes the joint angles, the robot arm angle configuration is displayed on the screen. Once you exit out of the display, the clinet sends the desired joint angles to the robot arm.

https://user-images.githubusercontent.com/45575958/232520796-f49ec2ef-3019-48d3-b9b6-0999a42b97fa.mp4

# Robot Arm
The robot is composed of:

1. 3D Printed Body
2. 9g Micro Servos
3. Raspberry Pi 4
4. 16 Pin PWM Driver

![IMG_5978](https://user-images.githubusercontent.com/45575958/232516272-0147a491-f3e1-4a41-ab33-6110470881d7.JPG)

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
