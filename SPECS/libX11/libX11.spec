Summary:	Core X11 protocol client library.
Name:		libX11
Version:	1.6.3
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libX11-1.6.3.tar.bz2
BuildRequires:	pkg-config util-macros fontconfig-devel libxcb-devel xtrans
Requires:	fontconfig libxcb
Provides:	pkgconfig(x11)
%description
Core X11 protocol client library.
%package	devel
Summary:	Header and development files for libX11
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}
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
%{_datadir}/*
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.6.3-1
-	initial version
