Summary:	The Xorg fonts.
Name:		xorg-fonts
Version:	7.7
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/font/font-util-1.3.1.tar.bz2
Source1:	http://ftp.x.org/pub/individual/font/encodings-1.0.4.tar.bz2
Source2:	http://ftp.x.org/pub/individual/font/font-adobe-100dpi-1.0.3.tar.bz2
Source3:	http://ftp.x.org/pub/individual/font/font-adobe-75dpi-1.0.3.tar.bz2
Source4:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
Source5:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
Source6:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
Source7:	http://ftp.x.org/pub/individual/font/font-alias-1.0.3.tar.bz2
Source8:	http://ftp.x.org/pub/individual/font/font-arabic-misc-1.0.3.tar.bz2
Source9:	http://ftp.x.org/pub/individual/font/font-bh-100dpi-1.0.3.tar.bz2
Source10:	http://ftp.x.org/pub/individual/font/font-bh-75dpi-1.0.3.tar.bz2
Source11:	http://ftp.x.org/pub/individual/font/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
Source12:	http://ftp.x.org/pub/individual/font/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
Source13:	http://ftp.x.org/pub/individual/font/font-bh-ttf-1.0.3.tar.bz2
Source14:	http://ftp.x.org/pub/individual/font/font-bh-type1-1.0.3.tar.bz2
Source15:	http://ftp.x.org/pub/individual/font/font-bitstream-100dpi-1.0.3.tar.bz2
Source16:	http://ftp.x.org/pub/individual/font/font-bitstream-75dpi-1.0.3.tar.bz2
Source17:	http://ftp.x.org/pub/individual/font/font-bitstream-type1-1.0.3.tar.bz2
Source18:	http://ftp.x.org/pub/individual/font/font-cronyx-cyrillic-1.0.3.tar.bz2
Source19:	http://ftp.x.org/pub/individual/font/font-cursor-misc-1.0.3.tar.bz2
Source20:	http://ftp.x.org/pub/individual/font/font-daewoo-misc-1.0.3.tar.bz2
Source21:	http://ftp.x.org/pub/individual/font/font-dec-misc-1.0.3.tar.bz2
Source22:	http://ftp.x.org/pub/individual/font/font-ibm-type1-1.0.3.tar.bz2
Source23:	http://ftp.x.org/pub/individual/font/font-isas-misc-1.0.3.tar.bz2
Source24:	http://ftp.x.org/pub/individual/font/font-jis-misc-1.0.3.tar.bz2
Source25:	http://ftp.x.org/pub/individual/font/font-micro-misc-1.0.3.tar.bz2
Source26:	http://ftp.x.org/pub/individual/font/font-misc-cyrillic-1.0.3.tar.bz2
Source27:	http://ftp.x.org/pub/individual/font/font-misc-ethiopic-1.0.3.tar.bz2
Source28:	http://ftp.x.org/pub/individual/font/font-misc-meltho-1.0.3.tar.bz2
Source29:	http://ftp.x.org/pub/individual/font/font-misc-misc-1.1.2.tar.bz2
Source30:	http://ftp.x.org/pub/individual/font/font-mutt-misc-1.0.3.tar.bz2
Source31:	http://ftp.x.org/pub/individual/font/font-schumacher-misc-1.1.2.tar.bz2
Source32:	http://ftp.x.org/pub/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
Source33:	http://ftp.x.org/pub/individual/font/font-sony-misc-1.0.3.tar.bz2
Source34:	http://ftp.x.org/pub/individual/font/font-sun-misc-1.0.3.tar.bz2
Source35:	http://ftp.x.org/pub/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
Source36:	http://ftp.x.org/pub/individual/font/font-xfree86-type1-1.0.4.tar.bz2
BuildRequires:	pkg-config util-macros xcursor-themes xorg-applications libXfont-devel font-util
%description
The Xorg font packages provide needed fonts to the Xorg applications.
%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36
%build
for pkg in `ls` ; do
	pushd $pkg
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
install -vdm 755 %{buildroot}/usr/share/fonts
ln -svfn %{_prefix}/share/fonts/X11/OTF %{buildroot}/usr/share/fonts/X11-OTF
ln -svfn %{_prefix}/share/fonts/X11/TTF %{buildroot}/usr/share/fonts/X11-TTF
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_prefix}/*
%exclude %{_libdir}/debug/
%exclude %{_prefix}/src/
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
-	initial version
