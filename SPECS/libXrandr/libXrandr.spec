Summary:	X11 Xrandr runtime library.
Name:		libXrandr
Version:	1.5.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXrandr=7a1f6df239341b76fd59ebbe101d6f180adb43bb
BuildRequires:	libXrender-devel libXext-devel
Requires:	libXrender libXext
%description
The X11 libXrandr library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXrender-devel libXext-devel
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
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.5.2-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4.2-1
- initial version
