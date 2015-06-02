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
BuildRequires:	util-macros proto libX11-devel libXmu-devel libXaw-devel libXrender-devel libXft-devel libxkbfile-devel libXt-devel libSM-devel libICE-devel fontconfig-devel freetype2-devel
Requires:	xorg-applications libX11 libXmu libXaw libXrender libXft libxkbfile libXt libSM libICE fontconfig freetype2
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
