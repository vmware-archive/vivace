Summary:	Service Provider Interface for the Assistive Technologies.
Name:		at-spi2-core
Version:	2.16.0
Release:	1
License:	LGPLv2+
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.16/%{name}-%{version}.tar.xz
%define sha1 at-spi2-core=efff62fb8cb8f629d5cdb2fca3e249fa69a12899
BuildRequires:	intltool glib-devel dbus-devel libX11-devel libXtst-devel libXext-devel libXi-devel
Requires:	dbus dbus-devel glib libX11 libXtst libXext libXi
%description
The At-Spi2 Core package is a part of the GNOME Accessibility Project. It provides a Service Provider Interface for the Assistive Technologies available on the GNOME platform and a library against which applications can be linked.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel dbus-devel libX11-devel libXtst-devel libXext-devel libXi-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
# --enable-vala
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_libexecdir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/pkgconfig/*.pc
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 2.16.0-1
-	initial version
