Summary:	Document system for GNOME-2
Name:		libbonobo
Version:	2.32.1
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.32/%{name}-%{version}.tar.bz2
%define sha1 libbonobo=c7650434a4f328eae6f38a29ee8dadd455f35f9c
Patch0:		libbonobo-glib-2_36.patch	
BuildRequires:	libart_lgpl-devel popt-devel ORBit2-devel
Requires:	libart_lgpl popt ORBit2
%description
The libbonobo package contains libbonobo libraries. This is a component and compound document system for GNOME-2.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libart_lgpl-devel popt-devel ORBit2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p1
%build
%configure  --sysconfdir=/etc/gnome/2.30.2 \
            --localstatedir=/var/lib       \
	    --disable-canberra
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%{_libexecdir}
%{_sbindir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.32.1-1
-	initial version
