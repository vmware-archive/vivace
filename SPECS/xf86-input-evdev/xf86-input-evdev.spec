%global security_hardening nonow
Summary:	Generic Linux input driver for the Xorg X server.
Name:		xf86-input-evdev
Version:	2.9.2
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:	libevdev-devel xorg-server-devel pixman-devel libpciaccess-devel
Requires:	libevdev xorg-server pixman libpciaccess
%description
The Xorg Evdev Driver package contains Generic Linux input driver for the Xorg X server. It handles keyboard, mouse, touchpads and wacom devices, though for touchpad and wacom advanced handling, additional drivers are required. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_mandir}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.9.2-1
-	initial version
