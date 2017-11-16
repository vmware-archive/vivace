Summary:	default session manager for LXDE.
Name:		lxsession
Version:	0.5.2
Release:	2	
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxsession=00d45cccbdd6fb05c46998671a7c12123a0a2179
BuildRequires:	libunique-devel polkit-devel dbus-glib-devel intltool
Requires:	libunique polkit dbus-glib
%description
The LXSession package contains the default session manager for LXDE.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --disable-man
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
#Do not pack lxpolkit. Use standard polkitd instead
%exclude %{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%exclude %{_bindir}/lxpolkit
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.5.2-2
-	Updated build requires & requires to build with Photon 2.0
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.2-1
-	initial version
