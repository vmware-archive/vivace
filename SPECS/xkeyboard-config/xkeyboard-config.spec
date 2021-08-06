%global debug_package %{nil}
Summary:	The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
Name:		xkeyboard-config
Version:	2.33
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
%define sha1 xkeyboard-config=eeccf05e0df69f42fbac700c5d3eca3129a49b5b
BuildRequires:	intltool libX11-devel
Requires:	libX11
%description
The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
%prep
%setup -q
%build
%configure --with-xkb-rules-symlink=xorg
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 2.33-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.14-1
- initial version
