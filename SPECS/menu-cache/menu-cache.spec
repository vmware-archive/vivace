Summary:	Libraries for application menus caching.
Name:		menu-cache
Version:	1.0.0
Release:	1
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool libfm-extra-devel glib-devel
Requires:	libfm-extra glib
%description
The Menu Cache package contains a library for creating and utilizing caches to speed up the manipulation for freedesktop.org defined application menus.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%{_libexecdir}/*
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.0-1
-	initial version
