Summary:	PCManFM file manager.
Name:		pcmanfm
Version:	1.2.3
Release:	1
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
BuildRequires:	libfm-devel
Requires:	libfm
%description
The PCManFM package contains an extremely fast, lightweight, yet feature-rich file manager with tabbed browsing.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	libfm-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
sed -i 's/System;//' %{buildroot}/usr/share/applications/pcmanfm.desktop
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.3-1
-	initial version
