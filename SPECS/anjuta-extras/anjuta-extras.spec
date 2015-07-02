Summary:	Extra plugins for anjuta, the GNOME Integrated Development Environment
Name:		anjuta-extras
Version:	3.10.0
Release:	1
License:	GPLV2+
URL:		http://anjuta.org/
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.xz
BuildRequires:	libtool anjuta-devel pkg-config ORBit2-devel desktop-file-utils intltool libgnomeui-devel libgnome-devel dbus gtk2-devel libgnome glib-devel libX11-devel libXext-devel libXinerama-devel gtk3-devel libXrender-devel libpng-devel libXrandr-devel systemd alsa-lib-devel gdk-pixbuf-devel libgnome-keyring-devel libxml2-devel python2-libs python2-devel harfbuzz-devel itstool pixman-devel cairo-devel pango-devel atk-devel GConf-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper libglade-devel perl pcre-devel binutils-devel gdl-devel libgda-devel gtksourceview-devel
Requires:	libgnome anjuta glib gnome-vfs libX11 libXext libXinerama libXrender alsa-lib libgda libXrandr pixman openssl gtk2 gtk3 libgnomeui python2 harfbuzz libgnomecanvas gdk-pixbuf libgnome-keyring libxml2 cairo pango atk GConf popt libbonobo libart_lgpl binutils gdl gtksourceview
%description
The package contains the following plugins:
    * Scintilla Editor
    * Scratchbox Support
    * Profiler (gprof)
    * Valgrind

%prep
%setup -q 
%build
./configure 	--prefix=%{_prefix} \
		--disable-static 

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_libdir}/anjuta/*.la

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_libdir}/anjuta/*.plugin
%{_libdir}/anjuta/*.so*
%{_datadir}


%changelog
*	Wed Jul 1 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.10.0-1
-	initial version
