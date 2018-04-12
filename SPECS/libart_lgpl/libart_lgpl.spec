Summary:	The libart is high-performance 2D graphics library
Name:		libart_lgpl
Version:	2.3.21
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
%define sha1 libart_lgpl=dbac185c65696381ef188de1f98b348b530e22f9
Patch0:		libart_lgpl-2.3.21-upstream_fixes-1.patch
BuildRequires:	libglade-devel
Requires:	libglade
%description
The libart_lgpl package contains the libart libraries. These are useful for high-performance 2D graphics.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libglade-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p1
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.3.21-1
-	initial version
