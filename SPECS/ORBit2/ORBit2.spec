Summary:	High-performance CORBA Object Request Broker
Name:		ORBit2
Version:	2.14.19
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.14/%{name}-%{version}.tar.bz2
BuildRequires:	libidl-devel
Requires:	libidl
%description
The ORBit2 package contains a high-performance CORBA Object Request Broker. This allows programs to send requests and receive replies from other programs.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libidl-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
#ac_cv_cflags_gcc_option__Werror_implicit_function_declaration=no
./configure --prefix=%{_prefix} \
            --sysconfdir=/etc/gnome/2.30.2
sed 's/-DG_DISABLE_DEPRECATED//' -i linc2/src/Makefile
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/*.a
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.14.19-1
-	initial version
