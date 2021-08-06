%global security_hardening nonow
Summary:	The Xorg Server
Name:		xorg-server
Version:	1.20.13
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		User Interface/X System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/xserver/%{name}-%{version}.tar.xz
%define sha1 xorg-server=4a846a4affeb3863e23c1d57a3b1bca4374a2ddb
BuildRequires:	xkeyboard-config xorg-fonts pixman-devel openssl-devel mesa-devel libxkbfile-devel libepoxy-devel xcb-util-keysyms-devel expat-devel libXfont2-devel
Requires:	xkeyboard-config xorg-fonts pixman openssl mesa libxkbfile libepoxy xcb-util-keysyms expat libXfont2

%description
The Xorg Server is the core of the X Window system.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pixman-devel openssl-devel mesa-devel libxkbfile-devel libepoxy-devel xcb-util-keysyms-devel libXfont2-devel
%description	devel
It contains the libraries and header files to create applications

%prep
%setup -q

%build
#make some fixes required by glibc-2.28:
sed -i '/unistd/a #include <sys/sysmacros.h>' hw/xfree86/common/xf86Xinput.c
sed -i '/stat\.h/a #include <sys/sysmacros.h>' hw/xfree86/os-support/linux/lnx_init.c
sed -i '/stat\.h/a #include <sys/sysmacros.h>' hw/xfree86/xorg-wrapper.c

%configure \
		--enable-glamor          \
		--enable-install-setuid  \
		--enable-suid-wrapper    \
		--disable-systemd-logind \
		--with-xkb-output=/var/lib/xkb
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mkdir -pv %{buildroot}/etc/X11/xorg.conf.d &&
mkdir -pv %{buildroot}/etc/sysconfig &&
cat >> %{buildroot}/etc/sysconfig/createfiles << "EOF"
/tmp/.ICE-unix dir 1777 root root
/tmp/.X11-unix dir 1777 root root
EOF
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig
%exclude %{_prefix}/src/
%{_localstatedir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.20.13-1
- Version update
* Thu Feb 13 2020 Alexey Makhalov <amakhalov@vmware.com> 1.19.1-2
- Added 10-evdev.conf conf file.
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 1.19.1-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.17.1-1
- Initial version
