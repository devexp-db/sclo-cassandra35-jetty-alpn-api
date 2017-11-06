%{?scl:%scl_package jetty-alpn-api}
%{!?scl:%global pkg_name %{name}}

%global addver v20160715

Name:           %{?scl_prefix}jetty-alpn-api
Version:        1.1.3
Release:        4%{?dist}
Summary:        Jetty ALPN API
License:        ASL 2.0 and EPL
URL:            http://www.eclipse.org/jetty
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.alpn.git/snapshot/alpn-api-%{version}.%{addver}.tar.bz2
Source1:        http://www.eclipse.org/legal/epl-v10.html
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  %{?scl_prefix_maven}maven-plugin-build-helper
BuildRequires:  %{?scl_prefix_maven}jetty-parent
BuildRequires:  %{?scl_prefix_maven}jetty-build-support
%{?scl:Requires: %scl_runtime}

%description
Jetty API for Application-Layer Protocol Negotiation.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n alpn-api-%{version}.%{addver}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Use packaging=bundle to get the manifest into jar
%pom_remove_plugin :maven-jar-plugin
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'
%{?scl:EOF}

cp %{SOURCE1} %{SOURCE2} .

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%license epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license epl-v10.html LICENSE-2.0.txt


%changelog
* Mon Nov 06 2017 Augusto Mecking Caringi <acaringi@redhat.com> - 1.1.3-4
- scl conversion

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Michael Simacek <msimacek@redhat.com> - 1.1.3-1
- Update to upstream version 1.1.3

* Wed Sep 21 2016 Michael Simacek <msimacek@redhat.com> - 1.1.2-1
- Update to upstream version 1.1.2.v20150522

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Michael Simacek <msimacek@redhat.com> - 1.1.0-3
- Fix manifest inclusion

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Michael Simacek <msimacek@redhat.com>
- Initial packaging
