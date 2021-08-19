%global pypi_name patch-ng

Name:           python-%{pypi_name}
Version:        1.17.4
Release:        1
Summary:        Library to parse and apply unified diffs
License:        MIT
Group:          Development/Python
URL:            https://github.com/conan-io/python-patch-ng
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
Library to parse and apply unified diffs.
This project is a fork from the original python-patch project.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
#{python_sitelib}/__pycache__/*
#{python_sitelib}/%{pypi_name}.py
#{python_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info
