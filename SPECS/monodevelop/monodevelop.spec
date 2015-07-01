Summary:	IDE for Mono and GTK#
Name:		monodevelop
Version:	5.9.4.2
Release:	1
License:	GPLv2+
URL:		http://www.monodevelop.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		monodevelop-avoidgiterrors.patch
Patch1:		monodevelop-downgrade_to_mvc3.patch
Patch2:		monodevelop-nunit-unbundle.patch
Patch3:		monodevelop-nuget-unbundle.patch
BuildRequires:	intltool gettext glib-devel tzdata mono-devel mono-extras shared-mime-info gtk-sharp2 gnome-sharp mono-addins dos2unix nunit nuget
Requires:	gettext glib mono-devel shared-mime-info gtk-sharp2 gnome-sharp mono-addins nunit nuget mono-extras
%description
MonoDevelop is a full-featured IDE for Mono and GTK#.
%prep
%setup -q -n %{name}-5.9.4
%patch0	-p1
%patch1	-p1
dos2unix external/nrefactory/ICSharpCode.NRefactory.Tests/ICSharpCode.NRefactory.Tests.csproj
%patch2	-p1
%patch3	-p1

# Delete shipped *.dll files
find -name '*.dll' -exec rm -f {} \;

%build
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.in
sed -i "s#mono-nunit#nunit#g" configure.in
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

./configure --prefix=%{_prefix} --enable-git --disable-update-mimedb \
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
*	Wed Jun 3 2015 Alexey Makhalov <amakhalov@vmware.com> 5.9.4.2-1
-	initial version
