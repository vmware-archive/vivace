Summary:	library that bridges ATK to At-Spi2 D-Bus service.
Name:		at-spi2-atk
Version:	2.38.0
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.38/%{name}-%{version}.tar.xz
%define sha1 at-spi2-atk=fc0a650bb0dd137889e882e33d9235ee9115df34
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	at-spi2-core-devel atk-devel glib-devel libX11-devel libxml2-devel
Requires:	at-spi2-core atk glib libX11 libxml2
Requires(post):	glib-schemas
%description
The At-Spi2 Atk package contains a library that bridges ATK to At-Spi2 D-Bus service.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	at-spi2-core-devel atk-devel glib-devel libX11-devel libxml2-devel
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
#%post
#glib-compile-schemas /usr/share/glib-2.0/schemas
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 2.38.0-1
- Version update
* Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
- initial version
