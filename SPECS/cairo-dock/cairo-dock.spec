Summary:	dock, panel, desklet.
Name:		cairo-dock
Version:	3.4.0
Release:	1
License:	LGPLv2+
URL:		http://glx-dock.org/
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://launchpad.net/cairo-dock-core/3.4/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	cmake dbus-glib-devel libXcomposite-devel libxml2-devel mesa-devel curl librsvg-devel glu-devel gtk3-devel
Requires:	dbus-glib libxml2 mesa curl librsvg glu gtk3 gsettings-desktop-schemas
Requires:	%{name}-libs = %{version}
%description
A pretty and convenient interface to your desktop: dock, panel, desklet.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	dbus-glib-devel libXcomposite-devel libxml2-devel mesa-devel curl librsvg-devel glu-devel gtk3-devel
%description	devel
It contains the header files to create applications 
%package	libs
Summary:	gldi library
Requires:	libXcomposite dbus-glib libxml2 mesa curl librsvg glu gtk3
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
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 3.4.0-1
-	initial version
