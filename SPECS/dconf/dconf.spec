Summary:	A low-level configuration system
Name:		dconf
Version:	0.15.0
Release:	1
License: 	LGPLv2.1+
URL:		https://wiki.gnome.org/action/show/Projects/dconf
Source0: 	http://download.gnome.org/sources/dconf/0.15/%{name}-%{version}.tar.xz
%define sha1 dconf=8449a5c090dd7e845f513b2d7ad18ba5dcc3dda7
Group: 		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	dbus
BuildRequires:	intltool gtk3-devel
BuildRequires:	desktop-file-utils gobject-introspection-devel
Requires:	dbus gobject-introspection gtk3

%description
dconf is a low-level configuration system. Its main purpose is to provide a backend to GSettings on platforms that don't already have configuration storage systems. 
%package devel
Summary:	Development libraries and header files 
Requires:	dbus gtk3-devel
Requires:	intltool desktop-file-utils
Requires:	libxslt gobject-introspection-devel

%description devel
The package contains libraries and header files for
developing applications.

%prep
%setup -q

%build
./configure \
			--prefix=%{_prefix} \
			--disable-static \
			--enable-man=no \
			--disable-editor  
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files

%defattr(-,root,root)
%doc COPYING NEWS
%{_bindir}/dconf
%{_libexecdir}
%{_datadir}/dbus-1
%{_datadir}/bash-completion
%{_datadir}/locale
%{_libdir}
%exclude %{_libdir}/debug

%files devel
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/dconf/
%{_includedir}
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/dconf.*
%changelog
*	Wed Jul 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.15.0-1
-	Initial build. First version

