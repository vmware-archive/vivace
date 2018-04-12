Summary:	ALSA library.
Name:		alsa-lib
Version:	1.1.5
Release:	1
License:	LGPLv2+
URL:		http://alsa-project.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.1.5.tar.bz2
%define sha1 alsa-lib=636ac0b2b759108ca9b0f4efa1c3e8650cf9c9f6
BuildRequires:	python2-devel python2-libs
Requires:	python2
%description
The ALSA Library package contains the ALSA library used by programs (including ALSA Utilities) requiring access to the ALSA sound interface.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 29 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.29-1
-	initial version
