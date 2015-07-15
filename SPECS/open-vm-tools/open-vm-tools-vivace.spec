Summary:	Usermode tools for VmWare virts
Name:		open-vm-tools-vivace
Version:	9.10.0
Release:	1
License:	LGPLv2+
URL:		https://github.com/vmware/open-vm-tools/archive/stable-9.10.x.zip
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/project/open-vm-tools/open-vm-tools/stable-9.10.0/open-vm-tools-%{version}.tar.gz
%define sha1 open-vm-tools=958c40c8038d52947680444f507f693825d358be
Patch0:		open-vm-tools-strerror_r-fix.patch
Patch1:		open-vm-tools-service-link.patch
BuildRequires: 	xerces-c-devel
BuildRequires: 	xml-security-c-devel
BuildRequires: 	libdnet
BuildRequires: 	libmspack
BuildRequires:	Linux-PAM
BuildRequires:	openssl-devel
BuildRequires:	procps-ng-devel
BuildRequires:	gtkmm-devel fuse-devel libXrandr-devel libXtst-devel
Requires:	gtkmm fuse libXrandr libXtst
Requires:	xerces-c
Requires:	libdnet
Requires:	libmspack
Requires:	xml-security-c
Requires:	openssl
%description
VmWare virtualization user mode tools
%prep
%setup -qn open-vm-tools-%{version}
%patch0 -p1
%patch1 -p1
%build
sed -i 's#/var/run/vmblock#/run/vmblock#' lib/include/vmblock.h
autoreconf -i
export CFLAGS="%{optflags} -DVMX86_DEVEL=1"
./configure --prefix=/usr --sysconfdir=/etc --without-kernel-modules --without-icu --disable-static
make %{?_smp_mflags}
%install

#collecting hacks to manually drop the vmhgfs module
install -vdm 755 %{buildroot}/lib/systemd/system

#stuff to enable vmtoolsd service
cat >> %{buildroot}/lib/systemd/system/vmtoolsd.service <<-EOF
[Unit]
Description=Service for virtual machines hosted on VMware
Documentation=http://open-vm-tools.sourceforge.net/about.php
ConditionVirtualization=vmware

[Service]
ExecStart=/usr/bin/vmtoolsd
TimeoutStopSec=5

[Install]
WantedBy=multi-user.target
EOF

# vmware-vmblock-fuse service
cat >> %{buildroot}/lib/systemd/system/vmware-vmblock-fuse.service <<-EOF
[Unit]
Description=Open Virtual Machine Tools (vmware-vmblock-fuse)
ConditionVirtualization=vmware

[Service]
Type=simple
ExecStartPre=/usr/bin/mkdir -p /run/vmblock-fuse
ExecStart=/usr/bin/vmware-vmblock-fuse -d -f -o subtype=vmware-vmblock,default_permissions,allow_other /run/vmblock-fuse

[Install]
WantedBy=multi-user.target
EOF

# Mount shared folders
cat >> %{buildroot}/lib/systemd/system/mnt-hgfs.mount <<-EOF
[Unit]
Description=Load VMware shared folders
ConditionPathExists=.host:/
ConditionVirtualization=vmware

[Mount]
What=.host:/
Where=/mnt/hgfs/
Type=vmhgfs
Options=defaults,noatime

[Install]
WantedBy=multi-user.target
EOF

make DESTDIR=%{buildroot} install
rm -f %{buildroot}/sbin/mount.vmhgfs
%post
/sbin/ldconfig
/bin/systemctl enable vmtoolsd
/bin/systemctl enable vmware-vmblock-fuse
/bin/systemctl enable mnt-hgfs.mount
/sbin/depmod

%preun
/bin/systemctl disable mnt-hgfs.mount
/bin/systemctl disable vmware-vmblock-fuse
/bin/systemctl disable vmtoolsd

%postun	-p /sbin/ldconfig
%files 
%defattr(-,root,root)
%{_libdir}/open-vm-tools/plugins/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_bindir}/*
%{_sysconfdir}/*
%{_datadir}/*
/lib/*
%{_sbindir}/*

%changelog
*	Tue Apr 21 2015 Divya Thaluru <dthaluru@vmware.com> 9.10.0-2
	Added open-vm-tools-stderr_r-fix upstream patch and removed glibc patch.
*	Thu Nov 06 2014 Sharath George <sharathg@vmware.com> 9.10.0-1
	Initial version
