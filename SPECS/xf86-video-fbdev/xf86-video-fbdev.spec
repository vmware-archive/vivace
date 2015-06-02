Summary:	X.Org Video Driver for framebuffer devices.
Name:		xf86-video-fbdev
Version:	0.4.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:	xorg-server-devel pixman-devel libpciaccess-devel
Requires:	xorg-server pixman libpciaccess
%description
The Xorg Fbdev Driver package contains the X.Org Video Driver for framebuffer devices. This driver is often used as fallback driver if the hardware specific and VESA drivers fail to load or are not present. If this driver is not installed, Xorg Server will print a warning on startup, but it can be safely ignored if hardware specific driver works well.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.4-1
-	initial version
