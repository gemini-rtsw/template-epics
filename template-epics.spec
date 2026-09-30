# EPICS support module / IOC template for the gemini-rtsw-ci pipeline.
# To reuse: rename this file, change %define name, and set Version.

%define _prefix  /gem_base/epics/support
%define name     template-epics
%define arch     %(uname -m)
# $GIT_HASH is passed in by build_rpm.sh; git is only the fallback.
%define checkout %(if [ -n "$GIT_HASH" ]; then echo "$GIT_HASH"; else git rev-parse --short HEAD 2>/dev/null || echo nogit; fi)

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary:  Template EPICS module for the gemini-rtsw-ci pipeline
Name:     %{name}
Version:  1.0.0
Release:  1.git.%{checkout}%{?dist}
License:  EPICS Open License
Source0:  %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix:   %{_prefix}

# Pin every BuildRequires exactly, with %{?dist}. Add support modules the same
# way, e.g.:  BuildRequires: geminiRec-devel = 4.1.13-3.git.5dcd2db%{?dist}
BuildRequires: epics-base-devel = 7.0.7-0.git.054b1d4%{?dist} re2c gemini-ade

%description
A minimal EPICS module: one library and one database, built by the
gemini-rtsw-ci pipeline.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/%{name}
cp -r db lib include configure %{buildroot}%{_prefix}/%{name}

%files
%{_prefix}/%{name}

%changelog
* Wed Sep 30 2026 Hawi Stecher <hawi.stecher@noirlab.edu> - 1.0.0-1
- Initial template.
