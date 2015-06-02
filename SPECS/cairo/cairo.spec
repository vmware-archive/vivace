Summary:	Cairo is a 2D graphics library with support for multiple output devices.
Name:		cairo
Version:	1.14.2
Release:	1
License:	LGPLv2 or MPLv1.1
URL:		http://cairographics.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.xz
BuildRequires:	util-macros proto libpng-devel glib-devel pixman-devel fontconfig-devel freetype2-devel libxcb-devel libXext-devel libXrender-devel libdrm-devel libX11-devel harfbuzz-devel 
Requires:	libpng glib pixman fontconfig freetype2 libxcb libXext libXrender libdrm libX11
%description
Cairo is a 2D graphics library with support for multiple output devices.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} \
	    --disable-static	\
	    --enable-tee
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.14.2-1
-	initial version
