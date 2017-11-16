Summary:	A media playback and management application
Name:           banshee
Version:        2.6.2
Release:        2 
License:        MIT/X11
Url:		http://banshee.fm/
Group:		Productivity/Multimedia/Sound/Players
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.xz
%define sha1 banshee=3182040b702c5ecea2d3c84ba5ac1f580a71be32
Patch0:         banshee-2.6.2-gstreamer-port-to-1.0.patch
BuildRequires:  gtk-sharp2-devel libtool gstreamer-devel sqlite-devel
BuildRequires:  which unzip gnome-sharp-devel sqlite-libs tzdata mono-devel mono-extras mono-addins dbus-glib-devel gstreamer-devel gstreamer-plugins-base-devel gtk3-devel gtk2-devel
BuildRequires:  intltool >= 0.35.0 dbus-sharp-glib taglib-sharp-devel mercurial
BuildRequires:  automake autoconf dbus-sharp
Requires:	mono mono-addins mono-extras dbus-glib dbus-sharp dbus-sharp-glib libtool gstreamer gstreamer-plugins-base taglib-sharp gtk3 gtk2
Requires:       gtk-sharp2 gnome-sharp sqlite
%description
Import, organize, and discover new music with Banshee through its
simple and powerful interface and wide array of innovative features.
Create your own radio stations or listen to a friends' through Last.fm
integration; experience automatic cover art fetching as you listen; and
easily browse, search, and control your media collection.
%prep
%setup -q 
%patch0 -p1
%build
NOCONFIGURE=1 ./autogen.sh
sed -i "s#gmcs#mcs#g; s#Mono 2.0#Mono 4.0#g; s#mono/2.0#mono/4.5#g; s#mono,2.0#mono,4.0#g" configure
./configure	--prefix=%{_prefix} \
		--disable-static \
	  	--disable-docs \
	  	--disable-youtube \
	  	--disable-docs \
	  	--disable-boo \
	  	--disable-mtp \
	  	--disable-appledevice \
	  	--enable-remote_audio=no \
	  	--enable-daap=no
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
#%find_lang %{name}
#chmod -x %{buildroot}%{_libdir}/%{name}/*.config
#chmod -x %{buildroot}%{_libdir}/%{name}/*/*.config
#%suse_update_desktop_file %{name}
#%suse_update_desktop_file %{name}-audiocd
#%suse_update_desktop_file %{name}-media-player

# Remove the libtool archives
#find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_libdir}/banshee

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS COPYING AUTHORS README
%{_bindir}/
%{_libdir}/banshee/*
%{_libdir}/pkgconfig/*.pc
# desktop files all reference the banshee binary
#%{_datadir}/applications/banshee.desktop
#%{_datadir}/applications/banshee-audiocd.desktop
#%{_datadir}/applications/banshee-media-player.desktop
#%dir %{_datadir}/appdata/
%{_datadir}

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6-2 
-	Updated build requires & requires to build with Photon 2.0
*	Wed Jun 24 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6-1
-	Initial version. 

