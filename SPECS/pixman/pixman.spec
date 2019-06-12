Summary:	The Pixman package contains a library that provides low-level pixel manipulation features such as image compositing and trapezoid rasterization. 
Name:		pixman
Version:	0.32.6
Release:	1%{?dist}
License:	MIT
URL:		http://cairographics.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
%define sha1 pixman=8791343cbf6d99451f4d08e8209d6ac11bf96df2
Provides:	pkgconfig(pixman-1)
%description
The Pixman package contains a library that provides low-level pixel manipulation features such as image compositing and trapezoid rasterization. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 0.32.6-1
-	initial version
