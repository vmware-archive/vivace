Summary:	X11 Damage extension.
Name:		libXdamage
Version:	1.1.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	libXfixes-devel
Requires:	libXfixes
Provides:	pkgconfig(xdamage)
%description
The X11 Damage extension.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXfixes-devel
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
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.4-1
-	initial version
