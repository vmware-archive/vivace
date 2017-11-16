Summary:	Core X11 protocol client library.
Name:		libX11
Version:	1.6.3
Release:	2	
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/libX11-1.6.3.tar.bz2
%define sha1 libX11=6f2aadf8346ee00b7419bd338461c6986e274733
BuildRequires:	xtrans-devel
Requires:	xfontconfig libxcb
Provides:	pkgconfig(x11)
%description
Core X11 protocol client library.
%package	devel
Summary:	Header and development files for libX11
Requires:	%{name} = %{version}
Requires:	xtrans-devel
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
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.3-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.6.3-1
-	initial version
