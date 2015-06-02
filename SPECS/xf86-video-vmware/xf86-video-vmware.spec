Summary:	The Xorg VMware Driver package contains the X.Org Video Driver for VMware SVGA virtual video cards. 
Name:		xf86-video-vmware
Version:	13.1.0
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:	xorg-server-devel pixman-devel libpciaccess-devel libX11-devel libXext-devel libdrm-devel mesa-devel
Requires:	xorg-server pixman libpciaccess libX11 libXext libdrm mesa
%description
The Xorg VMware Driver package contains the X.Org Video Driver for VMware SVGA virtual video cards. 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 13.1.0-1
-	initial version
