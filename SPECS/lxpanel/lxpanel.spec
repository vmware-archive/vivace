Summary:	The LXPanel package contains a lightweight X11 desktop panel.
Name:		lxpanel
Version:	0.8.1
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool lxmenu-data menu-cache-devel gtk2-devel libfm-devel libwnck-devel keybinder-devel libxml2-devel glib-devel libX11-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel
#intltool glib-devel gtk2-devel menu-cache-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel libfm-devel
Requires:	lxmenu-data menu-cache gtk2 libfm libwnck keybinder
#glib gtk2 menu-cache cairo pango gdk-pixbuf atk pixman harfbuzz libpng libXrender libfm
%description
The LXPanel package contains a lightweight X11 desktop panel.
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
./configure --prefix=%{_prefix} --with-plugins=all,-netstat
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.8.1-1
-	initial version
