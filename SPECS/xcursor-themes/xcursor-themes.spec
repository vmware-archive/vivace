%define debug_package %{nil}
Summary:	redglass and whiteglass animated cursor themes.
Name:		xcursor-themes
Version:	1.0.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
%define sha1 xcursor-themes=fb22702607810607ab1b9cde1c9a033430c5f037
BuildRequires:	xorg-applications libXcursor-devel
Requires:	libXcursor
%description
The xcursor-themes package contains the redglass and whiteglass animated cursor themes.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.4-1
-	initial version
