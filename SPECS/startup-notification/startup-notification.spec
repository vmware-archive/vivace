Summary:	The startup-notification package contains startup-notification libraries. 
Name:		startup-notification 
Version:	0.12
Release:	1
License:	GPLv2+
URL:		https://www.freedesktop.org/wiki/Software/startup-notification/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/startup-notification/releases/startup-notification-0.12.tar.gz
%define sha1 startup-notification=4198bce2808d03160454a2940d989f3a5dc96dbb
BuildRequires:	xcb-util-devel libX11-devel
Requires:	xcb-util libX11
%description
The startup-notification package contains startup-notification libraries. These are useful for building a consistent manner to notify the user through the cursor that the application is loading. 
%package devel
Summary:        Include Files and Libraries for Development
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
%description devel
Include Files and Libraries for Development
%prep
%setup -q 
%build
%configure --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%exclude %{_includedir}/*

%files devel
%defattr(-,root,root)
%{_includedir}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*	Wed Feb 24 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.12-1
-	initial version
