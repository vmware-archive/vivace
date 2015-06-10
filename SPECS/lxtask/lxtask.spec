Summary:	Lightweight task manager
Name:		lxtask
Version:	0.1.6
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool gtk2-devel gobject-introspection python2-libs python2-devel glib-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel libX11-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel libjpeg-turbo-devel
Requires:	gtk2 glib cairo pango gdk-pixbuf atk libX11 pixman libXrender libXext libpng harfbuzz libjpeg-turbo
%description
The LXTask package contains a lightweight and desktop-independent task manager.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1.6-1
-	initial version
