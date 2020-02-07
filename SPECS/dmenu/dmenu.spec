Summary:	dmenu is a dynamic menu for X, originally designed for dwm.
Name:		dmenu
Version:	4.9
Release:	1%{?dist}
License:	MIT/X
URL:		https://tools.suckless.org/dmenu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://dl.suckless.org/tools/dmenu-4.9.tar.gz
%define sha1 dmenu=73d1a9a844e8f285fc315ea4ee5b95da2b0bc8f4
BuildRequires:	libXinerama-devel libXft-devel xfontconfig-devel libX11-devel
Requires:	dwm libXinerama libXft xfontconfig libX11
%description
dmenu is a dynamic menu for X, originally designed for dwm.
It manages large numbers of user-defined menu items efficiently.
%prep
%setup -q
%build
make %{?_smp_mflags} CC=gcc
%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix}  install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
* Tue Jul 02 2019 Alexey Makhalov <amakhalov@vmware.com> 4.9-1
- initial version
