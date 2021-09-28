Summary:	The FriBidi package is an implementation of the Unicode Bidirectional Algorithm (BIDI)
Name:		fribidi
Version:	1.0.9
Release:	1%{?dist}
License:	LGPLv2+
URL:		https://github.com/fribidi
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/fribidi/fribidi/releases/download/v%{version}/%{name}-%{version}.tar.xz
%define sha1 fribidi=6646193abcbdb8434ff0cc5da28c252a59e7dfb4
BuildRequires:  meson >= 0.50
BuildRequires:  ninja-build
%description
The FriBidi package is an implementation of the Unicode Bidirectional Algorithm (BIDI)
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
mkdir build
cd build
meson --prefix=/usr --buildtype=release ..
ninja
%install
pushd build
DESTDIR=%{buildroot} ninja install
popd
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig
%{_datadir}/*
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 1.0.9-1
- Initial version
