Summary:	GNU's Ubiquitous Intelligent Language for Extension
Name:		guile
Version:	1.8.8
Release:	1
License:	LGPL-3.0+
URL:		http://www.gnu.org/software/guile/
Group:		Development/Languages/Scheme
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
%define sha1 guile=548d6927aeda332b117f8fc5e4e82c39a05704f9
BuildRequires:	libtool libltdl-devel pkg-config libxml2-devel

%description
The Guile package contains the Project GNU's extension language library. Guile also contains a stand alone Scheme interpreter. 

%package devel
License:        LGPLV2.1+
Group:          Development/Languages/Scheme
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Requires:       gmp-devel readline-devel ncurses-devel libffi
Requires:       guile
BuildRequires:	libtool libltdl-devel pkg-config libxml2-devel
Conflicts:      libguile1-devel

%description devel
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%prep
%setup -q 
sed -i 's# -Werror##g' configure
%build
./configure 	--prefix=%{_prefix} \
		--disable-static \
		--without-libunistring-prefix
GUILE_ERROR_ON_WARNING=no
make %{?_smp_mflags} -i
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -f usr/share/info/dir 
%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post devel
install-info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
install-info --info-dir=%{_infodir} %{_infodir}/r5rs.info.gz

%postun devel
install-info --delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
install-info --delete --info-dir=%{_infodir} %{_infodir}/r5rs.info.gz

%files 
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING* ChangeLog GUILE-VERSION HACKING
%doc LICENSE NEWS README THANKS
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/guile.1.gz
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}
%{_datadir}/guile
%{_datadir}/doc 
%{_datadir}/aclocal
%exclude %{_infodir}/dir 
%{_infodir}/*.gz
%{_libdir}/libguile*.so
%{_libdir}/libguile*.la
%{_libdir}/pkgconfig/*


%changelog
*	Wed Jul 1 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.8.8-1
-	initial version
