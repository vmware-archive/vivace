Summary:	The Xorg applications.
Name:		xorg-applications
Version:	7.7
Release:	3%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/iceauth-1.0.8.tar.bz2
%define sha1 iceauth=2ce23c40a17d98badeb8ce70d26e81a5ac0e178c
Source1:	http://ftp.x.org/pub/individual/app/luit-1.1.1.tar.bz2
%define sha1 luit=3130c14d7267cecce0ba2280643844b48cca49b0
Source2:	http://ftp.x.org/pub/individual/app/mkfontscale-1.2.1.tar.bz2
%define sha1 mkfontscale=fb9d0458a4476a237609b676f9cebcc64b0a8a85
Source3:	http://ftp.x.org/pub/individual/app/sessreg-1.1.2.tar.bz2
%define sha1 sessreg=169c1ff9fb152b4b4ca0cfbd3e1aee33af042016
Source4:	http://ftp.x.org/pub/individual/app/setxkbmap-1.3.2.tar.bz2
%define sha1 setxkbmap=44783734bc58fca93165a20da0bb3eca1ccb9ad9
Source5:	http://ftp.x.org/pub/individual/app/smproxy-1.0.6.tar.bz2
%define sha1 smproxy=bbb374ad7e184af7bcada70b90df81f82b9b71ad
Source6:	http://ftp.x.org/pub/individual/app/x11perf-1.6.1.tar.bz2
%define sha1 x11perf=c54ebef80b6cb565397fe2e3069e0d7470027e5a
Source7:	http://ftp.x.org/pub/individual/app/xauth-1.1.tar.bz2
%define sha1 xauth=16180e36d75a23cb182cb91e78f24273f1a63967
Source8:	http://ftp.x.org/pub/individual/app/xbacklight-1.2.3.tar.bz2
%define sha1 xbacklight=f0a6163738143ec23542b459aef567309a119e0c
Source9:	http://ftp.x.org/pub/individual/app/xcmsdb-1.0.5.tar.bz2
%define sha1 xcmsdb=b1d09b1a9a4324fa86c85340ae47cc34743423a9
Source10:	http://ftp.x.org/pub/individual/app/xcursorgen-1.0.7.tar.bz2
%define sha1 xcursorgen=109367eb23b0ad52cf5de15f50c02ebe872698ae
Source11:	http://ftp.x.org/pub/individual/app/xdpyinfo-1.3.2.tar.bz2
%define sha1 xdpyinfo=0922fc31f8fc82ac20e326a6c9eb33ed7d57ad87
Source12:	http://ftp.x.org/pub/individual/app/xdriinfo-1.0.6.tar.bz2
%define sha1 xdriinfo=11682ae1f04a311b832651d78bbf4c6ac77f0ed9
Source13:	http://ftp.x.org/pub/individual/app/xev-1.2.4.tar.bz2
%define sha1 xev=76d182ba0f57449fbc7a7a467dfb7f1df767b873
Source14:       http://ftp.x.org/pub/individual/app/xgamma-1.0.6.tar.bz2
%define sha1 xgamma=af1484d0d70bc71dc9d3b7b95645881b7165c41b
Source15:	http://ftp.x.org/pub/individual/app/xhost-1.0.8.tar.bz2
%define sha1 xhost=971670858a464d4f8eeb6f4e182f9fcd94149790
Source16:	http://ftp.x.org/pub/individual/app/xinput-1.6.3.tar.bz2
%define sha1 xinput=92ea7dfb3d8465921b0dca85da7d5b01cedae6c8
Source17:       http://ftp.x.org/pub/individual/app/xkbcomp-1.4.5.tar.bz2
%define sha1 xkbcomp=3505b70268572375078982cab98aeb96f72ff14c
Source18:	http://ftp.x.org/pub/individual/app/xkbevd-1.1.4.tar.bz2
%define sha1 xkbevd=629fea940692f9d971dfae36cd697b13337caaba
Source19:	http://ftp.x.org/pub/individual/app/xkbutils-1.0.4.tar.bz2
%define sha1 xkbutils=b09aef7cc3853eb12dbda332f55adec3add4447b
Source20:	http://ftp.x.org/pub/individual/app/xkill-1.0.5.tar.bz2
%define sha1 xkill=c5ee06b33adb252a41e4f737be6bd47651ff582a
Source21:	http://ftp.x.org/pub/individual/app/xlsatoms-1.1.3.tar.bz2
%define sha1 xlsatoms=9fdb1e8df6bb08529a812ac90f63d500bf5174cc
Source22:	http://ftp.x.org/pub/individual/app/xlsclients-1.1.4.tar.bz2
%define sha1 xlsclients=175af1c216a1db3de5023ecd6cce186e7693c6e4
Source23:	http://ftp.x.org/pub/individual/app/xmessage-1.0.5.tar.bz2
%define sha1 xmessage=d3eca72c7173d0d9547c676a16bcec51ca1213a2
Source24:	http://ftp.x.org/pub/individual/app/xmodmap-1.0.10.tar.bz2
%define sha1 xmodmap=69e041f8a8c501bd1feb68805a0880633a685bc8
Source25:	http://ftp.x.org/pub/individual/app/xpr-1.0.5.tar.bz2
%define sha1 xpr-1.0.5=0632c7d8632ac9d23f285811aaea805a2956e155
Source26:       http://ftp.x.org/pub/individual/app/xprop-1.2.5.tar.bz2
%define sha1 xprop=b2b69b50f0906df54c7e9fa4457f509650799417
Source27:	http://ftp.x.org/pub/individual/app/xrandr-1.5.1.tar.xz
%define sha1 xrandr=9f72957e0d2a26ece509336ea7e1529cc9ea881e
Source28:	http://ftp.x.org/pub/individual/app/xrdb-1.2.0.tar.bz2
%define sha1 xrdb=79596928246288a217abdec0e4a2315ec9b07963
Source29:	http://ftp.x.org/pub/individual/app/xrefresh-1.0.6.tar.bz2
%define sha1 xrefresh=11eb5b3f905631281d2cedd86a0b666bab0d9bdc
Source30:	http://ftp.x.org/pub/individual/app/xset-1.2.4.tar.bz2
%define sha1 xset-1.2.4=41a857f30ff5bb0dfbda1549bb703984344ea228
Source31:	http://ftp.x.org/pub/individual/app/xsetroot-1.1.2.tar.bz2
%define sha1 xsetroot=42ab81761823b44974feab86477007c49dbace50
Source32:	http://ftp.x.org/pub/individual/app/xvinfo-1.1.4.tar.bz2
%define sha1 xvinfo=136a70a72b23c81f4fe8f4c8cb7073316be16b44
Source33:	http://ftp.x.org/pub/individual/app/xwd-1.0.7.tar.bz2
%define sha1 xwd=65ce0617be29687cf6082c3a0e85d15a0dcccda9
Source34:	http://ftp.x.org/pub/individual/app/xwininfo-1.1.5.tar.bz2
%define sha1 xwininfo=9f67b1eb07c5824d437bf577cf6198962af1aeb7
Source35:	http://ftp.x.org/pub/individual/app/xwud-1.0.5.tar.bz2
%define sha1 xwud=a85d84a1b81f8e667ea6ac126d447590c93eb079
BuildRequires:	libpng-devel mesa-devel xbitmaps xcb-util-devel libxkbfile-devel libX11-devel libXt-devel libXmu-devel libXext-devel libXcursor-devel libXrender-devel libXfixes-devel libXtst-devel libXi-devel libXrandr-devel libXxf86vm-devel libXinerama-devel libXaw-devel libXpm-devel libXv-devel freetype2-devel libXau-devel libXfont2-devel
Requires:	libpng mesa xcb-util libxkbfile libX11 libXt libXmu libXext libXcursor libXrender libXfixes libXtst libXi libXrandr libXxf86vm libXinerama libXaw libXpm libXv freetype2 libXau libXfont2
%description
The Xorg applications provide the expected applications available in previous X Window implementations.
%description
The Xorg applications provide the expected applications available in previous X Window implementations.
%prep
# Using autosetup is not feasible
%setup -q -c %{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35
%build
for pkg in `ls` ; do
	pushd $pkg
	case $pkg in
	  luit-[0-9]* )
	    line1="#ifdef _XOPEN_SOURCE"
	    line2="#  undef _XOPEN_SOURCE"
	    line3="#  define _XOPEN_SOURCE 600"
	    line4="#endif"

	    sed -i -e "s@#ifdef HAVE_CONFIG_H@$line1\n$line2\n$line3\n$line4\n\n&@" sys.c
	    unset line1 line2 line3 line4
	  ;;
	  sessreg-* )
	    sed -e 's/\$(CPP) \$(DEFS)/$(CPP) -P $(DEFS)/' -i man/Makefile.in
	  ;;
	esac
	%configure
	make %{?_smp_mflags}
	popd
done
%install
for pkg in `ls` ; do
	pushd $pkg
	make DESTDIR=%{buildroot} install
	popd
done
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_prefix}/*
%exclude %{_libdir}/debug/
%exclude %{_prefix}/src/
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 7.7-3
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 7.7-2
- Updated build requires & requires to build with Photon 2.0
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
- initial version
