Summary:	X11 Xfont2 runtime library.
Name:		libXfont2
Version:	2.0.5
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXfont=b21b000ba527e05f77c2ec53855d2793b19189ba
BuildRequires:	libfontenc-devel freetype2-devel xtrans
Requires:	libfontenc freetype2
%description
The X11 Xfont runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libfontenc-devel freetype2-devel xtrans
%description	devel
It contains the libraries and header files to create applications
%prep
%autosetup
%build
%configure --disable-devel-docs
make %{?_smp_mflags}
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%exclude %{_libdir}/pkgconfig/*.pc
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 2.0.5-1
- Version update
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 2.0.3-1
- Version update
* Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.5.1-2
- Updated build requires & requires to build with Photon 2.0
* Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.5.1-1
- initial version
