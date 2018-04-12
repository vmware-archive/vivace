#%global debug_package %{nil}
Summary:	Firefox is a stand-alone browser based on the Mozilla codebase.
Name:		firefox
Version:	51.0.1
Release:	1
License:	MPLv1.1 or GPLv2+ or LGPLv2+
URL:		http://www.mozilla.org/projects/firefox
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://ftp.mozilla.org/pub/%{name}/releases/%{version}/source/%{name}-%{version}.source.tar.xz
%define sha1 firefox=b73255fd4f90fd0c1b107b566679da2df3f31cf1
Source1:        %{name}.desktop
Patch0:         Build-Skia-NEON-code-on-arm64.patch
#Patch1:         Disable-gcc-lifetime-dead-store-elimination-for-operator-new.patch
#Patch0:		fix_icu_vernum_firefox.patch
#Patch1:		firefox-build-with-gcc6.patch
#Patch2:		aarch64-no-static-sizes.patch
BuildRequires:	GConf-devel libevent-devel GConf autoconf213 gtk2-devel which python2-devel python2-libs unzip zip nspr-devel nss-devel icu-devel zlib-devel yasm-devel alsa-lib-devel libXt-devel libffi libXcomposite-devel libXfixes-devel libXdamage-devel
BuildRequires:	desktop-file-utils
Requires:	gtk2 nspr nss icu libevent zlib GConf yasm alsa-lib libXt libffi libXcomposite libXfixes libXdamage desktop-file-utils
%description
Firefox is a stand-alone browser based on the Mozilla codebase.
%prep
%setup -q
%patch0 -p1
#%patch1 -p1
#%patch2 -p0
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

# Uncomment this option if you wish to build with gtk+-2
ac_add_options --enable-default-toolkit=cairo-gtk2

# Uncomment these lines if you have installed optional dependencies:
#ac_add_options --enable-system-hunspell
#ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio
#ac_add_options --enable-alsa


# If you have installed GConf, comment out this line
ac_add_options --disable-gconf

# Stylo is the new CSS code, including the rust 'style'
# package. It is enabled by default but requires clang.
# Uncomment this if you do not wish to use stylo.
#ac_add_options --disable-stylo

# Comment out following options if you have not installed
# recommended dependencies:
# configure: error: System SQLite library is not compiled with SQLITE_SECURE_DELETE. 
#ac_add_options --enable-system-sqlite
ac_add_options --with-system-libevent
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

ac_add_options --disable-strip
ac_add_options --disable-install-strip

ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

# Optimization for size is broken with gcc7 and gcc6 for aarch64
# Build with gcc>=5 requires -fno-lifetime-dse
ac_add_options --enable-optimize="-O2 -fno-lifetime-dse"

# From firefox-40, using system cairo causes firefox to crash
# frequently when it is doing background rendering in a tab.
# This appears to again work in firefox-56
#ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-pthreads

ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
# configure: error: System PNG library is not compiled with APNG. 
#ac_add_options --with-system-png
ac_add_options --with-system-zlib

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
EOF
# libevent changed macros names in v 2.1
sed -i 's/_EVENT_SIZEOF/EVENT__SIZEOF/' ipc/chromium/src/base/message_pump_libevent.cc
# Firefox build is multithreaded by itself
export AUTOCONF=/usr/bin/autoconf2.13 &&
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
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 41.0-1
-	Upgraded to version 41.0
*	Thu May 28 2015 Alexey Makhalov <amakhalov@vmware.com> 38.0.1-1
-	initial version
