Summary:	TIFF libraries and associated utilities.
Name:		libtiff
Version:	4.0.3
Release:	1
License:	libtiff
URL:		http://www.remotesensing.org/libtiff
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.osgeo.org/%{name}/tiff-%{version}.tar.gz
%define sha1 tiff=652e97b78f1444237a82cbcfe014310e776eb6f0
Patch0:		tiff-4.0.3-fixes-1.patch
BuildRequires:	jpeg-devel
Requires:	jpeg
%description
The LibTIFF package contains the TIFF libraries and associated utilities. The libraries are used by many programs for reading and writing TIFF files and the utilities are used for general work with TIFF files.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libjpeg-turbo-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n tiff-%{version}
%patch0 -p1
%build
./configure --prefix=%{_prefix} --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.3-1
-	initial version
