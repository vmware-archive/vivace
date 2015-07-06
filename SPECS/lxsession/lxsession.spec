Summary:	default session manager for LXDE.
Name:		lxsession
Version:	0.5.2
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	libunique-devel polkit-devel dbus-glib-devel
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
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.2-1
-	initial version
