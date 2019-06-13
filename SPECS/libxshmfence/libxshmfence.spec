Summary:	X11 libxshmfence runtime library.
Name:		libxshmfence
Version:	1.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libxshmfence=a2ebe90e5595afca4db93a4359732af43b2b8c69
Patch0:         memfd_create.patch
BuildRequires:	pkg-config util-macros proto
Provides:	pkgconfig(xshmfence)
%description
The X11 Shared Memory fences library.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pkg-config util-macros proto
%description	devel
It contains the libraries and header files to create applications

%prep
%setup -q
%patch0 -p1
%build
autoreconf -fiv
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2-1
-	initial version
