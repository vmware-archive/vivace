Summary:	dock, panel, desklet.
Name:		cairo-dock
Version:	3.4.0
Release:	2	
License:	LGPLv2+
URL:		http://glx-dock.org/
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://launchpad.net/cairo-dock-core/3.4/%{version}/+download/%{name}-%{version}.tar.gz
%define sha1 cairo-dock=3273644aa4b848fda7a0c6825860930d61b48060
BuildRequires:	cmake dbus-glib-devel libXcomposite-devel libxml2-devel mesa-devel curl-devel curl-libs librsvg-devel glu-devel gtk3-devel
Requires:	dbus-glib libxml2 mesa curl librsvg glu gtk3 gsettings-desktop-schemas curl
Requires:	%{name}-libs = %{version}
%description
A pretty and convenient interface to your desktop: dock, panel, desklet.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	dbus-glib-devel libXcomposite-devel libxml2-devel mesa-devel curl-devel librsvg-devel glu-devel gtk3-devel
%description	devel
It contains the header files to create applications 
%package	libs
Summary:	gldi library
Requires:	libXcomposite dbus-glib libxml2 mesa curl-libs curl-devel librsvg glu gtk3
Provides:	libgldi.so.3()(64bit)
%description	libs
It contains the gldi library 
%prep
%setup -q
%build
cmake CMakeLists.txt -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}
%exclude %{_datadir}/applications
%files devel
%defattr(-,root,root)
%{_includedir}/*
%files libs
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.4.0-2
-	Updated build requires & requires to build with Photon 2.0
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 3.4.0-1
-	initial version
