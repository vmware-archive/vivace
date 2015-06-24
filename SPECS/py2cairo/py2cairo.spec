Name:           py2cairo
Version:        1.10.0
Release:	1
Summary:        Python Bindings for Cairo
Group:          Development/Languages
License:        LGPLv2+
Vendor:		VMware, Inc.
Distribution:	Photon
URL:            http://cairographics.org
Source0:        http://cairographics.org/releases/%{name}-%{version}.tar.bz2
BuildRequires: 	python2-devel pkg-config
BuildRequires: 	python2-libs
BuildRequires:	cairo-devel libxcb-devel libX11-devel
BuildRequires:	libpng-devel glib-devel pixman-devel fontconfig-devel freetype2-devel libXext-devel libXrender-devel libdrm-devel harfbuzz-devel 
Requires:	python2 cairo

%description
Python bindings for Cairo.

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix}
./waf build

%install
./waf install --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/*
%{_includedir}/*

%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.10.0-1
-	Initial build.	First version
