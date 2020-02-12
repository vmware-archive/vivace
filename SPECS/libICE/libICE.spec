Summary:	X11 ICE runtime library.
Name:		libICE
Version:	1.0.9
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libICE=3c3a857a117ce48a1947a16860056e77cd494fdf
BuildRequires:	xtrans
Requires:	proto
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
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
-	initial version
