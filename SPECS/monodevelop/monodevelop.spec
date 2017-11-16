%global debug_package %{nil}
Summary:	IDE for Mono and GTK#
Name:		monodevelop
# It was downgraded from 5.9.4.2 because of regression.
Version:	5.5.0.227
Release:	1
License:	GPLv2+
URL:		http://www.monodevelop.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://origin-download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
%define sha1 monodevelop=58ef250e999423b19e3716ed916db86dbd7a663c
Patch0:		build_ikvm_with_default_framework.patch
Patch1:		fix_autoreconf.patch
Patch2:		update_templates_for_gtk-sharp_2.12.patch
Patch3:		boo_mimetype.patch
Patch4:		monodevelop-nuget-unbundle.patch
Patch5:		monodevelop-avoidgiterrors.patch
BuildRequires:	mono-devel mono-extras shared-mime-info gtk-sharp2-devel gnome-sharp-devel mono-addins dos2unix nunit nuget
Requires:	mono-tools shared-mime-info gtk-sharp2 gnome-sharp mono-addins nunit nuget mono-extras
%description
MonoDevelop is a full-featured IDE for Mono and GTK#.
%prep
%setup -qn monodevelop-5.5
%patch0	-p1
%patch1	-p1
#dos2unix external/nrefactory/ICSharpCode.NRefactory.Tests/ICSharpCode.NRefactory.Tests.csproj
%patch2	-p1
%patch3	-p1
%patch4 -p1
%patch5 -p1
# Delete shipped *.dll files
find -name '*.dll' -exec rm -f {} \;

%build
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.in
sed -i "s#mono-nunit#nunit#g" configure.in
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

sed -i 's#<bindingRedirect oldVersion="4.0.0.0" newVersion="2.0.0.0"/>##g' src/core/MonoDevelop.Startup/app.config


./configure 	--prefix=%{_prefix} \
		--enable-git \
		--disable-update-mimedb \
		--disable-monoextensions \
	        --disable-update-desktopdb
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d -m 755 %{buildroot}/%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}/%{_datadir}/pixmaps/%{name}.svg
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}
%changelog
*	Wed Jun 3 2015 Alexey Makhalov <amakhalov@vmware.com> 5.5.0.227-1
-	initial version
