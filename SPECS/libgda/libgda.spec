Summary:	Libgda is a (relatively small) database access library. 
Name:		libgda
Version:	5.2.4
Release:	2	
License:	LGPL
URL:		http://www.gnome-db.org/
Group:		Productivity/Databases/Clients
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/5.2/%{name}-%{version}.tar.xz
%define sha1 libgda=9963fe39074f5ece1872387c955e1598f8b872af

Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	gtk2-devel gtk3-devel intltool glib-devel libxml2-devel itstool xpango-devel libtool desktop-file-utils openssl-devel python2-devel cracklib-python python2-libs python2-tools python2 libgnome-keyring-devel gobject-introspection gobject-introspection-python gobject-introspection-devel autoconf libgcrypt-devel xcairo-devel gdk-pixbuf-devel atk-devel pixman-devel scrollkeeper libxslt ncurses-devel readline-devel groff libpng-devel libXrender-devel libXext-devel libX11-devel harfbuzz-devel sqlite 
Requires:	dbus glib libxml2 xpango xcairo pixman libpng libXrender libXext libX11 harfbuzz gobject-introspection
%description
The GNOME-DB aims to provide a free unified data access architecture. GNOME-DB is useful for any application that accesses persistent data (not only databases, but data), since it now contains a pretty good data management API.
%package devel
Summary:          Development libraries and header files for libgda.
Group:            Development/Libraries
Requires:         glib-devel >= 2.0.0
Requires:         libxml2-devel
Requires:         libxslt >= 1.0.9
Requires:         %{name} = %{version}

%description devel
This package contains the header files and libraries needed to write
or compile programs that use libgda.

%package -n gda-sqlite
Summary:	GDA SQLite Provider
Group:		System Environment/Libraries
%description -n gda-sqlite
This package includes the GDA SQLite provider.

%package 5_0-doc
Summary:        GNU Data Access (GDA) Library -- Developer Documentation
Group:          Development/Libraries/C and C++
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc <= 1.3.91

%description 5_0-doc
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.


%prep
%setup -q

%build
./configure	--prefix=%{_prefix} \
		--enable-system-sqlite \
		--disable-gtk-doc \
		--disable-static \
		--enable-binreloc \
		--enable-gda-gi
		
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README NEWS
%{_prefix}%{_sysconfdir}/libgda-5.0/*
%{_bindir}/*
%{_datadir}/libgda-5.0
%exclude %{_datadir}/libgda-5.0/sqlite_*.xml
%{_datadir}/appdata
%{_datadir}/help
%{_datadir}/icons
%{_datadir}/locale
%{_libdir}/*.so.*
%{_datadir}/applications/
%{_datadir}/pixmaps/
%dir %{_libdir}/libgda-5.0
%dir %{_libdir}/libgda-5.0/providers
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libgda-5.0
%dir %{_includedir}/libgda-5.0/
%{_includedir}/libgda-5.0/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/libgda-5.0
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*.gir
%{_libdir}/girepository-1.0

%files 5_0-doc
%defattr(-, root, root)
%{_datadir}/gtk-doc/html/gda-browser/
%{_datadir}/gtk-doc/html/libgda-5.0/

%files -n gda-sqlite
%defattr(-,root,root)
%{_libdir}/libgda-5.0/providers/libgda-sqlite.so
%{_datadir}/libgda-5.0/sqlite_*.xml

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 5.2.4-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue Jun 30 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 5.2.4-1
-	Initial build. First version
