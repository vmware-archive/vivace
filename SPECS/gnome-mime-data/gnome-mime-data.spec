Summary:	The GNOME MIME Data
Name:		gnome-mime-data
Version:	2.18.0
Release:	1
License:	LGPLv2+
URL:		http://gnome.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.18/%{name}-%{version}.tar.bz2
%define sha1 gnome-mime-data=9ce7b1a24a97f275f60b416fae82d81c1010cb65
BuildArch:	noarch
BuildRequires:	intltool libxml2-devel
Requires:	libxml2
%description
ZThe GNOME MIME Data package contains the base set of file types and applications for GNOME-2.
%prep
%setup -q
%build
%configure --sysconfdir=/etc/gnome/2.30.2
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}
%{_datadir}
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.18.0-1
-	initial version
