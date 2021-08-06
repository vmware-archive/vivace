Summary:	X11 Xrender runtime library.
Name:		libXrender
Version:	0.9.10
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXrender=d55106de9260c2377c19d271d9b677744a6c7e81
BuildRequires:	libX11-devel
Requires:	libX11
Provides:	pkgconfig(xrender)
%description
The X11 Renderer library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libX11-devel
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
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 0.9.10-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 0.9.8-1
- initial version
