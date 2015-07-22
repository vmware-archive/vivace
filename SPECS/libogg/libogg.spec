Summary:	OGG library.
Name:		libogg
Version:	1.3.2
Release:	1
License:	BSD
URL:		http://www.xiph.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz
%define sha1 libogg=5e525ec6a4135066932935c01d2c309ea5009f8d
%description
The libogg package contains the Ogg file structure. This is useful for creating (encoding) or playing (decoding) a single physical bit stream.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
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
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/*
%changelog
*	Wed Jul 8 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.2-1
-	initial version
