%define debug_package %{nil}

Summary:	C# bindings for dbus
Name:		dbus-sharp
Version:	0.7
Release:	1
License:	MIT
URL:		http://mono.github.com/dbus-sharp/
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/downloads/mono/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool gettext glib-devel tzdata mono mono-devel mono-extras
Requires:	gettext glib mono
%description
D-Bus mono bindings for use with mono programs.
%prep
%setup -q

%build
# Mono 4
sed -i configure.ac \
	    -e "s#gmcs#mcs#g"
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
autoreconf -vif
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_libdir}
%changelog
*	Tue Jun 23 2015 Alexey Makhalov <amakhalov@vmware.com> 0.7-1
-	initial version
