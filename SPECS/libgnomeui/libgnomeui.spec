Summary:	The libgnomeui package contains libgnomeui libraries
Name:		libgnomeui
Version:	2.24.5
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires:	intltool libxml2-devel glib-devel gtk2-devel python2-libs python2-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel libgnomecanvas-devel libbonoboui-devel popt-devel libgnome-devel libbonobo-devel libSM-devel GConf-devel libart_lgpl-devel libICE-devel gnome-vfs-devel ORBit2-devel libgnome-keyring-devel libXinerama-devel dbus-glib-devel libglade-devel
Requires:	libxml2 glib gtk2 python2 cairo pango gdk-pixbuf atk pixman libpng libXrender libX11 libXext harfbuzz libgnomecanvas libbonoboui popt libgnome libbonobo libSM libICE libgnome-keyring libXinerama
%description
The libgnomeui package contains libgnomeui libraries.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.5-1
-	initial version
