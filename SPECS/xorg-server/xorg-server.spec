Summary:	The Xorg Server
Name:		xorg-server
Version:	1.17.1
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		User Interface/X System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/xserver/%{name}-%{version}.tar.bz2
BuildRequires:	pkg-config util-macros proto xkeyboard-config xorg-fonts pixman-devel openssl-devel libdrm-devel libX11-devel libxshmfence-devel mesa-devel libXext-devel libXdmcp-devel xtrans libxkbfile-devel libXfont-devel libpciaccess-devel libepoxy-devel libXau-devel libXdamage-devel libXfixes-devel libXxf86vm-devel xcb-util-keysyms-devel libxcb-devel
Requires:	xkeyboard-config xorg-fonts pixman openssl libdrm libX11 libxshmfence mesa libXext libXdmcp libxkbfile libXfont libpciaccess libepoxy libXau libXdamage libXfixes libXxf86vm xcb-util-keysyms libxcb
%description
The Xorg Server is the core of the X Window system.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}		 \
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
%{_prefix}/*
%{_localstatedir}/*
%exclude %{_libdir}/debug/
%exclude %{_prefix}/src/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.17.1-1
-	initial version
