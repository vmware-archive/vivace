Summary:	Remote Desktop Protocol client. 
Name:		rdesktop
Version:	1.8.3
Release:	1
License:	GPLv3
URL:		http://www.rdesktop.org/
Group:		Applications/Communications
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel glib-devel libXinerama-devel libpng-devel libXrandr-devel gobject-introspection-python python2-devel alsa-lib-devel
Requires:	glib libXinerama alsa-lib libXrandr openssl
%description
rdesktop is an open source client for Windows Remote Desktop Services, capable of natively speaking Remote Desktop Protocol (RDP) in order to present the user's Windows desktop. rdesktop is known to work with Windows versions such as NT 4 Terminal Server, 2000, XP, 2003, 2003 R2, Vista, 2008, 7, 2008 R2, 2008 and 2012 R2.
%prep
%setup -q 
%build
./configure 	--prefix=%{_prefix} \
		--disable-credssp \
		--disable-smartcard
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc COPYING doc/AUTHORS doc/keymapping.txt doc/keymap-names.txt doc/ipv6.txt doc/ChangeLog
%{_bindir}/rdesktop
%{_mandir}/man1/rdesktop.1*
%{_datadir}/rdesktop/keymaps

%changelog
*	Fri Jun 26 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.8.3-1
-	initial version
