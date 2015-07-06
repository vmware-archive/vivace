Summary:	The libfm package contains a library used to develop file managers providing some file management utilities.
Name:		libfm
Version:	1.2.3
Release:	1
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
Patch0:		host2guest_dnd_support.patch
BuildRequires:	gtk2-devel menu-cache-devel
Requires:	gtk2 menu-cache
%description
The libfm package contains a library used to develop file managers providing some file management utilities.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel menu-cache-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%patch0 -p1
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/*.la
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.1-1
-	initial version
