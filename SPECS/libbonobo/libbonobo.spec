Summary:	Document system for GNOME-2
Name:		libbonobo
Version:	2.32.1
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.bz2
Patch0:		libbonobo-glib-2_36.patch	
BuildRequires:	intltool libxml2-devel glib-devel gtk2-devel python2-libs python2-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel libglade-devel libart_lgpl-devel fontconfig-devel freetype2-devel libXinerama-devel popt-devel ORBit2-devel
Requires:	libxml2 glib gtk2 python2 cairo pango gdk-pixbuf atk pixman libpng libXrender libX11 libXext harfbuzz libglade libart_lgpl fontconfig freetype2 libXinerama popt ORBit2
%description
The libbonobo package contains libbonobo libraries. This is a component and compound document system for GNOME-2.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p1
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=/etc/gnome/2.30.2 \
            --localstatedir=/var/lib       \
	    --mandir=%{_prefix}/share/man  \
	    --disable-canberra
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%{_libexecdir}
%{_sbindir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.32.1-1
-	initial version
