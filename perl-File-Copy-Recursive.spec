#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Copy-Recursive
Version  : 0.45
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMUEY/File-Copy-Recursive-0.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMUEY/File-Copy-Recursive-0.45.tar.gz
Summary  : 'Perl extension for recursively copying files and directories'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Copy-Recursive-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
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

%package dev
Summary: dev components for the perl-File-Copy-Recursive package.
Group: Development
Provides: perl-File-Copy-Recursive-devel = %{version}-%{release}
Requires: perl-File-Copy-Recursive = %{version}-%{release}

%description dev
dev components for the perl-File-Copy-Recursive package.


%package perl
Summary: perl components for the perl-File-Copy-Recursive package.
Group: Default
Requires: perl-File-Copy-Recursive = %{version}-%{release}

%description perl
perl components for the perl-File-Copy-Recursive package.


%prep
%setup -q -n File-Copy-Recursive-0.45
cd %{_builddir}/File-Copy-Recursive-0.45

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Copy::Recursive.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
