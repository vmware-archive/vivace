Summary:	Lightweight image viewer
Name:		gpicview
Version:	0.2.4
Release:	1
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
%define sha1 gpicview=423143c850390db9784ad9812b9f929c18dd51ea
BuildRequires:	vte-devel libjpeg-turbo-devel
Requires:	vte
Requires:	libjpeg-turbo
%description
The GPicView package contains a lightweight image viewer.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d -m 755 %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/pixmaps/
rm -rf %{buildroot}%{_datadir}/icons
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.2.4-1
-	initial version
