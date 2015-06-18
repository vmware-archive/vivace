Summary:	MIME database
Name:		shared-mime-info
Version:	1.4
Release:	1
License:	GPLv2+
URL:		http://freedesktop.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.xz
BuildRequires:	intltool glib-devel libxml2-devel
#gtk2-devel which python2-devel python2-libs unzip zip nspr nss-devel icu-devel libjpeg-turbo-devel libpng-devel zlib-devel yasm-devel alsa-lib-devel fontconfig-devel freetype2-devel harfbuzz-devel cairo-devel libXt-devel libXext-devel libXrender-devel libX11-devel libffi pixman-devel glib-devel pango-devel gdk-pixbuf-devel atk-devel libSM-devel libICE-devel libXcomposite-devel libXfixes-devel libXdamage-devel
Requires:	gettext glib libxml2
%description
The Shared Mime Info package contains a MIME database. This allows central updates of MIME information for all supporting applications.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%changelog
*	Wed Jun 3 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4-1
-	initial version
