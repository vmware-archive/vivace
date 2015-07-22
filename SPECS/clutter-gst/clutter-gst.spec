Summary:	The Clutter Gst is an integration library for using GStreamer with Clutter.
Name:		clutter-gst 
Version:	2.0.14 
Release:	1
License:	LGPLv2.1+
URL:		https://blogs.gnome.org/clutter/
Group:		System/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.xz
%define sha1 clutter-gst=e0238f44046877116c7361eab255d775807365ac
BuildRequires:	gstreamer-plugins-base-devel clutter-devel
Requires:	gstreamer-plugins-base clutter

%description
The Clutter Gst is an integration library for using GStreamer with Clutter. Its purpose is to implement the ClutterMedia interface using GStreamer. 

%package devel
Summary: Development files for clutter-gst
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: gstreamer-plugins-base-devel clutter-devel

%description devel
The Clutter Gst is an integration library for using GStreamer with Clutter. Its purpose is to implement the ClutterMedia interface using GStreamer. 

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
rm -rf %{buildroot}%{_libdir}/gstreamer-1.0/*.la 
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
%{_includedir}
%{_libdir}/*.so
%{_libdir}/gstreamer-1.0/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0
%exclude %{_datadir}/gtk-doc 

%changelog
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.0.14 -1
-	initial version
