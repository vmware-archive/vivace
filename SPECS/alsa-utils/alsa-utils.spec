Summary:	ALSA Utilities.
Name:		alsa-utils
Version:	1.1.5
Release:	1
License:	LGPLv2+
URL:		http://alsa-project.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.alsa-project.org/pub/utils/alsa-utils-1.1.5.tar.bz2
%define sha1 alsa-utils=9e89d1df027e1e49da5f149544b97e5227ec252c
#Patch0:		ens1371.patch
BuildRequires:	alsa-lib-devel ncurses-devel
Requires:	linux-sound alsa-lib ncurses
%description
The ALSA Utilities package contains various utilities which are useful for controlling your sound card.
%prep
%setup -q
#%patch0 -p1
%build
./configure --prefix=%{_prefix} --disable-alsaconf --disable-xmlto
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d -m 755 $RPM_BUILD_ROOT/var/lib/alsa
%post
alsactl init
alsactl -L store
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
/lib/*
%{_sbindir}/*
%{_datadir}/*
%{_localstatedir}/*
%changelog
*	Fri May 29 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.29-1
-	initial version
