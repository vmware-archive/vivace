Summary:	Metapackage for Vivace User Interface
Name:		vui
Version:	4.0
Release:	1%{?dist}
License:	Apache License
Group:		System Environment/Base
URL:		http://photon.org
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	vui
BuildArch:	noarch
Requires: 	xinit dmenu st linux-drivers-gpu alsa-utils
# firefox
%description
Metapackage for Vivace User Interface.

%prep

%build

%files

%changelog
* Tue Aug 03 2021 Alexey Makhalov <amakhalov@vmware.com> 4.0-1
- Version update
* Thu Feb 13 2020 Alexey Makhalov <amakhalov@vmware.com> 3.0-1
- Version update
* Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1-1
- initial version
