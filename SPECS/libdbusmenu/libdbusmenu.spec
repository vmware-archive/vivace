Summary:	Common code for indicator-applet
Name:		libdbusmenu
Version:	12.10.2
Release:	1
License:	LGPLv3 or LGPLv2 and GPLv3
URL:		https://launchpad.net/libdbusmenu
Group:		User Interface/Library
Source0:	https://launchpad.net/%{name}/12.10/%{version}/+download/%{name}-%{version}.tar.gz
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	intltool gtk3-devel gnome-doc-utils json-glib-devel gtk2-devel
Requires:	gtk3 json-glib gtk2
%description
A small little library that was created by pulling out some comon code out of indicator-applet. It passes a menu structure across DBus so that a program can create a menu simply without worrying about how it is displayed on the other side of the bus.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	intltool gtk3-devel json-glib-devel gtk2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -c
cp -a %{name}-%{version} %{name}-gtk3-%{version}
%build
pushd %{name}-%{version}
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
./configure --prefix=%{_prefix}                 \
            --sysconfdir=%{_sysconfdir}         \
            --disable-static			\
	    --disable-scrollkeeper		\
	    --with-gtk=2			\
	    --enable-introspection		\
	    --disable-dumper
make %{?_smp_mflags}
popd
pushd %{name}-gtk3-%{version}
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
./configure --prefix=%{_prefix}                 \
            --sysconfdir=%{_sysconfdir}         \
            --disable-static			\
	    --disable-scrollkeeper		\
	    --with-gtk=3			\
	    --enable-introspection		\
	    --disable-dumper
popd
%install
pushd %{name}-gtk3-%{version}
make DESTDIR=%{buildroot} install
popd
pushd %{name}-%{version}
make DESTDIR=%{buildroot} install
popd
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/debug
%{_datadir}/*
%{_libexecdir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Wed Jun 24 2015 Alexey Makhalov <amakhalov@vmware.com> 12.10.2-1
-	Initial build. First version
