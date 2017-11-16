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
Patch0:		cairo-dock-plugins-time-h-conflicts.patch
%define sha1 cairo-dock-plugins=b603f96ba7c48eb0bc4248d8b344f6868ef509ed
BuildRequires:	cmake libXcomposite-devel dbus-glib-devel libxml2-devel mesa-devel curl librsvg-devel glu-devel gtk3-devel  cairo-dock-devel alsa-lib-devel ruby upower-devel libXxf86vm-devel vte-devel gnome-menus-devel
Requires:	libXcomposite dbus-glib libxml2 mesa curl librsvg glu gtk3 cairo-dock alsa-lib ruby upower libXxf86vm vte gnome-menus
%description
A pretty and convenient interface to your desktop: dock, panel, desklet.
%prep
%setup -q
%patch0 -p1
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
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.4.0-2
-	Added patch to build with Photon 2.0 with GCC6
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 3.4.0-1
-	initial version
