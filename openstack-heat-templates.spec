%global commit b5e110ea90ebdcb75ec4beb954a918fb6d842ca4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git
%global project heat-templates


Name: openstack-heat-templates
Version: 0
Release: 0.3%{alphatag}%{?dist}
Summary: Heat software config templates and DIB elements
License: ASL 2.0
URL: https://github.com/openstack/heat-templates
Source0: https://github.com/openstack/%{project}/archive/%{commit}.tar.gz#/%{project}-%{commit}.tar.gz

BuildArch: noarch

%description
Heat software config templates and image building elements

%prep
%setup -qn %{project}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR hot/software-config %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.rst
%{_datadir}/%{name}

%changelog
* Fri Apr  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0-0.3.96a0b0bgit
- Mitaka RC1 release

