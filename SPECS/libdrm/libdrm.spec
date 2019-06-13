Summary:	user space library for accessing the DRM.
Name:		libdrm
Version:	2.4.98
Release:	1%{?dist}
License:	MIT
URL:		http://dri.freedesktop.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
%define sha1 libdrm=4c8a11870a89f59c294bef0109939a7ffaa1fb26
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
#sed -e "/pthread-stubs/d" -i configure.ac &&
#autoreconf -fiv &&
%configure --enable-intel
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/libdrm/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 2.4.98-1
-	Version update
*	Thu Nov 30 2017 Alexey Makhalov <amakhalov@vmware.com> 2.4.88-1
-	Version update
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.4.67-1
-	Updated to version
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 2.4.61-1
-	initial version
