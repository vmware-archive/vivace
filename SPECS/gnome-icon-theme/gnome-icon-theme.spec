Summary:	The GNOME Icon Theme package contains an assortment of non-scalable icons of different sizes and themes. 
Name:		gnome-icon-theme
Version:	3.12.0
Release:	1
License:	GPLv2+
URL:		http://gnome-look.org
Group:		System/GUI/GNOME
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/3.12/%{name}-%{version}.tar.xz
BuildRequires:	gtk2-devel intltool hicolor-icon-theme 
Requires:	gtk2 hicolor-icon-theme 
BuildArch:	noarch
%description
The GNOME Icon Theme package contains an assortment of non-scalable icons of different sizes and themes. 
%prep
%setup -q
%build
./configure 	--prefix=%{_prefix} \
		--enable-icon-mapping=no
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%post
gtk-update-icon-cache gnome

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING_LGPL COPYING_CCBYSA3
%ghost %{_datadir}/icons/gnome/icon-theme.cache
%{_datadir}/icons/
%{_datadir}/pkgconfig/
%changelog
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.12.0-1
-	initial version
