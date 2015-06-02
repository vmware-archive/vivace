Summary:	X11 font utilities.
Name:		font-util
Version:	1.3.1
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/font/font-util-1.3.1.tar.bz2
#BuildRequires:	pkg-config util-macros xcursor-themes xorg-applications libXfont-devel
#BuildRequires:	pkg-config util-macros xcursor-themes xorg-applications libXfont-devel
#BuildRequires:	pkg-config util-macros libpng-devel mesa-devel xbitmaps xcb-util-devel libfontenc-devel libXfont-devel libICE-devel libSM-devel libxkbfile-devel libX11-devel libXt-devel libXmu-devel libXext-devel libXcursor-devel libXrender-devel libXfixes-devel libXtst-devel libXi-devel libXrandr-devel libXxf86vm-devel libXinerama-devel libXaw-devel libXpm-devel libXv-devel freetype2-devel libXau-devel libxcb-devel
#Requires:	libpng mesa xcb-util libfontenc libXfont libICE libSM libxkbfile libX11 libXt libXmu libXext libXcursor libXrender libXfixes libXtst libXi libXrandr libXxf86vm libXinerama libXaw libXpm libXv freetype2 libXau libxcb
%description
The Xorg font utilities.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.1-1
-	initial version
