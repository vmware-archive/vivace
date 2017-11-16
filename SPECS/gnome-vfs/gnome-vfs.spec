Summary:	The GNOME Virtual File System
Name:		gnome-vfs
Version:	2.24.4
Release:	2	
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
%define sha1 gnome-vfs=0dc634e7dd979fd218f378902c0ca1af80738961
Patch0:		gnome-vfs-2.24.1-disable-gnome-mime-data.patch
Patch1:		gnome-vfs2-g_memmove-no-more.patch
BuildRequires:	shadow intltool libxml2-devel dbus-glib-devel GConf-devel bzip2-devel gtk-doc
Requires:	libxml2 dbus-glib GConf bzip2
%description
The GNOME Virtual File System package contains virtual file system libraries. This is used as one of the foundations of the Nautilus file manager.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool libxml2-devel dbus-glib-devel GConf-devel bzip2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Fix build with automake 1.13, which does not like $(srcdir) in TESTS statements
sed -i 's:$(srcdir)/auto-test:../auto-test:' test/Makefile.am

%build
gtkdocize --copy
autoreconf -f -i
CFLAGS="%optflags -fno-strict-aliasing" \
./configure --prefix=%{_prefix} \
            --disable-static \
            --sysconfdir=/etc \
	    --with-pic \
	    --disable-howl
# fix compilation against new glib2
echo "#undef G_DISABLE_DEPRECATED" >> config.h
make %{?_smp_mflags}
%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=%{buildroot} install INSTALL="install -p"
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_sysconfdir}
%{_libexecdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.4-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.4-1
-	initial version
