%global security_hardening nonow
Summary:	X.Org Video Driver for NVidia Cards
Name:		xf86-video-nouveau
Version:	1.0.11
Release:	1
License:	MIT 
URL:		http://www.x.org/wiki/radeon/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/xf86-video-nouveau-1.0.11.tar.bz2
%define sha1 xf86-video-nouveau=ea94037f8dd05c223dd89c79a2e655ff58425892
BuildRequires:	libxcb-devel libdrm-devel xorg-server-devel pixman-devel
Requires:		libxcb libdrm xorg-server pixman

%description
The Xorg Nouveau Driver package contains the X.Org Video Driver for NVidia Cards including RIVA TNT, RIVA TNT2, GeForce 256, QUADRO, GeForce2, QUADRO2, GeForce3, QUADRO DDC, nForce, nForce2, GeForce4, QUADRO4, GeForce FX, QUADRO FX, GeForce 6XXX and GeForce 7xxx chipsets. 

%prep
%setup -q 

%build
./configure $XORG_CONFIG --prefix=%{_prefix} &&
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*

%changelog
*	Mon Aug 03 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.0.11-1
-	initial version
