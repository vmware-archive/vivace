Summary:	Lightweight image viewer
Name:		gpicview
Version:	0.2.4
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
BuildRequires:	intltool vte-devel gtk2-devel gobject-introspection python2-libs python2-devel glib-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel libX11-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel libjpeg-turbo-devel
Requires:	vte gtk2 glib cairo pango gdk-pixbuf atk libX11 pixman libXrender libXext libpng harfbuzz libjpeg-turbo
%description
The GPicView package contains a lightweight image viewer.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d -m 755 %{buildroot}/%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.2.4-1
-	initial version
