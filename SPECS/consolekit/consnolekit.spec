Summary:	system daemon for tracking users and sessions.
Name:		consolekit
Version:	0.4.6
Release:	1
License:	GPLv2+
URL:		http://www.freedesktop.org/wiki/Software/ConsoleKit
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://anduin.linuxfromscratch.org/sources/BLFS/svn/c/ConsoleKit-%{version}.tar.xz
BuildRequires:	dbus-glib-devel polkit-devel libacl-devel libX11-devel libXrender-devel libXext-devel glib-devel
Requires:	dbus-glib polkit libacl libX11 libXrender libXext glib
%description
The ConsoleKit package is a framework for keeping track of the various users, sessions, and seats present on a system. It provides a mechanism for software to react to changes of any of these items or of any of the metadata associated with them.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the ConsoleKit.
%prep
%setup -q -n ConsoleKit-%{version}
%build
#	    --with-systemdsystemunitdir=no
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --localstatedir=%{_localstatedir} \
	    --enable-udev-acl    \
	    --enable-pam-module
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/etc/pam.d
cat >> %{buildroot}/etc/pam.d/system-session << "EOF"
# Begin ConsoleKit addition

session   optional    pam_loginuid.so
session   optional    pam_ck_connector.so nox11

# End ConsoleKit addition
EOF

install -vdm 755 %{buildroot}/usr/lib/ConsoleKit/run-session.d
cat > %{buildroot}/usr/lib/ConsoleKit/run-session.d/pam-foreground-compat.ck << "EOF"
#!/bin/sh
TAGDIR=/var/run/console

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
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_lib}/*
%{_sbindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.4.6-1
-	initial version
