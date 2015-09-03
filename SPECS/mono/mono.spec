Summary:	Open source implementation of Microsoft's .NET Framework.
Name:		mono
Version:	4.0.1
Release:	1
License:	MIT
URL:		http://www.mono-project.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.44.tar.bz2
%define sha1 mono=dbdcfb62891f0b6229631887f201ee7fb3c0c3a0
Source1:	keypair.snk
Patch0:		mono-4.0.0-ignore-reference-assemblies.patch
BuildRequires:	gettext tzdata libgdiplus-devel
Requires:	gettext tzdata libgdiplus
Provides:	mono(Mono.Cairo)
Provides:	mono(Mono.Posix)
Provides:	mono(Mono.Security)
Provides:	mono(System)
Provides:	mono(System.Core)
Provides:	mono(System.Drawing)
Provides:	mono(System.Data)
Provides:	mono(System.Design)
Provides:	mono(System.Configuration)
Provides:	mono(System.Runtime.Remoting)
Provides:	mono(System.Windows.Forms)
Provides:	mono(System.ComponentModel.Composition)
Provides:	mono(System.ComponentModel.DataAnnotations)
Provides:	mono(System.Data.Services.Client)
Provides:	mono(System.Runtime.Serialization)
Provides:	mono(System.Security)
Provides:	mono(System.ServiceModel)
Provides:	mono(System.Web)
Provides:	mono(System.Web.Mvc)
Provides:	mono(System.Web.Razor)
Provides:	mono(System.Web.Services)
Provides:	mono(System.Web.WebPages.Razor)
Provides:	mono(System.Xaml)
Provides:	mono(System.Xml)
Provides:	mono(System.Xml.Linq)
Provides:	mono(mscorlib)
Provides:	mono(monodoc)
Provides:	mono(ICSharpCode.SharpZipLib)
Provides:	mono(Microsoft.Build.Framework)
Provides:	mono(Microsoft.Build.Utilities.v4.0)
Provides:	mono(Microsoft.Build)
Provides:	mono(Microsoft.Build.Engine)
Provides:	mono(Microsoft.CSharp)
Provides:	mono(WindowsBase)


%define _use_internal_dependency_generator 0
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | prefix=%{buildroot}%{_prefix} %{buildroot}%{_bindir}/mono-find-provides; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | prefix=%{buildroot}%{_prefix} %{buildroot}%{_bindir}/mono-find-requires; } | sort | uniq | grep ^...'

%description
Mono is an open source implementation of Microsoft's .NET Framework based on the ECMA standards for C# and the Common Language Runtime.

%package devel
Summary: Package config and shared objects for Mono
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: mono-tools = %{version}-%{release} libgdiplus-devel

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package tools
Summary: Development tools for Mono
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description tools
This package includes the development tools for building mono applications

%package nunit
Summary:	NUnit Testing Framework
License:	zlib with acknowledgement
Group:		Development/Languages
Requires: %{name} = %{version}-%{release}

%description nunit
NUnit is a unit-testing framework for all .Net languages. Initially
ported from JUnit, the current release, version 2.2, is the fourth
major release of this Unit based unit testing tool for Microsoft .NET.
It is written entirely in C# and has been completely redesigned to
take advantage of many .NET language features, for example
custom attributes and other reflection related capabilities. NUnit
brings xUnit to all .NET languages.

%package nunit-devel
Summary:	pkgconfig for nunit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}, pkg-config
Requires:	mono-nunit = %{version}-%{release}

%description nunit-devel
Development files for nunit

%package extras
Summary: Provides all the files which are not in a core/nunit rpms.
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
%description extras
Provides all the files which are not in a core/nunit rpms.

%prep
%setup -q 
%patch0	-p1
sed -i "s#mono/2.0#mono/4.5#g" data/mono-nunit.pc.in

%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --disable-rpath \
            --with-moonlight=no

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_sysconfdir}/pki/mono
install -p -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/mono/pi	

rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_prefix}/lib/mono/*/Mono.Security.Win32*
rm -f %{buildroot}%{_libdir}/libMonoSupportW.*
rm %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_datadir}/libgc-mono
rm -f %{buildroot}%{_bindir}/cilc
rm -f %{buildroot}%{_mandir}/man1/cilc.1*
rm -f %{buildroot}%{_prefix}/lib/mono/*/browsercaps-updater.exe*
rm -f %{buildroot}%{_prefix}/lib/mono/*/culevel.exe*
rm -f %{buildroot}%{_prefix}/lib/mono/2.0/cilc.exe*

rm -f %{buildroot}%{_prefix}/lib/mono/*/mscorlib.dll.so
rm -f %{buildroot}%{_prefix}/lib/mono/*/mcs.exe.so
rm -f %{buildroot}%{_prefix}/lib/mono/*/gmcs.exe.so
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/Microsoft
rm -f %{buildroot}%{_prefix}/lib/mono/4.0/dmcs.exe.so
rm -rf %{buildroot}%{_bindir}/mono-configuration-crypto
rm -rf %{buildroot}%{_mandir}/man?/mono-configuration-crypto*

%find_lang mcs
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files -f mcs.lang
%doc AUTHORS COPYING.LIB ChangeLog NEWS README.md
%{_bindir}/mono
%{_bindir}/mono-test-install
%{_bindir}/mono-gdb.py
%{_bindir}/mono-boehm
%{_bindir}/mono-service2
%{_bindir}/mono-sgen
%{_bindir}/mono-sgen-gdb.py
%{_libdir}/mono/lldb/mono.py*
%{_bindir}/csharp 
%{_prefix}/lib/mono/4.5/csharp.exe 
%{_prefix}/lib/mono/4.5/csharp.exe.*  
%{_bindir}/cert-sync 
%{_prefix}/lib/mono/4.5/cert-sync.exe 
%{_prefix}/lib/mono/4.5/cert-sync.exe.*  
%{_bindir}/chktrust 
%{_prefix}/lib/mono/4.5/chktrust.exe 
%{_prefix}/lib/mono/4.5/chktrust.exe.*  
%{_bindir}/gacutil 
%{_prefix}/lib/mono/4.5/gacutil.exe 
%{_prefix}/lib/mono/4.5/gacutil.exe.*  
%{_bindir}/ikdasm 
%{_prefix}/lib/mono/4.5/ikdasm.exe 
%{_prefix}/lib/mono/4.5/ikdasm.exe.*  
%{_bindir}/lc 
%{_prefix}/lib/mono/4.5/lc.exe 
%{_prefix}/lib/mono/4.5/lc.exe.*  
%{_bindir}/gacutil2
%{_bindir}/mcs
%{_prefix}/lib/mono/4.5/mcs.exe*
%{_bindir}/mozroots 
%{_prefix}/lib/mono/4.5/mozroots.exe 
%{_prefix}/lib/mono/4.5/mozroots.exe.*  
%{_bindir}/pdb2mdb 
%{_prefix}/lib/mono/4.5/pdb2mdb.exe 
%{_prefix}/lib/mono/4.5/pdb2mdb.exe.*  
%{_bindir}/setreg 
%{_prefix}/lib/mono/4.5/setreg.exe 
%{_prefix}/lib/mono/4.5/setreg.exe.*  
%{_bindir}/sn 
%{_prefix}/lib/mono/4.5/sn.exe 
%{_prefix}/lib/mono/4.5/sn.exe.*  
%{_bindir}/mono-heapviz
%{_bindir}/mprof-report
%{_mandir}/man1/certmgr.1.gz
%{_mandir}/man1/chktrust.1.gz
%{_mandir}/man1/gacutil.1.gz
%{_mandir}/man1/mcs.1.gz
%{_mandir}/man1/mono.1.gz
%{_mandir}/man1/mozroots.1.gz
%{_mandir}/man1/setreg.1.gz
%{_mandir}/man1/sn.1.gz
%{_mandir}/man5/mono-config.5.gz
%{_mandir}/man1/csharp.1.gz
%{_mandir}/man1/pdb2mdb.1.gz
%{_mandir}/man1/lc.1.gz
%{_mandir}/man1/mprof-report.1.gz
%{_libdir}/libMonoPosixHelper.so*
%dir %{_prefix}/lib/mono
%dir %{_prefix}/lib/mono/gac

%{_prefix}/lib/mono/gac/Commons.Xml.Relaxng 
%{_prefix}/lib/mono/4.5/Commons.Xml.Relaxng.dll 


%{_prefix}/lib/mono/gac/ICSharpCode.SharpZipLib
%{_prefix}/lib/mono/4.5/ICSharpCode.SharpZipLib.dll
%{_prefix}/lib/mono/gac/Mono.Debugger.Soft
%{_prefix}/lib/mono/4.5/Mono.Debugger.Soft.dll
%{_prefix}/lib/mono/gac/Mono.Cecil
%{_prefix}/lib/mono/gac/cscompmgd
%{_prefix}/lib/mono/4.5/cscompmgd.dll
%{_prefix}/lib/mono/gac/Microsoft.VisualC
%{_prefix}/lib/mono/4.5/Microsoft.VisualC.dll
%{_prefix}/lib/mono/gac/Mono.C5 
%{_prefix}/lib/mono/4.5/Mono.C5.dll
%{_prefix}/lib/mono/gac/Mono.Cairo
%{_prefix}/lib/mono/4.5/Mono.Cairo.dll
%{_prefix}/lib/mono/gac/Mono.CompilerServices.SymbolWriter
%{_prefix}/lib/mono/4.5/Mono.CompilerServices.SymbolWriter.dll
%{_prefix}/lib/mono/gac/Mono.CSharp
%{_prefix}/lib/mono/4.5/Mono.CSharp.dll
%{_prefix}/lib/mono/gac/System.Drawing
%{_prefix}/lib/mono/4.5/System.Drawing.dll
%{_prefix}/lib/mono/gac/Mono.Management 
%{_prefix}/lib/mono/4.5/Mono.Management.dll
%{_prefix}/lib/mono/gac/Mono.Posix
%{_prefix}/lib/mono/4.5/Mono.Posix.dll
%{_prefix}/lib/mono/gac/Mono.Security
%{_prefix}/lib/mono/4.5/Mono.Security.dll
%{_prefix}/lib/mono/gac/Mono.Simd
%{_prefix}/lib/mono/4.5/Mono.Simd.dll
%{_prefix}/lib/mono/gac/System
%{_prefix}/lib/mono/4.5/System.dll
%{_prefix}/lib/mono/gac/System.Configuration
%{_prefix}/lib/mono/4.5/System.Configuration.dll
%{_prefix}/lib/mono/gac/System.Core
%{_prefix}/lib/mono/4.5/System.Core.dll
%{_prefix}/lib/mono/gac/System.Security
%{_prefix}/lib/mono/4.5/System.Security.dll
%{_prefix}/lib/mono/gac/System.Xml
%{_prefix}/lib/mono/4.5/System.Xml.dll
%{_prefix}/lib/mono/gac/Mono.Tasklets
%{_prefix}/lib/mono/4.5/Mono.Tasklets.dll
%{_prefix}/lib/mono/gac/System.Net 
%{_prefix}/lib/mono/4.5/System.Net.dll
%{_prefix}/lib/mono/gac/System.Xml.Linq
%{_prefix}/lib/mono/4.5/System.Xml.Linq.dll
%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/mconfig
%config (noreplace) %{_sysconfdir}/mono/config
%config (noreplace) %{_sysconfdir}/mono/2.0/machine.config
%config (noreplace) %{_sysconfdir}/mono/2.0/settings.map
%{_libdir}/libmono*-2.0.so.*
%{_libdir}/libmono-profiler-*.so.*
%config (noreplace) %{_sysconfdir}/mono/4.0/*.config
%config (noreplace) %{_sysconfdir}/mono/4.0/settings.map
%config (noreplace) %{_sysconfdir}/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_sysconfdir}/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_sysconfdir}/mono/4.5/machine.config
%config (noreplace) %{_sysconfdir}/mono/4.5/settings.map
%config (noreplace) %{_sysconfdir}/mono/4.5/web.config
%dir %{_sysconfdir}/mono/4.0
%{_bindir}/dmcs
%{_bindir}/ccrewrite 
%{_prefix}/lib/mono/4.5/ccrewrite.exe 
%{_prefix}/lib/mono/4.5/ccrewrite.exe.*  
%{_prefix}/lib/mono/4.5/mscorlib.dll
%{_prefix}/lib/mono/4.5/mscorlib.dll.mdb
%{_prefix}/lib/mono/gac/Microsoft.CSharp
%{_prefix}/lib/mono/4.5/Microsoft.CSharp.dll
%{_prefix}/lib/mono/gac/System.Dynamic
%{_prefix}/lib/mono/4.5/System.Dynamic.dll
%{_prefix}/lib/mono/gac/Mono.Data.Tds
%{_prefix}/lib/mono/4.5/Mono.Data.Tds.dll
%{_prefix}/lib/mono/gac/System.ComponentModel.Composition
%{_prefix}/lib/mono/4.5/System.ComponentModel.Composition.dll
%{_prefix}/lib/mono/gac/System.EnterpriseServices
%{_prefix}/lib/mono/4.5/System.EnterpriseServices.dll
%{_prefix}/lib/mono/gac/System.Data
%{_prefix}/lib/mono/4.5/System.Data.dll
%{_prefix}/lib/mono/gac/System.Numerics
%{_prefix}/lib/mono/4.5/System.Numerics.dll
%{_prefix}/lib/mono/gac/System.Runtime.Caching
%{_prefix}/lib/mono/4.5/System.Runtime.Caching.dll
%{_prefix}/lib/mono/gac/System.Runtime.DurableInstancing
%{_prefix}/lib/mono/4.5/System.Runtime.DurableInstancing.dll
%{_prefix}/lib/mono/gac/System.Transactions
%{_prefix}/lib/mono/4.5/System.Transactions.dll
%{_prefix}/lib/mono/gac/System.Xaml
%{_prefix}/lib/mono/4.5/System.Xaml.dll
%{_prefix}/lib/mono/gac/WebMatrix.Data
%{_prefix}/lib/mono/4.5/WebMatrix.Data.dll
%{_prefix}/lib/mono/gac/Mono.CodeContracts
%{_prefix}/lib/mono/4.5/Mono.CodeContracts.dll
%{_prefix}/lib/mono/mono-configuration-crypto/4.5/mono-config*
%{_prefix}/lib/mono/mono-configuration-crypto/4.5/Mono.Configuration.Crypto.dll*
%{_mandir}/man1/ccrewrite.1.gz
%{_prefix}/lib/mono/gac/CustomMarshalers
%{_prefix}/lib/mono/4.5/CustomMarshalers.dll
%{_prefix}/lib/mono/gac/I18N.West
%{_prefix}/lib/mono/4.5/I18N.West.dll
%{_prefix}/lib/mono/gac/I18N
%{_prefix}/lib/mono/4.5/I18N.dll
%{_prefix}/lib/mono/gac/System.Json
%{_prefix}/lib/mono/4.5/System.Json.dll
%{_prefix}/lib/mono/gac/Mono.Parallel
%{_prefix}/lib/mono/4.5/Mono.Parallel.dll
%{_prefix}/lib/mono/gac/System.Json.Microsoft
%{_prefix}/lib/mono/4.5/System.Json.Microsoft.dll
%{_prefix}/lib/mono/4.5/Facades/*.dll
%{_prefix}/lib/mono/gac/System.IO.Compression
%{_prefix}/lib/mono/4.5/System.IO.Compression.dll
%{_prefix}/lib/mono/gac/System.IO.Compression.FileSystem
%{_prefix}/lib/mono/4.5/System.IO.Compression.FileSystem.dll
%{_prefix}/lib/mono/gac/System.Net.Http
%{_prefix}/lib/mono/4.5/System.Net.Http.dll
%{_prefix}/lib/mono/gac/System.Net.Http.WebRequest
%{_prefix}/lib/mono/4.5/System.Net.Http.WebRequest.dll
%{_prefix}/lib/mono/gac/System.Threading.Tasks.Dataflow 
%{_prefix}/lib/mono/4.5/System.Threading.Tasks.Dataflow.dll  

%files tools
%{_sysconfdir}/pki/mono/
%{_bindir}/mono-api-info
%{_prefix}/lib/mono/4.5/mono-api-info.exe
%{_prefix}/lib/mono/4.5/symbolicate.exe
%{_prefix}/lib/mono/4.5/symbolicate.exe.mdb
%{_bindir}/xbuild 
%{_prefix}/lib/mono/4.5/xbuild.exe 
%{_prefix}/lib/mono/4.5/xbuild.exe.*  
%{_prefix}/lib/mono/4.5/xbuild.rsp
%{_bindir}/genxs 
%{_prefix}/lib/mono/4.5/genxs.exe 
%{_prefix}/lib/mono/4.5/genxs.exe.*  
%{_prefix}/lib/mono/4.5/ictool*
%{_prefix}/lib/mono/4.5/mod*
%{_bindir}/al 
%{_prefix}/lib/mono/4.5/al.exe 
%{_prefix}/lib/mono/4.5/al.exe.*  
%{_bindir}/al2
%{_bindir}/caspol 
%{_prefix}/lib/mono/4.5/caspol.exe 
%{_prefix}/lib/mono/4.5/caspol.exe.*  
%{_bindir}/cert2spc 
%{_prefix}/lib/mono/4.5/cert2spc.exe 
%{_prefix}/lib/mono/4.5/cert2spc.exe.*  
%{_bindir}/certmgr 
%{_prefix}/lib/mono/4.5/certmgr.exe 
%{_prefix}/lib/mono/4.5/certmgr.exe.*  
%{_bindir}/dtd2rng 
%{_prefix}/lib/mono/4.5/dtd2rng.exe 
%{_prefix}/lib/mono/4.5/dtd2rng.exe.*  
%{_bindir}/dtd2xsd 
%{_prefix}/lib/mono/4.5/dtd2xsd.exe 
%{_prefix}/lib/mono/4.5/dtd2xsd.exe.*  
%{_bindir}/ilasm 
%{_prefix}/lib/mono/4.5/ilasm.exe 
%{_prefix}/lib/mono/4.5/ilasm.exe.*  
%{_bindir}/installvst 
%{_prefix}/lib/mono/4.5/installvst.exe 
%{_prefix}/lib/mono/4.5/installvst.exe.*  
%{_prefix}/lib/mono/4.5/installutil*
%{_bindir}/macpack 
%{_prefix}/lib/mono/4.5/macpack.exe 
%{_prefix}/lib/mono/4.5/macpack.exe.*  
%{_bindir}/mkbundle 
%{_prefix}/lib/mono/4.5/mkbundle.exe 
%{_prefix}/lib/mono/4.5/mkbundle.exe.*  
%{_bindir}/makecert 
%{_prefix}/lib/mono/4.5/makecert.exe 
%{_prefix}/lib/mono/4.5/makecert.exe.*  
%{_bindir}/mono-cil-strip 
%{_prefix}/lib/mono/4.5/mono-cil-strip.exe 
%{_prefix}/lib/mono/4.5/mono-cil-strip.exe.*  
%{_bindir}/mono-find-provides
%{_bindir}/mono-find-requires
%{_bindir}/monodis
%{_bindir}/monolinker 
%{_prefix}/lib/mono/4.5/monolinker.exe 
%{_prefix}/lib/mono/4.5/monolinker.exe.*  
%{_bindir}/mono-shlib-cop 
%{_prefix}/lib/mono/4.5/mono-shlib-cop.exe 
%{_prefix}/lib/mono/4.5/mono-shlib-cop.exe.* 
%{_bindir}/mono-xmltool 
%{_prefix}/lib/mono/4.5/mono-xmltool.exe 
%{_prefix}/lib/mono/4.5/mono-xmltool.exe.*  
%{_bindir}/monop 
%{_prefix}/lib/mono/4.5/monop.exe 
%{_prefix}/lib/mono/4.5/monop.exe.*  
%{_bindir}/monop2
%{_bindir}/permview 
%{_prefix}/lib/mono/4.5/permview.exe 
%{_prefix}/lib/mono/4.5/permview.exe.*  
%{_bindir}/peverify
%{_bindir}/prj2make
%{_bindir}/resgen 
%{_prefix}/lib/mono/4.5/resgen.exe 
%{_prefix}/lib/mono/4.5/resgen.exe.*  
%{_bindir}/resgen2
%{_bindir}/sgen 
%{_prefix}/lib/mono/4.5/sgen.exe 
%{_prefix}/lib/mono/4.5/sgen.exe.*  
%{_bindir}/secutil 
%{_prefix}/lib/mono/4.5/secutil.exe 
%{_prefix}/lib/mono/4.5/secutil.exe.* 
%{_bindir}/signcode 
%{_prefix}/lib/mono/4.5/signcode.exe 
%{_prefix}/lib/mono/4.5/signcode.exe.*  
%{_bindir}/cccheck 
%{_prefix}/lib/mono/4.5/cccheck.exe 
%{_prefix}/lib/mono/4.5/cccheck.exe.*  
%{_bindir}/crlupdate 
%{_prefix}/lib/mono/4.5/crlupdate.exe 
%{_prefix}/lib/mono/4.5/crlupdate.exe.*  
%{_bindir}/mdbrebase 
%{_prefix}/lib/mono/4.5/mdbrebase.exe 
%{_prefix}/lib/mono/4.5/mdbrebase.exe.*  
%{_prefix}/lib/mono/4.5/Microsoft.Common.tasks
%{_prefix}/lib/mono/4.5/MSBuild/Microsoft.Build*
%{_prefix}/lib/mono/4.5/Microsoft.Build.xsd
%{_prefix}/lib/mono/4.5/Microsoft.CSharp.targets
%{_prefix}/lib/mono/4.5/Microsoft.Common.targets
%{_prefix}/lib/mono/4.5/Microsoft.VisualBasic.targets
%{_prefix}/lib/mono/xbuild/
%{_prefix}/lib/mono/xbuild-frameworks/
%{_prefix}/lib/mono/gac/Microsoft.Build
%{_prefix}/lib/mono/4.5/Microsoft.Build.dll
%{_prefix}/lib/mono/gac/Microsoft.Build.Engine
%{_prefix}/lib/mono/4.5/Microsoft.Build.Engine.dll
%{_prefix}/lib/mono/gac/Microsoft.Build.Framework
%{_prefix}/lib/mono/4.5/Microsoft.Build.Framework.dll
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.Core
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.v4.0
%{_prefix}/lib/mono/4.5/Microsoft.Build.Tasks.v4.0.dll
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.v4.0
%{_prefix}/lib/mono/4.5/Microsoft.Build.Utilities.v4.0.dll
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.Core
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.v12.0
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.v12.0
%{_prefix}/lib/mono/gac/Mono.XBuild.Tasks 
%{_prefix}/lib/mono/4.5/Mono.XBuild.Tasks.dll
%{_prefix}/lib/mono/gac/System.Windows
%{_prefix}/lib/mono/4.5/System.Windows.dll
%{_prefix}/lib/mono/gac/System.Xml.Serialization
%{_prefix}/lib/mono/4.5/System.Xml.Serialization.dll

%files devel
%{_prefix}/lib/mono-source-libs/
%{_bindir}/pedump
%{_mandir}/man1/resgen.1.gz
%{_mandir}/man1/al.1.gz
%{_mandir}/man1/cert2spc.1.gz
%{_mandir}/man1/dtd2xsd.1.gz
%{_mandir}/man1/genxs.1.gz
%{_mandir}/man1/ilasm.1.gz
%{_mandir}/man1/macpack.1.gz
%{_mandir}/man1/makecert.1.gz
%{_mandir}/man1/mkbundle.1.gz
%{_mandir}/man1/mono-cil-strip.1.gz
%{_mandir}/man1/monodis.1.gz
%{_datadir}/mono-2.0/mono/cil/cil-opcodes.xml
%{_mandir}/man1/monolinker.1.gz
%{_mandir}/man1/mono-shlib-cop.1.gz
%{_mandir}/man1/mono-xmltool.1.gz
%{_mandir}/man1/monop.1.gz
%{_mandir}/man1/permview.1.gz
%{_mandir}/man1/prj2make.1.gz
%{_mandir}/man1/secutil.1.gz
%{_mandir}/man1/sgen.1.gz
%{_mandir}/man1/signcode.1.gz
%{_mandir}/man1/xbuild.1.gz
%{_mandir}/man1/mono-api-info.1.gz
%{_mandir}/man1/cccheck.1.gz
%{_mandir}/man1/crlupdate.1.gz
%{_prefix}/lib/mono/gac/PEAPI
%{_prefix}/lib/mono/4.5/PEAPI.dll  
%{_libdir}/libikvm-native.so
%{_libdir}/libmono-profiler-*.so
%{_libdir}/libmono*-2.0.so
%{_libdir}/pkgconfig/dotnet.pc
%{_libdir}/pkgconfig/mono-cairo.pc
%{_libdir}/pkgconfig/mono.pc
%{_libdir}/pkgconfig/mono-2.pc
%{_libdir}/pkgconfig/monosgen-2.pc
%{_libdir}/pkgconfig/cecil.pc
%{_libdir}/pkgconfig/dotnet35.pc
%{_libdir}/pkgconfig/mono-lineeditor.pc
%{_libdir}/pkgconfig/mono-options.pc
%{_libdir}/pkgconfig/wcf.pc
%{_libdir}/pkgconfig/xbuild12.pc
%{_includedir}/mono-2.0/mono/jit/jit.h
%{_includedir}/mono-2.0/mono/metadata/*.h
%{_includedir}/mono-2.0/mono/utils/*.h
%{_includedir}/mono-2.0/mono/cil/opcode.def

%files nunit
%{_bindir}/nunit-console 
%{_prefix}/lib/mono/4.5/nunit-console.exe 
%{_prefix}/lib/mono/4.5/nunit-console.exe.*  
%{_bindir}/nunit-console2
%{_bindir}/nunit-console4
%{_prefix}/lib/mono/gac/nunit-console-runner 
%{_prefix}/lib/mono/4.5/nunit-console-runner.dll
%{_prefix}/lib/mono/gac/nunit.core
%{_prefix}/lib/mono/4.5/nunit.core.dll  
%{_prefix}/lib/mono/gac/nunit.core.extensions
%{_prefix}/lib/mono/4.5/nunit.core.extensions.dll
%{_prefix}/lib/mono/gac/nunit.core.interfaces 
%{_prefix}/lib/mono/4.5/nunit.core.interfaces.dll
%{_prefix}/lib/mono/gac/nunit.framework
%{_prefix}/lib/mono/4.5/nunit.framework.dll
%{_prefix}/lib/mono/gac/nunit.framework.extensions
%{_prefix}/lib/mono/4.5/nunit.framework.extensions.dll
%{_prefix}/lib/mono/gac/nunit.mocks
%{_prefix}/lib/mono/4.5/nunit.mocks.dll
%{_prefix}/lib/mono/gac/nunit.util
%{_prefix}/lib/mono/4.5/nunit.util.dll

%files nunit-devel
%{_libdir}/pkgconfig/mono-nunit.pc

%files extras
#%files locale-extras
%{_prefix}/lib/mono/gac/I18N.CJK
%{_prefix}/lib/mono/4.5/I18N.CJK.dll
%{_prefix}/lib/mono/gac/I18N.MidEast
%{_prefix}/lib/mono/4.5/I18N.MidEast.dll
%{_prefix}/lib/mono/gac/I18N.Other
%{_prefix}/lib/mono/4.5/I18N.Other.dll
%{_prefix}/lib/mono/gac/I18N.Rare
%{_prefix}/lib/mono/4.5/I18N.Rare.dll
#%files extras
%{_bindir}/mono-service 
%{_prefix}/lib/mono/4.5/mono-service.exe 
%{_prefix}/lib/mono/4.5/mono-service.exe.*  
%{_prefix}/lib/mono/gac/mono-service
%{_prefix}/lib/mono/gac/System.Configuration.Install
%{_prefix}/lib/mono/4.5/System.Configuration.Install.dll
%{_prefix}/lib/mono/gac/System.Management
%{_prefix}/lib/mono/4.5/System.Management.dll
%{_prefix}/lib/mono/gac/System.Messaging
%{_prefix}/lib/mono/4.5/System.Messaging.dll
%{_prefix}/lib/mono/gac/System.ServiceProcess
%{_prefix}/lib/mono/4.5/System.ServiceProcess.dll
%{_prefix}/lib/mono/gac/System.Runtime.Caching
%{_prefix}/lib/mono/4.5/System.Runtime.Caching.dll
%{_prefix}/lib/mono/gac/System.Xaml
%{_prefix}/lib/mono/4.5/System.Xaml.dll
%{_prefix}/lib/mono/gac/Mono.Messaging.RabbitMQ
%{_prefix}/lib/mono/4.5/Mono.Messaging.RabbitMQ.dll
%{_prefix}/lib/mono/gac/Mono.Messaging
%{_prefix}/lib/mono/4.5/Mono.Messaging.dll  
%{_prefix}/lib/mono/gac/RabbitMQ.Client
%{_prefix}/lib/mono/4.5/RabbitMQ.Client.dll
%{_prefix}/lib/mono/4.5/RabbitMQ.Client.Apigen*
%{_mandir}/man1/mono-service.1.gz
#%files reactive
%{_prefix}/lib/mono/gac/System.Reactive.Core
%{_prefix}/lib/mono/4.5/System.Reactive.Core.dll  
%{_prefix}/lib/mono/gac/System.Reactive.Debugger
%{_prefix}/lib/mono/4.5/System.Reactive.Debugger.dll
%{_prefix}/lib/mono/gac/System.Reactive.Experimental
%{_prefix}/lib/mono/4.5/System.Reactive.Experimental.dll
%{_prefix}/lib/mono/gac/System.Reactive.Interfaces
%{_prefix}/lib/mono/4.5/System.Reactive.Interfaces.dll
%{_prefix}/lib/mono/gac/System.Reactive.Linq
%{_prefix}/lib/mono/4.5/System.Reactive.Linq.dll
%{_prefix}/lib/mono/gac/System.Reactive.Observable.Aliases 
%{_prefix}/lib/mono/4.5/System.Reactive.Observable.Aliases.dll
%{_prefix}/lib/mono/gac/System.Reactive.PlatformServices
%{_prefix}/lib/mono/4.5/System.Reactive.PlatformServices.dll
%{_prefix}/lib/mono/gac/System.Reactive.Providers
%{_prefix}/lib/mono/4.5/System.Reactive.Providers.dll
%{_prefix}/lib/mono/gac/System.Reactive.Runtime.Remoting
%{_prefix}/lib/mono/4.5/System.Reactive.Runtime.Remoting.dll
#%files reactive-winforms
%{_prefix}/lib/mono/gac/System.Reactive.Windows.Forms
%{_prefix}/lib/mono/4.5/System.Reactive.Windows.Forms.dll
%{_prefix}/lib/mono/gac/System.Reactive.Windows.Threading
%{_prefix}/lib/mono/4.5/System.Reactive.Windows.Threading.dll
#%files reactive-devel
%_libdir/pkgconfig/reactive.pc
#%files wcf
%{_prefix}/lib/mono/gac/System.IdentityModel
%{_prefix}/lib/mono/4.5/System.IdentityModel.dll
%{_prefix}/lib/mono/gac/System.IdentityModel.Selectors
%{_prefix}/lib/mono/4.5/System.IdentityModel.Selectors.dll
%{_prefix}/lib/mono/gac/System.ServiceModel
%{_prefix}/lib/mono/4.5/System.ServiceModel.dll
%{_prefix}/lib/mono/gac/System.ServiceModel.Activation
%{_prefix}/lib/mono/4.5/System.ServiceModel.Activation.dll
%{_prefix}/lib/mono/gac/System.ServiceModel.Discovery 
%{_prefix}/lib/mono/4.5/System.ServiceModel.Discovery.dll
%{_prefix}/lib/mono/gac/System.ServiceModel.Routing 
%{_prefix}/lib/mono/4.5/System.ServiceModel.Routing.dll  
%{_prefix}/lib/mono/gac/System.ServiceModel.Web
%{_prefix}/lib/mono/4.5/System.ServiceModel.Web.dll
#%files web
%{_bindir}/disco 
%{_prefix}/lib/mono/4.5/disco.exe 
%{_prefix}/lib/mono/4.5/disco.exe.*  
%{_bindir}/httpcfg 
%{_prefix}/lib/mono/4.5/httpcfg.exe 
%{_prefix}/lib/mono/4.5/httpcfg.exe.*
%{_bindir}/mconfig 
%{_prefix}/lib/mono/4.5/mconfig.exe 
%{_prefix}/lib/mono/4.5/mconfig.exe.*
%{_bindir}/soapsuds 
%{_prefix}/lib/mono/4.5/soapsuds.exe 
%{_prefix}/lib/mono/4.5/soapsuds.exe.*  
%{_bindir}/svcutil 
%{_prefix}/lib/mono/4.5/svcutil.exe 
%{_prefix}/lib/mono/4.5/svcutil.exe.*  
%{_bindir}/wsdl 
%{_prefix}/lib/mono/4.5/wsdl.exe 
%{_prefix}/lib/mono/4.5/wsdl.exe.*  
%{_bindir}/wsdl2
%{_bindir}/xsd 
%{_prefix}/lib/mono/4.5/xsd.exe 
%{_prefix}/lib/mono/4.5/xsd.exe.*  
%{_prefix}/lib/mono/gac/Microsoft.Web.Infrastructure
%{_prefix}/lib/mono/4.5/Microsoft.Web.Infrastructure.dll
%{_prefix}/lib/mono/gac/Mono.Http
%{_prefix}/lib/mono/4.5/Mono.Http.dll
%{_prefix}/lib/mono/gac/System.ComponentModel.DataAnnotations
%{_prefix}/lib/mono/4.5/System.ComponentModel.DataAnnotations.dll
%{_prefix}/lib/mono/gac/System.Net.Http.Formatting
%{_prefix}/lib/mono/4.5/System.Net.Http.Formatting.dll
%{_prefix}/lib/mono/gac/System.Runtime.Remoting
%{_prefix}/lib/mono/4.5/System.Runtime.Remoting.dll
%{_prefix}/lib/mono/gac/System.Runtime.Serialization.Formatters.Soap 
%{_prefix}/lib/mono/4.5/System.Runtime.Serialization.Formatters.Soap.dll
%{_prefix}/lib/mono/gac/System.Web
%{_prefix}/lib/mono/4.5/System.Web.dll
%{_prefix}/lib/mono/gac/System.Web.Abstractions
%{_prefix}/lib/mono/4.5/System.Web.Abstractions.dll
%{_prefix}/lib/mono/gac/System.Web.DynamicData
%{_prefix}/lib/mono/4.5/System.Web.DynamicData.dll  
%{_prefix}/lib/mono/gac/System.Web.Routing
%{_prefix}/lib/mono/4.5/System.Web.Routing.dll  
%{_prefix}/lib/mono/gac/System.Web.Services
%{_prefix}/lib/mono/4.5/System.Web.Services.dll
%{_prefix}/lib/mono/gac/System.Web.ApplicationServices 
%{_prefix}/lib/mono/4.5/System.Web.ApplicationServices.dll
%{_prefix}/lib/mono/gac/System.Web.Http
%{_prefix}/lib/mono/4.5/System.Web.Http.dll  
%{_prefix}/lib/mono/gac/System.Web.Http.SelfHost 
%{_prefix}/lib/mono/4.5/System.Web.Http.SelfHost.dll  
%{_prefix}/lib/mono/gac/System.Web.Http.WebHost 
%{_prefix}/lib/mono/4.5/System.Web.Http.WebHost.dll  
%{_prefix}/lib/mono/gac/System.Web.Razor
%{_prefix}/lib/mono/4.5/System.Web.Razor.dll
%{_prefix}/lib/mono/gac/System.Web.WebPages
%{_prefix}/lib/mono/4.5/System.Web.WebPages.dll
%{_prefix}/lib/mono/gac/System.Web.WebPages.Deployment
%{_prefix}/lib/mono/4.5/System.Web.WebPages.Deployment.dll
%{_prefix}/lib/mono/gac/System.Web.WebPages.Razor 
%{_prefix}/lib/mono/4.5/System.Web.WebPages.Razor.dll
%{_mandir}/man1/disco.1.gz
%{_mandir}/man1/httpcfg.1.gz
%{_mandir}/man1/mconfig.1.gz
%{_mandir}/man1/soapsuds.1.gz
%{_mandir}/man1/wsdl.1.gz
%{_mandir}/man1/xsd.1.gz
%config (noreplace) %{_sysconfdir}/mono/browscap.ini
%config (noreplace) %{_sysconfdir}/mono/2.0/Browsers/Compat.browser
%config (noreplace) %{_sysconfdir}/mono/4.0/Browsers/Compat.browser
%config (noreplace) %{_sysconfdir}/mono/4.5/Browsers/Compat.browser
%config (noreplace) %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_sysconfdir}/mono/mconfig/config.xml
%config (noreplace) %{_sysconfdir}/mono/2.0/web.config
#%files web-devel
%{_libdir}/pkgconfig/aspnetwebstack.pc
#%files winforms
%{_prefix}/lib/mono/gac/Accessibility
%{_prefix}/lib/mono/4.5/Accessibility.dll
%{_prefix}/lib/mono/gac/Mono.WebBrowser 
%{_prefix}/lib/mono/4.5/Mono.WebBrowser.dll
%{_prefix}/lib/mono/gac/System.Design 
%{_prefix}/lib/mono/4.5/System.Design.dll  
%{_prefix}/lib/mono/gac/System.Drawing.Design 
%{_prefix}/lib/mono/4.5/System.Drawing.Design.dll  
%{_prefix}/lib/mono/gac/System.Windows.Forms 
%{_prefix}/lib/mono/4.5/System.Windows.Forms.dll  
%{_prefix}/lib/mono/gac/System.Windows.Forms.DataVisualization 
%{_prefix}/lib/mono/4.5/System.Windows.Forms.DataVisualization.dll  
#%files mvc
%{_prefix}/lib/mono/gac/System.Web.DynamicData 
%{_prefix}/lib/mono/4.5/System.Web.DynamicData.dll 
%{_prefix}/lib/mono/gac/System.Web.Extensions
%{_prefix}/lib/mono/4.5/System.Web.Extensions.dll  
%{_prefix}/lib/mono/gac/System.Web.Extensions.Design 
%{_prefix}/lib/mono/4.5/System.Web.Extensions.Design.dll  
%{_prefix}/lib/mono/gac/System.Web.Mvc
%{_prefix}/lib/mono/4.5/System.Web.Mvc.dll
#%files mvc-devel
%{_libdir}/pkgconfig/system.web.extensions.design_1.0.pc
%{_libdir}/pkgconfig/system.web.extensions_1.0.pc
%{_libdir}/pkgconfig/system.web.mvc.pc
%{_libdir}/pkgconfig/system.web.mvc2.pc
%{_libdir}/pkgconfig/system.web.mvc3.pc
#%files winfx
%{_prefix}/lib/mono/gac/System.Data.Services.Client
%{_prefix}/lib/mono/4.5/System.Data.Services.Client.dll
%{_prefix}/lib/mono/gac/WindowsBase 
%{_prefix}/lib/mono/4.5/WindowsBase.dll
#%files data
%{_bindir}/sqlsharp 
%{_prefix}/lib/mono/4.5/sqlsharp.exe 
%{_prefix}/lib/mono/4.5/sqlsharp.exe.*  
%{_bindir}/sqlmetal 
%{_prefix}/lib/mono/4.5/sqlmetal.exe 
%{_prefix}/lib/mono/4.5/sqlmetal.exe.*  
%{_prefix}/lib/mono/gac/System.Data 
%{_prefix}/lib/mono/4.5/System.Data.dll
%{_prefix}/lib/mono/gac/System.Data.DataSetExtensions 
%{_prefix}/lib/mono/4.5/System.Data.DataSetExtensions.dll
%{_prefix}/lib/mono/gac/System.Data.Entity
%{_prefix}/lib/mono/4.5/System.Data.Entity.dll
%{_prefix}/lib/mono/gac/System.Data.Linq
%{_prefix}/lib/mono/4.5/System.Data.Linq.dll
%{_prefix}/lib/mono/gac/System.Data.Services 
%{_prefix}/lib/mono/4.5/System.Data.Services.dll  
%{_prefix}/lib/mono/gac/System.Data.Services.Client 
%{_prefix}/lib/mono/4.5/System.Data.Services.Client.dll
%{_prefix}/lib/mono/gac/System.DirectoryServices 
%{_prefix}/lib/mono/4.5/System.DirectoryServices.dll
%{_prefix}/lib/mono/gac/System.DirectoryServices.Protocols 
%{_prefix}/lib/mono/4.5/System.DirectoryServices.Protocols.dll  
%{_prefix}/lib/mono/gac/System.EnterpriseServices
%{_prefix}/lib/mono/4.5/System.EnterpriseServices.dll  
%{_prefix}/lib/mono/gac/System.Runtime.Serialization 
%{_prefix}/lib/mono/4.5/System.Runtime.Serialization.dll
%{_prefix}/lib/mono/gac/System.Transactions
%{_prefix}/lib/mono/4.5/System.Transactions.dll  
%{_prefix}/lib/mono/gac/Mono.Data.Tds 
%{_prefix}/lib/mono/4.5/Mono.Data.Tds.dll  
%{_prefix}/lib/mono/gac/Novell.Directory.Ldap
%{_prefix}/lib/mono/4.5/Novell.Directory.Ldap.dll
%{_prefix}/lib/mono/gac/WebMatrix.Data
%{_prefix}/lib/mono/4.5/WebMatrix.Data.dll
%{_mandir}/man1/sqlsharp.1.gz
#%files data-sqlite
%{_prefix}/lib/mono/gac/Mono.Data.Sqlite
%{_prefix}/lib/mono/4.5/Mono.Data.Sqlite.dll  
#%files data-oracle
%{_prefix}/lib/mono/gac/System.Data.OracleClient 
%{_prefix}/lib/mono/4.5/System.Data.OracleClient.dll  
#%files -n ibm-data-db2
%{_prefix}/lib/mono/gac/IBM.Data.DB2 
%{_prefix}/lib/mono/4.5/IBM.Data.DB2.dll  
#%files -n monodoc
%{_prefix}/lib/mono/gac/monodoc
%{_prefix}/lib/mono/monodoc/*
%{_prefix}/lib/monodoc
%{_bindir}/mdoc 
%{_prefix}/lib/mono/4.5/mdoc.exe 
%{_prefix}/lib/mono/4.5/mdoc.exe.*
%{_bindir}/mod
%{_bindir}/mdoc-*
%{_bindir}/mdass*
%{_bindir}/mdval*
%{_bindir}/monodoc*
%{_mandir}/man1/md*
%{_mandir}/man1/monodoc*
%{_mandir}/man5/mdoc*
#%files -n monodoc-devel
%{_libdir}/pkgconfig/monodoc.pc

%changelog
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.1.44-1
-	initial version
