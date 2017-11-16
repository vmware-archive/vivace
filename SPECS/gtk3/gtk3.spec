Summary:	GUI library.
Name:		gtk3
Version:	3.20.8 
Release:	2	
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/3.19/gtk+-%{version}.tar.xz
%define sha1 gtk+-3=53fcb97b219de6ef349db7dfcb9415e94de35222
BuildRequires:	libXi-devel libXfixes-devel at-spi2-atk-devel gtk2-devel libepoxy-devel
Requires:	glib-schemas libepoxy
Requires:	atk gdk-pixbuf xpango gobject-introspection libXi libXfixes at-spi2-atk hicolor-icon-theme
%description
The GTK+ 3 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel gobject-introspection-devel gobject-introspection-python libXi-devel libXfixes-devel at-spi2-atk-devel
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
%{_datadir}/aclocal/*
%{_datadir}/gir-1.0/*
%{_datadir}/gtk-3.0/*
%{_datadir}/gtk-doc/*

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.20.8-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.20.8-1
-	Updated to version 3.20.8
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.19.11-1
-	Updated to version 3.19.11
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 3.14.13-1
-	initial version
