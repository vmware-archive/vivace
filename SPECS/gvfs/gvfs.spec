Summary:	Userspace Virtual File System
Name:		gvfs
Version:	1.22.4
Release:	1
License:	GPLv3 and LGPLv2+ and BSD and MPLv2.0
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.24/%{name}-%{version}.tar.xz
BuildRequires:	intltool dbus-glib-devel fuse-devel libxml2-devel libarchive-devel libgcrypt-devel gtk3-devel
Requires:	libxml2 dbus-glib fuse glib-schemas libarchive libgcrypt gtk3
%description
The Gvfs package is a userspace virtual filesystem designed to work with the I/O abstractions of GLib's GIO library
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool libxml2-devel dbus-glib-devel fuse-devel libarchive-devel libgcrypt-devel gtk3-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
	    --disable-gphoto2 \
	    --enable-documentation=no
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_libexecdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Jul 8 2015 Alexey Makhalov <amakhalov@vmware.com> 1.24.1-1
-	initial version
