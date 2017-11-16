Summary:	Note-taking application
Name:		tomboy
Version:	1.15.9
Release:	1
License:	LGPLv2+ and GPLv2+ and MIT
URL:		http://projects.gnome.com/tomboy
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.15/%{name}-%{version}.tar.xz
%define sha1 tomboy=acab8348220cc7d6f7b20754770a974c0a3ee448
Patch0:		tomboy-tls-fix.patch
BuildRequires:	itstool mono-devel mono-extras gtk-sharp2-devel gnome-sharp-devel mono-addins desktop-file-utils gnome-doc-utils dbus-sharp dbus-sharp-glib gtk2-devel which libxml2-python
Requires:	mono shared-mime-info gtk-sharp2 gnome-sharp mono-addins gnome-doc-utils dbus-sharp dbus-sharp-glib
%description
Tomboy is a desktop note-taking application which is simple and easy to use.
It lets you organise your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gtk2-devel
%description	devel
It contains the header files to create applications 
%prep
%setup -q
%patch0 -p1
# Delete shipped *.dll files
find -name '*.dll' -exec rm -f {} \;

%build
./configure --prefix=%{_prefix} \
            --disable-scrollkeeper \
	    --disable-update-mimedb \
	    --disable-schemas-install\
	    --sysconfdir=%{_sysconfdir}
mkdir bin
make

%install
#make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR=%{buildroot} install INSTALL="install -p"
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
chmod a+x %{buildroot}%{_libdir}/%{name}/*.exe
chmod a+x %{buildroot}%{_libdir}/%{name}/addins/*.dll

install -d -m 755 %{buildroot}/%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}/%{_datadir}/pixmaps/%{name}.svg
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736869
SentUpstream: 2014-09-18
-->
<application>
<id type="desktop">tomboy.desktop</id>
<metadata_license>CC0-1.0</metadata_license>
<description>
<p>
Tomboy is a desktop note-taking application for GNU/Linux, Unix, Windows, and
Mac OS X.
Simple and easy to use, but with potential to help you organize the ideas and
information you deal with every day.
</p>
<p>
Have you ever felt the frustration at not being able to locate a website you
wanted to check out, or find an email you found interesting, or remember an idea
about the direction of the political landscape in post-industrial Australia?
Or are you one of those desperate souls with home-made, buggy, or not-quite-perfect
notes systems?
Time for Tomboy.
</p>
<p>
We bet you'll be surprised at how well a little application can make life less
cluttered and run more smoothly.
</p>
</description>
<url type="homepage">https://projects.gnome.org/tomboy/</url>
<screenshots>
<screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tomboy/a.png</screenshot>
</screenshots>
<!-- FIXME: change this to an upstream email address for spec updates
<updatecontact>someone_who_cares@upstream_project.org</updatecontact>
-->
</application>
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/tomboy.desktop

for i in %{buildroot}%{_datadir}/mime/*; do
  if [ ! "${i##*/}" = "packages" ]; then
    rm -rf $i
  fi
done

%post
touch --no-create %{_datadir}/icons/hicolor >/dev/null
touch --no-create %{_datadir}/mime/packages >/dev/null

%postun
update-mime-database >/dev/null
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null
  update-mime-database %{_datadir}/mime >/dev/null
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null
update-mime-database %{_datadir}/mime >/dev/null

%files
%defattr(-,root,root)
%{_bindir}
%{_sysconfdir}
%{_libdir}
%{_datadir}
%exclude %{_libdir}/debug
%exclude %{_libdir}/pkgconfig
%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig
%changelog
*	Wed Nov 15 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.15.9-2
-	Upgraded to version 1.15.9 & build on Photon 2.0
*	Tue Jun 23 2015 Alexey Makhalov <amakhalov@vmware.com> 1.15.4-1
-	initial version
