Summary:	GNOME keyring library 
Name:		libgnome-keyring
Version:	3.6.0
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.6/%{name}-%{version}.tar.xz
BuildRequires:	dbus-glib-devel libgcrypt-devel
Requires:	dbus-glib libgcrypt
%description
The libgnome-keyring is used by applications to integrate with the GNOME Keyring system.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	dbus-glib-devel libgcrypt-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 3.6.0-1
-	initial version
