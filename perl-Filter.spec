%define module  Filter
%define version 1.35
%define release %mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	Source filter modules for Perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{module}-%{version}.tar.bz2
Patch:		%{name}-1.31.shellbang.patch
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	perl-devel

%description
Source filter modules for Perl

%prep
%setup -q -n %{module}-%{version}
%patch

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
# clean up AFTER compilation
find examples -type f -name \*.bak | xargs rm -f
find examples -type f | xargs perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{perl_vendorarch}/Filter/Util/Call.pm
rm -rf %{buildroot}%{perl_vendorarch}/auto/Filter/Util/Call
rm -rf %{buildroot}%{_mandir}/*/Filter::Util::Call.*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes examples README
%{_mandir}/*/*
%{perl_vendorarch}/auto/Filter
%{perl_vendorarch}/Filter
%{perl_vendorarch}/filter-util.pl
%{perl_vendorarch}/perlfilter.pod

