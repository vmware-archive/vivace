Summary:	Vivace release files
Name:		vivace-release
Version:	0.2
Release:	1
License:	Apache License
Group:		System Environment/Base
URL:		http://photon.org
Source:		%{name}-%{version}.tar.xz
%define sha1 vivace-release=74c54070f45cb689e0d62ac00859a831196476f8
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	vivace-release
BuildArch:	noarch

%description
Vivace release files such as yum configs and other /etc/ release related files

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in *.repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/vivace.repo
%config(noreplace) /etc/yum.repos.d/vivace-iso.repo
