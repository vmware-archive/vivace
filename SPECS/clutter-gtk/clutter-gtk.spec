Summary:	The Clutter Gtk package is a library providing facilities to integrate Clutter into GTK+ applications. 
Name:		clutter-gtk 
Version:	1.6.2 
Release:	1
License:	LGPLv2.1+
URL:		https://blogs.gnome.org/clutter/
Group:		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.6/%{name}-%{version}.tar.xz
BuildRequires:	gtk3-devel clutter-devel
Requires:	gtk3 clutter

%description
The Clutter Gtk package is a library providing facilities to integrate Clutter into GTK+ applications. 

%package devel
Summary: Development files for clutter-gtk
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: gtk3-devel clutter-devel 

%description devel
The Clutter Gtk package is a library providing facilities to integrate Clutter into GTK+ applications. 

%prep
%setup -q 

%build
./configure 	--prefix=%{_prefix} \
		--disable-static \
		--disable-gtk-doc

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install 
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files 
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/locale
%exclude %{_datadir}/gtk-doc 

%changelog
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.0.14 -1
-	initial version
