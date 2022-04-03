# robot_arm_ros_client
ROS package which sends control commands to the raspberry pi server controlling the servo motors.

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

## TODO
I want to put everything in a docker file so that the entire environment is contained and you do not need ROS to run the client.

I also want to integrate the ROS Joy package so that we can use an Xbox controller to controll the robot arm.
