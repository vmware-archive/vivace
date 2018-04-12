Summary:	Mesa is an OpenGL compatible 3D graphics library.
Name:		mesa
Version:	17.2.6
Release:	1
License:	MIT
URL:		http://www.mesa3d.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.freedesktop.org/pub/%{name}/%{version}/%{name}-%{version}.tar.xz
%define sha1 mesa=03003f7d5966ef842d169020e95bcbdf92add055
BuildRequires:	libdrm-devel >= 2.4.88
BuildRequires:	libXdamage-devel libxshmfence-devel libXxf86vm-devel systemd-devel
Requires:	libdrm >= 2.4.88
Requires:	libXdamage libxshmfence libXxf86vm systemd
Provides:	pkgconfig(dri)
%description
Mesa is an OpenGL compatible 3D graphics library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libdrm-devel libXdamage-devel libxshmfence-devel libXxf86vm-devel systemd-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
# NOTE: texture-float is under patent
./configure CFLAGS='-O2' CXXFLAGS='-O2'        \
		--prefix=%{_prefix}	       \
		--sysconfdir=/etc              \
		--enable-texture-float         \
		--enable-gles1                 \
		--enable-gles2                 \
		--enable-osmesa                \
		--enable-xa                    \
		--enable-gbm                   \
		--enable-glx-tls               \
		--disable-omx		       \
		--with-egl-platforms="drm,x11" \
		--with-gallium-drivers="nouveau,r600,swrast,vc4" \
		--with-dri-drivers="nouveau,radeon,r200,swrast"

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
*	Thu Nov 30 2017 Alexey Makhalov <amakhalov@vmware.com> 17.2.6-1
-	Version update. Enable VC4 driver
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-1
-	Updated to version 11.1.2
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 10.5.5-1
-	initial version
