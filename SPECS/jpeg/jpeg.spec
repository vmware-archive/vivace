Summary:	Implements JPEG image encoding, decoding and transcoding.
Name:		jpeg
Version:	9a
Release:	1
License:	IJG
URL:		http://www.ijg.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.ijg.org/files/jpegsrc.v9a.tar.gz
%define sha1 jpeg=d65ed6f88d318f7380a3a5f75d578744e732daca
BuildRequires:	nasm
%description
libjpeg is a library that implements JPEG image encoding, decoding and transcoding.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
#sed -i -e '/^docdir/     s:$:/libjpeg-turbo-1.4.0:' \
#       -e '/^exampledir/ s:$:/libjpeg-turbo-1.4.0:' Makefile.in &&
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
*	Mon Aug 17 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 9a-1
-	initial version
