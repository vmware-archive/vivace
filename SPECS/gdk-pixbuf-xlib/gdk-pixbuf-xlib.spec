Summary:	deprecated Xlib interface to gdk-pixbuf
Name:		gdk-pixbuf-xlib
Version:	2.40.2
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gt.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.40/%{name}-%{version}.tar.xz
%define sha1 gdk-pixbuf-xlib=46c7261de823a1fa40cebfc90a741383b3a75025
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	gdk-pixbuf-devel libX11-devel
Requires:	gdk-pixbuf libX11
%description
The gdk-pixbuf-xlib package provides a deprecated Xlib interface to gdk-pixbuf, which is needed for some applications which have not been ported to use the new interfaces yet.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gdk-pixbuf-devel libX11-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release -Dgtk_doc=false ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Wed Aug 11 2021 Alexey Makhalov <amakhalov@vmware.com> 2.40.2-1
- initial version
