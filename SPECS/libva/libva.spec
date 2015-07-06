Summary:	provides access to hardware accelerated video processing. 
Name:		libva
Version:	1.5.1
Release:	1
License:	MIT
URL:		http://www.freedesktop.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	mesa-devel
Requires:	mesa
%description
The libva package contains a library which provides access to hardware accelerated video processing, using hardware to accelerate video processing in order to offload the central processing unit (CPU) to decode and encode compressed digital video. VA API video decode/encode interface is platform and window system independent targeted at Direct Rendering Infrastructure (DRI) in the X Window System however it can potentially also be used with direct framebuffer and graphics sub-systems for video output. Accelerated processing includes support for video decoding, video encoding, subpicture blending, and rendering. 
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	mesa-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_prefix}/src/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 1.5.1-1
-	initial version
