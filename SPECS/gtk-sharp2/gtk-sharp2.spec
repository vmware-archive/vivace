Summary:	GTK+ and GNOME bindings for Mono
Name:		gtk-sharp2
Version:	2.12.26
Release:	1
License:	GPLv2+
URL:		http://www.monodevelop.com
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}12/gtk-sharp-%{version}.tar.gz
BuildRequires:	intltool gettext glib-devel tzdata mono-devel gtk2-devel libglade-devel pango-devel libxml2-devel atk-devel cairo-devel gdk-pixbuf-devel pixman-devel libpng-devel libXrender-devel libX11-devel libXext-devel harfbuzz-devel
Requires:	gettext glib mono-core gtk2 libglade pango libxml2 atk cairo
Requires:	perl-XML-LibXML
%description
GTK+ and GNOME bindings for Mono.
%prep
%setup -q -n gtk-sharp-2.12.26
%build
autoreconf -vif
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.12.26-1
-	initial version
