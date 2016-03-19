%define raw_name    pack-pushbullet
%define name        pack-pushbullet
%define version     20160319
%define release     1
%define install_folder /usr/lib/

Name:       %{name}
Version:    %{version}
Release:    %{release}.%{dist}
License: GPL v3
Summary: Shinken pack to provide notifications via Slack
Group: Networking/Other
Source: https://github.com/mirwan/shinken-packs.git
URL: https://github.com/mirwan/shinken-packs
Distribution: Mirwan Inc
Vendor: Mirwan Inc
Packager: Erwan Miran <mirwan666@gmail.com>
BuildRoot:  %{_tmppath}/%{name}-%{version}
#Requires: python, python-dlnetsnmp

%description 
Shinken pack to provide notifications via Slack

%prep
%setup -q -n %{raw_name}

%pre
getent group shinken >/dev/null || /usr/sbin/groupadd -r shinken
getent passwd shinken >/dev/null || \
/usr/sbin/useradd -r -g shinken -d  %{_libdir}/shinken/ -s /bin/bash \
-c "Shinken user" shinken
exit 0

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 755 %{buildroot}/%{_libdir}/shinken/plugins/
%{__install} -d -m 755 %{buildroot}/%{_bindir}
<install>

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, shinken, shinken, 0755)
%{_libdir}/shinken/
%defattr(0755, shinken, shinken, 0755)
<files>
%doc

%changelog
* Sat Mar 19 2016 Erwan Miran <mirwan666@gmail.com>
- Initial Release
