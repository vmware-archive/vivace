%global security_hardening nonow
Summary:	VMMouse input driver for the Xorg X server.
Name:		xf86-input-vmmouse
Version:	13.0.0
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-input-vmmouse=0fa67d2ca9b2b26d32b93cc030fc3ea28964fe81
Patch0:		xf86-input-vmmouse-13.0.0-build_fix-1.patch
BuildRequires:	xorg-server-devel pixman-devel libpciaccess-devel
Requires:	xorg-server pixman libpciaccess
%description
The Xorg VMMouse Driver package contains the VMMouse input driver for the Xorg X server. The VMMouse driver enables support for the special VMMouse protocol that is provided by VMware virtual machines to give absolute pointer positioning. It can be used with Qemu, too.
%prep
%setup -q
%patch0 -p1
%build
sed -i -e '/__i386__/a iopl(3);' tools/vmmouse_detect.c      &&
./configure --prefix=%{_prefix}	       \
            --without-hal-fdi-dir      \
	    --without-hal-callouts-dir \
	    --with-udev-rules-dir=/lib/udev/rules.d
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
/lib/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 13.0.0-1
-	initial version
