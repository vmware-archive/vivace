Summary:	Metapackage for Vivace User Interface
Name:		vui
Version:	0.1
Release:	1%{?dist}
License:	Apache License
Group:		System Environment/Base
URL:		http://photon.org
Source:		%{name}-%{version}.tar.xz
%define sha1 vui=b82907f114c8bd81e6b7676a56fbe9d9977494ea
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	vui
BuildArch:	noarch
#Requires: 	thunderbird open-vm-tools-vivace
Requires: 	linux-drivers-gpu firefox gtksourceviewmm alsa-utils gpicview grdesktop gpicview hicolor-icon-theme
%description
Metapackage for Vivace User Interface.

%prep
%setup -q

%build

%install
find -type d -exec install -d {,%{buildroot}/}{} \;
find -type f -exec install -D -m 644 {,%{buildroot}/}{} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
#copy skel to root home folder
mkdir -p /root/.config
cp -a /etc/skel/.config/pcmanfm /root/.config/

%files
%{_sysconfdir}/skel/.config/*
%{_datadir}

%changelog
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1-1
-	initial version
