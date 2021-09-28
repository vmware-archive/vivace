Summary:	library for laying out and rendering of text.
Name:		xpango
Version:	1.48.7
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/pango/1.48/pango-%{version}.tar.xz
%define sha1 pango=b6ea5a5fd68070eea94b598efbc77d0ae11b6783
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	glib-devel xcairo-devel libXft-devel harfbuzz-devel fribidi-devel
Requires:	glib xcairo harfbuzz libXft fribidi
%description
Pango is a library for laying out and rendering of text, with an emphasis on internationalization. It can be used anywhere that text layout is needed, though most of the work on Pango so far has been done in the context of the GTK+ widget toolkit.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel xcairo-devel libXft-devel harfbuzz-devel fribidi-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup -n pango-%{version}
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%post
pango-querymodules --update-cache
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.48.7-1
- Version update
* Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.38.1-1
- Updated to version 1.38.1
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.36.8-1
- initial version
