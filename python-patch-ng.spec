%define module patch-ng
%define oname patch_ng

Name:		python-patch-ng
Version:	1.19.0
Release:	1
Summary:	Library to parse and apply unified diffs
License:	MIT
Group:		Development/Python
URL:		https://github.com/conan-io/python-patch-ng
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Library to parse and apply unified diffs.
This project is a fork from the original python-patch project.

%files
%{python_sitelib}/__pycache__/%{oname}*.pyc
%{python_sitelib}/%{oname}.py
%{python_sitelib}/%{oname}-%{version}.dist-info
