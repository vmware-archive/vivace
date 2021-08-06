Summary:	The Xorg fonts.
Name:		xorg-fonts
Version:	7.7
Release:	2%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/System
BuildArch:      noarch
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/font/encodings-1.0.5.tar.bz2
%define sha1 encodings=7ffec76dba1cfd5040c5b43ccfae930c83ddf92e
Source1:	http://ftp.x.org/pub/individual/font/font-alias-1.0.4.tar.bz2
%define sha1 font-alias=c59a4d10a73e2e492952bfc41ac2b8d0b1e1565d
Source2:	http://ftp.x.org/pub/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
%define sha1 font-adobe-utopia-type1=3113cfafb91c2c53df6a1fae57dca6c50fb8ce20
Source3:	http://ftp.x.org/pub/individual/font/font-bh-ttf-1.0.3.tar.bz2
%define sha1 font-bh-ttf=f42ebd527096011040a312e0f9cdf78d64177419
Source4:	http://ftp.x.org/pub/individual/font/font-bh-type1-1.0.3.tar.bz2
%define sha1 font-bh-type1=69ff038d38015cd305a4cd4d1a921fe3bd08bbde
Source5:	http://ftp.x.org/pub/individual/font/font-ibm-type1-1.0.3.tar.bz2
%define sha1 font-ibm-type1=bfc7d0a3aa0f96bf61ea26d6b3f5afbbdd0f35f6
Source6:	http://ftp.x.org/pub/individual/font/font-misc-ethiopic-1.0.4.tar.bz2
%define sha1 font-misc-ethiopic=12523d19ceb7b34de2556b835b2d6f14bccbc388
Source7:	http://ftp.x.org/pub/individual/font/font-xfree86-type1-1.0.4.tar.bz2
%define sha1 font-xfree86-type1=1381f274a178cbd08627560e17a4a8f6653be3f7
BuildRequires:	pkg-config util-macros xcursor-themes xorg-applications font-util
%description
The Xorg font packages provide needed fonts to the Xorg applications.
%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7
%build
for pkg in `ls` ; do
	pushd $pkg
	%configure
	make %{?_smp_mflags}
	popd
done
%install
for pkg in `ls` ; do
	pushd $pkg
	make DESTDIR=%{buildroot} install
	popd
done
install -vdm 755 %{buildroot}/usr/share/fonts
ln -svfn %{_prefix}/share/fonts/X11/OTF %{buildroot}/usr/share/fonts/X11-OTF
ln -svfn %{_prefix}/share/fonts/X11/TTF %{buildroot}/usr/share/fonts/X11-TTF
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_prefix}/*
%changelog
* Wed Aug 04 2021 Alexey Makhalov <amakhalov@vmware.com> 7.7-2
- Version update
* Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 7.7-1
- initial version
