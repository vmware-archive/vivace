Summary:	LXDE Terminal Emulator
Name:		lxterminal
Version:	0.2.0
Release:	1%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
%define sha1 lxterminal=0c2269c43aa463e5dbf869d935745226b3c9943a
BuildRequires:	vte-devel gtk2-devel ncurses-devel
Requires:	vte gtk2 ncurses
%description
The LXTerminal package contains a VTE-based terminal emulator for LXDE with support for multiple tabs.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
# Use utilities-terminal icon
sed -e 's/Icon=lxterminal/Icon=utilities-terminal/' -i %{buildroot}/usr/share/applications/lxterminal.desktop
#
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.2.0-1
-	initial version
