Summary:	X11 Authorization Protocol library.
Name:		libXau
Version:	1.0.8
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXau=d9512d6869e022d4e9c9d33f6d6199eda4ad096b
BuildRequires:	proto
Requires:	proto
%description
The libXau package contains a library implementing the X11 Authorization Protocol. This is useful for restricting client access to the display.
%package	devel
Summary:	Header and development files for libXau
Requires:	%{name} = %{version}
Requires:	proto
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_mandir}/*
%{_includedir}/*
%changelog
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.8-1
-	initial version
