%global debug_package %{nil}
Summary:	Pinta is a free, open source drawing/editing program modeled after Paint.NET
Name:           pinta
Version:        1.6
Release:        1
License:        MIT/X11
Url:		http://pinta-project.com/
Group:		Productivity/Graphics/Bitmap Editors
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:        https://github.com/PintaProject/Pinta/releases/download/1.6/pinta-1.6.zip
%define sha1 pinta=d7f221791e8de9c25f86a8a29134f22d6bba8489
BuildRequires:  unzip mono-devel >= 2.8 mono-addins 
BuildRequires:  automake autoconf gtk-sharp2-devel
Requires:	mono-addins
Requires:       gtk-sharp2
%description
Pinta is a free, open source drawing/editing program modeled after Paint.NET. Its goal is to provide users with a simple yet powerful way to draw and manipulate images on Linux, Mac, Windows, and *BSD. 
%prep
%setup -qn pinta-1.6  
%build
find . -name "*.csproj" -print -exec sed -i 's#, Version=2.0.0.0, Culture=neutral, PublicKeyToken=.*processorArchitecture=MSIL" />#" />#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
find . -name "Pinta.Install.proj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g' {} \;

./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_bindir}/pinta
mkdir -p %{buildroot}%{_libdir}/pinta
make DESTDIR=%{buildroot} install 
mv %{buildroot}%{_bindir}/pinta %{buildroot}%{_bindir}/pinta-%{version}
cp %{buildroot}%{_bindir}/pinta-%{version}/* %{buildroot}%{_bindir}

%files
%defattr(-, root, root)
%doc license-mit.txt license-pdn.txt readme.md
%{_libdir}/%{name}/*
%{_bindir}/*
%{_datadir}/*

%changelog
*	Tue Jun 16 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6-1
-	Initial version. 

