%define debug_package %{nil}

Summary:	C# bindings for dbus-glib
Name:		dbus-sharp-glib
Version:	0.5
Release:	1
License:	MIT
URL:		http://mono.github.com/dbus-sharp-glib/
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/downloads/mono/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool gettext glib-devel tzdata mono-devel mono-extras dbus-sharp
Requires:	gettext glib mono dbus-sharp
%description
D-Bus glib mono bindings for use with mono programs.
%prep
%setup -q

%build
# Mono 4
sed -i configure.ac \
	    -e "s#gmcs#mcs#g"
autoreconf -vif
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_libdir}
%changelog
*	Tue Jun 23 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5-1
-	initial version
