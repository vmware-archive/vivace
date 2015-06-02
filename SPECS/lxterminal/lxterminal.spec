Summary:	LXDE Terminal Emulator
Name:		lxterminal
Version:	0.2.0
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
BuildRequires:	intltool vte-devel gtk2-devel gobject-introspection python2-libs python2-devel ncurses-devel glib-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel libX11-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel
Requires:	vte gtk2 ncurses glib cairo pango gdk-pixbuf atk libX11 pixman libXrender libXext libpng harfbuzz
%description
The LXTerminal package contains a VTE-based terminal emulator for LXDE with support for multiple tabs.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
# Use utilities-terminal icon
sed -e 's/Icon=lxterminal/Icon=utilities-terminal/' -i %{buildroot}/usr/share/applications/lxterminal.desktop
#
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.2.0-1
-	initial version
