# Ansible

[Ansible tutorial](https://github.com/leucos/ansible-tuto)
[](https://blog.risingstack.com/getting-started-with-ansible-infrastructure-automation/)

## Installation

sudo apt-get install libffi-dev libssl-dev

```
mkvirtualenv ansible-tuto
workon
pip install ansible
```

```
mkdir bootstrap-raspberry
cd bootstrap-raspberry
touch ansible.cfg
touch hosts
```

## Test
ansible -i hosts -m ping all
ansible -i hosts -m shell -a 'grep DISTRIB_RELEASE /etc/lsb-release' all
ansible -i hosts -m shell -a 'uname -a' all
