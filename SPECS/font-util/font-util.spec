Summary:	X11 font utilities.
Name:		font-util
Version:	1.3.1
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/font/font-util-1.3.1.tar.bz2
%define sha1 font-util=0b16add3637c64b0bbaf1dd223b71b0421100c20
%description
The Xorg font utilities.
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
%exclude %{_libdir}/debug
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.1-1
-	initial version
