ROSMOD
======

ROSMOD is a tool suite for rapid prototyping component-based software applications using the Robot Operating System (ROS). Using ROSMOD, an application developer can create and manage *projects* for distributed real-time embedded systems. Each ROSMOD Project consists of *models* that represent the structure and behavior of the system:

* Software Model : One or more ROS packages in the workspace.
* Hardware Model: One or more Hardware devices.
* Deployment Model: A Mapping between ROS nodes/processes & Hardware devices.

Using these models, ROSMOD can:

* Generate a skeleton ROS workspace, including build system files.
* Preserve already generated work-in-progress ROS workspaces using code-preservation markers.
* Generate deployment-specific XML files for ROS node lifecycle management. 
* Generate timing analysis models from abstract business logic specification.
* Perform network analysis to admit/reject applications based on network profiles.

ROSMOD significantly improves the time taken to prototype ROS packages since much of the *boring* skeleton code e.g. port & timer initialization, callbacks for timers, servers & subscribers etc. are automatically generated from the Software Model. Once generated, a developer need only add the *"business logic"* of the generated callbacks to complete the package.

Using ROSMOD
------------

```bash
git clone --recursive https://github.com/finger563/rosmod
git submodule foreach git pull origin master
cd rosmod
sudo ./dependencies.py
cd src/rosmod_v0.3
./update_rosmod_egg <PATH_TO_EGG>
alias rosmod='python <PATH_TO_EGG/rosmod.egg>'
rosmod
```