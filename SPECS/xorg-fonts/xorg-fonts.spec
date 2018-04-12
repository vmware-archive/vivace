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
%define sha1 font-util=0b16add3637c64b0bbaf1dd223b71b0421100c20
Source1:	http://ftp.x.org/pub/individual/font/encodings-1.0.4.tar.bz2
%define sha1 encodings-1.0.4.tar.bz2=24ace2470403f85a0d393769204029bd8247992a
Source2:	http://ftp.x.org/pub/individual/font/font-adobe-100dpi-1.0.3.tar.bz2
%define sha1 font-adobe-100dpi-1.0.3.tar.bz2=53311cbd604f18bd9570727105a4222473d363e3
Source3:	http://ftp.x.org/pub/individual/font/font-adobe-75dpi-1.0.3.tar.bz2
%define sha1 font-adobe-75dpi-1.0.3.tar.bz2=6a2ec569336b5646682a14eee3c7790274beffd1
Source4:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
%define sha1 font-adobe-utopia-100dpi-1.0.4.tar.bz2=9e80cf5bbd5522a5cfad2a9f8f8fce86de0f0226
Source5:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
%define sha1 font-adobe-utopia-75dpi-1.0.4.tar.bz2=50e837322a09f1a7c40fb78fc6aad1a157284507
Source6:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
%define sha1 font-adobe-utopia-type1-1.0.4.tar.bz2=3113cfafb91c2c53df6a1fae57dca6c50fb8ce20
Source7:	http://ftp.x.org/pub/individual/font/font-alias-1.0.3.tar.bz2
%define sha1 font-alias-1.0.3.tar.bz2=96b0aa38f88a54ef32ab85d3eef6f29b0437f70d
Source8:	http://ftp.x.org/pub/individual/font/font-arabic-misc-1.0.3.tar.bz2
%define sha1 font-arabic-misc-1.0.3.tar.bz2=322ae41e74deea8de11fa077fd0e0191927a667c
Source9:	http://ftp.x.org/pub/individual/font/font-bh-100dpi-1.0.3.tar.bz2
%define sha1 font-bh-100dpi-1.0.3.tar.bz2=47d5e50be9e78695017650a088da52bfcf1eeb40
Source10:	http://ftp.x.org/pub/individual/font/font-bh-75dpi-1.0.3.tar.bz2
%define sha1 font-bh-75dpi-1.0.3.tar.bz2=7290567d42a0f5adb6a3ad170524bb7ed59871d7
Source11:	http://ftp.x.org/pub/individual/font/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
%define sha1 font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2=bc4f804e49db8c6add04f52ffb1c0cd63e714b2c
Source12:	http://ftp.x.org/pub/individual/font/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
%define sha1 font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2=3c6678e6bbb2bd352baaf610a8f6aac9c5140c85
Source13:	http://ftp.x.org/pub/individual/font/font-bh-ttf-1.0.3.tar.bz2
%define sha1 font-bh-ttf-1.0.3.tar.bz2=f42ebd527096011040a312e0f9cdf78d64177419
Source14:	http://ftp.x.org/pub/individual/font/font-bh-type1-1.0.3.tar.bz2
%define sha1 font-bh-type1-1.0.3.tar.bz2=69ff038d38015cd305a4cd4d1a921fe3bd08bbde
Source15:	http://ftp.x.org/pub/individual/font/font-bitstream-100dpi-1.0.3.tar.bz2
%define sha1 font-bitstream-100dpi-1.0.3.tar.bz2=138376f8683c09b9068c7c124842a7af9f0fcc2e
Source16:	http://ftp.x.org/pub/individual/font/font-bitstream-75dpi-1.0.3.tar.bz2
%define sha1 font-bitstream-75dpi-1.0.3.tar.bz2=975e9f7872483394ebd87610f8bbc924d99bea34
Source17:	http://ftp.x.org/pub/individual/font/font-bitstream-type1-1.0.3.tar.bz2
%define sha1 font-bitstream-type1-1.0.3.tar.bz2=7633551be3525c501278e81259b22ad9a893de4d
Source18:	http://ftp.x.org/pub/individual/font/font-cronyx-cyrillic-1.0.3.tar.bz2
%define sha1 font-cronyx-cyrillic-1.0.3.tar.bz2=e5af8c2e8fb23955808a08bd38728ab3ad284d61
Source19:	http://ftp.x.org/pub/individual/font/font-cursor-misc-1.0.3.tar.bz2
%define sha1 font-cursor-misc-1.0.3.tar.bz2=1649271129bbeff3aeee70a9da87a8e5e59162c1
Source20:	http://ftp.x.org/pub/individual/font/font-daewoo-misc-1.0.3.tar.bz2
%define sha1 font-daewoo-misc-1.0.3.tar.bz2=0c7b24e08e6d42eb006d79ae7ab4bbf446d59f7a
Source21:	http://ftp.x.org/pub/individual/font/font-dec-misc-1.0.3.tar.bz2
%define sha1 font-dec-misc-1.0.3.tar.bz2=a748d35b8b0241abd3e1d85f80da318b529a74d0
Source22:	http://ftp.x.org/pub/individual/font/font-ibm-type1-1.0.3.tar.bz2
%define sha1 font-ibm-type1-1.0.3.tar.bz2=bfc7d0a3aa0f96bf61ea26d6b3f5afbbdd0f35f6
Source23:	http://ftp.x.org/pub/individual/font/font-isas-misc-1.0.3.tar.bz2
%define sha1 font-isas-misc-1.0.3.tar.bz2=cbd9bf441b25362123c817b1aa7a7be1ee4a9321
Source24:	http://ftp.x.org/pub/individual/font/font-jis-misc-1.0.3.tar.bz2
%define sha1 font-jis-misc-1.0.3.tar.bz2=8c08c5fe01d4605f2886822cb3655548a6535e58
Source25:	http://ftp.x.org/pub/individual/font/font-micro-misc-1.0.3.tar.bz2
%define sha1 font-micro-misc-1.0.3.tar.bz2=db3e912d41bda20f60b520c19e65bd7134ee1224
Source26:	http://ftp.x.org/pub/individual/font/font-misc-cyrillic-1.0.3.tar.bz2
%define sha1 font-misc-cyrillic-1.0.3.tar.bz2=9c0e283ae59e7b05c0798fe0645cc822d22dcb0c
Source27:	http://ftp.x.org/pub/individual/font/font-misc-ethiopic-1.0.3.tar.bz2
%define sha1 font-misc-ethiopic-1.0.3.tar.bz2=3f6af53047cb1206d737e8e8fbbbbb315c5419bb
Source28:	http://ftp.x.org/pub/individual/font/font-misc-meltho-1.0.3.tar.bz2
%define sha1 font-misc-meltho-1.0.3.tar.bz2=f0693ea8fbc1d43177014155a0ecd2516348b51b
Source29:	http://ftp.x.org/pub/individual/font/font-misc-misc-1.1.2.tar.bz2
%define sha1 font-misc-misc-1.1.2.tar.bz2=c6d28c56880807963175cbbd682fb6f75a35f77d
Source30:	http://ftp.x.org/pub/individual/font/font-mutt-misc-1.0.3.tar.bz2
%define sha1 font-mutt-misc-1.0.3.tar.bz2=245d3041d9138b7e4a00858228adad2de304043b
Source31:	http://ftp.x.org/pub/individual/font/font-schumacher-misc-1.1.2.tar.bz2
%define sha1 font-schumacher-misc-1.1.2.tar.bz2=fbe3629e9dcc03d12300d4ebab64fd038ea98952
Source32:	http://ftp.x.org/pub/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
%define sha1 font-screen-cyrillic-1.0.4.tar.bz2=de1f0226f74d7e4d3ee9ab0b9c87478ab2a7db30
Source33:	http://ftp.x.org/pub/individual/font/font-sony-misc-1.0.3.tar.bz2
%define sha1 font-sony-misc-1.0.3.tar.bz2=8d0dd87148283c8ac8c5ac37906b12fab5ddb1d8
Source34:	http://ftp.x.org/pub/individual/font/font-sun-misc-1.0.3.tar.bz2
%define sha1 font-sun-misc-1.0.3.tar.bz2=6a72602557bb5dfe46c1ee3b56658aeed1e04f9d
Source35:	http://ftp.x.org/pub/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
%define sha1 font-winitzki-cyrillic-1.0.3.tar.bz2=29249b49eac7e3f32d7a1a93808fcfd9d399011c
Source36:	http://ftp.x.org/pub/individual/font/font-xfree86-type1-1.0.4.tar.bz2
%define sha1 font-xfree86-type1-1.0.4.tar.bz2=1381f274a178cbd08627560e17a4a8f6653be3f7
BuildRequires:	pkg-config util-macros xcursor-themes xorg-applications libXfont-devel font-util
%description
The Xorg font packages provide needed fonts to the Xorg applications.
%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36
%build
for pkg in `ls` ; do
	pushd $pkg
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
