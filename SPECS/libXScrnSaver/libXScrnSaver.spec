Summary:	X11 Screen Saver runtime library.
Name:		libXScrnSaver
Version:	1.2.2
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXScrnSaver=7b8298eec371c33a71232e3653370a98f03c6c88
BuildRequires:	proto libXext-devel
Requires:	libXext
%description
The X11 Screen Saver runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	proto libXext-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.2-1
-	initial version
