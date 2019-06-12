Summary:	The Desktop File Utils package contains command line utilities for working with Desktop entries
Name:		desktop-file-utils
Version:	0.22
Release:	1%{?dist}
License:	GPLv2+
URL:		http://freedesktop.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://freedesktop.org/software/%{name}/releases/%{name}-%{version}.tar.xz
%define sha1 desktop-file-utils=617f130091dbcc5e739d82ee48e2b3932da5957d
BuildRequires:	intltool glib-devel
Requires:	glib
%description
The Desktop File Utils package contains command line utilities for working with Desktop entries. These utilities are used by Desktop Environments and other applications to manipulate the MIME-types application databases and help adhere to the Desktop Entry Specification.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.22-1
-	initial version
