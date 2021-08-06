Summary:	The Xorg protocol headers.
Name:		xorgproto
Version:	2021.4
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
BuildArch:      noarch
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://xorg.freedesktop.org/archive/individual/proto/%{name}-%{version}.tar.bz2
%define sha1 xorgproto=dec30f11deefa1e1655db24f4dc42fbafad368fd
BuildRequires:	pkg-config
BuildRequires:	util-macros
Provides:	pkgconfig(xproto)
%description
The Xorg protocol headers provide the header files required to build the system, and to allow other applications to build against the installed X Window system.
%prep
%setup -q

%build
%configure
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 2021.4-1
- Renamed to xorgproto
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 7.7-2
- Updated xproto, randrproto
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
- initial version
