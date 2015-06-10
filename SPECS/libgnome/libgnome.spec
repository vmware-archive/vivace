Summary:	The libgnomeui package contains GNOME library
Name:		libgnome
Version:	2.32.1
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.bz2
Patch0:		libgnome-glib-2_36.patch
BuildRequires:	intltool libxml2-devel glib-devel gtk2-devel python2-libs python2-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel libglade-devel libart_lgpl-devel fontconfig-devel freetype2-devel libXinerama-devel libbonobo-devel GConf-devel gnome-vfs-devel popt-devel ORBit2-devel dbus-glib-devel
Requires:	libxml2 glib gtk2 python2 cairo pango gdk-pixbuf atk pixman libpng libXrender libX11 libXext harfbuzz libglade libart_lgpl fontconfig freetype2 libXinerama libbonobo GConf gnome-vfs popt ORBit2 dbus-glib
%description
The libgnome package contains the libgnome library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p0
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
