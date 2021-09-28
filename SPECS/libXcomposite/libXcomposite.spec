Summary:	X11 Composite Extension library.
Name:		libXcomposite
Version:	0.4.5
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXcomposite=902631efb55a798c81086e5ff90b60349839db40
BuildRequires:	libXfixes-devel
Requires:	libXfixes
%description
The X11 Composite Extension library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXfixes-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
%configure
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%exclude %{_libdir}/pkgconfig
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig
%{_datadir}/*
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 0.4.5-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.4-1
- initial version
