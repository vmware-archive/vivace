%global debug_package %{nil}
#%global _tarballversion %{version}+md58+dhx1

Summary:	Package manager for NuGet repositories.
Name:		nuget
Version:	2.8.3
Release:	1
License:	MIT
URL:		http://nuget.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0: http://download.mono-project.com/sources/%{name}/%{name}-%{version}+md58+dhx1.tar.bz2
Source1:	nuget-core.pc
Source2:	nuget.sh
Patch0:		nuget-fix_xdt_hintpath
BuildRequires:	tzdata mono-devel mono-more
Requires:	mono-core mono-more
%description
Package manager for NuGet repositories.
%prep
%setup -qn nuget-git
%patch0 -p1

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build
xbuild xdt/XmlTransform/Microsoft.Web.XmlTransform.csproj
xbuild src/Core/Core.csproj /p:Configuration="Mono Release"
xbuild src/CommandLine/CommandLine.csproj /p:Configuration="Mono Release"

%install
%{__mkdir_p} %{buildroot}%{_prefix}/lib/nuget
%{__mkdir_p} %{buildroot}%{_datadir}/pkgconfig
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pkgconfig/
%{__install} -m0755 %{SOURCE2} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE2}`
sed -i -e 's/cli/mono/' %{buildroot}%{_bindir}/*
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.Core.dll %{buildroot}%{_prefix}/lib/nuget/
%{__install} -m0755 xdt/XmlTransform/bin/Debug/Microsoft.Web.XmlTransform.dll %{buildroot}%{_prefix}/lib/nuget/
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.exe %{buildroot}%{_prefix}/lib/nuget/

%files
%defattr(-,root,root)
%_prefix/lib/nuget
%_datadir/pkgconfig/nuget-core.pc
%_bindir/*

%changelog
*	Mon Jun 8 2015 Alexey Makhalov <amakhalov@vmware.com> 2.8.3-1
-	initial version
