%global debug_package %{nil}
Summary:	collection of GSettings schemas
Name:		gsettings-desktop-schemas
Version:	3.16.1
Release:	1
License:	GPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.16/%{name}-%{version}.tar.xz
%define sha1 gsettings-desktop-schemas=b7b0cd597f41410b92c2b4c8fbb9a3b3c0ba2749
BuildRequires:	intltool glib-devel glib-schemas gobject-introspection-devel gobject-introspection-python
Requires:	glib glib-schemas
%description
The GSettings Desktop Schemas package contains a collection of GSettings schemas for settings shared by various components of a GNOME Desktop.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel glib-schemas
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
glib-compile-schemas /usr/share/glib-2.0/schemas
%files
%defattr(-,root,root)
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%changelog
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 3.16.1-1
-	initial version
