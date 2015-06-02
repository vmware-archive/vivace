Summary:	OpenType text shaping engine.
Name:		harfbuzz
Version:	0.9.40
Release:	1
License:	MIT
URL:		http://www.freedesktop.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/%{name}/release/%{name}-%{version}.tar.bz2
BuildRequires:	glib-devel icu-devel freetype2-initial 
# TODO: fix cycle deps harfbuff <-> fretype2
AutoReq:	no
Requires:	glib icu
%description
The Harfbuzz package contains an OpenType text shaping engine.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
./configure --prefix=%{_prefix} --with-gobject
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.9.40-1
-	initial version
