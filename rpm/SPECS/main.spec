Name:           test.task
Version:        0.1
Release:        1%{?dist}
Summary:        Test task for RAIDIX
BuildArch:      noarch

License:        GPLv3
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  
Requires:       golang

%description
Test task for RAIDIX

%prep
%autosetup


%build
make compile


%install
make copy %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Wed Jun 08 2022 IamMushroom <eratoster@gmail.com>
- First release
