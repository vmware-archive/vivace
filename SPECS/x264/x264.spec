Summary:	Library for encoding video streams into the H.264/MPEG-4 AVC format
Name:		x264
Version:	20170822
Release:	1
License:	GPLv2
URL:		http://www.videolan.org/vlc
Group:		System Environment/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.videolan.org/x264/snapshots/x264-snapshot-20170822-2245-stable.tar.bz2
%define sha1 x264=6cd281541e5f0d1ddc3368a6965acc68a990b51d
BuildRequires:	yasm
%description
x264 package provides a library for encoding video streams into the H.264/MPEG-4 AVC format.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}-%{release}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n x264-snapshot-20170822-2245-stable
%build
./configure --prefix=%{_prefix} \
            --disable-static \
	    --enable-shared \
	    --disable-cli
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.so
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%changelog
*	Tue Dec 05 2017 Alexey Makhalov <amakhalov@vmware.com> 20170822-1
-	initial version
