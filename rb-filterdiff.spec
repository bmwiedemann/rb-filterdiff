#
# spec file for package rb-filterdiff
#
# Copyright (c) 2026 SUSE LLC
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
#


Name:           rb-filterdiff
Version:        filled-in-by-service
Release:        0
Summary:        Filter-and-diff helper for debugging reproducible builds
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/bmwiedemann/reproducibleopensuse
Source:         %{name}-%{version}.tar
BuildRequires:  cmake
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       diffutils
Requires:       grep
Requires:       sed
Recommends:     bash-completion
# For bundled filters
Recommends:     binutils
Recommends:     cpio
Recommends:     gawk
Recommends:     gnutls
Recommends:     perl
#Recommends:     python3-xdis
Recommends:     rpm
Recommends:     strace

%description
rb-filterdiff runs two files through the same normalizing filter and diffs the
results, so that expected/irrelevant differences are removed and the meaningful
difference between two build artifacts (object files, cpio archives, RPM
headers, build logs, ...) is easy to spot. It bundles a collection of such
filters used when debugging reproducible builds.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/rb-filterdiff
%{_libexecdir}/rb-filterdiff/
%{_datadir}/bash-completion/completions/rb-filterdiff

%changelog
