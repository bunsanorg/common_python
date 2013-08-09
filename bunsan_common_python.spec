%define _builddir   .
%define _sourcedir  .
%define _specdir    .
%define _rpmdir     .

Name:       bunsan_common_python
Version:    %{yandex_mail_version}
Release:    %{yandex_mail_release}
Url:        %{yandex_mail_url}

Summary:    Root package for bunsan python libraries
License:    GPLv3
Group:      System Environment/Libraries
Packager:   Aleksey Filippov <sarum9in@yandex-team.ru>
Distribution:   Red Hat Enterprise Linux

BuildArch:  noarch

Requires:   python26

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Root package for bunsan python libraries.


%build
python2.6 setup.py build


%install
rm -rf %{buildroot}
python2.6 setup.py --root="${buildroot}" --prefix=/usr


%clean
%{__rm} -rf %{buildroot}


%files
%defattr (-,root,root,-)
%{_prefix}/lib/python2.6/site-packages/bunsan_common-0.0-py2.6.egg-info
%{_prefix}/lib/python2.6/site-packages/bunsan/__init__.pyc
%{_prefix}/lib/python2.6/site-packages/bunsan/__init__.py


%changelog
