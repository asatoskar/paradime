# Guide to Install OpenCV from Source on Fedora 25 with opencv_contrib modules

**Install the following packages**

For installation process

> sudo dnf install cmake python-devel numpy gcc gcc-c++ git

For GUI features

> sudo dnf install gtk2-devel libdc1394-devel libv4l-devel gstreamer-plugins-base-devel

For image format support

>sudo dnf install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel

For Thread Building Blocks support

>sudo dnf install tbb-devel

For Eigen support

>sudo dnf install eigen3-devel

**Download OpenCV from GitHub**

>cd ~

>git clone https://github.com/opencv/opencv.git

>git clone https://github.com/opencv/opencv_contrib.git

**Set up the build**

>cd ~/opencv

>mkdir build

>cd bulid

Now type in the following cmake command :-

# CMake Command To Build OpenCV with OpenCV_Contrib

>cmake -D CMAKE_BUILD_TYPE=RELEASE \

>	-D CMAKE_INSTALL_PREFIX=/usr/local \
	
>	-D INSTALL_C_EXAMPLES=ON \
	
>	-D INSTALL_PYTHON_EXAMPLES=ON \
	
>	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	
>	-D WITH_TBB=ON \
	
>	-D WITH_EIGEN=ON \
	
>	-D BUILD_DOCS=ON \
	
>	-D BUILD_EXAMPLES=ON ..

in the same folder, run the make command

>make

This will take a good amount of time. Once the 'make' command finishes:

>sudo make install

OpenCv should now be installed in : */usr/local/lib/python2.7/site-packages*

**Add this location to the PYTHONPATH in ~/.bashrc file in order to use the cv2 module.**

>sudo nano ~/.bashrc

>*Add the following to the end of the file*

>export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

Save and exit.

**Test the install**

>python2

>\>\>\>import cv2
