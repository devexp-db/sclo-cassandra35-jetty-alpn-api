%global addver v20141014

Name:           jetty-alpn-api
Version:        1.1.0
Release:        3%{?dist}
Summary:        Jetty ALPN API
License:        ASL 2.0 and EPL
URL:            http://www.eclipse.org/jetty
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.alpn.git/snapshot/alpn-api-%{version}.%{addver}.tar.bz2
Source1:        http://www.eclipse.org/legal/epl-v10.html
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)

%description
Jetty API for Application-Layer Protocol Negotiation.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n alpn-api-%{version}.%{addver}

# Use packaging=bundle to get the manifest into jar
%pom_remove_plugin :maven-jar-plugin
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'

cp %{SOURCE1} %{SOURCE2} .

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%license epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license epl-v10.html LICENSE-2.0.txt


%changelog
* Tue Aug 04 2015 Michael Simacek <msimacek@redhat.com> - 1.1.0-3
- Fix manifest inclusion

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Michael Simacek <msimacek@redhat.com>
- Initial packaging
