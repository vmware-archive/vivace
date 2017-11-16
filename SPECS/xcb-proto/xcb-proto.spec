%global debug_package %{nil}
Summary:	provides the XML-XCB protocol descriptions.
Name:		xcb-proto
Version:	1.11
Release:	1
License:	MIT
URL:		http://xcb.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
%define sha1 xcb-proto=608bd60663e223464d38acec0183ddb827776401
BuildRequires:	python2-devel
BuildRequires:	python2-libs
Requires:	python2
%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb uses to generate the majority of its code and API. 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.11-1
-	initial version
