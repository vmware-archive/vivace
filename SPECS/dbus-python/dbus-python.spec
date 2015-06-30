Summary:	Dbus bindings for python
Name:		dbus-python
Version:	1.2.0
Release:	1
License:	MIT
URL:		http://www.freedesktop.org/wiki/Software/DBusBindings/
Group:		User Interface/Library
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	intltool dbus dbus-glib-devel glib-devel python2-devel python2-libs
Requires:	dbus dbus-glib glib python2
%description
D-Bus python bindings for use with python programs.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure PYTHON=python --prefix=%{_prefix} 
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Jun 24 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.0-1
-	Initial build. First version
