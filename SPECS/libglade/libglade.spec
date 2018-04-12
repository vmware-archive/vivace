Summary:	libglade libraries
Name:		libglade
Version:	2.6.4
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
%define sha1 libglade=8465851733b8a0efbe57c43efc0f140d8e2d2edb
BuildRequires:	intltool gtk2-devel python2-libs python2-devel libxml2-devel
Requires:	gtk2 python2 libxml2
%description
The libglade package contains libglade libraries. These are useful for loading Glade interface files in a program at runtime.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool gtk2-devel python2-libs python2-devel libxml2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
sed -i '/DG_DISABLE_DEPRECATED/d' glade/Makefile.in
%configure --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.6.4-1
-	initial version
