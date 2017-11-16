Summary:	Lightweight display manager
Name:		lxdm
Version:	0.5.3
Release:	2	
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
%define sha1 lxdm=8c4f7439fa7b56a97e8b19dc62af02a88ae12b45
Source1:	lxdm.conf
Source2:	default.png
Source3:	greeter.ui
BuildRequires:	intltool gtk2-devel librsvg-devel consolekit-devel Linux-PAM-devel systemd-devel
Requires:	lxdm-themes gtk2 librsvg consolekit Linux-PAM systemd libxcb which
%description
The LXDM is a lightweight Display Manager for the LXDE desktop. It can also be used as an alternative to other Display Managers such as GNOME's GDM or KDE's KDM.
%prep
%setup -q
%build
cat > pam/lxdm << "EOF"
#%PAM-1.0
auth        include    system-auth
account     include    system-account
password    include    system-password
session     include    system-session
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

cat >> $RPM_BUILD_ROOT/etc/lxdm/PostLogout << "EOF"
# Workaround: --exit-with-session doesn't work.
# dbus-daemon --session is started in /etc/skel/.xinitrc and terminated here.
for p in `ps ax | grep "dbus-daemon" | grep "session" | awk '{print $1}'` ; do
    kill $p
done
EOF

sed -i 's/ --exit-with-session//' %{buildroot}/etc/lxdm/Xsession

%post
ln -sf /lib/systemd/system/graphical.target /lib/systemd/system/default.target
systemctl enable lxdm

%preun
systemctl disable lxdm

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libexecdir}/*
/lib/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*
%exclude %{_datadir}/lxdm/themes/Industrial/
%exclude %{_libdir}/debug
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.5.3-2
-	Updated build requires & requires to build with Photon 2.0
* 	Fri Aug 26 2016	Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.5.3-1
-	Upgraded to version 0.5.3
*	Fri Jun 12 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.5.0-2
-	Excluded the Industrial theme and added our custom theme as a dependency. 
*	Fri Jun 12 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.0-1
-	initial version
