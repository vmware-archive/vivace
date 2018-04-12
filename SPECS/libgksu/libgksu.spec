%global security_hardening none
Summary:	GKSu is a library that provides a Gtk+ frontend to su and sudo. It supports login shells and preserving environment when acting as a su frontend. 
Name:		libgksu 
Version:	2.0.12
Release:	1
License:	GPLv2+
URL:		http://www.nongnu.org/gksu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://people.debian.org/~kov/gksu/libgksu-2.0.12.tar.gz
Patch0:		autoreconf-fix.patch
%define sha1 libgksu=81a541ccfe9ea278dd3e2a80b3287f02f6eb88f8
BuildRequires:	libgtop-devel gtk2-devel libgnome-keyring-devel GConf-devel startup-notification-devel gtk-doc intltool
Requires:	gtk2 libgtop libgnome-keyring GConf startup-notification 
%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It supports login shells and preserving environment when acting as a su frontend.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 

%prep
%setup -q 
%patch0	-p1
%build
touch NEWS
touch README
autoreconf -vif
./configure --prefix=%{_prefix}	\
	    --disable-static \
		--disable-option-checking
sed -i 's#        if test -z \"$(DES#\tif test -z \"$(DES#g' Makefile
sed -i '/@INTLTOOL_SCHEMAS_RULE@/d' Makefile
make
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%{_bindir}/*
/usr/etc/*
%exclude %{_libdir}/debug/

%files devel
%{_includedir}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*/*.pc
%{_datadir}/*
%changelog
*	Wed Feb 24 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.0.12-1
-	initial version
