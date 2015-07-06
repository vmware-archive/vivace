Summary:	provides extension libraries on top of libxcb.
Name:		xcb-util-wm
Version:	0.4.1
Release:	1
License:	MIT
URL:		http://xcb.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:	libxcb-devel xcb-util-devel
Requires:	libxcb xcb-util
%description
XCB util-wm module provides the following library:
  - ewmh: provides the client and window-manager helpers for EWMH.
  - icccm: provides the client and window-manager helpers for ICCCM. 
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
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.1-1
-	initial version
