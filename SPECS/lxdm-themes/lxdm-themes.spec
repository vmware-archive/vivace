Summary:	Customized theme for LXDM. 
Name:		lxdm-themes
Version:	1
Release:	1
License:	GPLv2+
URL:		http://gnome-look.org
Group:		System/GUI/GNOME
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.12/%{name}-%{version}.tar.xz
%define sha1 lxdm-themes=289aa4a4f15425b7638e4f2b4bf82d9a436e56d5 
BuildArch:	noarch
%description
Customized theme for LXDM. 
%prep
%setup -qn lxdm-themes

%install
install -d -m 755 %{buildroot}%{_datadir}/lxdm/themes/blue/
install -d -m 755 %{buildroot}%{_datadir}/backgrounds/
install -m 644 themes/blue/* %{buildroot}%{_datadir}/lxdm/themes/blue/
install -m 644 background/weave.png %{buildroot}%{_datadir}/backgrounds/

%files
%defattr(-, root, root)
%{_datadir}/lxdm/themes/blue/
%{_datadir}/backgrounds/

%changelog
*	Fri Aug 28 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1-1
-	initial version
