Summary:	bitmap images for X applications.
Name:		xbitmaps
Version:	1.1.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
%define sha1 xbitmaps=1cb0e485a66280e9a64b48426140b8a0de9cf169
BuildArch:      noarch
BuildRequires:	util-macros
%description
The xbitmaps package contains bitmap images used by multiple applications for X.
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
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.1.2-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.1-1
- initial version
