Summary:	cairomm is a C++ wrapper for the cairo graphics library. It offers all the power of cairo with an interface familiar to C++ developers, including use of the Standard Template Library where it makes sense.
Name:		cairomm
Version:	1.12.0
Release:        2	
License:	LGPLv2 or MPLv1.1
URL:		http://cairographics.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
%define sha1 cairomm=5a09a3f604cec2ddb4dfcace28dbe74a53585585
BuildRequires:	xcairo-devel libsigc++
Requires:	xcairo libsigc++ >= 2.8.0
%description
cairomm is a C++ wrapper for the cairo graphics library. It offers all the power of cairo with an interface familiar to C++ developers, including use of the Standard Template Library where it makes sense.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	xcairo-devel libsigc++
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} 
make 
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.12.0-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Mar 03 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.12.0-1
-	Updated to version 1.12.0
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.10.0-1
-	initial version
