#
# spec file for package amqpclient
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           amqpclient
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Simple AMQP python CLI applications for receiving/sending
Url:            https://github.com/okurz/amqpclient
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/amqpclient/amqpclient-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Simple AMQP python CLI applications for receiving/sending

%prep
%setup -q -n amqpclient-%{version}

%build
%python_build

%check
%python_check

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
