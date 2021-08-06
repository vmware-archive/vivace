Summary:	X11 Cursor management library.
Name:		libXcursor
Version:	1.2.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXcursor=cca0b34955d3c2f657f05a2a2c40f75353ddd912
BuildRequires:	libXfixes-devel libXrender-devel
Requires:	libXfixes libXrender
%description
The X11 Cursor management library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXfixes-devel libXrender-devel
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
%{_datadir}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.2.0-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.14-1
- initial version
