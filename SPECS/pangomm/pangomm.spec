Summary:	The Pangomm package provides a C++ interface to Pango. 
Name:		pangomm
Version:	2.40.1
Release:	2	
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangomm/2.36/%{name}-%{version}.tar.xz
%define sha1 pangomm=2b3904e635d6cf3b8088f7a8c6e2f8a5034f6516
BuildRequires:	xpango-devel glibmm-devel cairomm-devel
Requires:	cairomm xpango glibmm
%description
The Pangomm package provides a C++ interface to Pango.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	xpango-devel glibmm-devel cairomm-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} &&
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
pango-querymodules --update-cache  
%files
%defattr(-,root,root)
#%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.40.1-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon Aug 30 2016	Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.40.1-1
-	Upgraded to version 2.40.1
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.39.1-1
-	Updated to version 2.38.1 
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.36.0-1
-	initial version
