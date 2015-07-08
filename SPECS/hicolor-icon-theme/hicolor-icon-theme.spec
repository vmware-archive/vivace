Summary:	hicolor icon theme.
Name:		hicolor-icon-theme
Version:	0.15
Release:	1
License:	GPLv2+
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildArch:	noarch
%description
The hicolor-icon-theme package contains a default fallback theme for implementations of the icon theme specification.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%postun
gtk-update-icon-cache %{_datadir}/icons/hicolor
%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor
%files
%defattr(-,root,root)
%{_datadir}/icons/hicolor
%changelog
*	Wed Jul 8 2015 Alexey Makhalov <amakhalov@vmware.com> 0.15-1
-	initial version
