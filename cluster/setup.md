# Setup

## Prepare the Raspberry Pis

In the following we walk through how to set up the RPI operating system (OS) and Kubernetes. Note that I’m using macOS as the host operating system, that is, where I prepare the SD cards and install the RPI OS (steps 1. and 2. below), so you may end up using different tools if you’re carrying out these steps in a different environment, say Linux or Windows.

### Preparing the SD cards

Open up the disk utility app and erase/format the SD cards using the MS-DOS (FAT) format:

### Install the Operating System on the SD cards

Download a 64bit GNU/Linux OS, such as
[Ubuntu 19.10](http://cdimage.ubuntu.com/releases/eoan/release/ubuntu-19.10.1-preinstalled-server-arm64+raspi3.img.xz) or
[Ubuntu 20.04](http://cdimage.ubuntu.com/ubuntu/releases/20.04/release/ubuntu-20.04-preinstalled-server-arm64+raspi.img.xz)
and extract the image like so:

```
$ xz -d ubuntu-19.10.1-preinstalled-server-arm64+raspi3.img.xz
$ unxz
```

You can read more about Ubuntu and Raspberry Pi on this
dedicated [page](https://ubuntu.com/download/raspberry-pi).

Now, following these [instructions for macOS](https://ubuntu.com/tutorials/create-an-ubuntu-image-for-a-raspberry-pi-on-macos#1-overview),
flash the SD card (install the OS, make it bootable):

```
# Identify the SD card
diskutil list
...
/dev/disk2 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *64.0 GB    disk2
   1:                 DOS_FAT_32 RPNODE0                 64.0 GB    disk2s1

# Unmount the SD card:
$ diskutil unmountdisk /dev/disk2
Unmount of all volumes on disk2 was successful

# now, flash the SD card with the OS:
$ sudo dd if=ubuntu-20.04-preinstalled-server-arm64+raspi.img of=/dev/disk2 bs=8m
1485+1 records in
1485+1 records out
3115115520 bytes transferred in 126.646778 secs (24596879 bytes/sec)
```
If you get the `dd: bs: illegal numeric value` error,
you might need to change `bs=8m` to `bs=8M`.

```
# flush cache (pending disk writes):
$ sync /dev/disk2

# eject SD card so you can insert into the Pi:
$ diskutil eject /dev/disk2
Disk /dev/disk2 ejected
```

### Enable the SSH server (only if using Raspbian)

SSH is not activated by default in Raspbian.
If we want to create a headless system (without monitor and keyboard),
we will first need to activate SSH access.
To do so, we will have to create an empty file called `ssh`
inside the MicroSD card's `/boot` partition.
We navigate to where the card is mounted (usually `/media`)
and enter the `boot` partition:

```
touch SSH
```

### Cloud init

#### usercfg.txt

#hdmi_group=2
#hdmi_mode=82
#disable_overscan=1
#overscan_left=100
#overscan_top=100
framebuffer_width=1920
framebuffer_height=1080

dtoverlay=disable-wifi
dtoverlay=disable-bt

#### user-data

```yaml
cloud-config
hostname: kube-node0
#fqdn: kube-node0.example.com

disable_root: true
ssh_pwauth: false

#chpasswd:
#  expire: true
#  list:
#  - pi:raspberry

groups:
  - pi

users:
  - default

system_info:
  # This will affect which distro class gets used
  distro: ubuntu
  # Default user name + that default users groups (if added/used)
  default_user:
    name: pi
    homedir: /home/pi
    lock_passwd: true
    gecos: Pi
    primary_group: pi
    groups: [adm, audio, cdrom, dialout, dip, floppy, lxd, netdev, plugdev, sudo, video]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
    shell: /bin/bash
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDf+a0hxMq3FCTyzqEq75CCU/+eRLk6cCLmJyAGKRdGl4rCIZXF1ujB7CFfTchipwEHv/XzDqv1VSio2d98NC0jt/5VYltk89FxIEDoNW16DgD+Nux1kGEzUEM0NJS4XLeDmAeuu0LjvlnFDLTj2aPKjEfQrj19Mso85t1r9coyh4FCKY8jFBfs9ff+M8SnDYjpwnl2dey0+P5fDXBkurTIc2ymjWhWRW2py6QlBlnlNZzRBeu40B3J75ilLNdIyzS7ylLK1o2RVpPgNlMj1oqZd/nSp9RNFyaEyFBcaNnuxEnRQ1RqmAuvE/odTWP24QeWHp0XsAM8N0kjtHrUAl+7 pi@kube-master
  #Automatically discover the best ntp_client
  ntp_client: auto

runcmd:
  - sed -i '$ s/$/ cgroup_enable=memory cgroup_memory=1/' /boot/firmware/cmdline.txt
  - echo "Welcome to the Raspberry Pi cluster!" > /etc/motd

package_update: true
#package_upgrade: true
apt_boot_if_required: true
packages:
  - vim
  - ntp

locale: "en_US.UTF-8"
timezone: "Europe/Zurich"

#write_files:
#  - content: |
#        pi    ALL=(ALL) NOPASSWD: ALL
#        Defaults:pi    !requiretty
#    owner: root:root
#    path: /etc/sudoers.d/pi
#    permissions: '0444'

```
```
  - sed -i -e '/^Port/s/^.*$/Port 4444/' /etc/ssh/sshd_config
  - sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config
```

ssh_pwauth: True
disable_root_opts: no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"$USER\" rather than the user \"root\".';echo;sleep 10"

Automatically discover the best ntp_client
ntp_client: auto
Remember that if you have manage_etc_hosts: true set in your user-data file, this will get overwritten.
manage_etc_hosts: true

`sudo cloud-init clean --logs --reboot` from [here](https://www.raspberrypi.org/forums/viewtopic.php?t=255465)
touch /etc/cloud/cloud-init.disabled

`manage_resolv_conf` [here](https://stackoverflow.com/questions/48736348/using-cloud-init-to-change-resolv-conf)

Resources:
* [](https://blog.hypriot.com/post/cloud-init-cloud-on-hypriot-x64/)
* [](https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup)
* [](https://wiki.archlinux.org/index.php/Cloud-init)
* [](https://serverfault.com/questions/412113/aws-how-to-stop-cloud-init-from-disabling-root-login)
* [](https://www.zetta.io/en/help/articles-tutorials/cloud-init-reference/)
* [](http://www.jedimt.com/2019/12/deploying-k8s-on-raspberry-pi4-with-hypriot-and-cloud-init/)

#### meta-data

```
#instance-id: KubeNode0
#local-hostname: kube-node0
#hostname: kube-node0

```

#### network-config (not necessary)

```
version: 2
renderer: networkd
ethernets:
  eth0:
    dhcp4: true
```

<!-- ```
version: 2
renderer: networkd
ethernets:
  eth0:
    dhcp4: false
    addresses: [10.0.0.10/27]
```

```
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      addresses: [10.0.0.1/27]
```

Other:
```
version: 2
ethernets:
  interface0:
    match:
      mac_address: "52:54:00:12:34:00"
    set-name: interface0
    addresses:
      - 192.168.1.10/255.255.255.0
    gateway4: 192.168.1.254
``` -->

#### Status
When cloud-init is finished running, it touches the file /var/lib/cloud/instance/boot-finished Checking for its existence is probably the simplest option. If you need to check that cloud-init finished without any error, you can also look at /var/lib/cloud/data/result.json
Log files:
* /var/log/cloud-init-output.log


```
cloud-init status
```

#### Note
Pay attention to hyphens und underscores: [](https://bugzilla.redhat.com/show_bug.cgi?id=1786350).

### Rename username (for Ubuntu only)

Follow the instructions [here](https://www.linuxuprising.com/2019/04/how-to-change-username-on-ubuntu-debian.html)
to rename `ubuntu` to `pi`.

### GPU memory

Reduce the GPU memory to 16 MB (I set it to the minimum as I’ll likely never connect a display to any of the Pi).

### Setup master node

Log into the Raspberry Pi with username `ubuntu` and password `ubuntu`.
You will be prompted to change the password.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install net-tools
```

### Change hostname:


* kube-master
* kube-node0
* kube-node1

```
sudo hostnamectl set-hostname NEW_NAME
```

On master and nodes, modify `/etc/hosts` by adding the following lines:
```
# Kubernetes addresses
10.0.0.1 kube-master
10.0.0.10 kube-node0
10.0.0.11 kube-node1
```
or
```bash
echo -e "# Kubernetes addresses" | sudo tee -a /etc/hosts
echo -e "10.0.0.1\tkube-master" | sudo tee -a /etc/hosts
echo -e "10.0.0.10\tkube-node0" | sudo tee -a /etc/hosts
echo -e "10.0.0.11\tkube-node1" | sudo tee -a /etc/hosts
```

### Adjust config.txt

```
sudo vim /boot/firmware/usercfg.txt
```

### Disable swap

```
sudo dphys-swapfile swapoff && \
sudo dphys-swapfile uninstall && \
sudo update-rc.d dphys-swapfile remove
sudo systemctl disable dphys-swapfile
```
This should now show no entries:
```
sudo swapon --summary
```


###

```
sudo apt-get update
sudo apt-get install xubuntu-core slick-greeter
```
Choose `lightdm`

This will take a while. Once everything is installed,
the final step is to set Slick Greeter as the login screen.
Create `/etc/lightdm/lightdm.conf` with the following content:

```
[SeatDefaults]
greeter-session=slick-greeter
```
And finally:
```
sudo reboot
```

### Activate WIFI on Ubuntu server?
WIP

### Static IP for Pi Router on Home Network
Since I’ll be using this as a jumpbox, I needed a static IP address for it on my home network. I did the following:

    Looked up the MAC address for the wlan0 network device.

```
ifconfig wlan0
```
Logged in to my home router’s admin portal (for me this was at 192.168.1.1) and reserved a static IP address for this MAC address.


To disable cloud-init's network configuration capabilities, write a file
`/etc/cloud/cloud.cfg.d/99-disable-network-config.cfg` with the following:
```
network: {config: disabled}
```

Move (or remove) any files present in `/etc/netplan` directory to other location.

Create a file called `01-kube-net-config.yaml` inside `/etc/netplan` with the
following content:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      addresses: [10.0.0.1/27]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

http://www.subnet-calculator.com/cidr.php

The value for gateway4 is your router or default gateway.
These addresses reference Google’s public DNS servers.

To apply the changes, run sudo netplan --debug try, then sudo netplan --debug generate, sudo netplan --debug apply, and reboot for good measures. Once the RPI comes back up again, you can check the network configuration with ip addr.

Once all the configurations are successfully applied, restart the Network-Manager service by running the following command:
```
sudo systemctl restart network-manager
```

If you are using a Ubuntu Server, instead use the following command:
```
sudo systemctl restart systemd-networkd
```

Now to verify if the new configurations are successfully applied, run the following command to verify the IP address:
```
ip a
```

> :mega: By default, Ubuntu desktop version ships with Network Manager. In most desktop environments, it does a good job. In this case, the netplan file should hand over networking to Network Manager.


#### For Raspbian (don't do this)

```
sudo vim /etc/dhcpcd.conf
```

```
interface eth0
static ip_address=10.0.0.10/27
#static domain_name_servers=8.8.8.8,8.8.4.4
nolink
```

Reboot and check with `ip a`.

### Install and set up dnsmasq

```
sudo apt-get install dnsmasq
```

[](https://downey.io/blog/create-raspberry-pi-3-router-dhcp-server/)

Make a new configuration file for dnsmasq
sudo vim /etc/dnsmasq.conf

```
# Our DHCP service will be providing addresses over our eth0 adapter
interface=eth0

# We will listen on the static IP address we declared earlier
listen-address=10.0.0.1

# My cluster doesn't have that many Pis, but since we'll be using this as
# a jumpbox it is nice to give some wiggle-room.
# We also declare here that the IP addresses we lease out will be valid for
# 12 hours
dhcp-range=10.0.0.10,10.0.0.31,12h

# Decided to assign static IPs to the kube cluster members
# This would make it easier for tunneling, certs, etc.
dhcp-host=MAC_ADDRESS_NODE0,10.0.0.10
dhcp-host=MAC_ADDRESS_NODE1,10.0.0.11

# This is where you declare any name-servers. We'll just use Google's
server=8.8.8.8
server=8.8.4.4

# Bind dnsmasq to the interfaces it is listening on (eth0)
bind-interfaces

# Never forward plain names (without a dot or domain part)
domain-needed

# Never forward addresses in the non-routed address spaces.
bogus-priv

# Use the hosts file on this machine
expand-hosts

# Useful for debugging issues
# log-queries
# log-dhcp
```

If everything went as planned, you should be able to validate that dnsmasq is running by doing:

```
sudo service dnsmasq status
```

### Forward Internet from WiFi (wlan0) to Ethernet (eth0)

We need to make sure that the nodes in the cluster network are able to access the outside internet,
so the next is to set up some internet forwarding.

First edit `/etc/sysctl.conf` and uncomment the following line:
```
net.ipv4.ip_forward=1
```
You should then reboot the server for this to take effect.
Alternately you can run `sudo sysctl net.ipv4.ip_forward=1`
to make the change without rebooting. If you choose to do this you will
still want to edit `/etc/sysctl.conf` to make the setting permanent.

You then add the following iptables rules:
```
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

After all this, the iptables rules should look like the following:
```
sudo iptables -L -n -v

Chain INPUT (policy ACCEPT 12 packets, 870 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 ACCEPT     all  --  wlan0  eth0    0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
    0     0 ACCEPT     all  --  eth0   wlan0   0.0.0.0/0            0.0.0.0/0

Chain OUTPUT (policy ACCEPT 6 packets, 1080 bytes)
 pkts bytes target     prot opt in     out     source               destination
```

I wanted to make sure these rules survived across reboots, so I installed a package called iptables-persistent:

```
sudo apt install iptables-persistent
```
As part of the installation process, choose `yes` when asked
to save the current rules to `/etc/iptables/rules.v4`.

After all of this, reboot again and sshed in again.

### Testing It All Out

After all of this, I plugged the Pi Router into the switch with all of my clustered Pis. I turned the switch on and off again to force them all to try and reacquire a new DHCP lease and then ran the following on the Pi Router to see if any DHCP leases were granted:
```
cat /var/lib/misc/dnsmasq.leases
```
Yep, they were all there! Since I added expand-hosts to the dnsmasq.conf configuration, I was able to ssh on to them by hostname like this:
```
ssh pi@kube-node1
```
I executed a few curl commands (e.g. curl http://example.com) to confirm that they had internet access and everything worked wonderfully! Additionally, from within blathers I was able to ssh pi@nook to confirm that the clustered Pis could communicate with each other.

### Set Up Keyless SSH Access Between Hosts

On each node (master and workers), generate a private/public key pair:
```
ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N ""
```
For example, after generating a private/public key pair on the master node,
transfer the public key to a worker node:
```
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@kube-node1
```
Then test it by logging into `kube-node1` from the master node.


Next we are going to remove the ability to SSH in with just your password.
```
vim /etc/ssh/sshd_config
```
Find this in the file:
```
PasswordAuthentication yes
```
Change it to:
```
PasswordAuthentication no
```

### Disable WIFI on nodes

#### Raspbian

Open the `/boot/config.txt` file and find the following line:
```
# Additional overlays and parameters are documented /boot/overlays/README
```

And add this line under it:
```
dtoverlay=disable-wifi
```
You can also add:
```
dtoverlay=disable-bt
```
to disable bluetooth.

### Memory cgroups

We need to enable container features in the kernel in order to run containers.

#### Ubuntu
for Ubuntu 19.10, we need to manually enable memory cgroups. To achieve this, execute the following command:

```
sudo sed -i '$ s/$/ cgroup_enable=memory cgroup_memory=1/' /boot/firmware/nobtcmd.txt
```
#### Raspbian
for Raspbian, we need to manually enable memory cgroups. To achieve this, execute the following command:

```
sudo sed -i '$ s/$/ cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1/' /boot/cmdline.txt
```


### Install Docker on master node (not required with k3s)

```
curl -sSL get.docker.com | sh
```

### Install k3s on the master node

```
curl -sfL https://get.k3s.io | sh -
```

Now check if all is well, you should see something like the following:
```
sudo kubectl version

Client Version: version.Info{Major:"1", Minor:"17", GitVersion:"v1.17.4+k3s1", GitCommit:"3eee8ac3a1cf0a216c8a660571329d4bda3bdf77", GitTreeState:"clean", BuildDate:"2020-03-25T16:13:30Z", GoVersion:"go1.13.8", Compiler:"gc", Platform:"linux/arm64"}
Server Version: version.Info{Major:"1", Minor:"17", GitVersion:"v1.17.4+k3s1", GitCommit:"3eee8ac3a1cf0a216c8a660571329d4bda3bdf77", GitTreeState:"clean", BuildDate:"2020-03-25T16:13:30Z", GoVersion:"go1.13.8", Compiler:"gc", Platform:"linux/arm64"}
```

```
sudo systemctl status k3s
```

#### Options

The first line specifies in which mode we would like to write the k3s configuration (required when not running commands as root) and the second line actually says k3s not to deploy its default load balancer named servicelb and proxy traefik, instead we will install manually metalb as load balancer and nginx as proxy which are in my opinion better and more widely used.

```
$ export K3S_KUBECONFIG_MODE="644"
$ export INSTALL_K3S_EXEC=" --no-deploy servicelb --no-deploy traefik"
```

### Join worker nodes
Now we can join worker nodes to the cluster.

First, we need to get the value for `K3S_TOKEN` from the master (control plane)
node and then we
```
export K3S_TOKEN=`sudo cat /var/lib/rancher/k3s/server/node-token`
```

Then, from the master node, execute:
```
ssh pi@kube-node1 "curl -sfL http://get.k3s.io | K3S_URL=https://10.0.0.1:6443 K3S_TOKEN=$K3S_TOKEN sh -"
```
where `10.0.0.1` is the IP address of the master node.

### Connect remotely to the cluster

If you don't want to connect via SSH to a node every time you need to query your cluster, it is possible to install `kubectl` (k8s command line tool) on your local machine and control remotely your cluster.

Install `kubectl` following these [instructions](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Copy the k3s config file `/etc/rancher/k3s/k3s.yaml` located on the master node to our local machine into `~/.kube/config`.
Inside the newly created `~/.kube/config` file, change the line
`server: https://127.0.0.1:6443` to `server: https://192.168.1.181:6443`,
where `192.168.1.181` is the IP address of the master node

Try using `kubectl` from your local machine:
```
kubectl get nodes -o wide
```

For security purpose, limit the file's read/write permissions to just yourself:
```
chmod 600 ~/.kube/config
```

### Install Helm

Next, we install [Helm](https://helm.sh/)
using a [script](https://helm.sh/docs/intro/install/#from-script):
```
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

### Redirecting audio output

The sound will output to HDMI by default if both HDMI and the 3.5mm audio jack are connected. You can, however, force the system to output to a particular device using raspi-config.

For those of you who want to know how to do this without raspi-config:
For HDMI

sudo amixer cset numid=3 2

For 3.5mm audio jack

sudo amixer cset numid=3 1


### Additional software

#### Web browser

epiphany-browser

#### Node.js

To install Node.js v14.x, execute these
[commands](https://github.com/nodesource/distributions/blob/master/README.md#deb):
```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```
