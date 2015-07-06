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
BuildRequires:	vte-devel
Requires:	vte
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
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.2.4-1
-	initial version
