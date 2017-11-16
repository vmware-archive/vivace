Summary:	A video playback application designed to work with GNOME 3.
Name:           totem
Version:        3.10.1
Release:       	2 
License:        GPLV2+
Url:		https://wiki.gnome.org/Apps/Videos
Group:		Productivity/Multimedia/Video/Players
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:        https://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.xz
%define sha1 totem=ee3802de84ac2cf34b38f91ae6de59b0d17ff4dc
BuildRequires:  libtool gstreamer-devel clutter-devel gsettings-desktop-schemas-devel clutter-gst-devel clutter-gtk-devel gst-plugins-good-devel gst-plugins-bad-devel pygobject
BuildRequires:  itstool unzip gnome-sharp-devel libxml2-devel dbus-glib-devel gstreamer-devel xcairo-devel gstreamer-plugins-base-devel gtk3-devel libpeas-devel libxml2-python
BuildRequires:  intltool >= 0.35.0 dbus-sharp-glib taglib-sharp-devel glib-devel gnome-icon-theme totem-pl-parser-devel
Requires:	dbus-glib dbus-sharp dbus-sharp-glib libtool gstreamer gstreamer-plugins-base taglib-sharp gtk3 libxml2 gst-plugins-good
Requires:       gnome-sharp glib xcairo clutter clutter-gst clutter-gtk gst-plugins-bad totem-pl-parser libpeas gsettings-desktop-schemas
%description
Totem is movie player for the GNOME desktop based on GStreamer.
It features a playlist, a full-screen mode, seek and volume controls,
as well as complete keyboard navigation.
%package devel
Summary:        Documentation & Development files for Totem Movie Player
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
This package contains developer documentation.

%prep
%setup -q 

%build
./configure	--prefix=%{_prefix} \
		--with-plugins=none \
		--enable-browser-plugins=no \
		--disable-static 
	  	
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
update-mime-database %{_datadir}/mime &> /dev/null 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas  
/sbin/ldconfig
update-mime-database %{_datadir}/mime &> /dev/null 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
/usr/libexec
%{_datadir}
%{_libdir}
%exclude %{_datadir}/gtk-doc

%files devel
%defattr(-, root, root)
%{_datadir}/gtk-doc
%{_includedir}/
%{_libdir}/*.so
%{_libdir}/pkgconfig
%{_datadir}/gir-1.0

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.10.1-2
-	Updated build requires & requires to build with Photon 2.0
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.10.1-1
-	Initial version. 

