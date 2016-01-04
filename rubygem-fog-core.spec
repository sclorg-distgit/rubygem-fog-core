%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from fog-core-1.22.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-core

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.29.0
Release: 1%{?dist}
Summary: Shared classes and tests for fog providers and services
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(excon)
BuildRequires: %{?scl_prefix}rubygem(formatador)
BuildRequires: %{?scl_prefix_ror}rubygem(mime-types)
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest-stub-const)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(builder)
Requires: %{?scl_prefix}rubygem(excon) >= 0.38
Requires: %{?scl_prefix}rubygem(excon) < 1
Requires: %{?scl_prefix}rubygem(formatador) >= 0.2
Requires: %{?scl_prefix}rubygem(formatador) < 1
Requires: %{?scl_prefix_ror}rubygem(mime-types)
Requires: %{?scl_prefix}rubygem(net-scp) >= 1.1
Requires: %{?scl_prefix}rubygem(net-scp) < 2
Requires: %{?scl_prefix}rubygem(net-ssh) >= 2.1.3
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Shared classes and tests for fog providers and services.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
#pushd .%{gem_instdir}
#%{?scl:scl enable %{scl} - << \EOF}
#ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
#%{?scl:EOF}
#popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUT*
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.md
%{gem_instdir}/fog-core.gemspec
%{gem_instdir}/spec
%{gem_instdir}/tests

%changelog
* Mon Jun 15 2015 Josef Stribny <jstribny@redhat.com> - 1.29.0-1
- Update to 1.29.0

* Thu Nov 27 2014 Tomas Hrcka <thrcka@redhat.com> - 1.24.0-3
- rebuilt

* Wed Nov 26 2014 Tomas Hrcka <thrcka@redhat.com> - 1.24.0-2
- First build for vagrant1 scl

* Mon Sep 29 2014 Brett Lentz <blentz@redhat.com> - 1.24.0-1
- upstream release 1.24.0

* Tue Jul 29 2014 Brett Lentz <blentz@redhat.com> - 1.23.0-1
- upstream release 1.23.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Vít Ondruch <vondruch@redhat.com> - 1.22.0-1
- Initial package
