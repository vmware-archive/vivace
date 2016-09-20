# Vivace

Vivace is a desktop environment for PhotonOS. It is a set of extra RPMs like xorg-server, lxde, firefox...

## Source code
```
git clone https://github.com/vmware/vivace.git
cd vivace
git submodule update --init
```

## Build
```
make packages
```

## Pre-built Vivace binaries
Pre-built binaries for Vivace are available through the following YUM repository that can be configured on your Photon deployment.

## Vivace YUM repository
Create the file "/etc/yum.repos.d/vivace.repo" with the following contents.
```
[vivace]
name=VMware Vivace 0.2(x86_64)
baseurl=https://vmware.bintray.com/vivace_release_0.2
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY
gpgcheck=0
enabled=1
skip_if_unavailable=True
```

## Install
Vivace provides RPM meta package with dependencies on all the Vivace's RPMs.
```
tdnf install vui
```
