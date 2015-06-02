Summary:	Extra libraries and files for menu-cache-gen.
Name:		libfm-extra
Version:	1.2.3
Release:	1
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/pcmanfm/libfm-%{version}.tar.xz
BuildRequires:	intltool glib-devel
Requires:	glib
%description
The libfm package contains a library and other files required by menu-cache-gen libexec of menu-cache-1.0.0.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q -n libfm-%{version}
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
            --with-extra-only \
	    --with-gtk=no     \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.1-1
-	initial version
