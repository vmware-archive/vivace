%global debug_package %{nil}
Summary:	Multimedia metadata reading/writing library for popular formats
Name:		taglib-sharp
Version:	2.1.0.0
Release:	1
License:	LGPLv2+
URL:		https://www.novell.com/products/linuxpackages/opensuse11.1/taglib-sharp.html
Group:		Development/Languages/Mono
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.banshee.fm/%{name}/%{version}/%{name}-%{version}.tar.gz
%define sha1 taglib-sharp=352a0b15cc1371f1bf6e57f8e7f763c0b86213b6
BuildRequires:	mono-devel
Requires:	mono
Provides:	pkgconfig(taglib-sharp)
%description
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away format
specificity. TagLib# offers either a common API for all formats or
access to specific APIs for a given format.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	mono-devel
%description	devel
Multimedia metadata reading/writing library for popular formats
%prep
%setup -q 
%build
sed -i "s#gmcs#mcs#g" configure
./configure --prefix=%{_prefix} --disable-docs
make
%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/taglib-sharp.pc %{buildroot}%{_libdir}/pkgconfig/taglib-sharp.pc
%clean
rm -rf %{buildroot}
%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_libdir}/mono/taglib-sharp
%dir %{_libdir}/mono/gac/taglib-sharp
%dir %{_libdir}/mono/gac/taglib-sharp/%{version}__db62eba44689b5b0
%dir %{_libdir}/mono/gac/policy.2.0.taglib-sharp
%dir %{_libdir}/mono/gac/policy.2.0.taglib-sharp/0.0.0.0__db62eba44689b5b0
%{_libdir}/mono/gac/taglib-sharp/*/*.dll*
%{_libdir}/mono/gac/policy.2.0.taglib-sharp/*/*
%{_libdir}/mono/taglib-sharp/taglib-sharp.dll
%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/taglib-sharp.pc
%changelog
*	Thu May 21 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.1.0.0-1
-	initial version
