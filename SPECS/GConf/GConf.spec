Summary:	configuration database system used by many GNOME applications
Name:		GConf
Version:	3.2.5
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.xz
BuildRequires:	intltool libxml2-devel glib-devel dbus-glib-devel
Requires:	libxml2 glib dbus-glib
%description
The GConf package contains a configuration database system used by many GNOME applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=/etc \
            --libexecdir=/usr/lib/GConf \
	    --disable-orbit \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
ln -s gconf.xml.defaults %{buildroot}/etc/gconf/gconf.xml.system
%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 3.2.5-1
-	initial version
