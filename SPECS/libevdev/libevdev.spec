Summary:	The Libevdev package contains common functions for Xorg input drivers.
Name:		libevdev
Version:	1.4.2
Release:	1%{?dist}
License:	MIT
URL:		http://www.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
%define sha1 libevdev=97b48a26f492b3ecb7de47236404e8aadfbe6ae0
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
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_mandir}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4.2-1
-	initial version
