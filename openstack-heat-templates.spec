%global commit 5eb75ccc5132b6e4e0af05ec9d30e287311901ff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global project heat-templates

Name: openstack-heat-templates
Version: XXX
Release: XXX
Summary: Heat software config templates and DIB elements
License: ASL 2.0
URL: https://github.com/openstack/heat-templates
Source0: https://github.com/openstack/%{project}/archive/%{commit}.tar.gz#/%{project}-%{shortcommit}.tar.gz

BuildArch: noarch

%description
Heat software config templates and image building elements

%prep
%setup -qn %{project}-%{upstream_version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR hot/software-config %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.rst
%{_datadir}/%{name}

%changelog
