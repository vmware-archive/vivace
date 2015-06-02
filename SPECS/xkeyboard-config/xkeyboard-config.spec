Summary:	The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
Name:		xkeyboard-config
Version:	2.14
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
BuildRequires:	pkg-config intltool util-macros proto libX11-devel  
Requires:	libX11
#BuildRequires:	pkg-config util-macros libpng-devel mesa-devel xbitmaps xcb-util-devel libfontenc-devel libXfont-devel libICE-devel libSM-devel libxkbfile-devel libX11-devel libXt-devel libXmu-devel libXext-devel libXcursor-devel libXrender-devel libXfixes-devel libXtst-devel libXi-devel libXrandr-devel libXxf86vm-devel libXinerama-devel libXaw-devel libXpm-devel libXv-devel freetype2-devel libXau-devel libxcb-devel
#Requires:	libpng mesa xcb-util libfontenc libXfont libICE libSM libxkbfile libX11 libXt libXmu libXext libXcursor libXrender libXfixes libXtst libXi libXrandr libXxf86vm libXinerama libXaw libXpm libXv freetype2 libXau libxcb
%description
The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --with-xkb-rules-symlink=xorg
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.14-1
-	initial version
