Summary:	toolkit for image loading and pixel buffer manipulation.
Name:		gdk-pixbuf
Version:	2.42.6
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gt.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.42/%{name}-%{version}.tar.xz
%define sha1 gdk-pixbuf=320ed10a4cb74a0770de91a9e5741767ebdef2bf
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	libpng-devel libtiff-devel libX11-devel gtk-doc libjpeg-turbo-devel glib-devel shared-mime-info
Requires:	libpng libtiff libX11 libjpeg-turbo glib shared-mime-info
%description
The Gdk Pixbuf is a toolkit for image loading and pixel buffer manipulation. It is used by GTK+ 2 and GTK+ 3 to load and manipulate images.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libpng-devel libtiff-devel libX11-devel libjpeg-turbo-devel glib-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release -Dintrospection=disabled -Dinstalled_tests=false -Dgtk_doc=false ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%post
gdk-pixbuf-query-loaders --update-cache
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_datadir}/*
%changelog
* Thu Aug 05 2021 Alexey Makhalov <amakhalov@vmware.com> 2.42.6-1
- Version update
* Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.33.2-1
- Updated to version 2.33.2
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.31.4-1
- initial version
