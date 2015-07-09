Summary:	GUI library.
Name:		gtk2
Version:	2.24.28
Release:	1
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-%{version}.tar.xz
BuildRequires:	atk-devel gdk-pixbuf-devel pango-devel libXinerama-devel
Requires:	atk gdk-pixbuf pango libXinerama hicolor-icon-theme
%description
The GTK+ 2 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel pango-devel libXinerama-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n gtk+-%{version}
%build
sed -i 's#l \(gtk-.*\).sgml#& -o \1#' docs/{faq,tutorial}/Makefile.in &&
sed -i -e 's#pltcheck.sh#$(NULL)#g' gtk/Makefile.in                   &&
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.28-1
-	initial version
