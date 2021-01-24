# cloud-init

## Resources

* [An Introduction to Cloud-Config Scripting](https://www.digitalocean.com/community/tutorials/an-introduction-to-cloud-config-scripting)
* [How To Use Cloud-Config For Your Initial Server Setup](https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup)
* [Tutorial - How to use cloud-init to customize a Linux virtual machine in Azure on first boot](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-automate-vm-deployment)

## Logs and co.

* /var/log/cloud-init-output.log
* /var/lib/cloud/instance/scripts

## Files

### `meta-data`

```yamls
instance-id: iid-local01;
local-hostname: node01
```

### `user-data`



## Modules

### `runcmd`

```yaml
runcmd:
- [ wget,"https://s3.amazonaws.com/demo-ssm/init.sh", -O, "/tmp/init.sh" ]
- [ bash, /tmp/init.sh ]
```

### `write_files`

```yaml
write_files:
- encoding: base64
  content: bmV0d29yazoKIHZlcnNpb246IDIKIGV0aGVybmV0czoKICAgZW5zMTkyOgogICAgYWRkcmVzc2VzOiBbMTkyLjE2OC4xMTEuMTExLzI0XQogICAgZ2F0ZXdheTQ6IDE5Mi4xNjguMTExLjEK
  path: /etc/netplan/50-cloud-init.yaml
runcmd:
- netplan apply
```

The base64 encoded `write_files` part above corresponds to:

```yaml
network:
  version: 2
  ethernets:
    ens192:
      addresses: [192.168.111.111/24]
      gateway4: 192.168.111.1
```


