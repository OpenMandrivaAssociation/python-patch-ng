Name:           python-patch-ng
Version:        1.18.0
Release:        1
Summary:        Library to parse and apply unified diffs
License:        MIT
Group:          Development/Python
URL:            https://github.com/conan-io/python-patch-ng
Source0:	https://pypi.io/packages/source/p/patch-ng/patch-ng-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)

%description
Library to parse and apply unified diffs.
This project is a fork from the original python-patch project.

%files
%{python_sitelib}/patch_ng-%{version}-py*.*-info
%{python_sitelib}/patch_ng.py

#--------------------------------------------------------------------

%prep
%autosetup -n patch-ng\-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

