Network Access Unlocked Toolkit (NAU Tools)
====

NauTools is a open source project initially built to bypass 802.1X port security with a easy to use interaction 
interface. This tool is an active device in the middle tool, built on Raspberry Pi 3B+ and Kali that has the capability 
of performing attacks using tools like Metasploit and Responder and open a side channel (over Wi-Fi) for an attacker to 
actively test utilizing their own machine.

Setup
-----
The setup of this utility is pretty simple. Just run `nau_setup.sh` and then run `pip3 install -r requirements.txt`

Cleanup
-------

Reboot might be required at the end of this step.

License
-------
Copyright Tanoy Bose 2019

Wiki and Usage Guide
--------------------
The NAU Toolkit has various four main interfaces.
```
(nau)# 
```

### nau_configure

These are a set of required pre-configurations for the tool to work optimally.

```
(nau_configure)# 
```
### nau_tap
```
(nau_tap)#
```

### nau_rules
```
(nau_rules)# 
```

### nau_inject
The inject module has two basic usages

#### inject_protocol
```
(nau_inject)# inject_protocol <smb|crackmapexec|rdp|responder>
```

#### inject_sshpivot
```
(nau_inject)# inject_sshpivot lport rhost rport username password
```


To Do
-------
[ ] More documentation

[ ] Research and bypass 802.1AE bypass

[ ] Code cleanup
