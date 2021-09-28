Summary:	MIME database
Name:		shared-mime-info
Version:	2.1
Release:	1%{?dist}
License:	GPLv2+
URL:		http://freedesktop.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://gitlab.freedesktop.org/xdg/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%define sha1 shared-mime-info=3d41d131350eec61e00f6fa26e6bfd6e242d8ef4
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	itstool xmlto glib-devel libxml2-devel
Requires:	itstool xmlto glib libxml2
%description
The Shared Mime Info package contains a MIME database. This allows central updates of MIME information for all supporting applications.
%prep
%autosetup
%build
sed -i "s/xmlto,/xmlto, '--skip-validation',/" data/meson.build
mkdir build
cd build
meson --prefix=/usr --buildtype=release -Dupdate-mimedb=true ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 2.1-1
- Version update
* Wed Jun 3 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4-1
- initial version
