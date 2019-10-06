
* [Set up](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/5)

## Install additional packages

```shell
sudo apt-get install vim
```

## Set up Github
git config --global user.email "filippo82@users.noreply.github.com"
git config --global user.name "Filippo B"
git config --global core.editor "vim"

## Download and install Miniconda

```shell
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
md5sum Miniconda3-latest-Linux-armv7l.sh
bash Miniconda3-latest-Linux-armv7l.sh
# Choose not to add anything to .bashrc
echo ". /home/pi/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate" >> ~/.bashrc
source ~/.bashrc
conda update conda
conda install python=3.6.6
conda install ipython numpy
```

## Add Berryconda channel and create an environment
```shell
conda config --add channels rpi
conda create --name cv
conda activate cv
conda install pip
```
