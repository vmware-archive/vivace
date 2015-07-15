Summary:	libpeas is a GObject based plugins engine, and is targeted at giving every application the chance to assume its own extensibility. 
Name:		libpeas
Version:	1.14.0
Release:	1
License:	LGPLv2+
URL:		https://developer.gnome.org/libpeas/stable/
Group:		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.14/%{name}-%{version}.tar.xz
%define sha1 libpeas=18a85ab41f578997ff1e9860ce178d7c5116c616
BuildRequires:	intltool gobject-introspection-devel gtk3-devel
Requires:	gtk3 gobject-introspection
%description
libpeas is a GObject based plugins engine, and is targeted at giving every application the chance to assume its own extensibility. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gobject-introspection-devel gtk3-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build

./configure 	--prefix=%{_prefix} \
		--disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}/icons

%files devel
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/libpeas/
%{_includedir}
%{_libdir}/*.so
%{_libdir}/pkgconfig
%{_datadir}/gir-1.0/*.gir
%{_datadir}/locale

%changelog
*	Mon Jul 13 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.14.0-1
-	initial version
