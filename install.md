
* [Set up](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/5)

## Install additional packages

```shell
sudo apt-get install vim
```

## Download and install Miniconda

```shell
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
md5sum Miniconda3-latest-Linux-armv7l.sh
bash Miniconda3-latest-Linux-armv7l.sh
source ~/.bashrc
conda update conda
```

## Add Berryconda channel and create an environment for Python 3.6
```shell
conda config --add channels rpi
conda create --name py36 python=3.6
source activate py36
```
