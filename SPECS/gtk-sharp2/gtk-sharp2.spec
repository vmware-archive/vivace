Summary:	GTK+ and GNOME bindings for Mono
Name:		gtk-sharp2
Version:	2.12.26
Release:	1
License:	GPLv2+
URL:		http://www.monodevelop.com
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}12/gtk-sharp-%{version}.tar.gz
%define sha1 gtk-sharp=2f5007362f374a5a967dc6b16cdaaf3921dad1fa
BuildRequires:	gettext tzdata mono-devel libglade-devel
Requires:	gettext mono libglade
Requires:	perl-XML-LibXML
%description
GTK+ and GNOME bindings for Mono.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gettext tzdata mono-devel libglade-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n gtk-sharp-2.12.26
%build
autoreconf -vif
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
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.12.26-1
-	initial version
