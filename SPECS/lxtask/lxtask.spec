Summary:	Lightweight task manager
Name:		lxtask
Version:	0.1.6
Release:	1%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxtask=c61192c8393dd827bd3abad69837d783cfb07d54
BuildRequires:	intltool gtk2-devel
Requires:	gtk2
%description
The LXTask package contains a lightweight and desktop-independent task manager.
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
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1.6-1
-	initial version
