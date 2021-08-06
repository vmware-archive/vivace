Summary:	library for handling OpenGL function pointer management.
Name:		libepoxy
Version:	1.5.8
Release:	1%{?dist}
License:	MIT
URL:		http://crux.nu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/anholt/libepoxy/releases/download/%{version}/%{name}-%{version}.tar.xz
%define sha1 libepoxy=3befbe7ec9bb1759d321d5490ea7ff33bf5b52b6
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	mesa-devel
Requires:	mesa
%description
libepoxy is a library for handling OpenGL function pointer management.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	mesa-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
mkdir build
cd build

meson --prefix=%{_prefix} \
      --buildtype=release ..
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.5.8-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 1.4.0-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2-1
- Initial version
