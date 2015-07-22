Summary:	cairomm is a C++ wrapper for the cairo graphics library. It offers all the power of cairo with an interface familiar to C++ developers, including use of the Standard Template Library where it makes sense.
Name:		cairomm
Version:	1.10.0
Release:	1
License:	LGPLv2 or MPLv1.1
URL:		http://cairographics.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
%define sha1 cairomm=f08bf8a331067f0d1e876523f07238fba6b26b99
BuildRequires:	cairo-devel libsigc++  
Requires:	cairo libsigc++
%description
cairomm is a C++ wrapper for the cairo graphics library. It offers all the power of cairo with an interface familiar to C++ developers, including use of the Standard Template Library where it makes sense.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	cairo-devel libsigc++  
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
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.10.0-1
-	initial version
