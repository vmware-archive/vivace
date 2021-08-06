Summary:	m4 macros used by all of the Xorg packages.
Name:		util-macros
Version:	1.19.3
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
BuildArch:      noarch
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/util/%{name}-%{version}.tar.bz2
%define sha1 util-macros=4097f75e327b9579d1bd657fa8b01b55238ad8f5
%description
The util-macros package contains the m4 macros used by all of the Xorg packages.
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
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.19.3-1
- Version update
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.19.0-1
- initial version
