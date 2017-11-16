Summary:	X11 Xft runtime library.
Name:		libXft
Version:	2.3.2
Release:	2	
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXft=e025d790a7b6c4d283a78d8df06615cb10278e2d
BuildRequires:	libXrender-devel xfontconfig-devel
Requires:	libXrender xfontconfig
%description
The X11 Xft runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libXrender-devel xfontconfig-devel
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
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.3.2-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 2.3.2-1
-	initial version
