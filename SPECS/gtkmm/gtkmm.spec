Summary:	gtkmm is the official C++ interface for the popular GUI library GTK+. 
Name:		gtkmm
Version:	2.24.4
Release:	1
License:	LGPLv2+
URL:		http://www.gtkmm.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.24/%{name}-%{version}.tar.xz
BuildRequires:	atk-devel gdk-pixbuf-devel pango-devel pangomm-devel atkmm-devel gtk2-devel glib-devel libX11-devel libXext-devel libXinerama-devel cairo-devel cairomm-devel libXrender-devel fontconfig-devel pixman-devel libpng-devel harfbuzz-devel freetype2-devel gobject-introspection-devel gobject-introspection-python python2-devel python2-libs
Requires:	atk atkmm gtk2 pangomm gdk-pixbuf pango glib libX11 libXext libXinerama libXrender gobject-introspection
%description
gtkmm is the official C++ interface for the popular GUI library GTK+. Highlights include typesafe callbacks, and a comprehensive set of widgets that are easily extensible via inheritance.

%package	devel
Summary:	Header and development files
Group: 		Development/Libraries
Requires:	%{name} = %{version}, gtk2-devel, glib, libsigc++
Requires: 	atk-devel, pango-devel
%description	devel
It contains the libraries and header files to create gtkmm applications. 

%prep
%setup -q -n gtkmm-%{version}

%build
./configure --prefix=%{_prefix} --enable-static --enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post
-p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc ChangeLog PORTING
%doc %{_datadir}/doc/gtkmm-2.4
%{_includedir}/gtkmm-2.4
%{_includedir}/gdkmm-2.4
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/gtkmm-2.4
%{_libdir}/gdkmm-2.4
%{_libdir}/pkgconfig/*.pc
%{_datarootdir}/devhelp/books/gtkmm-2.4/gtkmm-2.4.devhelp2
%changelog
*	Tue Jun 16 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.4-1
-	initial version
