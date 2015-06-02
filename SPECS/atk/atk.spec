Summary:	Accessibility interfaces to have full access to view and control running applications.
Name:		atk
Version:	2.16.0
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.16/%{name}-%{version}.tar.xz
BuildRequires:	glib-devel gobject-introspection-devel gobject-introspection-python python2-devel python2-libs
Requires:	glib
%description
ATK provides the set of accessibility interfaces that are implemented by other toolkits and applications. Using the ATK interfaces, accessibility tools have full access to view and control running applications.
%package	devel
Summary:	Header and development files for
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
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
-	initial version
