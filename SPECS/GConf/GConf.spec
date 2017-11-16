Summary:	configuration database system used by many GNOME applications
Name:		GConf
Version:	3.2.5
Release:        2
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.2/%{name}-%{version}.tar.xz
%define sha1 GConf=340b3cb634ef64f0c31af9d971d4f3da95d1787c
BuildRequires:	intltool shadow libxml2-devel dbus-glib-devel polkit-devel
Requires:	libxml2 dbus-glib polkit dbus-devel
%description
The GConf package contains a configuration database system used by many GNOME applications.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libxml2-devel dbus-glib-devel polkit-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=/etc \
            --libexecdir=/usr/lib/GConf \
	    --disable-orbit \
	    --enable-defaults-service \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
ln -s gconf.xml.defaults %{buildroot}/etc/gconf/gconf.xml.system
%post
/sbin/ldconfig
if [ $1 -gt 1 ]; then
  if ! fgrep -q gconf.xml.system %{_sysconfdir}/gconf/2/path; then
    sed -i -e 's@xml:readwrite:$(HOME)/.gconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/gconf/gconf.xml.system@' %{_sysconfdir}/gconf/2/path
  fi
fi

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
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.2.5-2
-	Updated build requires
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 3.2.5-1
-	initial version
