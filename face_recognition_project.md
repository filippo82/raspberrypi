# Face recognition with Raspberry Pi

## Resources
* [Build a Hardware-based Face Recognition System for $150 with the Nvidia Jetson Nano and Python](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)
* [Install dlib and face_recognition on a Raspberry Pi](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)
* [dlib](https://github.com/davisking/dlib)

```shell
source activate py36
```

```shell
sudo apt-get install cmake \
  libopenblas-dev \
  liblapack-dev \
  libjpeg-dev
```

```shell
sudo vim /etc/dphys-swapfile
```
change `DCONF_SWAPSIZE=100` to `CONF_SWAPSIZE=1024` and save / exit vim

```shell
sudo /etc/init.d/dphys-swapfile restart
```

```shell
mkdir -p dlib
git clone -b 'v19.18' --single-branch https://github.com/davisking/dlib.git dlib/
cd ./dlib
python setup.py install --compiler-flags "-mfpu=neon"
```

Compile OpenCV

```shell
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
```

Download OpenCV source code

```shell
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.1.zip
unzip opencv.zip
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout tags/4.1.1
```

cmake -D'CMAKE_BUILD_TYPE=RELEASE' \
-D'CMAKE_INSTALL_PREFIX=/usr/local' \
-D'INSTALL_PYTHON_EXAMPLES=ON' \
-D'WITH_GTK=ON' \
-D'OPENCV_EXTRA_MODULES_PATH=~/Software/opencv_contrib/modules' \
-D'PYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")' \
-D'PYTHON_LIBRARY=$(python -c "import distutils.sysconfig as sysconfig; print(sysconfig.get_config_var('LIBDIR'))")' \
-D'ENABLE_NEON=ON' \
-D'ENABLE_VFPV3=ON' \
-D'BUILD_EXAMPLES=ON' \
-D'OPENCV_PYTHON3_INSTALL_PATH=~/miniconda3/envs/py36/lib/python3.6/site-packages' \
-D'PYTHON3_EXECUTABLE:FILEPATH=/home/pi/miniconda3/envs/py36/bin/python' ..


```shell
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
pip install face_recognition
# conda install opencv # Error
```

```shell
sudo vim /etc/dphys-swapfile
```
change `DCONF_SWAPSIZE=1024` to `CONF_SWAPSIZE=100` and save / exit vim

autoconf automake autotools-dev gdal-data gfortran gfortran-8 ibverbs-providers libaec0 libarmadillo9 libarpack2 libcaf-openmpi-3 libcharls2 libcoarrays-dev libcoarrays-openmpi-dev libdap25 libdapclient6v5 libdapserver7v5 libepsilon1 libevent-core-2.1-6 libevent-pthreads-2.1-6 libfreexl1 libfyba0 libgdal20 libgdcm2.8 libgeos-3.7.1 libgeos-c1v5 libgeotiff2 libgfortran-8-dev libgl2ps1.4 libhdf4-0-alt libhdf5-103 libhdf5-openmpi-103 libhwloc-dev libhwloc-plugins libhwloc5 libibverbs-dev libibverbs1 libkmlbase1 libkmlconvenience1 libkmldom1 libkmlengine1 libkmlregionator1 libkmlxsd1 liblept5 libltdl-dev libmariadb3 libminizip1 libnetcdf-c++4 libnetcdf13 libnl-3-dev libnl-route-3-dev libodbc1 libogdi3.2 libopencv-calib3d3.2 libopencv-contrib3.2 libopencv-core3.2 libopencv-features2d3.2 libopencv-flann3.2 libopencv-highgui3.2 libopencv-imgcodecs3.2 libopencv-imgproc3.2 libopencv-ml3.2 libopencv-objdetect3.2 libopencv-photo3.2 libopencv-shape3.2 libopencv-stitching3.2 libopencv-superres3.2 libopencv-video3.2 libopencv-videoio3.2 libopencv-videostab3.2 libopencv-viz3.2 libopenmpi-dev libopenmpi3 libpmix2 libproj13 libqhull7 libsigsegv2 libsocket++1 libspatialite7 libsuperlu5 libsz2 libtbb2 libtesseract4 libtool liburiparser1 libvtk6.3 libxerces-c3.2 m4 mariadb-common mysql-common ocl-icd-libopencl1 odbcinst odbcinst1debian2 openmpi-bin openmpi-common proj-bin proj-data python3-opencv

```shell
sudo /etc/init.d/dphys-swapfile restart
```
