Summary:	GtkSourceView is a text widget that extends the standard GTK+ text widget GtkTextView.
Name:		gtksourceview
Version:	3.15.1
Release:	1
License:	LGPL-2.1+
URL:		https://wiki.gnome.org/Projects/GtkSourceView
Group:		System/GUI/GNOME
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/3.15/%{name}-%{version}.tar.xz
BuildRequires:	gobject-introspection-devel gobject-introspection-python intltool libxml2-devel glib-devel glibc-devel gtk2-devel gtk3-devel pango-devel cairo-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libX11-devel libXrender-devel libXext-devel harfbuzz-devel python2-devel cracklib-python
Requires:	atk gdk-pixbuf pango glib libX11 libXext libXinerama libXrender gobject-introspection pango cairo gdk-pixbuf atk pixman libpng libX11 libXrender libXext harfbuzz python2
%description
GtkSourceView is a portable C library that extends the standard GTK+ framework for multiline text editing with support for configurable syntax highlighting, unlimited undo/redo, search and replace, a completion framework, printing and other features typical of a source code editor. 
%package	devel
Summary:	GTK+ Source Editing Widget
Group:          Development/Languages/C and C++
Requires:	%{name} = %{version}
%description	devel
GtkSourceView is a portable C library that extends the standard GTK+ framework for multiline text editing with support for configurable syntax highlighting, unlimited undo/redo, search and replace, a completion framework, printing and other features typical of a source code editor. 
%prep
%setup -q 

%build
./configure	--prefix=%{_prefix} \
		--disable-static \
		--disable-gtk-doc
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING MAINTAINERS NEWS README
%{_libdir}/libgtksourceview-3.0.so.*
%{_datadir}/gtksourceview-3.0/
%{_datadir}/locale/
%files devel
%defattr(-, root, root)
%{_includedir}/gtksourceview-3.0/
%{_libdir}/libgtksourceview-3.0.so
%{_libdir}/*.la
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/pkgconfig/gtksourceview-3.0.pc
%{_datadir}/gir-1.0/GtkSource-3.0.gir
%{_datadir}/gtk-doc/html/gtksourceview-3.0/

%changelog
*	Tue Jun 30 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.15.1-1
-	initial version
