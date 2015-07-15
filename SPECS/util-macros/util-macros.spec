Summary:	m4 macros used by all of the Xorg packages.
Name:		util-macros
Version:	1.19.0
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
BuildArchitectures: noarch
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/util/%{name}-%{version}.tar.bz2
%define sha1 util-macros=00cfc636694000112924198e6b9e4d72f1601338
%description
The util-macros package contains the m4 macros used by all of the Xorg packages.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.19.0-1
-	initial version
