Summary:	VLC media player
Name:		vlc
Version:	2.2.8
Release:	1
License:	GPLv2
URL:		http://www.videolan.org/vlc
Group:		System Environment/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://mirror.os6.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
%define sha1 vlc=b960ec5bdb9a51da285430fc68962927ccc87187
Patch0:		vlc-2.2.8-ffmpeg3-1.patch
BuildRequires:	gstreamer-plugins-base-devel gtk2-devel lua-devel ncurses-devel libxml2-devel systemd-devel libgcrypt-devel ffmpeg-devel
Requires:	gstreamer-plugins-base gtk2 lua ncurses libxml2 systemd libgcrypt ffmpeg
%description
VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gstreamer-plugins-base-devel gtk2-devel lua-devel ncurses-devel libxml2-devel libgcrypt-devel ffmpeg-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%patch0 -p1
%build
sed -i 's/error-implicit-function-declaration//' configure
./configure --prefix=%{_prefix} \
            --disable-static \
	    --disable-mad \
	    --disable-a52
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so
%{_datadir}/*
%exclude %{_datadir}/kde4/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%changelog
*	Tue Dec 05 2017 Alexey Makhalov <amakhalov@vmware.com> 2.2.8-1
-	Version update
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.2.0-2
-	Updated build requires & requires to build with Photon 2.0
*	Thu Jul 9 2015 Alexey Makhalov <amakhalov@vmware.com> 2.2.0-1
-	initial version
