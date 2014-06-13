%define modname	Filter
%define modver	1.39

Summary:	Source filter modules for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{modver}.tar.gz
Patch0:	%{name}-1.31.shellbang.patch
BuildRequires:	perl-devel

%description
Source filter modules for Perl

%prep
%setup -qn %{modname}-%{modver}
%patch0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
# clean up AFTER compilation
find examples -type f -name \*.bak | xargs rm -f
find examples -type f | xargs perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

%check
make test

%install

%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}/Filter/Util/Call.pm
rm -rf %{buildroot}%{perl_vendorarch}/auto/Filter/Util/Call
rm -rf %{buildroot}%{_mandir}/*/Filter::Util::Call.*

%files
%doc Changes examples README
%{perl_vendorarch}/auto/Filter
%{perl_vendorarch}/Filter
%{perl_vendorarch}/filter-util.pl
%{perl_vendorarch}/perlfilter.pod
%{_mandir}/man3/*

