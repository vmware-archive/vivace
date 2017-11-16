Summary:	OpenType text shaping engine.
Name:		xharfbuzz
Version:	1.6.3
Release:	1
License:	MIT
URL:		http://www.freedesktop.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-%{version}.tar.bz2
%define sha1 harfbuzz=11b89febd6fd7225358cd2386b0f9d4e685c10e7
BuildRequires:	glib-devel icu-devel freetype2-initial 
# TODO: fix cycle deps harfbuff <-> fretype2
AutoReq:	no
Requires:	glib >= 2.48.2
Requires:       icu
%description
The Harfbuzz package contains an OpenType text shaping engine.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel icu-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -qn harfbuzz-%{version} 
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
