Summary:	GNOME Integrated Development Environment
Name:		anjuta
Version:	3.14.0
Release:	1
License:	GPL
URL:		http://anjuta.org/
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.xz
Patch0:		anjuta-3.14.0-build-crash-fix.patch 
%define sha1 anjuta=d7988414cdd52675a973744a60346e541555d3d0

BuildRequires:	libtool autogen autoconf automake pkg-config ORBit2-devel desktop-file-utils intltool libgnomeui-devel libgnome-devel dbus libgnome glib-devel libX11-devel libXext-devel libwnck-devel gtk3-devel gobject-introspection-devel libXinerama-devel vte290-devel libXrender-devel libpng-devel libXrandr-devel gnome-icon-theme gnome-doc-utils apr apr-util systemd alsa-lib-devel gdk-pixbuf-devel libgnome-keyring-devel gnome-vfs-devel libxml2-devel python2-libs python2-devel harfbuzz-devel itstool pixman-devel cairo-devel pango-devel atk-devel GConf-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper libglade-devel perl pcre-devel binutils-devel gdl-devel libgda-devel gtksourceview-devel libunique-devel libxslt shared-mime-info at-spi2-core-devel dconf-devel sqlite-autoconf glibc-devel ncurses-devel libcroco-devel librsvg-devel libogg-devel libvorbis-devel libltdl-devel gvfs gda-sqlite
Requires:	libgnome glib gnome-vfs libX11 libXext libXinerama libXrender libglade alsa-lib libgda libXrandr pixman gnome-vfs openssl libgnomeui python2 harfbuzz libgnomecanvas gdk-pixbuf libgnome-keyring gobject-introspection libxml2 cairo pango atk GConf popt libbonobo libart_lgpl binutils gdl gtksourceview vte290 libwnck libunique autoconf at-spi2-core dconf sqlite-autoconf glibc ncurses gtk3 libcroco librsvg libogg libltdl libvorbis gvfs gda-sqlite dbus

%description
Anjuta DevStudio is a versatile Integrated Development Environment (IDE)
on GNOME Desktop Environment and features a number of advanced
programming facilities. These include project management, application and
class wizards, an on-board interactive debugger, powerful source editor,
syntax highlighting, intellisense autocompletions, symbol navigation,
version controls, integrated GUI designing and other tools.
%package devel
Summary: Libraries and include files for Anjuta plugins development
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: libgnomeui-devel, libglade-devel, pkg-config dconf-devel sqlite-autoconf glibc-devel ncurses-devel gtk3-devel libcroco-devel libvorbis-devel libltdl-devel gvfs gda-sqlite libgda-devel

%description devel
Libraries, header files and API docs for developing Anjuta plugins

%prep
%setup -q 
%patch0 -p1 
%build
./configure 	--prefix=%{_prefix} \
				--disable-static 

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --delete-original \
		     --dir %{buildroot}/%{_datadir}/applications      \
			  %{buildroot}%{_datadir}/applications/%{name}.desktop

ln -s anjuta/anjuta_logo.png %{buildroot}%{_datadir}/pixmaps/anjuta.png

%clean
rm -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
glib-compile-schemas /usr/share/glib-2.0/schemas
/sbin/ldconfig

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
glib-compile-schemas /usr/share/glib-2.0/schemas
/sbin/ldconfig


%files 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc doc/ScintillaDoc.html
%{_bindir}/%{name}*
%{_libdir}/lib%{name}*.so.*
%{_libdir}/%{name}
%{_datadir}/help
%{_datadir}/anjuta
%{_datadir}/appdata
%{_datadir}/applications
%{_datadir}/doc
%{_datadir}/glib-2.0
%{_datadir}/icons
%{_datadir}/locale
%{_datadir}/pixmaps
%{_datadir}/man
%{_datadir}/mime
%{_datadir}/gir-1.0

%files devel
%defattr (-, root, root)
%{_includedir}/*%{name}*
%{_libdir}/pkgconfig/*%{name}*
%{_libdir}/lib%{name}*.so
%{_libdir}/*.la
%{_datadir}/gtk-doc/html/*%{name}*
%{_libdir}/girepository-1.0

%changelog
* 	Fri Jul	24 2015	Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.14.0-1
-	Added more build dependencies and updated the version
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.13.92-1
-	initial version 
