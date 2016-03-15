Summary:        XML::LibXML::Simple module
Name:           perl-XML-LibXML-Simple
Version:        0.95
Release:        1
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML
Source0:        http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/XML-LibXML-Simple-%{version}.tar.gz
%define sha1 XML-LibXML-Simple=4dd4c82fb70662458523a1218165d18ceafc8252
Vendor:		VMware, Inc.
Distribution:	Photon
BuildArch:      noarch
BuildRequires:	perl
Requires:	perl

%description
The XML::LibXML::Simple module is a rewrite of XML::Simple to use the XML::LibXML parser for XML structures,instead of the plain Perl or SAX parsers.

%prep
%setup -q -n XML-LibXML-Simple-%{version}

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
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 0.95-1
-	Initial version.



