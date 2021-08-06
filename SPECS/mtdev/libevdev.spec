Summary:	The Libevdev package contains common functions for Xorg input drivers.
Name:		libevdev
Version:	1.11.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
%define sha1 libevdev=a2358a22365f9537f4ed1571efe134b5a22979f7
BuildRequires:	python3-libs python3-devel
%description
The Libevdev package contains common functions for Xorg input drivers.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
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
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_libdir}/*.la
%{_mandir}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.11.0-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4.2-1
- initial version
