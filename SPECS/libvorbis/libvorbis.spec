Summary:	The Vorbis General Audio Compression Codec.
Name:		libvorbis
Version:	1.3.5
Release:	1
License:	BSD
URL:		http://www.xiph.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
%define sha1 libvorbis=7b4cdd4a73fadfed457ae40984cb0cc91146b300
BuildRequires:	libogg-devel
Requires:	libogg
%description
The libvorbis package contains a general purpose audio and music encoding format. This is useful for creating (encoding) and playing (decoding) sound in an open (patent free) format.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libogg-devel
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
*	Wed Jul 8 2015 Alexey Makhalov <amakhalov@vmware.com> 1.3.5-1
-	initial version
