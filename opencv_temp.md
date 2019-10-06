
* [OpenCV dependencies](https://github.com/chrismeyersfsu/playbook-opencv/blob/master/roles/common/defaults/main.yml)
* [Installation in Linux ](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)
* [GitHub issue](https://github.com/opencv/opencv/issues/15328)


### 04.10.2019

```shell
cmake -D'CMAKE_BUILD_TYPE=RELEASE' \
-D'CMAKE_INSTALL_PREFIX=/usr/local' \
-D'OPENCV_EXTRA_MODULES_PATH=~/Software/opencv_contrib/modules' \
-D'ENABLE_NEON=ON' \
-D'ENABLE_VFPV3=ON' \
-D'BUILD_TESTS=OFF' \
-D'OPENCV_ENABLE_NONFREE=ON' \
-D'INSTALL_PYTHON_EXAMPLES=ON' \
-D'CMAKE_CXX_FLAGS=-latomic' \
-D'OPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic' \
-D'BUILD_opencv_ts=OFF' \
-D'ENABLE_PRECOMPILED_HEADERS=OFF' \
-D'BUILD_EXAMPLES=ON' \
-D'BUILD_opencv_python2=OFF' \
-D'BUILD_opencv_python3=ON' \
-D'HAVE_opencv_python3=ON' \
-D'PYTHON3_EXECUTABLE:FILEPATH=/home/pi/miniconda3/envs/cv/bin/python' \
-D'PYTHON_DEFAULT_EXECUTABLE:FILEPATH=/home/pi/miniconda3/envs/cv/bin/python' ..
```
What about this one? Shall I test it?
```shell
-D'OPENCV_PYTHON3_INSTALL_PATH=/home/pi/miniconda3/envs/cv/lib/python3.6/site-packages'
```

make -j4
sudo make install
sudo ldconfig

Reset the swap file size:
sudo /etc/init.d/dphys-swapfile restart

cd ~/miniconda3/envs/cv/lib/python3.6/site-packages/
ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-arm-linux-gnueabihf.so cv2.so
