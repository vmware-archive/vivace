Summary:	default configuration for LXDE.
Name:		lxde-common
Version:	0.99.0
Release:	1
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool consolekit-devel lxde-icon-theme lxsession openbox-devel 
Requires:	consolekit lxde-icon-theme lxsession openbox lxappearance xinit pcmanfm xcompmgr cairo-dock-plugins
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
@vmtoolsd -n vmusr
@xcompmgr
@cairo-dock -c
EOF

%post
update-mime-database /usr/share/mime &&
gtk-update-icon-cache -qf /usr/share/icons/hicolor &&
update-desktop-database -q

# TODO: install to home - not good idea.
cat > ~/.xinitrc << "EOF"
ck-launch-session startlxde
EOF
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*
%changelog
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.99.0-1
-	initial version
