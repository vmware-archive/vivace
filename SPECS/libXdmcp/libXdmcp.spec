Summary:	X Display Manager Control Protocol library.
Name:		libXdmcp
Version:	1.1.3
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXdmcp=0a8f8a274f829331efb1e8e2027c38631b204dd0
BuildRequires:	xorgproto
%description
The libXdmcp package contains a library implementing the X Display Manager Control Protocol. This is useful for allowing clients to interact with the X Display Manager.
%package	devel
Summary:	Header and development files for libXdmcp
Requires:	%{name} = %{version}
Requires:	xorgproto
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_docdir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.1.3-1
- Version update
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.2-1
- initial version
