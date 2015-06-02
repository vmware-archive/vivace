Summary:	The LXMenu Data package provides files required to build freedesktop.org menu spec-compliant desktop menus for LXDE. 
Name:		lxmenu-data
Version:	0.1.4
Release:	1
License:	LGPLv3
URL:		http://downloads.sourceforge.net/lxde
BuildArchitectures: noarch
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool
%description
The LXMenu Data package provides files required to build freedesktop.org menu spec-compliant desktop menus for LXDE. 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_datadir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1.4-1
-	initial version
