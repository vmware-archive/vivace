Summary:	Power Management
Name:		upower
Version:	0.9.23
Release:	1
License:	GPLv2+
URL:		http://upower.freedesktop.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://upower.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildRequires:	dbus-glib-devel gobject-introspection-devel gobject-introspection-python polkit-devel libusb-devel
Requires:	dbus-glib polkit libusb
%description
The UPower package provides an interface to enumerating power devices, listening to device events and querying history and statistics.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	dbus-glib-devel gobject-introspection-devel polkit-devel libusb-devel
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
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_localstatedir}/*
/lib/*
%{_libdir}/*
%exclude %{_libdir}/debug
%{_libexecdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.9.23-1
-	initial version
