Summary:	Mozilla's JavaScript engine.
Name:		js
Version:	17.0.0
Release:	1
License:	GPLv2+ or LGPLv2+ or MPLv1.1
URL:		http://www.mozilla.org/js
Group:		Development/Languages
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.mozilla.org/pub/mozilla.org/%{name}/moz%{name}%{version}.tar.gz
BuildRequires:	libffi nspr python2-libs python2-devel
Requires:	libffi nspr python2
%description
JS is Mozilla's JavaScript engine written in C/C++.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using this package.
%prep
%setup -q -n moz%{name}%{version}/js/src
%build
./configure --prefix=%{_prefix} \
	    --enable-threadsafe \
	    --with-system-ffi \
	    --with-system-nspr
#	    --enable-readline \
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/include/js-17.0/            \
     %{buildroot}/usr/lib/libmozjs-17.0.a         \
     %{buildroot}/usr/lib/pkgconfig/mozjs-17.0.pc \
     -type f -exec chmod -v 644 {} \;
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Tue May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 17.0.0-1
-	initial version
