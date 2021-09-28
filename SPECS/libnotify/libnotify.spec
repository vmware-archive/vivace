Summary:	The library to send desktop notifications
Name:		libnotify
Version:	0.7.9
Release:	1%{?dist}
License:	LGPLv2+
URL:		https://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/0.7/%{name}-%{version}.tar.xz
%define sha1 libnotify=75f80afad4d77b4968bfbcd47f4beea5ac2cc87b
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	gtk3-devel
Requires:	gtk3
%description
The libnotify library is used to send desktop notifications to a notification daemon, as defined in the Desktop Notifications spec.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gtk3-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release -Dintrospection=disabled -Ddocbook_docs=disabled -Dman=false -Dgtk_doc=false ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Sat Aug 07 2021 Alexey Makhalov <amakhalov@vmware.com> 0.7.9-1
- initial version
