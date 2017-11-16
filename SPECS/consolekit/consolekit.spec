Summary:	system daemon for tracking users and sessions.
Name:		consolekit
Version:	0.4.6
Release:	2	
License:	GPLv2+
URL:		http://www.freedesktop.org/wiki/Software/ConsoleKit
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://anduin.linuxfromscratch.org/sources/BLFS/svn/c/ConsoleKit-%{version}.tar.xz
%define sha1 ConsoleKit=fabed310860c6eda2fe99218d534dc838a9aa226
BuildRequires:	dbus-glib-devel systemd-devel
BuildRequires:  polkit-devel libacl-devel libXrender-devel libXext-devel Linux-PAM-devel
Requires:	dbus-glib polkit libacl libXrender libXext dbus-devel Linux-PAM systemd
%description
The ConsoleKit package is a framework for keeping track of the various users, sessions, and seats present on a system. It provides a mechanism for software to react to changes of any of these items or of any of the metadata associated with them.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:       polkit-devel libacl-devel libXrender-devel libXext-devel libgudev-devel
%description 	devel
Install this package if you want do compile applications using the ConsoleKit.
%prep
%setup -q -n ConsoleKit-%{version}
%build
#	    --with-systemdsystemunitdir=no
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --localstatedir=%{_localstatedir} \
	    --enable-pam-module
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/etc/pam.d
install -vdm 755 %{buildroot}/etc/tmpfiles.d
install -vdm 755 %{buildroot}/usr/lib/ConsoleKit/run-session.d
cat > %{buildroot}/usr/lib/ConsoleKit/run-session.d/pam-foreground-compat.ck << "EOF"
#!/bin/sh
TAGDIR=/var/run/console
echo "D /var/log/ConsoleKit/ 0755 root root" >> %{buildroot}/etc/tmpfiles.d/console-kit.conf
[ -n "$CK_SESSION_USER_UID" ] || exit 1
[ "$CK_SESSION_IS_LOCAL" = "true" ] || exit 0

TAGFILE="$TAGDIR/`getent passwd $CK_SESSION_USER_UID | cut -f 1 -d:`"

if [ "$1" = "session_added" ]; then
mkdir -p "$TAGDIR"
echo "$CK_SESSION_ID" >> "$TAGFILE"
fi

if [ "$1" = "session_removed" ] && [ -e "$TAGFILE" ]; then
sed -i "\%^$CK_SESSION_ID\$%d" "$TAGFILE"
[ -s "$TAGFILE" ] || rm -f "$TAGFILE"
fi
EOF
chmod -v 755 %{buildroot}/usr/lib/ConsoleKit/run-session.d/pam-foreground-compat.ck

%post
cat >> /etc/pam.d/system-session << "EOF"
# Begin ConsoleKit addition
session   optional    pam_loginuid.so
session   optional    pam_ck_connector.so nox11
# End ConsoleKit addition
EOF

%preun
sed '/Begin ConsoleKit/,/End ConsoleKit/d' -i /etc/pam.d/system-session

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
/lib/*
%{_sbindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.4.6-2
-	Updated build requires & requires to build with Photon 2.0 & added conf files to create dir in /var/log
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.6-1
-	initial version
