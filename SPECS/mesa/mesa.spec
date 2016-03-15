Summary:	Mesa is an OpenGL compatible 3D graphics library.
Name:		mesa
Version:	11.1.2
Release:	1
License:	MIT
URL:		http://www.mesa3d.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.freedesktop.org/pub/%{name}/%{version}/%{name}-%{version}.tar.gz
%define sha1 mesa=a9600ccb8350ef490f1d3c3fa9d93bcb347b87b7
BuildRequires:	libdrm-devel libXdamage-devel libxshmfence-devel libXxf86vm-devel systemd 
Requires:	libdrm libXdamage libxshmfence libXxf86vm systemd
Provides:	pkgconfig(dri)
%description
Mesa is an OpenGL compatible 3D graphics library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libdrm-devel libXdamage-devel libxshmfence-devel libXxf86vm-devel systemd 
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
		--with-gallium-drivers="nouveau,r600,svga,swrast"
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 11.1.2-1
-	Updated to version 11.1.2
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 10.5.5-1
-	initial version
