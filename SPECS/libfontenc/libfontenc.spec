Summary:	X11 Fontenc runtime library.
Name:		libfontenc
Version:	1.1.2
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libfontenc=2beffa0e9260c479b49f90f789318c7f9db2d41d
BuildRequires:	pkg-config proto zlib-devel
Requires:	zlib
Provides:	pkgconfig(fontenc)
%description
The X11 Fontenc runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	proto zlib-devel
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
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.2-1
-	initial version
