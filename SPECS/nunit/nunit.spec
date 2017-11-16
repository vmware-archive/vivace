%global debug_package %{nil}
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac

Summary:	Unit test framework for .NET applications.
Name:		nunit
Version:	2.6.3
Release:	1
License:	MIT
URL:		http://www.nunit.org/
Group:		Applications/Text
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://launchpad.net/nunitv2/trunk/%{version}/+download/NUnit-%{version}-src.zip
%define sha1 NUnit=3d8a4126edab1ce82f931c11b45c8607d2f90830
Source1:	nunit.pc
Source2:	nunit-gui.sh
Source3:	nunit-console.sh
BuildRequires:	unzip mono-devel mono-extras
Requires:	mono mono-extras
%description
NUnit is a testing framework for .NET applications.
%prep
%setup -qn NUnit-%{version}
%build
# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
xbuild /property:Configuration=Debug ./src/NUnitCore/core/nunit.core.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitCore/interfaces/nunit.core.interfaces.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitFramework/framework/nunit.framework.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitMocks/mocks/nunit.mocks.csproj
xbuild /property:Configuration=Debug ./src/ClientUtilities/util/nunit.util.dll.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console/nunit-console.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console-exe/nunit-console.exe.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui/nunit-gui.csproj
xbuild /property:Configuration=Debug ./src/GuiComponents/UiKit/nunit.uikit.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiException/UiException/nunit.uiexception.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui-exe/nunit-gui.exe.csproj

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_monodir}/nunit
%{__mkdir_p} %{buildroot}%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 %{SOURCE2} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE2}`26
%{__install} -m0755 %{SOURCE3} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE3}`26
%{__install} -m0644 src/ConsoleRunner/nunit-console-exe/App.config %{buildroot}%{_monodir}/nunit/nunit-console.exe.config
%{__install} -m0644 src/GuiRunner/nunit-gui-exe/App.config %{buildroot}%{_monodir}/nunit/nunit.exe.config
find %{_builddir}/%{?buildsubdir}/bin -name \*.dll -exec %{__install} \-m0755 "{}" "%{buildroot}%{_monodir}/nunit/" \;
find %{_builddir}/%{?buildsubdir}/bin -name \*.exe -exec %{__install} \-m0755 "{}" "%{buildroot}%{_monodir}/nunit/" \;
for i in nunit-console-runner.dll nunit.core.dll nunit.core.interfaces.dll nunit.framework.dll nunit.mocks.dll nunit.util.dll ; do
	gacutil -i %{buildroot}%{_monodir}/nunit/$i -package nunit -root %{buildroot}%{_libdir}
	done

%files
%defattr(-,root,root)
%{_monogacdir}/nunit*
%{_monodir}/nunit
%{_bindir}/*
%{_libdir}/pkgconfig/nunit.pc
%changelog
*	Mon Jun 8 2015 Alexey Makhalov <amakhalov@vmware.com> 2.6.3-1
-	initial version
