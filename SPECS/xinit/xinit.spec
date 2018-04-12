Summary:	The xinit package contains a usable script to start the xserver.
Name:		xinit
Version:	1.3.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
%define sha1 xinit=de3469080d73ced1f7d7a1803e813bc6ea352072
BuildRequires:	libX11-devel
#Requires:	libX11 twm xclock xterm xf86-input-evdev xf86-video-intel xf86-input-vmmouse xf86-video-vmware xf86-video-fbdev
Requires:	libX11 twm xclock xterm xf86-input-evdev xf86-video-fbdev
%description
The xinit package contains a usable script to start the xserver.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --with-xinitdir=/etc/X11/app-defaults
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.4-1
-	initial version
