%global debug_package %{nil}
Summary:	provides the XML-XCB protocol descriptions.
Name:		xcb-proto
Version:	1.14.1
Release:	1%{?dist}
License:	MIT
URL:		http://xcb.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
%define sha1 xcb-proto=836d5b2dd00ff21bd038e92764fda9a256a1b022
BuildRequires:	python3-devel
BuildRequires:	python3-libs
Requires:	python3
%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb uses to generate the majority of its code and API.
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
%{_prefix}/*
%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 1.14.1-1
- Version update
* Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.11-1
- initial version
