Summary:	toolkit for image loading and pixel buffer manipulation.
Name:		gdk-pixbuf
Version:	2.33.2
Release:	1
License:	LGPLv2+
URL:		http://www.gt.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.31/%{name}-%{version}.tar.xz
%define sha1 gdk-pixbuf=aa271542181436f5acdf1378354308865011601a
BuildRequires:	libpng-devel libtiff-devel libX11-devel gobject-introspection-devel gobject-introspection-python gtk-doc libjpeg-turbo-devel
Requires:	libpng libtiff libX11 gobject-introspection libjpeg-turbo
%description
The Gdk Pixbuf is a toolkit for image loading and pixel buffer manipulation. It is used by GTK+ 2 and GTK+ 3 to load and manipulate images.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libpng-devel libtiff-devel libX11-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --with-x11
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
gdk-pixbuf-query-loaders --update-cache
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
%{_datadir}/*
%changelog
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.19.11-1
-	Updated to version 2.33.2
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.31.4-1
-	initial version
