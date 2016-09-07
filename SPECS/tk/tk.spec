Summary:	A TCL GUI Toolkit. 
Name:		tk
Version:	8.6.5
Release:	1
License:	BSD
URL:		https://www.tcl.tk/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
%define sha1 tk=e63f9e46cfd4ea37799554b003958b54b51dc347
BuildRequires:	tcl-devel libX11-devel
Requires:   tcl libX11
%description
The Tk package contains a TCL GUI Toolkit. 

#%package	devel
#Summary:	Header and development files
#Requires:	%{name} = %{version}
#Requires:	mesa-devel
#%description	devel
#It contains the libraries and header files to create applications 
%prep
%setup -qn %{name}%{version}

%build
cd unix
./configure --prefix=/usr \
			--disable-static \
            --mandir=/usr/share/man \
            $([ $(uname -m) = x86_64 ] && echo --enable-64bit) 

make %{?_smp_mflags}
sed -e "s@^\(TK_SRC_DIR='\).*@\1/usr/include'@" \
    -e "/TK_B/s@='\(-L\)\?.*unix@='\1/usr/lib@" \
    -i tkConfig.sh

%install		
cd unix
make DESTDIR=%{buildroot} install install-private-headers 
ln -v -sf wish8.6 %{buildroot}/usr/bin/wish

%files
%defattr(-,root,root)
%{_libdir}/*
%{_bindir}/*
%exclude %{_libdir}/debug/
%exclude %{_includedir}/*
%{_datadir}
#%files devel
#%defattr(-,root,root)
#%{_libdir}/*.la
#%{_includedir}/*
%changelog
*   Mon Apr 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 8.6.5-1
-   Initial version
