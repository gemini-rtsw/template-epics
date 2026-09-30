# template-epics

Minimal **EPICS** package (IOC or support module) for the
[gemini-rtsw-ci](https://github.com/gemini-rtsw/gemini-rtsw-ci) pipeline.
It builds one library (`helloApp/src`) and one database (`helloApp/Db`) and
installs them under `/gem_base/epics/support/template-epics`.

The pipeline needs two files: `.github/workflows/ci.yml` and `template-epics.spec`.
Everything else is ordinary EPICS source.

## Use it for a new package

1. On GitHub, click **Use this template** → **Create a new repository**, then clone it
   with its submodule:
   ```bash
   git clone --recurse-submodules git@github.com:gemini-rtsw/<name>.git
   ```
   The `gemini-rtsw-ci` submodule comes with the copy; there is nothing to add.
2. Grant the new repo **Write** access to `rpm-repo`: org **Packages** → `rpm-repo` →
   **Package settings** → **Manage Actions access** → add the repo, role **Write**.
   This can only be done once the repo exists, so the build GitHub starts on the new
   repo's first commit fails here, harmlessly.
3. **Rename before you push to `main`**: `template-epics` in the spec file name and in
   `%define name` (which is also the install directory under `/gem_base/epics/support`).
   The file name does not matter to CI -- it builds whatever `*.spec` it finds -- but
   `%define name` does: an unrenamed copy publishes a second `template-epics` RPM into
   the shared rpm-repo, where it competes with this template's own builds. Doing the
   rename on a branch with a PR is safe, since PR builds publish nothing.
4. Replace `helloApp` with your own `*App` directory, and list it in the top `Makefile`.
5. Add support modules to `configure/RELEASE`, each with a pinned
   `BuildRequires` in the spec.

## Build locally

```bash
./gemini-rtsw-ci/build_rpm.sh --el 9      # RPM lands in rpms/
./gemini-rtsw-ci/dev_environment.sh --el 9  # shell in the build environment
```
