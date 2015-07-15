Summary:	X11 composite manager.
Name:		xcompmgr
Version:	1.1.7
Release:	1
License:	Copyright only
URL:		http://www.freedesktop.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
%define sha1 xcompmgr=5590d1bdd2669f083e4c2bb25edd89cce8abbd58
BuildRequires:	libXcomposite-devel libXdamage-devel libXrender-devel 
Requires:	libXcomposite libXdamage libXrender 
%description
xcompmgr is a sample compositing manager for X server.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.7-1
-	initial version
