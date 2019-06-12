Summary:	Mesa OpenGL Utility library.
Name:		glu
Version:	9.0.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.mesa3d.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{name}/%{name}-%{version}.tar.bz2
%define sha1 glu=c2814bbaf1e60e28a75ec80f4646047c0da742bd
BuildRequires:	mesa-devel
Requires:	mesa
%description
This package provides the Mesa OpenGL Utility library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	mesa-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}	\
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%exclude %{_includedir}/*
%files devel
%defattr(-,root,root)
%{_libdir}/*.la
%{_includedir}/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 9.0.0-1
-	initial version
