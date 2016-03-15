Summary:	The gtksourceviewmm application is a C++ wrapper for the gtksourceview widget library. 
Name:		gtksourceviewmm
Version:	3.18.0
Release:	1
License:	LGPL-2.1+
URL:		https://developer.gnome.org/gtksourceviewmm/stable/
Group:		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/3.12/%{name}-%{version}.tar.xz
%define sha1 gtksourceviewmm=5104c6fa2d3082686fffd1e6f5f5977138fb71bc
BuildRequires:	intltool libxml2-devel gtksourceview-devel gtkmm3-devel cracklib-python
Requires:	glibmm gobject-introspection gtksourceview gtkmm3 
%description
The gtksourceviewmm application is a C++ wrapper for the gtksourceview widget library. 
%package	devel
Summary:	Header and library file for gtksourceviewmm
Group:          Development/Languages/C and C++
Requires:	%{name} = %{version}
Requires:	gtksourceview-devel gtkmm3-devel intltool libxml2-devel cracklib-python
%description	devel
The gtksourceviewmm application is a C++ wrapper for the gtksourceview widget library. 
%prep
%setup -q 

%build
./configure	--prefix=%{_prefix} \
		--disable-static 

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/gtksourceviewmm-3.0/
%{_libdir}/gtksourceviewmm-3.0/
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig
%{_datadir}/doc
%{_datadir}/devhelp


%changelog
*	Fri Mar 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.18.0-1
-	Updated to version 3.18.0 
*	Tue Jun 30 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.12.0-1
-	initial version
