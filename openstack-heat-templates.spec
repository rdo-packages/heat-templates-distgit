%global commit 5eb75ccc5132b6e4e0af05ec9d30e287311901ff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag 20141111git

Name: openstack-heat-templates
Version: 0
Release: 0.2.%{alphatag}%{?dist}
Summary: Heat software config templates and DIB elements
Group: System Environment/Base
License: ASL 2.0
URL: https://github.com/openstack/heat-templates
Source0: https://github.com/openstack/heat-templates/archive/%{commit}/heat-templates-%{commit}.tar.gz

BuildArch: noarch

%description
Heat software config templates and image building elements

%prep
%setup -qn heat-templates-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR hot/software-config %{buildroot}%{_datadir}/%{name}

%files
%doc LICENSE README.rst
%{_datadir}/%{name}

%changelog
* Tue Nov 11 2014 Jeff Peeler <jpeeler@redhat.com> 0-0.2.20141111git
- Rebase to 5eb75ccc5132b6e4e0af05ec9d30e287311901ff
- Removed everything except software-config
- Removed unnecessary requires and obsoletes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20140407git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Jeff Peeler <jpeeler@redhat.com> 0-0.1.20140407git
- Rebase to 65a4f8bebc72da71c616e2e378b7b1ac354db1a3

* Fri Mar 7 2014 Jeff Peeler <jpeeler@redhat.com> 0-0.1.20140307git
- Rebase to e19e827ddfcc174dd0821f54d6af036e0a330e1e

* Mon Jan 6 2014 Steven Dake <sdake@redhat.com> 0-0.1.20140106git
- Improvements based upon review comments

* Thu Dec 12 2013 Steven Dake <sdake@redhat.com> 0-0.1.20131212git
- Improvements from review comments

* Thu Sep 5 2013 Steven Dake <sdake@redhat.com> 0.0.1-1
- Initial heat-templates rpm
