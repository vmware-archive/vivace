Summary:	GTK+ and GNOME bindings for Mono
Name:		gnome-sharp
Version:	2.24.2
Release:	1
License:	GPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires:	intltool gettext glib-devel tzdata mono-devel gtk2-devel libglade-devel pango-devel libxml2-devel atk-devel cairo-devel gdk-pixbuf-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel gtk-sharp2 libgnomeui-devel libgnomecanvas-devel libgnome-devel libart_lgpl-devel gnome-vfs-devel popt-devel libbonobo-devel libbonoboui-devel libSM-devel libXinerama-devel dbus-glib-devel libICE-devel
Requires:	gettext glib mono-core gtk2 libglade pango libxml2 atk cairo gtk-sharp2 libgnomeui libgnomecanvas libgnome libart_lgpl gnome-vfs libSM libICE
%description
GTK+ and GNOME bindings for Mono.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.2-1
-	initial version
