%global debug_package %{nil}
Summary:	Firefox is a stand-alone browser based on the Mozilla codebase.
Name:		firefox
Version:	78.12.0
Release:	1%{?dist}
License:	MPLv1.1 or GPLv2+ or LGPLv2+
URL:		http://www.mozilla.org/projects/firefox
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://ftp.mozilla.org/pub/%{name}/releases/%{version}esr/source/%{name}-%{version}esr.source.tar.xz
%define sha1 firefox=83ae378d8bddd9efc5badb99a6246979313f7134
Patch0:		fix-configure-failure-ignore-wrong-include-dirs.patch
Source1:        %{name}.desktop
BuildRequires:  clang-devel rust curl cbindgen nasm yasm
BuildRequires:	libevent-devel autoconf213 gtk2-devel gtk3-devel which python3-devel python3-libs unzip zip nspr-devel nss-devel icu-devel zlib-devel alsa-lib-devel libffi nodejs-devel libpng-devel libXcomposite-devel libnotify-devel libXcursor-devel dbus-glib-devel
#BuildRequires:	desktop-file-utils
# GConf-devel libXdamage-devel libXt-devel
Requires:	gtk2 gtk3 nspr nss icu libevent zlib alsa-lib libffi nodejs libpng libXcomposite libnotify libXcursor dbus-glib
#desktop-file-utils
# GConf libXdamage libXt
%description
Firefox is a stand-alone browser based on the Mozilla codebase.
%prep
%autosetup -p1
%build
cat > mozconfig << "EOF"
# If you have a multicore machine, all cores will be used by default.
# If desired, you can reduce the number of cores used, e.g. to 1, by
# uncommenting the next line and setting a valid number of CPU cores.
#mk_add_options MOZ_MAKE_FLAGS="-j1"

# If you have installed DBus-Glib comment out this line:
#ac_add_options --disable-dbus

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
ac_add_options --disable-necko-wifi

# Uncomment this option if you wish to build with gtk+-3
#ac_add_options --enable-default-toolkit=cairo-gtk3

# Uncomment these lines if you have installed optional dependencies:
#ac_add_options --enable-system-hunspell
#ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio
ac_add_options --enable-alsa

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

# Disabling debug symbols makes the build much smaller and a little
# faster. Comment this if you need to run a debugger. Note: This is
# required for compilation on i686.
ac_add_options --disable-debug-symbols

# The elf-hack is reported to cause failed installs (after successful builds)
# on some machines. It is supposed to improve startup time and it shrinks
# libxul.so by a few MB - comment this if you know your machine is not affected.
ac_add_options --disable-elf-hack

# You cannot distribute the binary if you do this
ac_add_options --enable-official-branding

# Optimization for size is broken with gcc7 and gcc6 for aarch64
# Build with gcc>=5 requires -fno-lifetime-dse
#ac_add_options --enable-optimize="-O2 -fno-lifetime-dse"

# The default level of optimization again produces a working build with gcc.
ac_add_options --enable-optimize

# From firefox-40, using system cairo causes firefox to crash
# frequently when it is doing background rendering in a tab.
# This appears to again work in firefox-56
#ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-system-jpeg
# --with-system-png won't work because the system's libpng doesn't have APNG support
# ac_add_options --with-system-png
ac_add_options --with-system-zlib

# The following option unsets Telemetry Reporting. With the Addons Fiasco,
# Mozilla was found to be collecting user's data, including saved passwords and
# web form data, without users consent. Mozilla was also found shipping updates
# to systems without the user's knowledge or permission.
# As a result of this, use the following command to permanently disable
# telemetry reporting in Firefox.
unset MOZ_TELEMETRY_REPORTING

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
EOF
# libevent changed macros names in v 2.1
#sed -i 's/_EVENT_SIZEOF/EVENT__SIZEOF/' ipc/chromium/src/base/message_pump_libevent.cc

#make some fixes required by glibc-2.28:
#sed -i '/unistd/a #include <sys/sysmacros.h>' xpcom/io/nsLocalFileUnix.cpp

# Firefox build is multithreaded by itself
export AUTOCONF=/usr/bin/autoconf2.13
export CC=gcc CXX=g++
export MOZBUILD_STATE_PATH=${PWD}/mozbuild
./mach configure
./mach build
%install
DESTDIR=%{buildroot} ./mach install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}/
%changelog
* Thu Aug 05 2021 Alexey Makhalov <amakhalov@vmware.com> 78.12.0-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 51.0.1-1
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 41.0-1
- Upgraded to version 41.0
* Thu May 28 2015 Alexey Makhalov <amakhalov@vmware.com> 38.0.1-1
- initial version
