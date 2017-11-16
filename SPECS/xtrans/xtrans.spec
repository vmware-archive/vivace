%global debug_package %{nil}
Summary:	Abstract network code for X.
Name:		xtrans
Version:	1.3.5
Release:	2	
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/xtrans-1.3.5.tar.bz2
%define sha1 xtrans=2d3ae1839d841f568bc481c6116af7d2a9f9ba59
BuildRequires:	pkg-config xfreetype2-devel xfreetype2 util-macros xfontconfig-devel libxcb-devel
Requires:	libxcb
%description
Abstract network code for X.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pkg-config util-macros libxcb-devel
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
%{_datadir}
%files devel
%{_includedir}
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.3.5-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.5-1
-	initial version
