

### Raspbian version
You can check the release of Raspbian, simply reading the content of the os-release file.

```shell
cat /etc/os-release
```

### How to safely shutdown
Hold down both `Alt`+`PrintScreen`, and while holding those keys, hit the following keys in sequence, one at a time, with a few seconds pause between them:
`R E I S U B`
A handy mnemonic to remember that is, `R`eboot `E`ven `I`f `S`ystem `U`tterly `B`roken.
Substitute `O` for `B` to shutdown the system instead of rebooting (`O`=off, `B`=boot).

[Magic SysRq key](https://en.wikipedia.org/wiki/Magic_SysRq_key)
