Summary:	LibGTop is a library to get system specific data about running Processes.
Name:		libgtop
Version:	2.31.3
Release:	1
License:	GPLv2+
URL:		https://developer.gnome.org/libgtop/stable/
Group:		Development/Libraries/GNOME
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.31/%{name}-%{version}.tar.xz
BuildRequires:	glib-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	libX11-devel

%description
LibGTop is a library to get system specific data such as CPU and Memory Usage and information about running Processes.Even if LibGTop is a part of the GNOME desktop environment, the main interface of LibGTop is totally independent from any particular desktop environment, so you can also use it as a standalone library in any piece of GPLed software.

%package devel
Summary:	Header and library files for the development.
Group:		Development/Libraries
Requires:       %{name} = %{version}

%description devel
LibGTop is a library to get system specific data such as CPU and Memory Usage and information about running Processes.Even if LibGTop is a part of the GNOME desktop environment, the main interface of LibGTop is totally independent from any particular desktop environment, so you can also use it as a standalone library in any piece of GPLed software.

%prep
%setup -q

%build
./configure 	--prefix=/usr \
		--disable-static

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%post 
/sbin/ldconfig
install-info --info-dir=%{_datadir}/info %{_datadir}/info/%{name}2.info.gz

%postun
/sbin/ldconfig
install-info --delete --info-dir=%{_datadir}/info %{_datadir}/info/%{name}2.info.gz

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README copyright.txt
%{_libdir}/*.so.*
%{_datadir}/info/*
%exclude %{_datadir}/info/dir

%files devel
%defattr(-, root, root)
%{_includedir}/libgtop-2.0
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc
%{_datadir}/locale

%changelog
*	Mon Jul 06 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.31.3-1
	Initial version
