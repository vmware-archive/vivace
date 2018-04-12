Summary:	The LXPanel package contains a lightweight X11 desktop panel.
Name:		lxpanel
Version:	0.8.1
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxpanel=bfaf34b2574b02b9703777904e658ed082cf17dd
BuildRequires:	lxmenu-data menu-cache-devel gtk2-devel libfm-devel libwnck-devel keybinder-devel libxml2-devel
Requires:	lxmenu-data menu-cache gtk2 libfm libwnck keybinder libxml2
%description
The LXPanel package contains a lightweight X11 desktop panel.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel libfm-devel libwnck-devel keybinder-devel libxml2-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --with-plugins=all,-netstat
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.8.1-1
-	initial version
