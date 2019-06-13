Summary:	library for handling OpenGL function pointer management.
Name:		libepoxy
Version:	1.4.0
Release:	1%{?dist}
License:	MIT
URL:		http://crux.nu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/anholt/libepoxy/releases/download/v1.4/%{name}-%{version}.tar.xz
%define sha1 libepoxy=e390e2b1e20938be0cfb171afa51116663e8db26
BuildRequires:	mesa-devel
Requires:	mesa
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
%configure
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
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 1.4.0-1
- Version update
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2-1
- Initial version
