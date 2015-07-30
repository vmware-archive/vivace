%global security_hardening nonow
Summary:	Multimedia metadata reading/writing library for popular formats
Name:		xf86-video-intel
Version:	2.99.917 
Release:	1
License:	MIT 
URL:		http://www.x.org/wiki/IntelGraphicsDriver/
Group:		Development/Languages/Mono
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/xf86-video-intel-2.99.917.tar.bz2
%define sha1 xf86-video-intel=9af9ded7a29026c211e5eb50a547e3e33976301d
BuildRequires:	libxcb-devel libdrm-devel xorg-server-devel pixman-devel
Requires:	libxcb libdrm xorg-server pixman

%description
The Xorg Intel Driver package contains the X.Org Video Driver for Intel integrated video cards including 8xx, 9xx, Gxx, Qxx and HD graphics processors (SandyBridge, IvyBridge and Haswell). 

%prep
%setup -q 

%build
./configure $XORG_CONFIG --prefix=%{_prefix} --enable-kms-only --enable-uxa &&
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*
/usr/libexec

%changelog
*	Tue Jul 28 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.99.917-1
-	initial version
