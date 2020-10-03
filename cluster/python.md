# Python


## Install virtualenv

# Ubuntu 19.10
```
sudo apt-get install python3-pip python3-virtualenv python3-virtualenvwrapper
```

Append this to `.bashrc`
```
## Virtualenv and Virtualenvwrapper
export WORKON_HOME=$HOME/Work/virtualenvs
export PROJECT_HOME=$HOME/Work
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source $HOME/.local/bin/virtualenvwrapper.sh
```

## Packaging

* [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

## Virtual environments

* [](https://docs.python-guide.org/dev/virtualenvs/)
* [StackOverflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
