%global debug_package %{nil}
Summary:	Stand-alone mail/news client.
Name:		thunderbird
Version:	31.7.0
Release:	2	
License:	MPLv1.1 or GPLv2+ or LGPLv2+
URL:		http://www.mozilla.org/projects/thunderbird
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://ftp.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/source/%{name}-%{version}.source.tar.bz2
Patch0:         fix_icu_vernum.patch
Patch1:         build-with-gcc6.patch
%define sha1 thunderbird=90e18f8ecccdaf1ee39493223a7e3ad8b3b7bede
Source1:        %{name}.desktop
BuildRequires:	gtk2-devel which unzip zip nspr-devel nss nss-libs nss-devel icu-devel yasm-devel alsa-lib-devel libffi libXcomposite-devel autoconf213
BuildRequires:	desktop-file-utils
Requires:	gtk2 nspr nss icu yasm alsa-lib libXcomposite desktop-file-utils
%description
Thunderbird is a stand-alone mail/news client based on the Mozilla codebase. It uses the Gecko rendering engine to enable it to display and compose HTML emails.
%prep
%setup -q -n comm-esr31
%patch0	-p1
%patch1	-p1
%build
cat > mozconfig << "EOF"
# If you have a multicore machine, all cores will be used by default.
# If desired, you can reduce the number of cores used, e.g. to 1, by
# uncommenting the next line and setting a valid number of CPU cores.
#mk_add_options MOZ_MAKE_FLAGS="-j1"

# If you have installed DBus-Glib comment out this line:
ac_add_options --disable-dbus

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
ac_add_options --disable-necko-wifi

# If you have installed libnotify comment out this line:
ac_add_options --disable-libnotify

# GStreamer is necessary for H.264 video playback in HTML5 Video Player;
# to be enabled, also remember to set "media.gstreamer.enabled" to "true"
# in about:config. If you have GStreamer 0.x.y, comment out this line:
ac_add_options --disable-gstreamer
# or uncomment this line, if you have GStreamer 1.x.y
#ac_add_options --enable-gstreamer=1.0

# Uncomment these lines if you have installed optional dependencies:
#ac_add_options --enable-system-hunspell
#ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio

# If you want to compile the Mozilla Calendar, uncomment this line:
#ac_add_options --enable-calendar

# Comment out following options if you have not installed
# recommended dependencies:
#ac_add_options --enable-system-sqlite
#ac_add_options --with-system-libevent
#ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-icu

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=/usr

ac_add_options --disable-crashreporter
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-debug
ac_add_options --disable-tests

ac_add_options --enable-optimize
ac_add_options --enable-strip
ac_add_options --enable-install-strip

ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-pthreads

ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
#ac_add_options --with-system-png
ac_add_options --with-system-zlib
EOF

cd mozilla/media/webrtc/trunk/webrtc/modules/video_coding/codecs/vp8 &&
  sed -e 's/IMG_FMT_I420/VPX_&/'    \
      -e 's/\[PLANE_/\[VPX_PLANE_/' \
      -i  vp8_impl.cc               &&
cd -
export AUTOCONF=/usr/bin/autoconf2.13 &&
export CFLAGS+='-fpermissive' &&
export CXXFLAGS+='-fpermissive' &&
make %{?_smp_mflags} -f client.mk
%install
make -f client.mk DESTDIR=%{buildroot} install INSTALL_SDK=
chown -R 0:0 %{buildroot}/usr/lib/thunderbird-31.7.0
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
%post
#this is needed to get gnome-panel to update the icons
update-desktop-database &> /dev/null || :
ln -sfv /usr/lib/thunderbird-31.7.0/chrome/icons/default/default256.png \
        /usr/share/pixmaps/thunderbird.png
#touch --no-create %{_datadir}/icons/hicolor || :
#if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
#    %{_bindir}/gtk-update-icon-cache --quiet ${_datadir}/icons/hicolor &> /dev/null || :
#fi

%postun
#this is needed to get gnome-panel to update the icons
update-desktop-database &> /dev/null || :
#touch --no-create %{_datadir}/icons/hicolor || :
#if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
#    %{_bindir}/gtk-update-icon-cache --quiet ${_datadir}/icons/hicolor &> /dev/null || :
#fi

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/
#%{_datadir}/icons/
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 31.7.0-2
-	Added patches to build with Photon 2.0
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 31.7.0-1
-	initial version
