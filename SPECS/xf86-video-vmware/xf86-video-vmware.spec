%global security_hardening nonow
Summary:	The Xorg VMware Driver package contains the X.Org Video Driver for VMware SVGA virtual video cards. 
Name:		xf86-video-vmware
Version:	13.3.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-video-vmware=f01335fe6bdb507e749571bfcd69163aed97312a
BuildRequires:	xorg-server-devel
Requires:	xorg-server
%description
The Xorg VMware Driver package contains the X.Org Video Driver for VMware SVGA virtual video cards. 
%prep
%autosetup
%build
%configure
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 13.3.0-1
- Version update
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 13.1.0-1
- initial version
