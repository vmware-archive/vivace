Summary:	File manager.
Name:		mc
Version:	4.8.14
Release:	1
License:	GPLv3+
URL:		http://www.mignight-commander.org/
Group:		System Environment/Shells
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.midnight-commander.org/downloads/%{name}-%{version}.tar.xz
%define sha1 mc=ae64b22a213fac8b8231b5407b8aa312ca25c38f
BuildRequires:	glib-devel pcre-devel ncurses-devel
Requires:	glib pcre ncurses
%description
MC (Midnight Commander) is a text-mode full-screen file manager and visual shell. It provides a clear, user-friendly, and somewhat protected interface to a Unix system while making many frequent file operations more efficient and preserving the full power of the command prompt.
%prep
%setup -q 
%build
./configure --prefix=%{_prefix}	\
            --sysconfdir=/etc \
	    --with-screen=ncurses \
	    --enable-charset
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
%{_libexecdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%changelog
*	Fri Jun 5 2015 Alexey Makhalov <amakhalov@vmware.com> 4.8.14-1
-	initial version
