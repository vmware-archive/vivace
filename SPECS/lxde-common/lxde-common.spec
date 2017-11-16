%global debug_package %{nil}
Summary:	default configuration for LXDE.
Name:		lxde-common
Version:	0.99.0
Release:	2	
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxde-common=8ae027a26043620990a5c5d96a31e46b0ff669da
BuildRequires:	consolekit-devel lxde-icon-theme lxsession openbox-devel intltool
Requires:	consolekit lxde-icon-theme lxsession openbox lxappearance xinit pcmanfm xcompmgr cairo-dock-plugins shared-mime-info
%description
The LXDE Common package provides a set of default configuration for LXDE.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
cat > %{buildroot}/etc/xdg/lxsession/LXDE/autostart << "EOF"
@pcmanfm --desktop --profile LXDE
@xscreensaver -no-splash
@xcompmgr
@cairo-dock -c
EOF

install -d %{buildroot}/etc/skel/
cat > %{buildroot}/etc/skel/.xinitrc << "EOF"
ck-launch-session startlxde
EOF

%post
update-mime-database /usr/share/mime &&
gtk-update-icon-cache -qf /usr/share/icons/hicolor &&
update-desktop-database -q
cp /etc/skel/.xinitrc /root

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.99.0-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.99.0-1
-	initial version
