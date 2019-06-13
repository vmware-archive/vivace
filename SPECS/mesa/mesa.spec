Summary:	Mesa is an OpenGL compatible 3D graphics library.
Name:		mesa
Version:	18.1.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.mesa3d.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.freedesktop.org/pub/%{name}/%{version}/%{name}-%{version}.tar.xz
%define sha1 mesa=8d4daf725f20404f980b981c9693b58756ba6c48
BuildRequires:	libdrm-devel >= 2.4.88 libxshmfence-devel
BuildRequires:	libXdamage-devel libXxf86vm-devel systemd-devel
BuildRequires:	python3-mako expat-devel llvm-devel
Requires:	libdrm >= 2.4.88 libxshmfence llvm
Requires:	libXdamage libXxf86vm systemd
Provides:	pkgconfig(dri)
%description
Mesa is an OpenGL compatible 3D graphics library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libdrm-devel libXdamage-devel libXxf86vm-devel systemd-devel libxshmfence-devel llvm-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
sh ./configure CFLAGS='-O2' CXXFLAGS='-O2' LDFLAGS=-lLLVM \
               --prefix=%{_prefix}            \
               --sysconfdir=/etc              \
               --enable-texture-float         \
               --enable-osmesa                \
               --enable-xa                    \
               --enable-gbm                   \
               --enable-glx-tls               \
               --with-platforms="drm,x11" \
               --with-gallium-drivers="i915,nouveau,r600,radeonsi,svga,swrast,vc4"

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%exclude %{_libdir}/pkgconfig/*.pc
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%changelog
*	Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 18.1.6-1
-	Version update
*	Thu Nov 30 2017 Alexey Makhalov <amakhalov@vmware.com> 17.2.6-1
-	Version update. Enable VC4 driver
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-1
-	Updated to version 11.1.2
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 10.5.5-1
-	initial version
