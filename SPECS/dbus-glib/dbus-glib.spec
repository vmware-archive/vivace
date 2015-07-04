Summary:	glib interface for DBus API.
Name:		dbus-glib
Version:	0.104
Release:	1
License:	GPLv2+
URL:		http://dbus.freedesktop.org
Group:		Applications/File
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	dbus glib-devel
Requires:	dbus glib
%description
The D-Bus GLib package contains GLib interfaces to the D-Bus API.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}                 \
            --sysconfdir=%{_sysconfdir}         \
            --disable-static

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/debug
%{_datadir}/*
%{_libexecdir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.104-1
-	Initial build. First version
