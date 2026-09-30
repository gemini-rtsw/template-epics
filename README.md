# template-epics

Minimal **EPICS** package (IOC or support module) for the
[gemini-rtsw-ci](https://github.com/gemini-rtsw/gemini-rtsw-ci) pipeline.
It builds one library (`helloApp/src`) and one database (`helloApp/Db`) and
installs them under `/gem_base/epics/support/template-epics`.

The pipeline needs two files: `.github/workflows/ci.yml` and `template-epics.spec`.
Everything else is ordinary EPICS source.

## Use it for a new package

1. Copy this repo, then rename `template-epics` in the spec file name and in
   `%define name`.
2. Replace `helloApp` with your own `*App` directory, and list it in the top `Makefile`.
3. Add support modules to `configure/RELEASE`, each with a pinned
   `BuildRequires` in the spec.
4. Add the submodule and grant the repo **Write** access to `rpm-repo`, as
   described in the gemini-rtsw-ci README ("Start a new repo").

## Build locally

```bash
./gemini-rtsw-ci/build_rpm.sh --el 9      # RPM lands in rpms/
./gemini-rtsw-ci/dev_environment.sh --el 9  # shell in the build environment
```
