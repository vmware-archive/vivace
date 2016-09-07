Summary:	The Tcl package contains the Tool Command Language, a robust general-purpose scripting language. 
Name:		tcl
Version:	8.6.5
Release:	1
License:	BSD
URL:		https://www.tcl.tk/
Group:		Development/Languages/Tcl
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
%define sha1 tcl=c3a50ea58dac00a3c7e83cb4a4651c40d0f55160
#BuildRequires:	readline-devel

%description
The Tcl package contains the Tool Command Language, a robust general-purpose scripting language. 

%package devel
Summary: Package Headers and shared objects for Tcl
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
%description devel
Development files for Tcl. 


%prep
%setup -qn %{name}%{version}
%build
export SRCDIR=`pwd`

cd unix

./configure --prefix=/usr           \
            --mandir=/usr/share/man \
            $([ $(uname -m) = x86_64 ] && echo --enable-64bit)

make %{?_smp_mflags}

sed -e "s#$SRCDIR/unix#/usr/lib#" \
    -e "s#$SRCDIR#/usr/include#"  \
    -i tclConfig.sh

sed -e "s#$SRCDIR/unix/pkgs/tdbc1.0.4#/usr/lib/tdbc1.0.4#" \
    -e "s#$SRCDIR/pkgs/tdbc1.0.4/generic#/usr/include#"    \
    -e "s#$SRCDIR/pkgs/tdbc1.0.4/library#/usr/lib/tcl8.6#" \
    -e "s#$SRCDIR/pkgs/tdbc1.0.4#/usr/include#"            \
    -i pkgs/tdbc1.0.4/tdbcConfig.sh

sed -e "s#$SRCDIR/unix/pkgs/itcl4.0.4#/usr/lib/itcl4.0.4#" \
    -e "s#$SRCDIR/pkgs/itcl4.0.4/generic#/usr/include#"    \
    -e "s#$SRCDIR/pkgs/itcl4.0.4#/usr/include#"            \
    -i pkgs/itcl4.0.4/itclConfig.sh

unset SRCDIR

%install
rm -rf %{buildroot}/*
cd unix 
make install install-private-headers DESTDIR=%{buildroot}
ln -v -sf tclsh8.6 /usr/bin/tclsh

%check
make -k check 

%clean
rm -rf %{buildroot}/*

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*
%{_datadir}/*
%{_libdir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*

%changelog
*   Mon Apr 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 8.6.5-1
-   Initial version
