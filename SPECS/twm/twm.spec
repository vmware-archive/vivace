Summary:	A very minimal window manager.
Name:		twm
Version:	1.0.9
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	util-macros proto xorg-server-devel libX11-devel libXmu-devel libXaw-devel libXrender-devel libXft-devel libxkbfile-devel libXt-devel libSM-devel libICE-devel fontconfig-devel freetype2-devel libXext-devel
Requires:	xorg-server libX11 libXmu libXaw libXrender libXft libxkbfile libXt libSM libICE fontconfig freetype2 libXext
%description
The twm package contains a very minimal window manager.
%prep
%setup -q
%build
sed -i -e '/^rcdir =/s,^\(rcdir = \).*,\1/etc/X11/app-defaults,' src/Makefile.in &&
./configure --prefix=%{_prefix}
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
-	initial version
