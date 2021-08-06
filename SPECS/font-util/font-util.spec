Summary:	X11 font utilities.
Name:		font-util
Version:	1.3.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/font/font-util-%{version}.tar.bz2
%define sha1 font-util=1b36275c174b64a9c16da5c902c91546789a67ef
%description
The Xorg font utilities.
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%exclude %{_libdir}/debug
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.3.2-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.1-1
- initial version
