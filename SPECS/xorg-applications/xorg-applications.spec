Summary:	The Xorg applications.
Name:		xorg-applications
Version:	7.7
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/bdftopcf-1.0.5.tar.bz2
Source1:	http://ftp.x.org/pub/individual/app/iceauth-1.0.7.tar.bz2
Source2:	http://ftp.x.org/pub/individual/app/luit-1.1.1.tar.bz2
Source3:	http://ftp.x.org/pub/individual/app/mkfontdir-1.0.7.tar.bz2
Source4:	http://ftp.x.org/pub/individual/app/mkfontscale-1.1.2.tar.bz2
Source5:	http://ftp.x.org/pub/individual/app/sessreg-1.1.0.tar.bz2
Source6:	http://ftp.x.org/pub/individual/app/setxkbmap-1.3.1.tar.bz2
Source7:	http://ftp.x.org/pub/individual/app/smproxy-1.0.6.tar.bz2
Source8:	http://ftp.x.org/pub/individual/app/x11perf-1.6.0.tar.bz2
Source9:	http://ftp.x.org/pub/individual/app/xauth-1.0.9.tar.bz2
Source10:	http://ftp.x.org/pub/individual/app/xbacklight-1.2.1.tar.bz2
Source11:	http://ftp.x.org/pub/individual/app/xcmsdb-1.0.5.tar.bz2
Source12:	http://ftp.x.org/pub/individual/app/xcursorgen-1.0.6.tar.bz2
Source13:	http://ftp.x.org/pub/individual/app/xdpyinfo-1.3.2.tar.bz2
Source14:	http://ftp.x.org/pub/individual/app/xdriinfo-1.0.5.tar.bz2
Source15:	http://ftp.x.org/pub/individual/app/xev-1.2.2.tar.bz2
Source16:	http://ftp.x.org/pub/individual/app/xgamma-1.0.6.tar.bz2
Source17:	http://ftp.x.org/pub/individual/app/xhost-1.0.7.tar.bz2
Source18:	http://ftp.x.org/pub/individual/app/xinput-1.6.1.tar.bz2
Source19:	http://ftp.x.org/pub/individual/app/xkbcomp-1.3.0.tar.bz2
Source20:	http://ftp.x.org/pub/individual/app/xkbevd-1.1.4.tar.bz2
Source21:	http://ftp.x.org/pub/individual/app/xkbutils-1.0.4.tar.bz2
Source22:	http://ftp.x.org/pub/individual/app/xkill-1.0.4.tar.bz2
Source23:	http://ftp.x.org/pub/individual/app/xlsatoms-1.1.2.tar.bz2
Source24:	http://ftp.x.org/pub/individual/app/xlsclients-1.1.3.tar.bz2
Source25:	http://ftp.x.org/pub/individual/app/xmessage-1.0.4.tar.bz2
Source26:	http://ftp.x.org/pub/individual/app/xmodmap-1.0.9.tar.bz2
Source27:	http://ftp.x.org/pub/individual/app/xpr-1.0.4.tar.bz2
Source28:	http://ftp.x.org/pub/individual/app/xprop-1.2.2.tar.bz2
Source29:	http://ftp.x.org/pub/individual/app/xrandr-1.4.3.tar.bz2
Source30:	http://ftp.x.org/pub/individual/app/xrdb-1.1.0.tar.bz2
Source31:	http://ftp.x.org/pub/individual/app/xrefresh-1.0.5.tar.bz2
Source32:	http://ftp.x.org/pub/individual/app/xset-1.2.3.tar.bz2
Source33:	http://ftp.x.org/pub/individual/app/xsetroot-1.1.1.tar.bz2
Source34:	http://ftp.x.org/pub/individual/app/xvinfo-1.1.2.tar.bz2
Source35:	http://ftp.x.org/pub/individual/app/xwd-1.0.6.tar.bz2
Source36:	http://ftp.x.org/pub/individual/app/xwininfo-1.1.3.tar.bz2
Source37:	http://ftp.x.org/pub/individual/app/xwud-1.0.4.tar.bz2
BuildRequires:	pkg-config util-macros libpng-devel mesa-devel xbitmaps xcb-util-devel libfontenc-devel libXfont-devel libICE-devel libSM-devel libxkbfile-devel libX11-devel libXt-devel libXmu-devel libXext-devel libXcursor-devel libXrender-devel libXfixes-devel libXtst-devel libXi-devel libXrandr-devel libXxf86vm-devel libXinerama-devel libXaw-devel libXpm-devel libXv-devel freetype2-devel libXau-devel libxcb-devel
Requires:	libpng mesa xcb-util libfontenc libXfont libICE libSM libxkbfile libX11 libXt libXmu libXext libXcursor libXrender libXfixes libXtst libXi libXrandr libXxf86vm libXinerama libXaw libXpm libXv freetype2 libXau libxcb
%description
The Xorg applications provide the expected applications available in previous X Window implementations. 
%prep
%setup -q -c %{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37
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
	./configure --prefix=%{_prefix}
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
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
-	initial version
