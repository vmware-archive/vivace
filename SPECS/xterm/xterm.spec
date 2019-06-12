Summary:	Xterm is a terminal emulator for the X Window System. 
Name:		xterm
Version:	318
Release:	1%{?dist}
License:	MIT
URL:		http://invisible-island.net/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://invisible-island.net/%{name}/%{name}-%{version}.tgz
%define sha1 xterm=6717a0f2ff445bb1f83cd92828b5f784a10023c3
BuildRequires:	proto libXaw-devel libX11-devel libXt-devel libXmu-devel ncurses-devel
Requires:	xorg-applications libXaw libX11 libXt libXmu ncurses
%description
xterm is a terminal emulator for the X Window System. 
%prep
%setup -q
%build
sed -i '/v0/{n;s/new:/new:kb=^?:/}' termcap &&
printf '\tkbs=\\177,\n' >> terminfo &&
TERMINFO=/usr/share/terminfo \
./configure --prefix=%{_prefix} --with-app-defaults=/etc/X11/app-defaults
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
#make DESTDIR=%{buildroot} install-ti
cat >> %{buildroot}/etc/X11/app-defaults/XTerm << "EOF"
*VT100*locale: true
*VT100*faceName: Monospace
*VT100*faceSize: 10
*backarrowKeyIsErase: true
*ptyInitialErase: true
EOF
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*
%exclude %{_libdir}
%exclude %{_prefix}/src/
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 318-1
-	initial version
