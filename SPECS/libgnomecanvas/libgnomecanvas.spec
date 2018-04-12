Summary:	The libgnomeui package contains GNOME canvas library
Name:		libgnomecanvas
Version:	2.30.3
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
%define sha1 libgnomecanvas=a5b07f33c44c460434dd0dad457d2fffb8a1baf9
BuildRequires:	libart_lgpl-devel
Requires:	libart_lgpl
%description
The libgnomecanvas package contains the GNOME canvas library. It is an engine for structured graphics and one of the essential GNOME libraries.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libart_lgpl-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.30.3-1
-	initial version
