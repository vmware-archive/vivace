Summary:	library for writing single instance applications.
Name:		libunique
Version:	1.1.6
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
Patch0:		libunique-1.1.6-upstream_fixes-1.patch
BuildRequires:	autoconf automake intltool gtk2-devel glib-devel libX11-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel gobject-introspection
#intltool glib-devel gtk2-devel menu-cache-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel libfm-devel
Requires:	gtk2
#glib gtk2 menu-cache cairo pango gdk-pixbuf atk pixman harfbuzz libpng libXrender libfm
%description
The libunique package contains a library for writing single instance applications.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%patch0 -p1
%build
# current configure uses old auto tools
autoreconf --install
./configure --prefix=%{_prefix} \
	    --disable-static \
	    --disable-dbus
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.6-1
-	initial version
