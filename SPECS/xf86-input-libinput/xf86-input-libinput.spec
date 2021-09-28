%global security_hardening nonow
Summary:	Libinput input driver for the Xorg X server.
Name:		xf86-input-libinput
Version:	1.1.0
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-input-libinput=22acbdfe7a305ed90a9300dd02e0989c17e99b37
BuildRequires:	libinput-devel xorg-server-devel
Requires:	libinput xorg-server
%description
The X.Org Libinput Driver is a thin wrapper around libinput and allows for libinput to be used for input devices in X. This driver can be used as as drop-in replacement for evdev and synaptics. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libinput-devel xorg-server-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
%configure
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/X11/xorg.conf.d/40-libinput.conf
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_mandir}/*
%changelog
* Tue Aug 10 2021 Alexey Makhalov <amakhalov@vmware.com> 1.1.0-1
- initial version
