Summary:	Cairo is a 2D graphics library with support for multiple output devices.
Name:		xcairo
Version:	1.17.4
Release:	1%{?dist}
License:	LGPLv2 or MPLv1.1
URL:		http://cairographics.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://cairographics.org/releases/cairo-%{version}.tar.xz
%define sha1 cairo=68712ae1039b114347be3b7200bc1c901d47a636
BuildRequires:	libpng-devel pixman-devel libXrender-devel libdrm-devel glib-devel
Requires:	libpng pixman libXrender libdrm glib
Obsoletes:	cairo
%description
Cairo is a 2D graphics library with support for multiple output devices.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libpng-devel pixman-devel libdrm-devel libXrender-devel glib-devel
Obsoletes:	cairo-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup -n cairo-%{version}
%build
%configure --disable-static	\
	    --enable-tee
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/cairo
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/pkgconfig
%{_datadir}/*
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 1.17.4-1
- Version update
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.14.2-1
- initial version
