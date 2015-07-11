Summary:	Metapackage for Vivace User Interface
Name:		vui
Version:	0.1
Release:	1
License:	Apache License
Group:		System Environment/Base
URL:		http://photon.org
Source:		%{name}-%{version}.tar.xz
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	vui
BuildArch:	noarch
Requires:	lxde-common lxdm alsa-utils lxterminal firefox thunderbird gpicview grdesktop lxtask

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
cp -a /etc/skel/.config/cairo-dock /root/.config/ 
cp -a /etc/skel/.config/pcmanfm /root/.config/

%files
%{_sysconfdir}/skel/.config/*
%{_datadir}
