Summary:	Yasm assembler.
Name:		yasm
Version:	1.3.0
Release:	1%{?dist}
License:	BSD
URL:		http://www.tortall.net/projects/yasm
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.tortall.net/projects/%{name}/releases/%{name}-%{version}.tar.gz
%define sha1 yasm=b7574e9f0826bedef975d64d3825f75fbaeef55e
BuildRequires:	python3-devel python3-libs
Requires:	python3
%description
Yasm is a complete rewrite of the NASM-2.11.08 assembler.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
sed -i 's#) ytasm.*#)#' Makefile.in &&
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_mandir}/*
%changelog
*	Fri May 29 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.0-1
-	initial version
