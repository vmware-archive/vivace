Summary:	CSS2 parsing and manipulation library.
Name:		libcroco
Version:	0.6.8
Release:	1
License:	LGPLv2
URL:		http://www.gnome.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.xz
BuildRequires:	glib-devel libxml2-devel
Requires:	glib libxml2
%description
The libcroco package contains a standalone CSS2 parsing and manipulation library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel libxml2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 0.6.8-1
-	initial version
