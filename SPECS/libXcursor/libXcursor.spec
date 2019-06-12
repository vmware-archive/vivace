Summary:	X11 Cursor management library.
Name:		libXcursor
Version:	1.1.14
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXcursor=89870756758439f9216ddf5f2d3dca56570fc6b7
BuildRequires:	libXfixes-devel libXrender-devel
Requires:	libXfixes libXrender
%description
The X11 Cursor management library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXfixes-devel libXrender-devel
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
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.14-1
-	initial version
