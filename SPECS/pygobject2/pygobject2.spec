%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pygobject2
Version:        2.28.6
Release:	1
Summary:        Python Bindings for GObject
Group:          Development/Languages
License:        LGPLv2+
Vendor:		VMware, Inc.
Distribution:	Photon
URL:            ftp://ftp.gnome.org
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/pygobject/2.28/pygobject-%{version}.tar.xz
%define sha1 pygobject=b1749ba806499f4c2780dbd1cbb363aaf1f41e78
Patch0:		pygobject-2.28.6-fixes-1.patch
BuildRequires: 	python2-devel
BuildRequires: 	python2-libs
BuildRequires: 	glib-devel
Requires:	python2
Requires:	glib
Provides:	pygobject2

%description
Python bindings for GLib and GObject.

%prep
%setup -q -n pygobject-%{version}
%patch0 -p1
%build
%configure --disable-cairo --without-cairo --disable-introspection
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/python*/*
%{_includedir}/*
%{_datadir}/*

%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 2.28.6-1
-	Initial build.	First version
