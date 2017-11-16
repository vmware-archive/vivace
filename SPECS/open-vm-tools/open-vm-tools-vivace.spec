Summary:	Usermode tools for VmWare virts
Name:		open-vm-tools-vivace
Version:	10.0.5
Release:	2	
License:	LGPLv2+
URL:		https://github.com/vmware/open-vm-tools/archive/stable-9.10.x.zip
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:    http://downloads.sourceforge.net/project/open-vm-tools/open-vm-tools-%{version}.tar.gz
%define sha1 open-vm-tools=9d29a17cce539b032317d0a8c55977666daa137e
Patch0:		Fix-build-failure-with-GCC-6.patch
Patch1:		include-sys-macros-directly.patch
BuildRequires: 	xerces-c-devel
BuildRequires: 	xml-security-c-devel
BuildRequires: 	libdnet-devel
BuildRequires: 	libmspack-devel
BuildRequires:	Linux-PAM-devel
BuildRequires:	openssl-devel
BuildRequires:	procps-ng-devel
BuildRequires:	gtk2-devel
BuildRequires:  systemd-devel
BuildRequires:	gtkmm-devel
BuildRequires:	gtkmm3-devel fuse-devel libXrandr-devel libXtst-devel
Requires:		gtkmm3 gtkmm fuse libXrandr libXtst
Requires:		xerces-c
Requires:		systemd
Requires:		libdnet
Requires:		Linux-PAM
Requires:		libmspack
Requires:		xml-security-c
Requires:		openssl
Requires:		gtk2
Obsoletes:		open-vm-tools
%description
VmWare virtualization user mode tools
%prep
%setup -qn open-vm-tools-%{version}
%patch0 -p1
%patch1 -p1

%build
sed -i 's#/var/run/vmblock#/run/vmblock#' lib/include/vmblock.h
touch ChangeLog
autoreconf -i
export CFLAGS="%{optflags} -DVMX86_DEVEL=1"
export CXXFLAGS="-g -O2 -std=c++11 -Dvmblock_fuse"
sh ./configure --prefix=/usr --sysconfdir=/etc --without-kernel-modules --without-icu --disable-static 
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
Requires=vgauthd.service
After=cloud-final.service

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

#vgauthd service
cat >> %{buildroot}/lib/systemd/system/vgauthd.service <<-EOF
[Unit]
Description=VGAuth Service for open-vm-tools
Documentation=http://github.com/vmware/open-vm-tools
ConditionVirtualization=vmware
PartOf=vmtoolsd.service

[Service]
ExecStart=/usr/bin/VGAuthService ls -s
TimeoutStopSec=5

[Install]
RequiredBy=vmtoolsd.service
EOF

make DESTDIR=%{buildroot} install
rm -f %{buildroot}/sbin/mount.vmhgfs
chmod -x %{buildroot}/etc/pam.d/vmtoolsd

# Move vm-support to /usr/bin
mv %{buildroot}%{_sysconfdir}/vmware-tools/vm-support %{buildroot}%{_bindir}

%post
/sbin/ldconfig
systemctl enable vmware-vmblock-fuse.service
%systemd_post vgauthd.service vmtoolsd.service vmware-vmblock-fuse.service mnt-hgfs.mount
/bin/systemctl enable mnt-hgfs.mount
/sbin/depmod

%preun
%systemd_preun vmtoolsd.service vgauthd.service vmware-vmblock-fuse.service mnt-hgfs.mount
/bin/systemctl disable mnt-hgfs.mount

# Tell VMware that open-vm-tools is being uninstalled
if [ "$1" = "0" -a                      \
     -e %{_bindir}/vmware-checkvm -a    \
     -e %{_bindir}/vmware-rpctool ] &&  \
     %{_bindir}/vmware-checkvm &> /dev/null; then
   %{_bindir}/vmware-rpctool 'tools.set.version 0' &> /dev/null || /bin/true
fi

%postun	
/sbin/ldconfig
%systemd_postun_with_restart vmtoolsd.service vgauthd.service vmware-vmblock-fuse.service mnt-hgfs.mount

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
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 10.0.5-2
-	Updated build requires & requires to build with Photon 2.0
*	Fri Aug 26 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 10.0.5-1
-	Upgraded to version 10.0.5, using the original naming conventions for release.
	Updated the spec to match Photon version. 
*   Wed Aug 12 2015 Alexey Makhalov <amakhalov@vmware.com> 10.0.0-256
-   Update version to 10.0.0.
*	Tue Apr 21 2015 Divya Thaluru <dthaluru@vmware.com> 9.10.0-2
	Added open-vm-tools-stderr_r-fix upstream patch and removed glibc patch.
*	Thu Nov 06 2014 Sharath George <sharathg@vmware.com> 9.10.0-1
	Initial version
