Summary:	Accessibility interfaces to have full access to view and control running applications.
Name:		atk
Version:	2.36.0
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.36/%{name}-%{version}.tar.xz
%define sha1 atk=7e4accf756bb76323acf7f91d8618e739aff56e6
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
#BuildRequires:	gobject-introspection-devel python3-gobject-introspection
BuildRequires:  glib-devel
Requires:	glib
%description
ATK provides the set of accessibility interfaces that are implemented by other toolkits and applications. Using the ATK interfaces, accessibility tools have full access to view and control running applications.
%package	devel
Summary:	Header and development files for
Requires:	%{name} = %{version}
#Requires:	gobject-introspection-devel python3-gobject-introspection
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release -Dintrospection=false ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Thu Aug 05 2021 Alexey Makhalov <amakhalov@vmware.com> 2.36.0-1
- Version update
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
- initial version
