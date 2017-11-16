Summary:	USB access library
Name:		libusb
Version:	1.0.19
Release:	2	
License:	LGPLv2+
URL:		http://sourceforge.net/projects/libusb
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	 http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
%define sha1 libusb=c5d14ced155233ceeb5107c7eb3b94b16649ae05
BuildRequires:	systemd-devel
Requires:	systemd
%description
The libusb package contains a library used by some applications for USB device access.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.9.19-2
-	Updated build requires & requires to build with Photon 2.0
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.19-1
-	initial version
