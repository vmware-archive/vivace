Summary:	The Pangomm package provides a C++ interface to Pango. 
Name:		pangomm
Version:	2.36.0
Release:	1
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangomm/2.36/%{name}-%{version}.tar.xz
%define sha1 pangomm=eb23bca29b2ea216b58f39292a9c5e5c293716c5
BuildRequires:	pango-devel glibmm-devel cairomm-devel
Requires:	cairomm pango glibmm
%description
The Pangomm package provides a C++ interface to Pango.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pango-devel glibmm-devel cairomm-devel
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
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.36.0-1
-	initial version
