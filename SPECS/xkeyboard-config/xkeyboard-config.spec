%global debug_package %{nil}
Summary:	The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
Name:		xkeyboard-config
Version:	2.14
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
%define sha1 xkeyboard-config=b37c42b26739bedb9716c60c92f721c1ad934116
BuildRequires:	intltool libX11-devel  
Requires:	libX11
%description
The XKeyboardConfig package contains the keyboard configuration database for the X Window System.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --with-xkb-rules-symlink=xorg
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.14-1
-	initial version
