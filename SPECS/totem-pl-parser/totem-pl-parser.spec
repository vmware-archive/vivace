Summary:	The Totem PL Parser package contains a simple GObject-based library used to parse a host of playlist formats, as well as save those. 
Name:           totem-pl-parser
Version:        3.10.1
Release:        1
License:        GPLv2
Url:		https://developer.gnome.org/totem-pl-parser/stable/
Group:		Productivity/Multimedia/Video/Players
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:        https://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.xz
BuildRequires:  glib-devel libsoup-devel libxml2-devel intltool gmime-devel gmime gobject-introspection-devel gobject-introspection-python
Requires:       libsoup glib gmime libxml2 gobject-introspection
%description
The Totem PL Parser package contains a simple GObject-based library used to parse a host of playlist formats, as well as save those. 
%package devel
Summary: 	Development files for totem-pl-parser
Group:   	Development/Libraries
Requires: 	%{name} = %{version}
Requires:       glib-devel libsoup-devel libxml2-devel intltool gmime-devel gmime
%description devel
The Totem PL Parser package contains a simple GObject-based library used to parse a host of playlist formats, as well as save those.

%prep
%setup -q 

%build

./configure	--prefix=%{_prefix} \
		--disable-static 
	  	
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/totem-pl-parser/
%{_libdir}/*.so
%{_libdir}/girepository-1.0
%{_libdir}/*.la
%{_libdir}/pkgconfig
%doc %{_datadir}/gtk-doc/html/totem-pl-parser/
%{_datadir}

%changelog
*	Mon Jul 13 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.10.1-1
-	Initial version. 

