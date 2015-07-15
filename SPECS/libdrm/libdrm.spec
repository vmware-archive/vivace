Summary:	user space library for accessing the DRM.
Name:		libdrm
Version:	2.4.61
Release:	1
License:	MIT
URL:		http://dri.freedesktop.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
%define sha1 libdrm=fce70371540af0490541b05d96c6b6b43f1fab80
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
sed -e "/pthread-stubs/d" -i configure.ac &&
autoreconf -fiv &&
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 2.4.61-1
-	initial version
