Summary:	GUI library.
Name:		gtk2
Version:	2.24.30
Release:	2	
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-%{version}.tar.xz
%define sha1 gtk+-2=aa5bc6dca583cf2bff137606dc2014f6ea559da7
BuildRequires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel xcairo-devel xfontconfig-devel libX11-devel
Requires:	atk gdk-pixbuf xpango libXinerama hicolor-icon-theme xcairo xfontconfig libX11
%description
The GTK+ 2 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n gtk+-%{version}
%build
sed -i 's#l \(gtk-.*\).sgml#& -o \1#' docs/{faq,tutorial}/Makefile.in &&
sed -i -e 's#pltcheck.sh#$(NULL)#g' gtk/Makefile.in                   &&
export PKG_CONFIG_PATH=/usr/lib/pkgconfig
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --with-gdktarget=x11
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
cat > %{buildroot}/etc/gtk-2.0/gtkrc << "EOF"
include "/usr/share/themes/Clearlooks/gtk-2.0/gtkrc"
gtk-icon-theme-name = "elementary"
EOF
%post
gtk-query-immodules-2.0 --update-cache
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.30-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon Aug 30 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.30-1
-	Upgraded to version 2.24.30 
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.28-1
-	initial version
