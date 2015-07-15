Summary:	grdesktop is a GNOME frontend, for the remote desktop client (rdesktop).
Name:		grdesktop
Version:	0.23
Release:	1
License:	GPL
URL:		http://www.nongnu.org/grdesktop/index.html
Group:		Applications/Communications
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.savannah.gnu.org/releases/grdesktop/%{name}-%{version}.tar.gz
%define sha1 grdesktop=99f3110212a7594bd60c6f9d05bb8afb8e0588f1
BuildRequires:	libgnomeui-devel gtk2-devel gtk3-devel gobject-introspection-devel alsa-lib-devel libxml2-devel GConf-devel scrollkeeper
Requires:	rdesktop alsa-lib gtk2 gtk3 libgnomeui libxml2 GConf
%description
grdesktop is a GNOME frontend, for the remote desktop client (rdesktop).
It can save several connections (including their options), and browse the network for available terminal servers.
%prep
%setup -q 
%build
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
        --with-keymap-path=%{_datadir}/rdesktop/keymaps

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
ln -s grdesktop/icon.png %{buildroot}%{_datadir}/pixmaps/grdesktop.png

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO doc
%{_bindir}/
%{_datadir}/
%{_prefix}/man
%{_sysconfdir}

%changelog
*	Fri Jun 26 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.23-1
-	initial version
