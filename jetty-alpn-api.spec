%global addver v20141014

Name:           jetty-alpn-api
Version:        1.1.0
Release:        1%{?dist}
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
* Thu Mar 12 2015 Michael Simacek <msimacek@redhat.com>
- Initial packaging
