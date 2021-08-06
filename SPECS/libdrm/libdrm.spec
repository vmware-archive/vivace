Summary:	user space library for accessing the DRM.
Name:		libdrm
Version:	2.4.107
Release:	1%{?dist}
License:	MIT
URL:		http://dri.freedesktop.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz
%define sha1 libdrm=372eb85849d1858a892dc5569edfa278640a9732
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	libXmu-devel libXpm-devel libpciaccess-devel
Requires:	libXmu libXpm libpciaccess
Provides:	pkgconfig(libdrm)
%description
libdrm provides a user space library for accessing the DRM, direct rendering manager, on operating systems that support the ioctl interface. libdrm is a low-level library, typically used by graphics drivers such as the Mesa DRI drivers, the X drivers, libva and similar projects.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXmu-devel libXpm-devel libpciaccess-devel
%description	devel
libdrm provides a user space library for accessing the DRM, direct rendering manager, on operating systems that support the ioctl interface. libdrm is a low-level library, typically used by graphics drivers such as the Mesa DRI drivers, the X drivers, libva and similar projects.
%prep
%setup -q
%build
mkdir build
cd build

meson --prefix=%{_prefix} \
      --buildtype=release   \
      -Dudev=true           \
      -Dvalgrind=false
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/libdrm/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 2.4.107-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 2.4.98-1
- Version update
* Thu Nov 30 2017 Alexey Makhalov <amakhalov@vmware.com> 2.4.88-1
- Version update
* Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.4.67-1
- Updated to version
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 2.4.61-1
- initial version
