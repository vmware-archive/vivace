Summary:	grdesktop is a GNOME frontend, for the remote desktop client (rdesktop).
Name:		grdesktop
Version:	0.23
Release:	1
License:	GPL
URL:		http://www.nongnu.org/grdesktop/index.html
Group:		Applications/Communications
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.savannah.gnu.org/releases/grdesktop/%{name}-%{version}.tar.gz
BuildRequires:	libgnomeui-devel libgnome-devel gtk2-devel libgnome glib-devel libX11-devel libXext-devel libXinerama-devel gtk3-devel libXrender-devel libpng-devel libXrandr-devel gobject-introspection-python python2-devel alsa-lib-devel gnome-vfs-devel libgnomecanvas-devel gdk-pixbuf-devel libgnome-keyring-devel libxml2-devel cairo-devel pango-devel atk-devel GConf-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper
Requires:	rdesktop libgnome glib gnome-vfs libX11 libXext libXinerama libXrender alsa-lib libXrandr openssl gtk2 gtk3 libgnomeui libgnomecanvas gdk-pixbuf libgnome-keyring libxml2 cairo pango atk GConf popt libbonobo libart_lgpl
%description
grdesktop is a GNOME frontend, for the remote desktop client (rdesktop).
It can save several connections (including their options), and browse the network for available terminal servers.
%prep
%setup -q 
%build
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
        --with-keymap-path=%{_datadir}/rdesktop/keymaps

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
ln -s grdesktop/icon.png %{buildroot}/%{_datadir}/pixmaps/grdesktop.png

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO doc
%{_bindir}/
%{_datadir}/
%{_prefix}/man
%{_sysconfdir}

%changelog
*	Fri Jun 26 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.23-1
-	initial version
