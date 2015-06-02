%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pygtk
Version:        2.24.0
Release:	1
Summary:        Python Bindings for GTK
Group:          Development/Languages
License:        LGPLv2+
Vendor:		VMware, Inc.
Distribution:	Photon
URL:            ftp://ftp.gnome.org
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires: 	python2-devel
BuildRequires: 	python2-libs
BuildRequires: 	gobject-introspection-devel
BuildRequires: 	glib-devel
BuildRequires:	pygobject = 2.28.6 atk-devel pango-devel gtk2-devel py2cairo cairo-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel gdk-pixbuf-devel
Requires:	python2
Requires:	gobject-introspection
Requires:	glib pango gtk2 
Requires:	pygobject = 2.28.6

%description
Python bindings for GTK.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/python*/*
%{_libdir}/pygtk/*
%{_datadir}/*
%{_includedir}/*

%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.0-1
-	Initial build.	First version
