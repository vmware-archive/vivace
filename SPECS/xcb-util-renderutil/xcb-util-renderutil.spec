Summary:	provides extension libraries on top of libxcb.
Name:		xcb-util-renderutil
Version:	0.3.9
Release:	1%{?dist}
License:	MIT
URL:		http://xcb.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
%define sha1 xcb-util-renderutil=cb533b1d039f833f070e7d6398c221a31d30d5e2
BuildRequires:	libxcb-devel xcb-util-devel
Requires:	libxcb xcb-util
%description
XCB util-renderutil module provides the following library:
  - render-util: Provides convenience functions for the Render extension. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libxcb-devel xcb-util-devel
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
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 0.3.9-1
-	initial version
