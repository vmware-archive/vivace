Summary:	Plugins set for cairo-dock.
Name:		cairo-dock-plugins
Version:	3.4.0
Release:	1
License:	LGPLv2+
URL:		http://glx-dock.org/
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://launchpad.net/cairo-dock-plug-ins/3.4/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	cmake intltool util-macros libX11-devel libXext-devel libXcomposite-devel libXdamage-devel libXrender-devel libXfixes-devel cairo-devel dbus dbus-glib-devel libxml2-devel mesa-devel curl librsvg-devel glu-devel libXtst-devel libXrandr-devel libXinerama-devel gtk3-devel glib-devel pango-devel gdk-pixbuf-devel atk-devel libXi-devel cairo-dock-devel alsa-lib-devel ruby upower-devel python2-libs python2-devel libXxf86vm-devel vte-devel gnome-menus-devel
Requires:	libX11 libXext libXcomposite libXdamage libXrender libXfixes cairo dbus dbus-glib libxml2 mesa curl librsvg glu libXtst libXrandr libXinerama gtk3 glib pango gdk-pixbuf atk libXi cairo-dock alsa-lib ruby upower libXxf86vm vte gnome-menus
%description
A pretty and convenient interface to your desktop: dock, panel, desklet.
%prep
%setup -q
%build
cmake CMakeLists.txt -DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-Denable-sensors-support=FALSE \
	-Denable-libido-support=FALSE \
	-Denable-dbusmenu-support=FALSE \
	-Denable-ical-support=FALSE \
	-Denable-impulse=FALSE \
	-Denable-keyboard-indicator=FALSE \
	-Denable-exif-support=FALSE \
	-Denable-weblets=FALSE \
	-Denable-recent-events=FALSE \
	-Denable-indicator-support=FALSE \
	-Denable-vala-interface=FALSE \
	-Denable-mail=FALSE
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 3.4.0-1
-	initial version
