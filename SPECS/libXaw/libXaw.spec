Summary:	X11 Athena Widget library.
Name:		libXaw
Version:	1.0.12
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXaw=6919476379accaf21f2331004e5cfa7939a6786b
BuildRequires:	libXmu-devel libXpm-devel
Requires:	libXmu libXpm
%description
The Athena Widget based on Xt library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXmu-devel libXpm-devel
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
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.13-1
-	initial version
