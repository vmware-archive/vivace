Summary:	gtkmm is the official C++ interface for the popular GUI library GTK+. 
Name:		gtkmm3
Version:	3.19.6
Release:	1
License:	LGPLv2+
URL:		http://www.gtkmm.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/3.16/gtkmm-%{version}.tar.xz
%define sha1 gtkmm=74c436dbad3bfb68beb599d00526316cc08c3da4
BuildRequires:	pangomm-devel atkmm-devel gtk3-devel libxslt glibmm gdk-pixbuf-devel cairomm-devel
Requires:	atkmm gtk3 pangomm gdk-pixbuf cairomm
%description
gtkmm is the official C++ interface for the popular GUI library GTK+. Highlights include typesafe callbacks, and a comprehensive set of widgets that are easily extensible via inheritance.

%package	devel
Summary:	Header and development files
Group: 		Development/Libraries
Requires:	%{name} = %{version}, gtk3-devel, glibmm, libsigc++
Requires:	pangomm-devel atkmm-devel
%description	devel
It contains the libraries and header files to create gtkmm applications. 

%prep
%setup -qn gtkmm-%{version}

%build
./configure 	--prefix=%{_prefix} \
		--enable-static \
		--enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/libgdkmm-3.0.so.*
%{_libdir}/libgtkmm-3.0.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/gdkmm-3.0/
%{_includedir}/gtkmm-3.0/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/gdkmm-3.0.pc
%{_libdir}/pkgconfig/gtkmm-3.0.pc
%{_libdir}/gdkmm-3.0/
%{_libdir}/gtkmm-3.0/
%{_datadir}

%changelog
*	Fri Mar 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.19.6-1
-	Updated to version 3.19.6
*	Mon Jul 06 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.14.0-1
-	initial version
