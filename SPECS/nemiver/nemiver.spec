Summary:	Nemiver graphical debugger
Name:		nemiver
Version:	0.9.6
Release:	1
License:	GPL
URL:		https://wiki.gnome.org/Apps/Nemiver/
Group:		Development/Debuggers
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/0.9/%{name}-%{version}.tar.xz

Patch0:		nemiver_fix_bool_conversion.patch
%define sha1 nemiver=72e305179b541e7c3209fae5f8c59a39a2644e90
BuildRequires:	sqlite-devel gnome-vfs-devel pkg-config perl desktop-file-utils libgnomeui-devel gdb libgnome-devel gettext dbus libgnome glib-devel gtk3-devel systemd-devel libgtop-devel alsa-lib-devel libgnome-keyring-devel boost-devel python2-libs python2-devel harfbuzz-devel itstool pixman-devel GConf-devel vte290-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper libglade-devel perl pcre-devel binutils-devel gdl-devel libgda-devel gtksourceview gtksourceviewmm-devel 
Requires:	sqlite libgnome glib  alsa-lib libgda vte290 pixman openssl gtk3 libgnomeui python2 harfbuzz libgnomecanvas libgnome-keyring GConf popt libbonobo systemd libart_lgpl binutils gdl gtksourceviewmm gdb libgtop boost

%description
Nemiver is an on going effort to write an easy to use standalone C/C++ debugger that integrates well in the GNOME environment.

%package devel
Summary: Development files for Nemiver
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: libgnomeui-devel, libglade-devel, pkg-config boost-devel gnome-vfs libxml2 glibmm libgtop-devel

%description devel
Nemiver is an on going effort to write an easy to use standalone C/C++ debugger that integrates well in the GNOME environment.

%prep
%setup -q 
%patch0 -p1
%build
./configure 	--prefix=%{_prefix} \
		--disable-static \
		--disable-schemas-install

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install 	--dir %{buildroot}%{_datadir}/applications	\
			--remove-category=Application	\
			--delete-original	\
			%{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s ../icons/hicolor/48x48/apps/nemiver.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &> /dev/null 
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null 
/sbin/ldconfig

%postun
/sbin/ldconfig
update-mime-database %{_datadir}/mime &> /dev/null 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 

%files 
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_bindir}/*
%{_libdir}/nemiver/
%{_prefix}%{_sysconfdir}/gconf
%{_datadir}/nemiver/
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_mandir}/man1/nemiver.1.gz
%{_datadir}/help
%{_datadir}/locale
%{_datadir}/pixmaps
%{_datadir}/appdata

%files devel
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_includedir}/nemiver/

%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.9.6-1
-	Upgraded to vesion 0.9.6 to build with Photon 2.0
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.9.5-1
-	initial version
