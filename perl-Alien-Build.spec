%global _empty_manifest_terminate_build 0
Name:           perl-Alien-Build
Version:        2.41
Release:        1
Summary:        Alien::Build Perl module
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-Build
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(FFI::CheckLib)
BuildRequires:  perl-File-chdir
BuildRequires:  perl(Path::Tiny) >= 0.077
BuildRequires:  perl(PkgConfig::LibPkgConf::Client) >= 0.04
BuildRequires:  perl(PkgConfig::LibPkgConf::Util) >= 0.04
BuildRequires:  perl(Test2::API) >= 1.302096
BuildRequires:  perl(Test2::V0) >= 0.000060
Requires:       gcc
Requires:       perl(PkgConfig::LibPkgConf::Client) >= 0.04
Requires:       perl(PkgConfig::LibPkgConf::Util) >= 0.04
Requires:       perl(Test2::API) >= 1.302096

%description
This package provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at run time.
 
%package Plugin-Decode-HTML
Summary:        Alien::Build plugin to extract links from HTML
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts:      perl-Alien-Build < 1.76
 
%description Plugin-Decode-HTML
This Alien::Build plugin decodes an HTML file listing into a list of
candidates for your Prefer plugin.
 
%package Plugin-Decode-Mojo
Summary:        Alien::Build plugin to extract links from HTML
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
 
%description Plugin-Decode-Mojo
This Alien::Build plugin decodes an HTML file listing into a list of
candidates for your Prefer plugin.

%package help
Summary:  Alien::Build Perl module
Provides: perl-Alien-Build-doc

%description help
This package provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at run time.
 
%prep
%setup -q -n Alien-Build-%{version}
 
%build
export PERL_MM_OPT=""
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
 
%install
export PERL_MM_OPT=""
rm -rf $RPM_BUILD_ROOT

%{make_install}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

pushd %{buildroot}
touch filelist.lst
if [ -d usr/bin ];then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ];then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ];then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib ];then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
popd
mv %{buildroot}/filelist.lst .
 
%check
make test
 
%files -f filelist.lst
%defattr(-,root,root,-)
%doc Changes Changes.Alien-Base Changes.Alien-Base-Wrapper Changes.Test-Alien
%doc example README SUPPORT
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Alien/Build/Plugin/Decode/HTML.pm
%exclude %{perl_vendorlib}/Alien/Build/Plugin/Decode/Mojo.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Alien::Build::Plugin::Decode::HTML.3pm.*
%exclude %{_mandir}/man3/Alien::Build::Plugin::Decode::Mojo.3pm.*
 
%files Plugin-Decode-HTML
%{perl_vendorlib}/Alien/Build/Plugin/Decode/HTML.pm
%{_mandir}/man3/Alien::Build::Plugin::Decode::HTML.3pm.*
 
%files Plugin-Decode-Mojo
%doc Changes.Alien-Build-Decode-Mojo
%{perl_vendorlib}/Alien/Build/Plugin/Decode/Mojo.pm
%{_mandir}/man3/Alien::Build::Plugin::Decode::Mojo.3pm.*

%files help
%{_mandir}/*

%changelog
* Mon Jul 19 2021 Xu Jin <jinxu@kylinos.cn> - 2.41-1
- Update package to 2.41

* Thu Aug 13 2020 dingyue<dingyue5@huawei.com> - 2.28-2
- delete requires 

* Fri Aug 7 2020 dingyue<dingyue5@huawei.com> - 2.28-1
- Package Init 
