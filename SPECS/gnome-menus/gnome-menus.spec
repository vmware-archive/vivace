Summary:	GNOME Menus
Name:		gnome-menus
Version:	3.6.0
Release:	1
License:	GPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.6/%{name}-%{version}.tar.xz
#BuildRequires:	intltool vte-devel gtk2-devel  ncurses-devel glib-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel libX11-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel
#Requires:	vte gtk2 ncurses glib cairo pango gdk-pixbuf atk libX11 pixman libXrender libXext libpng harfbuzz
BuildRequires:	intltool glib-devel gobject-introspection python2-libs python2-devel
Requires:	glib
%description
The GNOME Menus package contains an implementation of the draft Desktop Menu Specification from freedesktop.org. It also contains the GNOME menu layout configuration files, .directory files and a menu related utility program.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 3.6.0-1
-	initial version
