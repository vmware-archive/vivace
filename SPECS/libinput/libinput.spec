Summary:	Input devices handling library
Name:		libinput
Version:	1.18.1
Release:	1%{?dist}
License:	MIT
URL:		http://www.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
%define sha1 libinput=3440086fc24b6bb8e7f0c9386d11b2f548581e0f
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	libevdev-devel mtdev-devel systemd-devel
Requires:	libevdev mtdev systemd-udev
%description
libinput is a library that handles input devices for display servers and other applications that need to directly deal with input devices. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libevdev-devel mtdev-devel systemd-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
mkdir build
cd build
meson --prefix=/usr \
      --buildtype=release \
      -Ddebug-gui=false \
      -Dtests=false \
      -Ddocumentation=false \
      -Dlibwacom=false ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -rf %{buildroot}%{_datadir}/zsh
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
/usr/libexec/%{name}/
%{_datadir}/%{name}/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%{_mandir}/*
%changelog
* Tue Aug 10 2021 Alexey Makhalov <amakhalov@vmware.com> 1.18.1-1
- initial version
