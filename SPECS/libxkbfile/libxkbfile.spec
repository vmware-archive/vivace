Summary:	X11 libxkbfile runtime library.
Name:		libxkbfile
Version:	1.1.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libxkbfile=487f314b6dbc17e93d0fe1e3741392156a9ca895
BuildRequires:	libX11-devel
Requires:	libX11
Provides:	pkgconfig(xkbfile)
%description
The X11 libxkbfile runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libX11-devel
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.a
%{_libdir}/*.la
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.1.0-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.8-1
- initial version
