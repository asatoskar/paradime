# CMake Command To Build OpenCV with OpenCV_Contrib

\ 
cmake -D CMAKE_BUILD_TYPE=RELEASE \

	-D CMAKE_INSTALL_PREFIX=/usr/local \
	
	-D INSTALL_C_EXAMPLES=ON \
	
	-D INSTALL_PYTHON_EXAMPLES=ON \
	
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	
	-D WITH_TBB=ON \
	
	-D WITH_EIGEN=ON \
	
	-D BUILD_DOCS=ON \
	
	-D BUILD_EXAMPLES=ON ..
