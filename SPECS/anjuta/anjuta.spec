Summary:	GNOME Integrated Development Environment
Name:		anjuta
Version:	3.13.92
Release:	1
License:	GPL
URL:		http://anjuta.org/
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/3.13/%{name}-%{version}.tar.xz
BuildRequires:	libtool pkg-config ORBit2-devel desktop-file-utils intltool libgnomeui-devel libgnome-devel dbus gtk2-devel libgnome glib-devel libX11-devel libXext-devel libXinerama-devel gtk3-devel libXrender-devel libpng-devel libXrandr-devel systemd alsa-lib-devel gdk-pixbuf-devel libgnome-keyring-devel libxml2-devel python2-libs python2-devel harfbuzz-devel itstool pixman-devel cairo-devel pango-devel atk-devel GConf-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper libglade-devel perl pcre-devel binutils-devel gdl-devel libgda-devel gtksourceview-devel
Requires:	libgnome glib gnome-vfs libX11 libXext libXinerama libXrender alsa-lib libgda libXrandr pixman openssl gtk2 gtk3 libgnomeui python2 harfbuzz libgnomecanvas gdk-pixbuf libgnome-keyring libxml2 cairo pango atk GConf popt libbonobo libart_lgpl binutils gdl gtksourceview
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
Requires: libgnomeui-devel, libglade-devel, pkg-config 

%description devel
Libraries, header files and API docs for developing Anjuta plugins

%prep
%setup -q 
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
/sbin/ldconfig

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
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
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.13.92-1
-	initial version
