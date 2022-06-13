Name:           test.task
Version:        0.1
Release:        1%{?dist}
Summary:        Test task for RAIDIX

License:        GPLv3
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  golang
Requires:       golang

%description
Test task for RAIDIX

%define debug_package %{nil}

%prep
%autosetup


%build
make compile


%install
make copy INSTALLPATH=%{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Wed Jun 08 2022 IamMushroom <eratoster@gmail.com>
- First release
