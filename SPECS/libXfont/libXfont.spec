Summary:	X11 Xfont runtime library.
Name:		libXfont
Version:	1.5.1
Release:	2	
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXfont=e63a354de5dc2d8cba08d50add1519471412a618
BuildRequires:	libfontenc-devel xfreetype2-devel xtrans-devel
Requires:	libfontenc xfreetype2
%description
The X11 Xfont runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libfontenc-devel xfreetype2-devel xtrans-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --disable-devel-docs
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%exclude %{_libdir}/pkgconfig/*.pc
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.5.1-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.5.1-1
-	initial version
