Summary:	Mesa is an OpenGL compatible 3D graphics library.
Name:		mesa
Version:	21.1.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.mesa3d.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.freedesktop.org/pub/%{name}/%{version}/%{name}-%{version}.tar.xz
%define sha1 mesa=1490d713e3b3692189bba78a8c3660d6c8077fb5
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
BuildRequires:	libdrm-devel >= 2.4.88 libxshmfence-devel
BuildRequires:	libXdamage-devel libXxf86vm-devel systemd-devel libXrandr-devel
BuildRequires:	python3-mako expat-devel llvm-devel
#python3-mako has missing Requires python3-setuptools and python3-markupsafe, ading em here:
BuildRequires:  python3-setuptools python3-markupsafe
Requires:	libdrm >= 2.4.88 libxshmfence libllvm
Requires:	libXdamage libXxf86vm systemd libXrandr
Provides:	pkgconfig(dri)
%description
Mesa is an OpenGL compatible 3D graphics library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libdrm-devel libXdamage-devel libXxf86vm-devel systemd-devel libxshmfence-devel llvm-devel libXrandr-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
sed '1s/python/&3/' -i bin/symbols-check.py
mkdir build
cd build

meson --prefix=%{_prefix}            \
      --datadir=%{_datadir}/mesa     \
      --buildtype=release            \
      -Dplatforms="x11"              \
      -Ddri-drivers="i965,nouveau"   \
      -Dgallium-drivers="i915,nouveau,r600,radeonsi,svga,swrast,vc4" \
      -Dgallium-nine=false           \
      -Dglx=dri                      \
      -Dvalgrind=disabled            \
      -Dlibunwind=disabled           \
      ..

ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/*.pc
%{_datadir}/mesa/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 21.1.6-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 18.1.6-1
- Version update
* Thu Nov 30 2017 Alexey Makhalov <amakhalov@vmware.com> 17.2.6-1
- Version update. Enable VC4 driver
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-2
- Updated build requires & requires to build with Photon 2.0
* Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-1
- Updated to version 11.1.2
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 10.5.5-1
- initial version
