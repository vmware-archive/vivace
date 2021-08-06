Summary:	X11 libXtst runtime library.
Name:		libXtst
Version:	1.2.3
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXtst=27d004db631bee3a82155d3caf961d9584207d36
BuildRequires:	libXi-devel
Requires:	libXi
%description
The X11 libXtst runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXi-devel
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
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.2.3-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.2-1
- initial version
