Summary:	libglade libraries
Name:		libglade
Version:	2.6.4
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
BuildRequires:	intltool libxml2-devel glib-devel gtk2-devel python2-libs python2-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel
Requires:	libxml2 glib gtk2 python2 cairo pango gdk-pixbuf atk pixman libpng libXrender libX11 libXext harfbuzz
%description
The libglade package contains libglade libraries. These are useful for loading Glade interface files in a program at runtime.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
sed -i '/DG_DISABLE_DEPRECATED/d' glade/Makefile.in
./configure --prefix=%{_prefix} --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.6.4-1
-	initial version
