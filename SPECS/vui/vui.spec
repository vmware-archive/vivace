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
Requires:	lxde-common alsa-utils lxterminal firefox thunderbird

%description
Metapackage for Vivace User Interface.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/root/.config
find -type d -exec install -d {,%{buildroot}/root/.config/}{} \;
find -type f -exec install -D -m 644 {,%{buildroot}/root/.config/}{} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/root/.config
