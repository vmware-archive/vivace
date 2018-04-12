Summary:	library and support programs used for configuring and customizing font access.
Name:		xfontconfig
Version:	2.11.1
Release:	1
License:	MIT and Public Domain and UCD
URL:		http://fontconfig.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.freedesktop.org/software/fontconfig/release/fontconfig-%{version}.tar.bz2
%define sha1 fontconfig=08565feea5a4e6375f9d8a7435dac04e52620ff2
Patch0:         handle_glibc_update.patch
BuildRequires:	expat-devel xfreetype2-devel
Requires:	expat expat-devel xfreetype2
%description
The Fontconfig package contains a library and support programs used for configuring and customizing font access.
%package	devel
Summary:	Header and development files for fontconfig
Requires:	%{name} = %{version}
Requires:	expat-devel xfreetype2-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -qn fontconfig-%{version}
%patch0 -p1
%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
	    --localstatedir=%{_localstatedir} \
	    --disable-docs       \
	    --docdir=%{_datadir}/fontconfig-2.11.1
make %{?_smp_mflags}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
%files
%defattr(-,root,root)
%{_prefix}/*
%{_sysconfdir}/*
%{_var}/*
%exclude %{_libdir}/debug/
%exclude %{_includedir}/
%exclude %{_prefix}/src/
%exclude %{_libdir}/pkgconfig/*.pc
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%changelog
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 2.11.1-1
-	initial version
