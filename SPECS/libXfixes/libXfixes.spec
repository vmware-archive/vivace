Summary:	X11 XFIXES extension.
Name:		libXfixes
Version:	6.0.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXfixes=5b114fc4def6ef3a516f1c06741a595c16f668e1
BuildRequires:	libXext-devel
Requires:	libXext
Provides:	pkgconfig(xfixes)
%description
The X11 Xfixes extension.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXext-devel
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
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 6.0.0-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 5.0.1-1
- initial version
