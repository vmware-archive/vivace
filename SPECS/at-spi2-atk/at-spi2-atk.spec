Summary:	library that bridges ATK to At-Spi2 D-Bus service.
Name:		at-spi2-atk
Version:	2.16.0
Release:	1
License:	LGPLv2+
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.16/%{name}-%{version}.tar.xz
%define sha1 at-spi2-atk=b3b8db5f1482b3fba2ed4a9528a7eac98515b607
BuildRequires:	at-spi2-core-devel atk-devel glib-devel libX11-devel
Requires:	at-spi2-core atk glib glib-schemas libX11
%description
The At-Spi2 Atk package contains a library that bridges ATK to At-Spi2 D-Bus service.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	at-spi2-core-devel atk-devel glib-devel libX11-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
# --enable-vala
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post
glib-compile-schemas /usr/share/glib-2.0/schemas
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
-	initial version
