Summary:	dmenu is a dynamic menu for X, originally designed for dwm.
Name:		dmenu
Version:	5.0
Release:	1%{?dist}
License:	MIT/X
URL:		https://tools.suckless.org/dmenu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://dl.suckless.org/tools/dmenu-%{version}.tar.gz
%define sha1 dmenu=6d48d324e0100f3e0c7c3ed5104dbe3ebcaeaef4
BuildRequires:	libXinerama-devel libXft-devel
Requires:	dwm libXinerama libXft
%description
dmenu is a dynamic menu for X, originally designed for dwm.
It manages large numbers of user-defined menu items efficiently.
%prep
%autosetup
%build
make %{?_smp_mflags} CC=gcc
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix}  install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 5.0-1
- Version update
* Tue Jul 02 2019 Alexey Makhalov <amakhalov@vmware.com> 4.9-1
- initial version
