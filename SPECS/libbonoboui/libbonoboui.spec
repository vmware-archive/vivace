Summary:	The Bonobo User Interface library
Name:		libbonoboui
Version:	2.24.5
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
%define sha1 libbonoboui=9657e7194ef3f5782f183e021fdb4014531b6cd8
BuildRequires:	libgnomecanvas-devel libgnome-devel
Requires:	libgnomecanvas libgnome
%description
The Bonobo User Interface library provides user interface code for Bonobo, the Object Activation Framework for GNOME 2.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libgnomecanvas-devel libgnome-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
%configure --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.5-1
-	initial version
