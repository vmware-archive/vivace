Summary:	X11 composite manager.
Name:		xcompmgr
Version:	1.1.7
Release:	1
License:	Copyright
URL:		http://www.freedesktop.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	intltool util-macros libX11-devel libXext-devel libXcomposite-devel libXdamage-devel libXrender-devel libXfixes-devel
Requires:	libX11 libXext libXcomposite libXdamage libXrender libXfixes
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
