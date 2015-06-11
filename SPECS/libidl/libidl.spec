Summary:	libraries for Interface Definition Language files
Name:		libidl
Version:	0.8.14
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.14/libIDL-%{version}.tar.bz2
BuildRequires:	intltool glib-devel
Requires:	glib
%description
The libIDL package contains libraries for Interface Definition Language files. This is a specification for defining portable interfaces.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n libIDL-%{version}
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/info/dir
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%exclude %{_datadir}/info
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_datadir}/info
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 0.8.14-1
-	initial version