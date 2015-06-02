Summary:	desktop-independent theme switcher for GTK+.
Name:		lxappearance
Version:	0.6.1
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool gtk2-devel glib-devel libX11-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel dbus-glib
#intltool glib-devel gtk2-devel menu-cache-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel libfm-devel
Requires:	gtk2 dbus-glib
#glib gtk2 menu-cache cairo pango gdk-pixbuf atk pixman harfbuzz libpng libXrender libfm
%description
The LXAppearance package contains a desktop-independent theme switcher for GTK+.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --disable-static \
	    --enable-dbus
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.6.1-1
-	initial version
