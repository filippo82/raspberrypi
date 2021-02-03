
## Configuration files
### .bashrc

#### Aliases
alias ll='ls -altrh'

### .vimrc
set mouse=a

## Security

## Users

* [How To Change Username On Ubuntu, Debian, Linux Mint Or Fedora](https://www.linuxuprising.com/2019/04/how-to-change-username-on-ubuntu-debian.html)

## Package management
* [15 dpkg commands to Manage Debian based Linux Servers](https://www.linuxsysadmins.com/15-dpkg-commands-in-linux-servers/)

```
$ sudo apt-get install apt-file
$ sudo apt-file update
$ apt-file list libssl-dev
```
The apt history is recorded in `/var/log/apt/history.log`
To see all the packages that went through dpkg, you can look at `/var/log/dpkg.log`.


## Networking

* [Have a Plan for Netplan](https://www.linuxjournal.com/content/have-plan-netplan)
* [Ubuntu Server Netplan for Wifi and Ethernet](https://askubuntu.com/questions/1042789/ubuntu-server-netplan-for-wifi-and-ethernet)
* [Wifi on Ubuntu 18 server](https://gist.github.com/austinjp/9b968c75c3e54004be7cd7a134881d85)
* [Netplan – How To Configure Static IP Address in Ubuntu 18.04 using Netplan](https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/netplan-how-to-configure-static-ip-address-in-ubuntu-18-04-using-netplan.html)


sudo ufw status

### Discover router addres

On macOS, you can determine the router’s ip with the following command:

```shell
$ netstat -rn | grep default
```

An example router IP is `192.168.1.1`.

### Get IP addresses handed out by `dnsmasq`

```shell
$ cat /var/lib/misc/dnsmasq.leases
```

## Security

### SSH

* [How to SSH Properly](https://gravitational.com/blog/how-to-ssh-properly/)

## Reverse SSH tunneling
* [What Is Reverse SSH Tunneling? (and How to Use It)](https://www.howtogeek.com/428413/what-is-reverse-ssh-tunneling-and-how-to-use-it/)
* [How to Setup Reverse SSH Tunnel on Linux](https://www.thegeekstuff.com/2013/11/reverse-ssh-tunnel/)

You could also add some options to your command: ssh –f –N –T –R 2210:localhost:22 username@yourMachine.com

    -f: tells the SSH to background itself after it authenticates, saving you time by not having to run something on the remote server for the tunnel to remain alive.
    -N: if all you need is to create a tunnel without running any remote commands then include this option to save resources.
    -T: useful to disable pseudo-tty allocation, which is fitting if you are not trying to create an interactive shell.


## Time and dedicated

* [How to Change the Timezone on your Ubuntu System](https://vitux.com/how-to-change-the-timezone-on-your-ubuntu-system/)

## Cluster admin
* [ClusterSSH](https://github.com/duncs/clusterssh)

## Various

### .vimrc

## Random commands

* hostnamectl
* lsb_release -a
* cat /etc/os-release
