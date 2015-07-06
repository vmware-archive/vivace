Summary:	GUI library.
Name:		gtk3
Version:	3.14.13
Release:	1
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/3.14/gtk+-%{version}.tar.xz
BuildRequires:	libXi-devel libXfixes-devel at-spi2-atk-devel gtk2-devel
Requires:	glib-schemas
Requires:	atk gdk-pixbuf pango gobject-introspection libXi libXfixes at-spi2-atk
%description
The GTK+ 3 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel pango-devel libXinerama-devel gobject-introspection-devel gobject-introspection-python libXi-devel libXfixes-devel at-spi2-atk-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n gtk+-%{version}
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
            --enable-gtk2-dependency \
            --enable-broadway-backend \
	    --enable-x11-backend      \
	    --disable-wayland-backend
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
cat > %{buildroot}/etc/gtk-3.0/settings.ini << "EOF"
[Settings]
gtk-theme-name = Clearwaita
gtk-fallback-icon-theme = elementary
EOF
%post
gtk-query-immodules-3.0 --update-cache
glib-compile-schemas /usr/share/glib-2.0/schemas
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%{_datadir}/applications/*
%{_datadir}/glib-2.0/*
%{_datadir}/icons/*
%{_datadir}/locale/*
%{_datadir}/man/*
%{_datadir}/themes/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/aclocal/*
%{_datadir}/gir-1.0/*
%{_datadir}/gtk-3.0/*
%{_datadir}/gtk-doc/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 3.14.13-1
-	initial version
