Name:    catimg
Version: 2.0
Release: 1%{?dist}
Summary: Print images in a terminal with 256 colors support


Group:   Applications/Multimedia
License: Unknown

URL:     https://github.com/posva/catimg
Source0: https://github.com/posva/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Print images in a terminal with 256 colors support


BuildRequires: cmake
Requires:


%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%files
/usr/bin/catimg*
%doc README.md



%changelog
* Fri Sep 18 2015 Mike Gerber <mike@sprachgewalt.de> - 2.0-1
- Initial spec file
