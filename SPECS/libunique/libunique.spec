Summary:	library for writing single instance applications.
Name:		libunique
Version:	1.1.6
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
%define sha1 libunique=d44ad06503efaaa0c660c5f8a817e90fbe254d1f
Patch0:		libunique-1.1.6-upstream_fixes-1.patch
BuildRequires:	autoconf automake gtk2-devel
Requires:	gtk2
%description
The libunique package contains a library for writing single instance applications.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%patch0 -p1
%build
# current configure uses old auto tools
autoreconf --install
%configure  --disable-static \
	    --disable-dbus
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.6-1
-	initial version
