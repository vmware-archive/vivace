Summary:	A streaming media framework 
Name:		gstreamer
Version:	1.5.1
Release:	1
License:	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.5.1.tar.xz
BuildRequires:	glib-devel libxml2-devel
BuildRequires:	gobject-introspection-devel gobject-introspection-python
Requires:	glib libxml2
Provides:	pkgconfig(gstreamer-1.0)
Provides:	pkgconfig(gstreamer-base-1.0)
%description
GStreamer is a streaming media framework that enables applications to share a common set of plugins for things like video encoding and decoding, audio encoding and decoding, audio and video filters, audio visualisation, web streaming and anything else that streams in real-time or otherwise. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel libxml2-devel
Requires:	gobject-introspection-devel gobject-introspection-python
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n gstreamer-%{version}

%build
./configure --prefix=%{_prefix} 
make

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README RELEASE TODO
%{_bindir}
#%{_sysconfdir}/*
%{_libdir}/*.so*
%{_libexecdir} 
%{_libdir}/gstreamer-1.0/*.so
#%{_datadir}/gir-1.0/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so 
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gstreamer-1.0/*.so
%{_libdir}/gstreamer-1.0/include*
%{_libdir}/gstreamer-1.0/*.la
%{_libdir}/girepository-1.0/* 
%{_datadir}/*

%changelog
*	Wed Jun 24 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.5.1-1
-	initial version
