%global debug_package %{nil}
Summary:	Open source implementation of Microsoft's .NET Framework.
Name:		mono-addins
Version:	1.1
Release:	1
License:	MIT
URL:		http://www.mono-project.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
%define sha1 mono-addins=dc3d494f484bfef0b7e7024939f18c7b4d7ee4db
Patch0:		mono-addins-1.0-libdir.patch
BuildRequires:	gtk-sharp2-devel mono-devel
Requires:	gtk-sharp2
%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.
%prep
%setup -q
%patch0 -p1
%build
sed -i "s#AC_PATH_PROG(MCS, gmcs, no)#AC_PATH_PROG(MCS, mcs, no)#g" configure.ac
autoreconf -vif
./configure --prefix=%{_prefix} \
            --enable-gui
#find . -name "Makefile*" -print -exec sed -i 's#ASSEMBLY_COMPILER_COMMAND = gmcs#ASSEMBLY_COMPILER_COMMAND = mcs#g; s#-r:Microsoft.Build.Utilities #-r:Microsoft.Build.Utilities.v4.0 #g' {} \;
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}
%changelog
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1-1
-	initial version
