Summary:	library for handling OpenGL function pointer management.
Name:		libepoxy
Version:	1.2
Release:	1
License:	MIT
URL:		http://crux.nu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://crux.nu/files/%{name}-%{version}.tar.gz
%define sha1 libepoxy=e700520711b9e4fa07c286aa36e431d8ad4133f5
BuildRequires:	mesa-devel python2-devel python2-libs python-xml
Requires:	mesa python2
%description
libepoxy is a library for handling OpenGL function pointer management.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	mesa-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./autogen.sh --prefix=%{_prefix}
make %{?_smp_mflags}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
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
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2-1
-	initial version
