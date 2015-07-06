Summary:	fork of the original IJG libjpeg which uses SIMD.
Name:		libjpeg-turbo
Version:	1.4.0
Release:	1
License:	IJG
URL:		http://sourceforge.net/projects/libjpeg-turbo
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	nasm
%description
libjpeg-turbo is a fork of the original IJG libjpeg which uses SIMD to accelerate baseline JPEG compression and decompression. libjpeg is a library that implements JPEG image encoding, decoding and transcoding.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
sed -i -e '/^docdir/     s:$:/libjpeg-turbo-1.4.0:' \
       -e '/^exampledir/ s:$:/libjpeg-turbo-1.4.0:' Makefile.in &&
./configure --prefix=%{_prefix} --disable-static \
                   --mandir=/usr/share/man \
		   --with-jpeg8     
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
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4.0-1
-	initial version
