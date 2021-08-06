Summary:	X11 SM runtime library.
Name:		libSM
Version:	1.2.3
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libSM=437d7b13fa2eba325df3a106f177df46ccec6546
BuildRequires:	libICE-devel
Requires:	libICE
Provides:	pkgconfig(sm)
%description
The X11 Session Management runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libICE-devel
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
