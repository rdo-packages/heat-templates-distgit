%global commit 3754320f2bd1910f0e2470fdfdbca5f4113a46c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag 20140106git

Name: openstack-heat-templates
Version: 0
Release: 0.1.%{alphatag}%{?dist}
Summary: Heat example templates and DIB elements
Group: System Environment/Base
License: ASL 2.0
URL: https://github.com/openstack/heat-templates
Source0: https://github.com/openstack/heat-templates/archive/%{commit}/heat-templates-%{commit}.tar.gz
Requires: openstack-heat-common
Requires: oz
Requires: qemu-img
Requires: openstack-glance
Requires: diskimage-builder
Requires: libvirt-daemon
Obsoletes: heat-jeos <= 9-1

BuildArch: noarch

%description
Heat example templates and image building elements

%prep
%setup -qn heat-templates-%{commit}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
rm -f tools/fetch-cloudformation-examples
cp -aR tools/* %{buildroot}%{_bindir}
cp -aR cfn %{buildroot}%{_datadir}/%{name}
cp -aR hot %{buildroot}%{_datadir}/%{name}
cp -aR jeos %{buildroot}%{_datadir}/%{name}
cp -aR  openshift-origin %{buildroot}%{_datadir}/%{name}/openshift-origin
cp -aR openshift-enterprise %{buildroot}%{_datadir}/%{name}/openshift-enterprise


%files
%doc LICENSE README.rst
%{_bindir}/heat-jeos.sh
%{_bindir}/cfn-json2yaml
%{_datadir}/%{name}

%changelog
* Mon Jan 6 2014 Steven Dake <sdake@redhat.com> 0-0.1.20140106git
- Improvements based upon review comments

* Thu Dec 12 2013 Steven Dake <sdake@redhat.com> 0-0.1.20131212git
- Improvements from review comments

* Thu Sep 5 2013 Steven Dake <sdake@redhat.com> 0.0.1-1
- Initial heat-templates rpm
