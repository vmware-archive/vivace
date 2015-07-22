Summary:	A very minimal window manager.
Name:		twm
Version:	1.0.9
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
%define sha1 twm=09e8a8f0d1072e11eb0d6e354d75a555b9952755
BuildRequires:	xorg-server-devel libXmu-devel libXaw-devel libXft-devel libxkbfile-devel libXt-devel
Requires:	xorg-server libXmu libXaw libXft libxkbfile libXt
%description
The twm package contains a very minimal window manager.
%prep
%setup -q
%build
sed -i -e '/^rcdir =/s,^\(rcdir = \).*,\1/etc/X11/app-defaults,' src/Makefile.in &&
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_prefix}/src/
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
-	initial version
