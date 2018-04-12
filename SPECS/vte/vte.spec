Summary:	Terminal Emulator Widget
Name:		vte
Version:	0.28.2
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.28/%{name}-%{version}.tar.xz
%define sha1 vte=b0af0701ef9d6c7ede9c578366b12a70ac47ab66
BuildRequires:	intltool gtk2-devel ncurses-devel
Requires:	gtk2 ncurses
%description
Vte is a library (libvte) implementing a terminal emulator widget for GTK+ 2, and a minimal demonstration application (vte) that uses libvte.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool gtk2-devel ncurses-devel
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%build
%configure  --libexecdir=%{_libdir}/vte \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.28.2-1
-	initial version
