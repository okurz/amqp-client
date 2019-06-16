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

# Please submit bugfixes or comments via https://bugs.opensuse.org/


# Define just "test" as a package in _multibuild file to distinguish test
# instructions here
%if "@BUILD_FLAVOR@" == ""
%define _test 0
%define name_ext %nil
%else
%define _test 1
%define name_ext -test
%endif

# only care about python3 version not to need to handle alternatives
%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         short_name amqpclient
Name:           %{short_name}%{?name_ext}
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Simple AMQP python CLI applications for receiving/sending
Url:            https://github.com/okurz/%{short_name}
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/%{short_name}/%{short_name}-%{version}.tar.xz
BuildRequires:  python-rpm-macros
%if 0%{?_test}
BuildRequires:  %{short_name}
%else
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-configargparse
Requires:       python-pika
%endif
BuildArch:      noarch
Provides:       %{short_name} == %{version}

%if 0%{?_test}
%else
%python_subpackages
%endif

%description
Simple AMQP python CLI applications for receiving/sending

%prep
%if 0%{?_test}
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}
%else
%setup -q
%endif

%build
%if 0%{?_test}
amqp-rx --help
amqp-tx --help
%else
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{_bindir}/*
%{python_sitelib}/*
%endif

%changelog
