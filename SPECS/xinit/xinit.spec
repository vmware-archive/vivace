Summary:	The xinit package contains a usable script to start the xserver.
Name:		xinit
Version:	1.4.1
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
%define sha1 xinit=d874a2eecf2c30291e327851b151fdab8183260c
BuildRequires:	libX11-devel
#Requires:	libX11 twm xclock xterm xf86-input-evdev xf86-video-intel xf86-input-vmmouse xf86-video-vmware xf86-video-fbdev
Requires:	libX11 dwm xterm xf86-input-evdev xf86-video-fbdev
%description
The xinit package contains a usable script to start the xserver.
%prep
%setup -q
%build
%configure --with-xinitdir=/etc/X11/app-defaults
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.4.1-1
- Version update
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.4-1
- initial version
