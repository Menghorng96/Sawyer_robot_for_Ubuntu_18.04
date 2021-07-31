# Sawyer_robot_for_Ubuntu_18.04

## Workstation Setup
1. Install Ubuntu 18.04
2. [Install ROS Melodic for Unbuntu 18.04](http://wiki.ros.org/melodic/Installation/Ubuntu)
   - Setup your sources.list: 
   ```
   $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
   ```
   - Set up your keys:
   ```
   $ sudo apt install curl # if you haven't already installed curl
   $ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
   ```
   Or:
   ```
   $ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 
   ```
   - Installation 
   ```
   $ sudo apt update
   $ sudo apt install ros-melodic-desktop-full
   ```
   - Dependencies for building packages
   ```
   $ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
   ```
   - Initialize rosdep
   ```
   $ sudo rosdep init
   $ rosdep update
   ```
   - Install rosinstall
   ```
   $ sudo apt-get install python-rosinstal
   ```
  
3. Create Development Workspace
   - Create ROS Workspace
   ```
   $ mkdir -p ~/ros_ws/src
   ```
   - Source ROS Setup
   ```
   $ source /opt/ros/melodic/setup.bash
   ```
   - Build
   ```
   $ cd ~/ros_ws
   $ catkin_make
   ```
4. INSTALL INTERA SDK DEPENDENCIES
```
$ sudo apt-get update
$ sudo apt-get install git-core python-argparse python-wstool python-vcstools python-rosdep ros-melodic-control-msgs ros-melodic-joystick-drivers ros-melodic-xacro ros-melodic-tf2-ros ros-melodic-rviz ros-melodic-cv-bridge ros-melodic-actionlib ros-melodic-actionlib-msgs ros-melodic-dynamic-reconfigure ros-melodic-trajectory-msgs ros-melodic-rospy-message-converter
```
5. Install Intera Robot SDK



6. 

## Gazebo Simulator


## Intera Interface Example



## Moveit Configuration


