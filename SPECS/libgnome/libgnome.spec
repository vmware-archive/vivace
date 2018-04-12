Summary:	The libgnomeui package contains GNOME library
Name:		libgnome
Version:	2.32.1
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.bz2
%define sha1 libgnome=a6bc277ff90ca2f83b91c5bc5222f03ab553a52b
Patch0:		libgnome-glib-2_36.patch
BuildRequires:	libbonobo-devel gnome-vfs-devel
Requires:	libbonobo gnome-vfs
%description
The libgnome package contains the libgnome library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libbonobo-devel gnome-vfs-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p0
%build
%configure  --sysconfdir=/etc/gnome/2.30.2 \
            --localstatedir=/var/lib       \
	    --disable-canberra
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mv %{buildroot}%{_datadir}/pixmaps/backgrounds %{buildroot}%{_datadir}/
rm -rf %{buildroot}%{_datadir}/pixmaps/
%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.32.1-1
-	initial version
