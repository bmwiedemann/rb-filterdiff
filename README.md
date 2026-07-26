# rb-filterdiff

A small helper for debugging [reproducible builds](https://reproducible-builds.org/):
run two files through the same *filter* that normalizes away expected/irrelevant
differences, then `diff -u` the results. This makes the *meaningful* difference between
two otherwise-noisy build artifacts (object files, cpio archives, RPM headers, build
logs, ...) easy to spot.

It is packaged separately from the `patchutils` project (which ships an unrelated
`filterdiff`), hence the `rb-` prefix.

## Usage

```
rb-filterdiff <filter> <file1> <file2> [extra diff options]
```

`<filter>` is either the name of one of the bundled filters (see below) or an arbitrary
command that reads a filename argument. Examples:

```sh
rb-filterdiff asmfilt old/foo.o new/foo.o        # compare disassembly, addresses stripped
rb-filterdiff rpmcpiofilt a.rpm b.rpm            # compare RPM payload file lists
rb-filterdiff 'cut -c9-' old/build.log new/build.log   # drop timestamp column, then diff
```

The bundled filters install into libexecdir and the `rb-filterdiff` wrapper prepends that
directory to `PATH`, so the short names resolve while arbitrary commands still work.

## Bundled filters

| Filter                  | Purpose                                              | Extra tool needed |
|-------------------------|------------------------------------------------------|-------------------|
| `asmfilt`               | `objdump -d` disassembly, leading addresses stripped | binutils          |
| `objdumpfilter`         | disassembly with addresses/offsets normalized        | binutils          |
| `sortstringsfilt`       | sorted `strings` output                              | binutils          |
| `cpiofilt`              | cpio archive table of contents                       | cpio              |
| `rpmcpiofilt`           | RPM payload table of contents                        | rpm, cpio         |
| `printrpmtags`          | dump all RPM header tags                             | rpm               |
| `printrpmtagsimmutable` | dump the RPM immutable header region                 | rpm               |
| `difflogfilt`           | list packages installed during a build (from log)    | perl              |
| `hexfilt`               | hex dump, one byte per line                          | perl              |
| `wordfilt`              | one word per line (for files with long lines)        | perl              |
| `gcovdumpfilter`        | `gcov-dump` output, file offsets stripped            | gcc, perl         |
| `make-d-filter`         | normalize `make -d` / strace-style logs              | coreutils, sed    |
| `stracefilter`          | normalize `strace` output (pids, addresses)          | coreutils, sed    |
| `nicifyfilter`          | un-uglify minified JavaScript                         | sed               |
| `x509filter`            | human-readable X.509 certificate dump                | gnutls (certtool) |
| `unmarshall.py`         | trace `.pyc` unmarshalling details                   | python3-xdis      |

## Build & install

```sh
cmake -B build
cmake --build build
cmake --install build          # honors DESTDIR / CMAKE_INSTALL_PREFIX
```

`rb-filterdiff` is installed to bindir; the filters to `<libexecdir>/rb-filterdiff/`;
a bash completion to `<datadir>/bash-completion/completions/`.

## Bash completion

Completing the first argument offers the bundled filter names plus filters you have
used before. The history is read from `$RB_FILTERDIFF_HISTORY` (default
`~/.rb-filterdiff_history`); each line is treated as a past command line whose second
shell-word is the filter, so multi-word filters like `rpm\ -qpvl` are offered as a
single argument. Point it at your own log with, e.g.:

```sh
export RB_FILTERDIFF_HISTORY=~/git/reproducibleopensuse/filterdiffhistory
```

## License

GPL-2.0-or-later
