Summary:	Managed Implementation of libgnome-keyring
Name:		gnome-keyring-sharp
Version:	1.0.2
Release:	1
License:	MIT
URL:		http://www.mono-project.com/docs/tools+libraries/libraries/
Group:		Development/Libraries/Other
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.go-mono.com/archive/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	glib-devel libtool gtk-sharp2 mono-devel libgnome-keyring-devel
Requires:	libgnome-keyring 
%description
gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.When the gnome-keyring-daemon is running, you can use this to retrive/store confidential information such as passwords, notes or network services user information.

%package devel
License:        MIT
Requires:       %{name} = %{version} pkg-config
Summary:        Managed implementation of libgnome-keyring
Group:          Development/Libraries/Other
AutoReqProv:    on

%description devel
When the gnome-keyring-daemon is running, you can use this to retrieve
and store confidential information such as passwords, notes or network
services user information.

%prep
%setup -q
%build
./configure --prefix=%{_prefix} --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_libdir}/libgnome-keyring-sharp-glue.so
%dir %{_prefix}/lib/mono/gnome-keyring-sharp-1.0
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0/Gnome.Keyring.dll
%{_prefix}/lib/mono/gac/Gnome.Keyring

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/gnome-keyring-sharp-1.0.pc
%{_libdir}/libgnome-keyring-sharp-glue.la
%changelog
*	Tue Jun 23 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.0.2-1
-	initial version
