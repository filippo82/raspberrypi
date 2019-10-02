# Face recognition with Raspberry Pi

## Resources
* [Build a Hardware-based Face Recognition System for $150 with the Nvidia Jetson Nano and Python](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)
* [Install dlib and face_recognition on a Raspberry Pi](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)
* [dlib](https://github.com/davisking/dlib)


```shell
sudo apt-get install cmake \
  libopenblas-dev \
  liblapack-dev \
  libjpeg-dev
```

```shell
sudo vim /etc/dphys-swapfile
```
change *DCONF_SWAPSIZE=100* to *CONF_SWAPSIZE=1024* and save / exit vim

```shell
sudo /etc/init.d/dphys-swapfile restart
```

```shell
mkdir -p dlib
git clone -b 'v19.18' --single-branch https://github.com/davisking/dlib.git dlib/
cd ./dlib
sudo python3 setup.py install --compiler-flags "-mfpu=neon"
```

```shell
sudo vim /etc/dphys-swapfile
```
change *DCONF_SWAPSIZE=1024* to *CONF_SWAPSIZE=100* and save / exit vim

```shell
sudo /etc/init.d/dphys-swapfile restart
```

```shell
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
```

```shell
sudo pip3 install face_recognition
```
