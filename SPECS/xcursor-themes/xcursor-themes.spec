%define debug_package %{nil}
Summary:	redglass and whiteglass animated cursor themes.
Name:		xcursor-themes
Version:	1.0.6
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
%define sha1 xcursor-themes=b56fd5bf5b1ada0532a85c27db0d296e392168c5
BuildRequires:	xorg-applications libXcursor-devel
Requires:	libXcursor
%description
The xcursor-themes package contains the redglass and whiteglass animated cursor themes.
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 1.0.6-1
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.4-1
- initial version
