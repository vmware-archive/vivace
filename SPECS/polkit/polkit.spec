Summary:	toolkit for defining and handling authorizations.
Name:		polkit
Version:	0.112
Release:	1
License:	LGPLv2+
URL:		http://www.freedesktop.org/software/polkit
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.gz
%define sha1 polkit=374397f1c32fa1290be0fce378fe9bab541ee4bf
BuildRequires:	intltool glib-devel js-devel expat systemd js gcc libtool
Requires:	glib js expat shadow systemd
%description
Polkit is a toolkit for defining and handling authorizations. It is used for allowing unprivileged processes to communicate with privileged processes.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	intltool glib-devel js-devel expat systemd
%description 	devel
Install this package if you want do compile applications using the polkit.
%prep
%setup -q
%build
# current configure uses old auto tools
#autoreconf -vif
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --localstatedir=%{_localstatedir} \
	    --disable-static \
	    --enable-libsystemd-login=no \
	    --with-authfw=shadow \
		--with-mozjs=mozjs-17.0
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/etc/pam.d
cat > %{buildroot}/etc/pam.d/polkit-1 << "EOF"
# Begin /etc/pam.d/polkit-1

auth     include        system-auth
account  include        system-account
password include        system-password
session  include        system-session

# End /etc/pam.d/polkit-1
EOF
%pre
getent group polkitd > /dev/null || groupadd -fg 27 polkitd &&
getent passwd polkitd > /dev/null || useradd -c "PolicyKit Daemon Owner" -d /etc/polkit-1 -u 27 \
        -g polkitd -s /bin/false polkitd

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so
%exclude %{_libdir}/debug
/lib/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%changelog
*	Tue May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.112-1
-	initial version
