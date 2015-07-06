Summary:	Shared functions for Ayatana indicators
Name:		libindicator
Version:	12.10.1
Release:	1
License:	GPLv3
URL:		https://launchpad.net/libindicator
Group:		User Interface/Library
Source0:	https://launchpad.net/%{name}/12.10/%{version}/+download/%{name}-%{version}.tar.gz
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	gtk3-devel
Requires:	gtk3
%description
A set of symbols and convenience functions that all Ayatana indicators are
likely to use.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gtk3-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
./configure --prefix=%{_prefix}                 \
            --sysconfdir=%{_sysconfdir}         \
            --disable-static			\
	    --with-gtk=3

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/debug
%{_datadir}/*
%{_libexecdir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Wed Jun 24 2015 Alexey Makhalov <amakhalov@vmware.com> 12.10.1-1
-	Initial build. First version
