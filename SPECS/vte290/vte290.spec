Summary:	Terminal Emulator Widget
Name:		vte290
Version:	0.36.3
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.36/vte-%{version}.tar.xz
%define sha1 vte=a7acc1594eb6fa249edccb059c21132b3aa2657b
BuildRequires:	intltool gtk3-devel ncurses-devel
Requires:	gtk3 ncurses
%description
Vte is a library (libvte) implementing a terminal emulator widget for GTK+ 3, and a minimal demonstration application (vte) that uses libvte.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool gtk3-devel ncurses-devel
%description	devel
It contains the header files to create applications 
%prep
%setup -qn vte-%{version}
%build
./configure 	--prefix=%{_prefix} \
            	--libexecdir=%{_libdir}/vte290 \
		--sysconfdir=%{_sysconfdir} \
	        --disable-static

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_sysconfdir}/profile.d
%exclude %{_libdir}/debug/
%{_datadir}/*
%exclude %{_sysconfdir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Tue Jul 07 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.36.3-1
-	initial version
