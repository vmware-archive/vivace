Summary:	Multitouch Protocol Translation Library
Name:		mtdev
Version:	1.1.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://bitmath.org/code/%{name}/%{name}-%{version}.tar.bz2
%define sha1 mtdev=1459f8b977b615c8e569b53ba119c980af2fa688
%description
Multitouch Protocol Translation Library which is used to transform all variants of kernel MT (Multitouch) events to the slotted type B protocol. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.la
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.1.6-1
- initial version
