Summary:	X11 XFIXES extension.
Name:		libXfixes
Version:	5.0.1
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXfixes=e14fa072bd70b30eef47391cac637bdb4de9e8a3
BuildRequires:	libXext-devel
Requires:	libXext
Provides:	pkgconfig(xfixes)
%description
The X11 Xfixes extension.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXext-devel
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
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 5.0.1-1
-	initial version
