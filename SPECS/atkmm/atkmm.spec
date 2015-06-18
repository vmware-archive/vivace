Summary:	Atkmm is the official C++ interface for the ATK accessibility toolkit library. 
Name:		atkmm
Version:	2.22.7
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.22/%{name}-%{version}.tar.xz
BuildRequires:	glib-devel glibmm atk-devel gobject-introspection-devel gobject-introspection-python python2-devel python2-libs
Requires:	glib glibmm libsigc++ pkg-config atk 
%description
Atkmm is the official C++ interface for the ATK accessibility toolkit library.
%package	devel
Summary:	Header and development files for
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} 
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Mon Jun 15 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.22.7-1
-	initial version
