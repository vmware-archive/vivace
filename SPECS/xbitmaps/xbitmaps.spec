Summary:	bitmap images for X applications.
Name:		xbitmaps
Version:	1.1.1
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
BuildArchitectures: noarch
BuildRequires:	util-macros
%description
The xbitmaps package contains bitmap images used by multiple applications for X.
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
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.1-1
-	initial version
