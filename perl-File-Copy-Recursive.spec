#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Copy-Recursive
Version  : 0.44
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/File-Copy-Recursive-0.44.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/File-Copy-Recursive-0.44.tar.gz
Summary  : 'Perl extension for recursively copying files and directories'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-Copy-Recursive-doc
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::File)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)

%description
File/Copy/Recursive version 0.43
================================
This module has 3 functions, one to copy files only, one to copy directories
only and one to do either depending on the argument's type.

%package doc
Summary: doc components for the perl-File-Copy-Recursive package.
Group: Documentation

%description doc
doc components for the perl-File-Copy-Recursive package.


%prep
%setup -q -n File-Copy-Recursive-0.44

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Copy/Recursive.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
