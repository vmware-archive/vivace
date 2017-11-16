Summary:	GStreamer streaming media framework plug-ins
Name:		gstreamer-plugins-base
Version:	1.5.1
Release:	2	
License:	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Group:		Applications/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
%define sha1 gst-plugins-base=fa6c377924fa6eed7f91a94a862a6f342c40a1f1
BuildRequires:	gstreamer-devel xpango-devel alsa-lib-devel libvorbis-devel
Requires:	gstreamer xpango alsa-lib libvorbis
%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.
%package	devel
Summary:	GStreamer Plugin Library Headers
Group: 		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer-devel xpango-devel alsa-lib-devel libvorbis-devel
%description	devel
GStreamer Plugins Base library development and header files.
%prep
%setup -q -n gst-plugins-base-%{version}
export DOCS_ARE_INCOMPLETE_PLEASE_FIXME=0
%build
./configure --prefix=%{_prefix} 
make %{?_smp_mflags}
                                                                       
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS gst-plugins-base.doap
%{_bindir}/gst-discoverer-1.0
%{_bindir}/gst-play-1.0
%{_bindir}/gst-device-monitor-1.0
%{_mandir}/man1/gst-discoverer-1.0*
%{_mandir}/man1/gst-play-1.0*
%{_mandir}/man1/gst-device-monitor-1.0*

%{_libdir}/*.so.*

%{_libdir}/gstreamer-1.0/*.so
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so 
%{_libdir}/pkgconfig/*.pc
%{_libdir}/gstreamer-1.0/*.so
%{_libdir}/gstreamer-1.0/*.la
%{_libdir}/girepository-1.0/*.typelib
#%{_datadir}/gir-1.0/*.gir
%{_datadir}/*

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.28-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Jun 25 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.24.28-1
-	initial version
