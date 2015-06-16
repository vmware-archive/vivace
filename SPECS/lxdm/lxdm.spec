Summary:	Lightweight display manager
Name:		lxdm
Version:	0.5.0
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:	lxdm.conf
Source2:	default.png
Source3:	greeter.ui
BuildRequires:	intltool gtk2-devel gobject-introspection python2-libs python2-devel glib-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel libX11-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel librsvg-devel consolekit-devel Linux-PAM systemd libxcb-devel
Requires:	gtk2 glib cairo pango gdk-pixbuf atk libX11 pixman libXrender libXext libpng harfbuzz librsvg consolekit Linux-PAM systemd libxcb
%description
The LXDM is a lightweight Display Manager for the LXDE desktop. It can also be used as an alternative to other Display Managers such as GNOME's GDM or KDE's KDM.
%prep
%setup -q
%build
cat > pam/lxdm << "EOF"
#%PAM-1.0
auth        include    system-auth
account     include    system-auth
password    include    system-auth
session     include    system-auth
EOF

sed -i 's:sysconfig/i18n:profile.d/i18n.sh:g' data/lxdm.in &&
sed -i 's:/etc/xprofile:/etc/profile:g' data/Xsession &&
sed -e 's/^bg/#&/'        \
    -e '/reset=1/ s/# //' \
        -e 's/logou$/logout/' \
	    -e "/arg=/a arg=$XORG_PREFIX/bin/X" \
	        -i data/lxdm.conf.in
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
            --with-pam
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/lxdm/
install -d $RPM_BUILD_ROOT/usr/share/backgrounds
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/backgrounds/
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/usr/share/lxdm/themes/Industrial/


%post
systemctl enable lxdm

%preun
systemctl disable lxdm

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
/lib/*
%{_libexecdir}/*
%{_sbindir}/*
%{_datadir}/*
%changelog
*	Fri Jun 12 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.0-1
-	initial version