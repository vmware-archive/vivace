Summary:	VLC media player
Name:		vlc
Version:	2.2.0
Release:	1
License:	GPLv2
URL:		http://www.videolan.org/vlc
Group:		System Environment/Multimedia
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://mirror.os6.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	gstreamer-plugins-base-devel gtk2-devel lua-devel ncurses-devel libxml2-devel systemd libgcrypt-devel
Requires:	gstreamer-plugins-base gtk2 lua ncurses libxml2 systemd libgcrypt
%description
VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gstreamer-plugins-base-devel gtk2-devel lua-devel ncurses-devel libxml2-devel libgcrypt-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --disable-static \
	    --disable-mad \
	    --disable-avcodec \
	    --disable-swscale \
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
*	Thu Jul 9 2015 Alexey Makhalov <amakhalov@vmware.com> 2.2.0-1
-	initial version
