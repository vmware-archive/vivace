Summary:	The GStreamer Good Plug-ins is a set of plug-ins considered by the GStreamer developers to have good quality code, correct functionality
Name:		gst-plugins-good
Version:	1.5.1 
Release:	1
License:	LGPL
URL:		http://gstreamer.freedesktop.org/
Group:		Applications/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.xz
%define sha1 gst-plugins-good=9c57e0877f8e8232d39bb0da7930aca591f13f02
BuildRequires:	gstreamer-plugins-base-devel 
Requires:	gstreamer-plugins-base
%description
The GStreamer Good Plug-ins is a set of plug-ins considered by the GStreamer developers to have good quality code, correct functionality, and the preferred license (LGPL). A wide range of video and audio decoders, encoders, and filters are included. 

%package	devel
Summary:	GStreamer Plugin Library Headers
Group: 		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer-plugins-base-devel 
%description	devel
The GStreamer Good Plug-ins is a set of plug-ins considered by the GStreamer developers to have good quality code, correct functionality, and the preferred license (LGPL). A wide range of video and audio decoders, encoders, and filters are included. 

%prep
%setup -q 
%build
./configure --prefix=%{_prefix} 
make %{?_smp_mflags}
                                                                       
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/gstreamer-1.0/*.la 
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS
%{_datadir}/
%{_libdir}/gstreamer-1.0/*.so
%exclude %{_libdir}/debug/

%files devel
%{_libdir}/gstreamer-1.0/*.la
%{_datadir}/locale
%{_datadir}/doc
%{_datadir}/gtk-doc
%{_datadir}/gstreamer-1.0

%changelog
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.5.1-1
-	initial version
