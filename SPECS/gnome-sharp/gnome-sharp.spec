Summary:	GTK+ and GNOME bindings for Mono
Name:		gnome-sharp
Version:	2.24.2
Release:	1
License:	GPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires:	intltool gettext gtk-sharp2-devel libgnomeui-devel
Requires:	gettext gtk-sharp2 libgnomeui
%description
GTK+ and GNOME bindings for Mono.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool gettext gtk-sharp2-devel libgnomeui-devel
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
%{_bindir}
%{_libdir}
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a
%{_datadir}
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.a
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.2-1
-	initial version
