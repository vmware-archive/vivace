%global security_hardening nonow

Summary:	X.Org Video Driver for Intel integrated video cards
Name:		xf86-video-intel
Version:	20190208
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/wiki/IntelGraphicsDriver/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/driver/xf86-video-intel-20190208.tar.xz
%define sha1 xf86-video-intel=de708903530dd529ba620ed08b268e310d441d32
BuildRequires:	libxcb-devel libdrm-devel xorg-server-devel pixman-devel
Requires:	libxcb libdrm xorg-server pixman

%description
The Xorg Intel Driver package contains the X.Org Video Driver for Intel integrated video cards including 8xx, 9xx, Gxx, Qxx and HD graphics processors (SandyBridge, IvyBridge and Haswell).

%prep
%setup -q
%build
./autogen.sh --prefix=/usr --enable-kms-only --enable-uxa --disable-selective-werror
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*
%exclude /usr/lib/debug
/usr/libexec

%changelog
* Mon Jul 01 2019 Alexey Makhalov <amakhalov@vmware.com> 20190208-1
- version update
* Tue Jul 28 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.99.917-1
- initial version
