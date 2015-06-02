Summary:	default session manager for LXDE.
Name:		lxsession
Version:	0.5.2
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool gtk2-devel glib-devel libX11-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel dbus-glib libunique-devel polkit-devel dbus-glib-devel
Requires:	gtk2 dbus-glib libunique polkit dbus-glib
%description
The LXSession package contains the default session manager for LXDE.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --disable-man
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.2-1
-	initial version
