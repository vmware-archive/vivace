Summary:	Cogl is a modern 3D graphics API.
Name:		cogl
Version:	1.20.0
Release: 	2	
License:	LGPLv2.1+
URL:		http://gnudatalanguage.sourceforge.net/
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/cogl/1.20/%{name}-1.20.0.tar.xz
%define sha1 cogl=46a0bfca30c440ad4b6a7b07ed7aa3e643d57401
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	gdk-pixbuf-devel mesa-devel xpango-devel libXrandr-devel libXcomposite-devel
Requires:	gdk-pixbuf mesa xpango libXrandr libXcomposite
%description
Cogl is a modern 3D graphics API with associated utility APIs designed to expose the features of 3D graphics hardware using a direct state access API design, as opposed to the state-machine style of OpenGL. 
%package	devel
Summary:	Header and development files
Group:		Development/Libraries/GNOME
Requires:	%{name} = %{version}

%description	devel
Cogl is a modern 3D graphics API with associated utility APIs designed to expose the features of 3D graphics hardware using a direct state access API design, as opposed to the state-machine style of OpenGL. 
%prep
%setup -q
%build
./configure 	--prefix=%{_prefix} \
		--disable-static

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING NEWS README ChangeLog
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/cogl/
%{_libdir}/pkgconfig/
%{_datadir}

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.20.0-2
-	Updated build requires & requires to build with Photon 2.0
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.20.0-1
-	Initial build. First version
