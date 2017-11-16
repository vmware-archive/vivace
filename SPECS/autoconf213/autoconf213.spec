%define __requires_exclude perl(find.pl)
Summary:	The package automatically configure source code
Name:		autoconf213
Version:	2.13
Release:	1%{?dist}
License:	GPLv2
URL:		http://www.gnu.org/software/autoconf
Group:		System Environment/Base
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz
%define sha1 autoconf=e4826c8bd85325067818f19b2b2ad2b625da66fc
Patch0:		autoconf-make-check.patch
Patch1:		autoconf-2.13-consolidated_fixes-1.patch
BuildRequires:	m4
Requires:	m4
Requires:	perl
BuildArch:      noarch
autoreq:	no
%description
The package contains programs for producing shell scripts that can
automatically configure source code.
%prep
%setup -qn autoconf-%{version}
#%patch0 -p1
%patch1 -p1
%build
mv -v autoconf.texi autoconf213.texi
rm -v autoconf.info
./configure \
	--prefix=%{_prefix} \
	--disable-silent-rules \
	--program-suffix=2.13
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}

%check
make -k check %{?_smp_mflags}  TESTSUITEFLAGS="1-500"

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Wed Nov 8 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.13-1
-	Initial build.	First version
