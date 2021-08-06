Summary:	library for common extensions to the X11 protocol.
Name:		libXext
Version:	1.3.4
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libXext-%{version}.tar.bz2
%define sha1 libXext=14e2451162e8766173b5b14c73e94a22b1fcab55
BuildRequires:	libX11-devel
Requires:	libX11
Provides:	pkgconfig(xext)
%description
Core X11 protocol client library.
%package	devel
Summary:	Header and development files for libXext
Requires:	%{name} = %{version}
Requires:	libX11-devel
%description	devel
libXext - library for common extensions to the X11 protocol.
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.3.4-1
- Version update
* Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.3-1
- initial version
