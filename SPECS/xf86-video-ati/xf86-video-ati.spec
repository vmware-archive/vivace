%global security_hardening nonow
Summary:	X.Org Video Driver for ATI Radeon video cards
Name:		xf86-video-ati
Version:	7.5.0
Release:	1
License:	MIT 
URL:		http://www.x.org/wiki/radeon/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/xf86-video-ati-7.5.0.tar.bz2
%define sha1 xf86-video-ati=9cfdaf0bd4a46781b5082c75ca546fc832598124
BuildRequires:	libxcb-devel libdrm-devel xorg-server-devel pixman-devel
Requires:		libxcb libdrm xorg-server pixman

%description
The Xorg ATI Driver package contains the X.Org Video Driver for ATI Radeon video cards including all chipsets ranging from R100 to R900 and the newer RAxx chipsets. 

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
*	Mon Aug 03 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 7.5.0-1
-	initial version
