Summary:	The libgnomeui package contains libgnomeui libraries
Name:		libgnomeui
Version:	2.24.5
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
%define sha1 libgnomeui=a89d88416403b20a958bd19257522cf7a75ea344
BuildRequires:	libbonoboui-devel libgnome-keyring-devel
Requires:	libbonoboui libgnome-keyring
%description
The libgnomeui package contains libgnomeui libraries.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libbonoboui-devel libgnome-keyring-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.5-1
-	initial version
