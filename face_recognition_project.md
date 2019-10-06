# Face recognition with Raspberry Pi

## Resources
* [Build a Hardware-based Face Recognition System for $150 with the Nvidia Jetson Nano and Python](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)
* [Install dlib and face_recognition on a Raspberry Pi](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)
* [dlib](https://github.com/davisking/dlib)

```shell
conda activate cv
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
sudo apt-get install libjpeg-dev libtiff-dev libjasper-dev libpng-dev
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

See [OpenCV file](./opencv_temp.md)

```shell
sudo apt-get install python3-picamera
sudo pip install --upgrade picamera[array]
pip install face_recognition
# conda install opencv # Error
```

```shell
sudo vim /etc/dphys-swapfile
```
change `DCONF_SWAPSIZE=1024` to `CONF_SWAPSIZE=100` and save / exit vim

```shell
sudo /etc/init.d/dphys-swapfile restart
```
