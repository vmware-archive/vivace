Summary:	An Open Source implementation of the GDI+ API.
Name:		libgdiplus
Version:	3.12
Release:	2	
License:	MIT
URL:		http://www.mono-project.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
%define sha1 libgdiplus=7f7d2b82c0d755bb854fd76d0d62120cdde35d8c
BuildRequires:	intltool xcairo-devel libtiff-devel
Requires:	xcairo libtiff
%description
An Open Source implementation of the GDI+ API.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool xcairo-devel libtiff-devel
%description	devel
It contains the libraries and header files to create applications 

%prep
%setup -q 

%build
./configure --prefix=%{_prefix} \
            --disable-static

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%{_libdir}/pkgconfig

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.la

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.12-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 3.12-1
-	initial version
