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
Source1:	http://ftp.x.org/pub/individual/proto/compositeproto-0.4.2.tar.bz2
Source2:	http://ftp.x.org/pub/individual/proto/damageproto-1.2.1.tar.bz2
Source3:	http://ftp.x.org/pub/individual/proto/dmxproto-2.3.1.tar.bz2
Source4:	http://ftp.x.org/pub/individual/proto/dri2proto-2.8.tar.bz2
Source5:	http://ftp.x.org/pub/individual/proto/dri3proto-1.0.tar.bz2
Source6:	http://ftp.x.org/pub/individual/proto/fixesproto-5.0.tar.bz2
Source7:	http://ftp.x.org/pub/individual/proto/fontsproto-2.1.3.tar.bz2
Source8:	http://ftp.x.org/pub/individual/proto/glproto-1.4.17.tar.bz2
Source9:	http://ftp.x.org/pub/individual/proto/inputproto-2.3.1.tar.bz2
Source10:	http://ftp.x.org/pub/individual/proto/kbproto-1.0.6.tar.bz2
Source11:	http://ftp.x.org/pub/individual/proto/presentproto-1.0.tar.bz2
Source12:	http://ftp.x.org/pub/individual/proto/randrproto-1.4.1.tar.bz2
Source13:	http://ftp.x.org/pub/individual/proto/recordproto-1.14.2.tar.bz2
Source14:	http://ftp.x.org/pub/individual/proto/renderproto-0.11.1.tar.bz2
Source15:	http://ftp.x.org/pub/individual/proto/resourceproto-1.2.0.tar.bz2
Source16:	http://ftp.x.org/pub/individual/proto/scrnsaverproto-1.2.2.tar.bz2
Source17:	http://ftp.x.org/pub/individual/proto/videoproto-2.3.2.tar.bz2
Source18:	http://ftp.x.org/pub/individual/proto/xcmiscproto-1.2.2.tar.bz2
Source19:	http://ftp.x.org/pub/individual/proto/xextproto-7.3.0.tar.bz2
Source20:	http://ftp.x.org/pub/individual/proto/xf86bigfontproto-1.2.0.tar.bz2
Source21:	http://ftp.x.org/pub/individual/proto/xf86dgaproto-2.1.tar.bz2
Source22:	http://ftp.x.org/pub/individual/proto/xf86driproto-2.1.1.tar.bz2
Source23:	http://ftp.x.org/pub/individual/proto/xf86vidmodeproto-2.3.1.tar.bz2
Source24:	http://ftp.x.org/pub/individual/proto/xineramaproto-1.2.1.tar.bz2
Source25:	http://ftp.x.org/pub/individual/proto/xproto-7.0.27.tar.bz2
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
	./configure --prefix=%{_prefix}
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
