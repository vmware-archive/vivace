Summary:	The xclock package contains a simple clock application which is used in the default xinit configuration.
Name:		xclock
Version:	1.0.7
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	libXmu-devel libXaw-devel libXft-devel libxkbfile-devel libXt-devel
Requires:	xorg-applications libXmu libXaw libXft libxkbfile libXt
%description
The xclock package contains a simple clock application which is used in the default xinit configuration.
%prep
%setup -q
%build
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.7-1
-	initial version
