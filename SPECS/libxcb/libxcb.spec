Summary:	Interface to the X Window System protocol.
Name:		libxcb
Version:	1.11
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
%define sha1 libxcb=8343b417d7eeb2a2c6b6c4a87a03a4fd0fc65c46
BuildRequires:	python2-devel
BuildRequires:	python2-libs
BuildRequires:	libXau-devel xcb-proto
BuildRequires:	libXdmcp-devel
BuildRequires:  python-xml
Requires:	libXdmcp
Requires:	libXau
Provides:	pkgconfig(x11-xcb)
%description
The libxcb package provides an interface to the X Window System protocol, which replaces the current Xlib interface. Xlib can also use XCB as a transport layer, allowing software to make requests and receive responses with both.
%package	devel
Summary:	Header and development files for libxcb
Requires:	%{name} = %{version}
Requires:	libXau-devel xcb-proto libXdmcp-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
sed -i "s/pthread-stubs//" configure
./configure --prefix=%{_prefix} \
            --enable-xinput \
	    --docdir=%{_datadir}/doc/libxcb-1.11

sed -i "s#from xml.etree.cElementTree import \*#from xml.etree.ElementTree import ElementTree#g" src/c_client.py
make %{?_smp_mflags}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%install
make DESTDIR=%{buildroot} install
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 1.11-1
-	initial version
