Summary:	library for laying out and rendering of text.
Name:		pango
Version:	1.36.8
Release:	1
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.36/%{name}-%{version}.tar.xz
BuildRequires:	fontconfig-devel freetype2-devel glib-devel harfbuzz-devel cairo-devel pixman-devel libXft-devel libpng-devel libX11-devel libXrender-devel libXext-devel gobject-introspection-devel gobject-introspection-python python2-devel python2-libs
Requires:	fontconfig freetype2 cairo pixman libXft libpng libX11 libXrender libXext
%description
Pango is a library for laying out and rendering of text, with an emphasis on internationalization. It can be used anywhere that text layout is needed, though most of the work on Pango so far has been done in the context of the GTK+ widget toolkit.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
pango-querymodules --update-cache
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.36.8-1
-	initial version
