Summary:	USB access library
Name:		libusb
Version:	1.0.19
Release:	1
License:	LGPLv2+
URL:		http://sourceforge.net/projects/libusb
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	 http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	systemd
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
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.19-1
-	initial version
