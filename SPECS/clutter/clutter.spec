Summary:	Clutter is a toolkit for creating compelling, dynamic, and portable graphical user interfaces
Name:		clutter 
Version:	1.22.4
Release:        2	
License:	LGPLv2.1+
URL:		https://blogs.gnome.org/clutter/
Group:		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.22/%{name}-%{version}.tar.xz
%define sha1 clutter=1665008f6c44a19d6aab23aa73cb19f85cafdfd2
BuildRequires:	atk-devel json-glib-devel cogl-devel xpango-devel libXcomposite-devel libXdamage-devel gdk-pixbuf-devel
Requires:	atk json-glib cogl xpango libXdamage libXcomposite gdk-pixbuf

%description
Clutter is a toolkit for creating compelling, dynamic, and portable graphical user interfaces. Clutter is free software, developed by the GNOME community.

%package devel
Summary: Development files for clutter
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: xcairo-devel gtk2-devel xpango-devel atk-devel libX11-devel libXext-devel libXcomposite-devel libXdamage-devel gdk-pixbuf-devel cogl-devel json-glib-devel

%description devel
Clutter is a toolkit for creating compelling, dynamic, and portable graphical user interfaces. Clutter is free software, developed by the GNOME community.

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
%doc README COPYING ChangeLog
%{_datadir}/gir-1.0
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/locale
%exclude %{_datadir}/gtk-doc 

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.22.4-2
-	Updated build requires & requires to build with Photon 2.0
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.22.4-1
-	initial version
