Summary:	X Display Manager Control Protocol library.
Name:		libXdmcp
Version:	1.1.2
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	proto
Requires:	proto
%description
The libXdmcp package contains a library implementing the X Display Manager Control Protocol. This is useful for allowing clients to interact with the X Display Manager. 
%package	devel
Summary:	Header and development files for libXdmcp
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
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_docdir}/*
%{_includedir}/*
%changelog
*	Fri May 15 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.2-1
-	initial version
