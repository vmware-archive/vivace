Summary:	Core X11 protocol client library.
Name:		libX11
Version:	1.7.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libX11-%{version}.tar.bz2
%define sha1 libX11=ff503c816f1e812070ac0e1841bc3634c3b370b6
BuildRequires:	xtrans
Requires:	xfontconfig libxcb
Provides:	pkgconfig(x11)
%description
Core X11 protocol client library.
%package	devel
Summary:	Header and development files for libX11
Requires:	%{name} = %{version}
Requires:	xtrans
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
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_datadir}/X11/
%{_mandir}/man5/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
 %{_libdir}/pkgconfig/
%{_docdir}/
%{_mandir}/man3/
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.7.2-1
- Version update
* Wed Jul 03 2019 Alexey Makhalov <amakhalov@vmware.com> 1.6.3-3
- Locale support
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.3-2
- Updated build requires & requires to build with Photon 2.0
* Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.6.3-1
- initial version
