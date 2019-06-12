%global security_hardening nonow
Summary:	The Xorg VMware Driver package contains the X.Org Video Driver for VMware SVGA virtual video cards. 
Name:		xf86-video-vmware
Version:	13.1.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-video-vmware=3af1d56a9a75b5f6e10a78db2ce155ec65498802
BuildRequires:	xorg-server-devel
Requires:	xorg-server
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
