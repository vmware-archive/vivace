%global debug_package %{nil}
Summary:	Firefox is a stand-alone browser based on the Mozilla codebase.
Name:		firefox
Version:	91.3.0
Release:	1%{?dist}
License:	MPLv1.1 or GPLv2+ or LGPLv2+
URL:		http://www.mozilla.org/projects/firefox
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://ftp.mozilla.org/pub/%{name}/releases/%{version}esr/source/%{name}-%{version}esr.source.tar.xz
%define sha1 firefox=bbd5d3a8d445115d9a70494d58f109ec15f2069e
Patch0:		fix-configure-failure-ignore-wrong-include-dirs.patch
Source1:        %{name}.desktop
BuildRequires:  clang-devel rust curl cbindgen nasm yasm
BuildRequires:	libevent-devel autoconf213 gtk2-devel gtk3-devel which python3-devel python3-libs unzip zip zlib-devel alsa-lib-devel libffi nodejs-devel libpng-devel libXcomposite-devel libnotify-devel libXcursor-devel dbus-glib-devel
BuildRequires:  nspr-devel >= 4.32
BuildRequires:  icu-devel >= 69.1
BuildRequires:  nss-devel >= 3.68
Requires:       gtk2 gtk3 libevent zlib alsa-lib libffi nodejs libpng libXcomposite libnotify libXcursor dbus-glib
Requires:       nspr >= 4.32
Requires:       icu >= 69.1
Requires:       nss >= 3.68
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

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
ac_add_options --disable-necko-wifi

# Uncomment these lines if you have installed optional dependencies:
#ac_add_options --enable-system-hunspell
#ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio
ac_add_options --enable-alsa

# Comment out following options if you have not installed
# recommended dependencies:
ac_add_options --with-system-icu
ac_add_options --with-system-libevent
#ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
#ac_add_options --with-system-webp

# You cannot distribute the binary if you do this
#ac_add_options --enable-official-branding

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

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=/usr
ac_add_options --enable-application=browser
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

# Optimization for size is broken with gcc7 and gcc6 for aarch64
# Build with gcc>=5 requires -fno-lifetime-dse
#ac_add_options --enable-optimize="-O2 -fno-lifetime-dse"

# The default level of optimization again produces a working build with gcc.
ac_add_options --enable-optimize

ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman
ac_add_options --with-system-jpeg
# --with-system-png won't work because the system's libpng doesn't have APNG support
#ac_add_options --with-system-png
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
export MACH_USE_SYSTEM_PYTHON=1
export MOZBUILD_STATE_PATH=${PWD}/mozbuild
./mach configure
./mach build
%install
DESTDIR=%{buildroot} MACH_USE_SYSTEM_PYTHON=1 ./mach install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}/
%changelog
* Tue Nov 23 2021 Alexey Makhalov <amakhalov@vmware.com> 91.3.0-1
- Version update
* Thu Aug 05 2021 Alexey Makhalov <amakhalov@vmware.com> 78.12.0-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 51.0.1-1
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 41.0-1
- Upgraded to version 41.0
* Thu May 28 2015 Alexey Makhalov <amakhalov@vmware.com> 38.0.1-1
- initial version
