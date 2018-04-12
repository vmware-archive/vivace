Summary:	The Xorg protocol headers.
Name:		proto
Version:	7.7
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
BuildArchitectures: noarch
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/proto/bigreqsproto-1.1.2.tar.bz2
%define sha1 bigreqsproto=ef1765eeb5e9e38d080225fe6a64ed7cd2984b46
Source1:	http://ftp.x.org/pub/individual/proto/compositeproto-0.4.2.tar.bz2
%define sha1 compositeproto=aa7b5abcfd5bbfad7cb681ce89dc1d6e381e3044
Source2:	http://ftp.x.org/pub/individual/proto/damageproto-1.2.1.tar.bz2
%define sha1 damageproto=bd0f0f4dc8f37eaabd9279d10fe2889710507358
Source3:	http://ftp.x.org/pub/individual/proto/dmxproto-2.3.1.tar.bz2
%define sha1 dmxproto=3b8b273b8ef3d8dbab998df9ec1dddf99edf4d91
Source4:	http://ftp.x.org/pub/individual/proto/dri2proto-2.8.tar.bz2
%define sha1 dri2proto=2bc4e8f00778b1f3fe58b4c4f93607ac2adafbbf
Source5:	http://ftp.x.org/pub/individual/proto/dri3proto-1.0.tar.bz2
%define sha1 dri3proto=1007eaa2f83022653a224f7d2e676ea51cba2f2b
Source6:	http://ftp.x.org/pub/individual/proto/fixesproto-5.0.tar.bz2
%define sha1 fixesproto=ab605af5da8c98c0c2f8b2c578fed7c864ee996a
Source7:	http://ftp.x.org/pub/individual/proto/fontsproto-2.1.3.tar.bz2
%define sha1 fontsproto=28c108bd6438c332122c10871c1fc6415591755f
Source8:	http://ftp.x.org/pub/individual/proto/glproto-1.4.17.tar.bz2
%define sha1 glproto=20e061c463bed415051f0f89e968e331a2078551
Source9:	http://ftp.x.org/pub/individual/proto/inputproto-2.3.1.tar.bz2
%define sha1 inputproto=126b6ad57b5432e154485f900920765eae8fda45
Source10:	http://ftp.x.org/pub/individual/proto/kbproto-1.0.6.tar.bz2
%define sha1 kbproto=a2cc82357c22a1f4d6243017982c32703c95575c
Source11:	http://ftp.x.org/pub/individual/proto/presentproto-1.0.tar.bz2
%define sha1 presentproto=432371cdc464881029c3f39f9bf81cc80a484e54
Source12:	http://ftp.x.org/pub/individual/proto/randrproto-1.4.1.tar.bz2
%define sha1 randrproto=7cd1daf5c56336079303d675b5a6788c90204016
Source13:	http://ftp.x.org/pub/individual/proto/recordproto-1.14.2.tar.bz2
%define sha1 recordproto=1f48c4b0004d8b133efd0498e8d88d68d3b9199c
Source14:	http://ftp.x.org/pub/individual/proto/renderproto-0.11.1.tar.bz2
%define sha1 renderproto=7ae9868a358859fe539482b02414aa15c2d8b1e4
Source15:	http://ftp.x.org/pub/individual/proto/resourceproto-1.2.0.tar.bz2
%define sha1 resourceproto=9ff9bb9243b0474330959dc3853973523c9dd9ce
Source16:	http://ftp.x.org/pub/individual/proto/scrnsaverproto-1.2.2.tar.bz2
%define sha1 scrnsaverproto=640a2cbef5893aacda74799e6fa4d973e629b753
Source17:	http://ftp.x.org/pub/individual/proto/videoproto-2.3.2.tar.bz2
%define sha1 videoproto=aa60e3b93c6a78ad03f1c502b910e7c45faaedbc
Source18:	http://ftp.x.org/pub/individual/proto/xcmiscproto-1.2.2.tar.bz2
%define sha1 xcmiscproto=59ae9ec6414964440bf654b207618e5dd66a32fb
Source19:	http://ftp.x.org/pub/individual/proto/xextproto-7.3.0.tar.bz2
%define sha1 xextproto=b8d736342dcb73b71584d99a1cb9806d93c25ff8
Source20:	http://ftp.x.org/pub/individual/proto/xf86bigfontproto-1.2.0.tar.bz2
%define sha1 xf86bigfontproto=312a2ea708b257520c1af4393b69d73a393a478f
Source21:	http://ftp.x.org/pub/individual/proto/xf86dgaproto-2.1.tar.bz2
%define sha1 xf86dgaproto=97a06120e7195c968875e8ba42e82c90ab54948b
Source22:	http://ftp.x.org/pub/individual/proto/xf86driproto-2.1.1.tar.bz2
%define sha1 xf86driproto=23e861f40ba0f0cbbfd7db7ba2ef623762ffca17
Source23:	http://ftp.x.org/pub/individual/proto/xf86vidmodeproto-2.3.1.tar.bz2
%define sha1 xf86vidmodeproto=11d54c3210887631ea71e8f8030a77692e964fc4
Source24:	http://ftp.x.org/pub/individual/proto/xineramaproto-1.2.1.tar.bz2
%define sha1 xineramaproto=818bffc16139d6e3de4344c83f00c495d3536753
Source25:	http://ftp.x.org/pub/individual/proto/xproto-7.0.27.tar.bz2
%define sha1 xproto=b34e7438623c8016cc8338549e5fcc29e2f64034
BuildRequires:	pkg-config
BuildRequires:	util-macros
Provides:	pkgconfig(xproto)
%description
The Xorg protocol headers provide the header files required to build the system, and to allow other applications to build against the installed X Window system.
%prep
%setup -q -c %{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25

%build
for pkg in `ls` ; do
	pushd $pkg
	%configure
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
%{_prefix}/*
%changelog
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
-	initial version
