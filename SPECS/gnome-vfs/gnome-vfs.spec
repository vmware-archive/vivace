Summary:	The GNOME Virtual File System
Name:		gnome-vfs
Version:	2.24.4
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
Patch0:		patch-port-glib2-2.6.31-and-up.diff
Patch1:		gnome-vfs2-g_memmove-no-more.patch
BuildRequires:	intltool libxml2-devel glib-devel dbus-glib-devel GConf-devel bzip2-devel gnome-mime-data
Requires:	libxml2 glib dbus-glib GConf bzip2 gnome-mime-data
%description
The GNOME Virtual File System package contains virtual file system libraries. This is used as one of the foundations of the Nautilus file manager.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p0
%patch1 -p1
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=/etc/gnome/2.30.2
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%{_libexecdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.4-1
-	initial version
