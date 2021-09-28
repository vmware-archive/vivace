Summary:	Service Provider Interface for the Assistive Technologies.
Name:		at-spi2-core
Version:	2.40.3
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.40/%{name}-%{version}.tar.xz
%define sha1 at-spi2-core=f6830b2a618f61b4ace5f47104d87cd0697536d6
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	intltool glib-devel dbus-devel libX11-devel libXtst-devel libXext-devel libXi-devel
Requires:	dbus glib libX11 libXtst libXext libXi
%description
The At-Spi2 Core package is a part of the GNOME Accessibility Project. It provides a Service Provider Interface for the Assistive Technologies available on the GNOME platform and a library against which applications can be linked.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel dbus-devel libX11-devel libXtst-devel libXext-devel libXi-devel
%description	devel
It contains the libraries and header files to create applications

%prep
%autosetup
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_libexecdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 2.40.3-1
- Version update
* Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
- initial version
