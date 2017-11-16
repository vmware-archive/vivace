Summary:	Power Management
Name:		upower
Version:	0.9.23
Release:	2	
License:	GPLv2+
URL:		http://upower.freedesktop.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://upower.freedesktop.org/releases/%{name}-%{version}.tar.xz
%define sha1 upower=8fc30c2d53b15c0a4e7c1bc077a912bc1aeb6138
BuildRequires:	dbus-glib-devel gobject-introspection-devel gobject-introspection-python polkit-devel libusb-devel intltool
BuildRequires:	libgudev-devel
Requires:	dbus-glib polkit libusb
Requires:	libgudev
%description
The UPower package provides an interface to enumerating power devices, listening to device events and querying history and statistics.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	dbus-glib-devel gobject-introspection-devel polkit-devel libusb-devel
Requires:	libgudev-devel
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
	    --localstatedir=%{_localstatedir} \
	    --enable-deprecated \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mv %{buildroot}/rules.d %{buildroot}/usr/lib/udev
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_localstatedir}/*
%{_libdir}/*
%exclude %{_libdir}/debug
%{_libexecdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.9.23-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.9.23-1
-	initial version
