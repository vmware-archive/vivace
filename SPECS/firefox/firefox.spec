Summary:	Firefox is a stand-alone browser based on the Mozilla codebase.
Name:		firefox
Version:	38.0.1
Release:	1
License:	MPLv1.1 or GPLv2+ or LGPLv2+
URL:		http://www.mozilla.org/projects/firefox
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://ftp.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/source/%{name}-%{version}.source.tar.bz2
%define sha1 firefox=20f52c37e099cb2b21f3a76c6e39fe698e1e79e8
Source1:        %{name}.desktop
BuildRequires:	gtk2-devel which python2-devel python2-libs unzip zip nspr nss-devel icu-devel zlib-devel yasm-devel alsa-lib-devel libXt-devel libffi libXcomposite-devel libXfixes-devel libXdamage-devel
BuildRequires:	desktop-file-utils
Requires:	gtk2 nspr nss icu zlib yasm alsa-lib libXt libffi libXcomposite libXfixes libXdamage desktop-file-utils
%description
Firefox is a stand-alone browser based on the Mozilla codebase.
%prep
%setup -q -n mozilla-release
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
ac_add_options --enable-application=browser

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
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

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
EOF
# Firefox build is multithreaded by itself
make -f client.mk
%install
make -f client.mk DESTDIR=%{buildroot} install INSTALL_SDK=
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
#In order to make branding work in a generic way, We find
#all the icons that are likely to be used for desktop files
#and install them appropriately
find browser/branding/official -name "default*.png" | tee icons.list
for i in $(cat icons.list) ; do
    size=$(echo $i | sed "s/.*default\([0-9]*\).png$/\1/")
    icondir=%{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/
    mkdir -p $icondir
    cp -a $i ${icondir}%{name}.png
done
rm icons.list #cleanup
%post
#this is needed to get gnome-panel to update the icons
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
    %{_bindir}/gtk-update-icon-cache --quiet ${_datadir}/icons/hicolor &> /dev/null || :
fi

%postun
#this is needed to get gnome-panel to update the icons
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
    %{_bindir}/gtk-update-icon-cache --quiet ${_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/
%{_datadir}/icons/
%changelog
*	Thu May 28 2015 Alexey Makhalov <amakhalov@vmware.com> 38.0.1-1
-	initial version
