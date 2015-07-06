Summary:	X11 libXt runtime library.
Name:		libXt
Version:	1.1.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	libX11-devel libSM-devel
Requires:	libX11 libSM 
Provides:	pkgconfig(xt)
%description
The X11 Toolkit Intrinsics library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libX11-devel libSM-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --with-appdefaultdir=/etc/X11/app-defaults
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
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.4-1
-	initial version
