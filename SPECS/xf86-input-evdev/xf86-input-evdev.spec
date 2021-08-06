%global security_hardening nonow
Summary:	Generic Linux input driver for the Xorg X server.
Name:		xf86-input-evdev
Version:	2.10.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-input-evdev=660de292d5a40e2b8f385965c6a4e149c981ba59
BuildRequires:	libevdev-devel xorg-server-devel pixman-devel libpciaccess-devel mtdev-devel
Requires:	libevdev xorg-server pixman libpciaccess mtdev
%description
The Xorg Evdev Driver package contains Generic Linux input driver for the Xorg X server. It handles keyboard, mouse, touchpads and wacom devices, though for touchpad and wacom advanced handling, additional drivers are required.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libevdev-devel xorg-server-devel pixman-devel libpciaccess-devel mtdev-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/X11/xorg.conf.d/10-evdev.conf
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_mandir}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 2.10.6-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.9.2-1
- initial version
