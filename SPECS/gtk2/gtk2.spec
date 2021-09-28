Summary:	GUI library.
Name:		gtk2
Version:	2.24.33
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gtk.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-%{version}.tar.xz
%define sha1 gtk+-2=6fb0199cbb858456ba5d6fc9d7e4641f73476e76
BuildRequires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel
Requires:	atk gdk-pixbuf xpango libXinerama
%description
The GTK+ 2 package contains libraries used for creating graphical user interfaces for applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	atk-devel gdk-pixbuf-devel xpango-devel libXinerama-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup -n gtk+-%{version}
%build
sed -i 's#l \(gtk-.*\).sgml#& -o \1#' docs/{faq,tutorial}/Makefile.in &&
sed -i -e 's#pltcheck.sh#$(NULL)#g' gtk/Makefile.in                   &&
export PKG_CONFIG_PATH=/usr/lib/pkgconfig
%configure --with-gdktarget=x11
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
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
%exclude %{_libdir}/pkgconfig
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig
%{_libdir}/*.la
%{_datadir}/*
%changelog
* Thu Aug 05 2021 Alexey Makhalov <amakhalov@vmware.com> 2.24.33-1
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.30-2
- Updated build requires & requires to build with Photon 2.0
* Tue Aug 30 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.30-1
- Upgraded to version 2.24.30
* Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.28-1
- initial version
