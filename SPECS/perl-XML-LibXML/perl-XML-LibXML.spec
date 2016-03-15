Summary:        XML::LibXML module
Name:           perl-XML-LibXML
Version:        2.0121
Release:        1
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML
Source0:        http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/XML-LibXML-%{version}.tar.gz
%define sha1 XML-LibXML=acba14e43f136c39eee5ea5475dbbb8f32903e52
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	perl libxml2-devel zlib-devel perl-XML-NamespaceSupport perl-XML-SAX
Requires:	perl libxml2 zlib perl-XML-NamespaceSupport perl-XML-SAX

%description
Perl interface to the GNOME libxml2 library.

%prep
%setup -q -n XML-LibXML-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name 'perllocal.pod' -delete

%check
make test

%files
%{perl_vendorlib}
%{_mandir}

%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 2.0121-1
-	Initial version.



