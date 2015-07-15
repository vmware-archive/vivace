Summary:	gtkmm is the official C++ interface for the popular GUI library GTK+. 
Name:		gtkmm
Version:	2.24.4
Release:	1
License:	LGPLv2+
URL:		http://www.gtkmm.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.24/%{name}-%{version}.tar.xz
%define sha1 gtkmm=e99866b0cb5a0d7387a7cef79253177310020b3d
BuildRequires:	pangomm-devel atkmm-devel gtk2-devel
Requires:	atkmm gtk2 pangomm
%description
gtkmm is the official C++ interface for the popular GUI library GTK+. Highlights include typesafe callbacks, and a comprehensive set of widgets that are easily extensible via inheritance.

%package	devel
Summary:	Header and development files
Group: 		Development/Libraries
Requires:	%{name} = %{version}, gtk2-devel, glib, libsigc++
Requires:	pangomm-devel atkmm-devel gtk2-devel
%description	devel
It contains the libraries and header files to create gtkmm applications. 

%prep
%setup -q -n gtkmm-%{version}

%build
./configure --prefix=%{_prefix} --enable-static --enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc ChangeLog PORTING
%doc %{_datadir}/doc/gtkmm-2.4
%{_includedir}/gtkmm-2.4
%{_includedir}/gdkmm-2.4
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/gtkmm-2.4
%{_libdir}/gdkmm-2.4
%{_libdir}/pkgconfig/*.pc
%{_datarootdir}/devhelp/books/gtkmm-2.4/gtkmm-2.4.devhelp2
%changelog
*	Tue Jun 16 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.4-1
-	initial version
