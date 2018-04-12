Summary:	A full-featured port of the WebKit rendering engine.
Name:		libwebkit
Version:	1.9.92
Release:	2	
License:	LGPLv2+
URL:		http://webkitgtk.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://webkitgtk.org/releases/webkit-1.9.92.tar.xz
Patch0:		libwebkit-bison-3.0-fix.patch
Patch1:		libwebkit-socket-error-fix.patch
%define sha1 webkit=6314dc6cd716de1380c5f8e62c76db3f2d5cbed8
BuildRequires:  bison automake
BuildRequires:  gtk2-devel
BuildRequires:  flex which mesa-devel
BuildRequires:  gcc gtk-doc 
BuildRequires:  ruby bash 
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  libjpeg-turbo-devel icu-devel
BuildRequires:  libsoup-devel libX11-devel
BuildRequires:  libxslt-devel libXcomposite-devel
BuildRequires:  sqlite-devel
Requires:	gstreamer-plugins-base icu
Requires:	libsoup
Requires:	libjpeg-turbo
Requires:	sqlite-libs
Requires:	gtk3
Requires:	libxslt
Requires:	gtk2
Requires:	mesa
Requires:	libX11
Requires:	libXcomposite

%description
WebKitGTK+ is a full-featured port of the WebKit rendering engine, suitable for projects requiring any kind of web integration, from hybrid HTML/CSS applications to full-fledged web browsers.

%package devel
Group:          Development/Libraries/C and C++
Summary:        Development Library for rendering web content
Requires:       %{name} = %{version}
%description devel
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  

%package doc
Group:          Development/Libraries/C and C++
Summary:        Documentation for libwebkit, a development Library for rendering web content
Requires:       %{name} = %{version}
%description doc
Documentation for libwebkit, a development Library for rendering web content

%prep
%setup -q -n webkit-%{version}
%patch0 -p1
%patch1 -p1

%build
export LIBS='-lrt -lm -lpthread'
./configure --prefix=%{_prefix} \
			--enable-geolocation=no \
			--enable-video=no \
			--with-gtk=2.0 \
			--enable-webkit2=no
			
env - PATH=$PATH USER=$USER HOME=$HOME make	%{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files  
%defattr(-, root, root)
/usr/bin
%{_libdir}/*.so.*
/usr/libexec
%{_datadir}/locale

%files devel 
%defattr(-, root, root)
%{_includedir}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig
%{_datadir}/webkitgtk-1.0

%files doc 
%defattr(-, root, root)
%{_datadir}/gtk-doc

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.9.92-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Oct 01 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.9.92-1
-	initial version
