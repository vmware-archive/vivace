Summary:	The GNOME Doc Utils
Name:		gnome-doc-utils
Version:	0.20.10
Release:	1
License:	LGPLv2+ and GPLv2+ and GFDL
URL:		http://gnome.org
Group:		System Environment/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.20/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool libxslt gobject-introspection-devel
Requires:	libxml2 libxslt
BuildArch:	noarch
%description
Documentation tools for GNOME
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}
%changelog
*	Tue Jun 23 2015 Alexey Makhalov <amakhalov@vmware.com> 0.20.10-1
-	initial version
