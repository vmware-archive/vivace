Summary:	X11 ICE runtime library.
Name:		libICE
Version:	1.0.10
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libICE=5b5eb125d4f43a3ab8153b0f850963ee6c982c24
BuildRequires:	xtrans
Provides:	pkgconfig(ice)
%description
The X11 Inter-Client Exchange runtime library.
%package	devel
Summary:	Header and development files
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.0.10-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
- initial version
