Summary:	GUI library.
Name:		gtk3
Version:	3.24.30
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/3.24/gtk+-%{version}.tar.xz
%define sha1 gtk+-3=b16d0ed86c613708b161eb96b56f4df1e52a1e48
BuildRequires:	atk-devel gdk-pixbuf-devel libXi-devel libXfixes-devel at-spi2-atk-devel libepoxy-devel xpango-devel libXrandr-devel
Requires:	glib-schemas libepoxy
Requires:	atk gdk-pixbuf xpango libXi libXfixes at-spi2-atk libXrandr
%description
The GTK+ 3 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel libXi-devel libXfixes-devel at-spi2-atk-devel libepoxy-devel libXrandr-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup -n gtk+-%{version}
%build
%configure \
            --enable-broadway-backend \
	    --enable-x11-backend      \
	    --disable-wayland-backend
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
cat > %{buildroot}/etc/gtk-3.0/settings.ini << "EOF"
[Settings]
gtk-theme-name = Adwaita
gtk-icon-theme-name = oxygen
gtk-font-name = DejaVu Sans 12
gtk-cursor-theme-size = 18
gtk-toolbar-style = GTK_TOOLBAR_BOTH_HORIZ
gtk-xft-antialias = 1
gtk-xft-hinting = 1
gtk-xft-hintstyle = hintslight
gtk-xft-rgba = rgb
gtk-cursor-theme-name = Adwaita
EOF
cat > %{buildroot}/etc/gtk-3.0/gtk.css << "EOF"
*  {
   -GtkScrollbar-has-backward-stepper: 1;
   -GtkScrollbar-has-forward-stepper: 1;
}
EOF
mv %{buildroot}%{_bindir}/gtk-update-icon-cache %{buildroot}%{_bindir}/gtk-update-icon-cache-3.0

%post
gtk-query-immodules-3.0 --update-cache
glib-compile-schemas /usr/share/glib-2.0/schemas
gtk-update-icon-cache-3.0

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%exclude %{_libdir}/*.la
%{_datadir}/applications/*
%{_datadir}/glib-2.0/*
%{_datadir}/icons/*
%{_datadir}/locale/*
%{_datadir}/man/*
%{_datadir}/themes/*
%{_datadir}/gettext/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/pkgconfig/
%{_datadir}/aclocal/*
%{_datadir}/gtk-3.0/*
%{_datadir}/gtk-doc/*

%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 3.24.30-1
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.20.8-2
- Updated build requires & requires to build with Photon 2.0
* Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.20.8-1
- Updated to version 3.20.8
* Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.19.11-1
- Updated to version 3.19.11
* Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 3.14.13-1
- initial version
