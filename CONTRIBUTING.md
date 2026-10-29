# Contributing to Waraq

Thanks for your interest in Waraq. The project is a single-file, offline-first
EPUB reader, so small changes can have a large effect on portability and
privacy.

## Before you start

- Open an issue before a large feature, a change to the reading model, or a new
  dependency.
- Keep the built reader self-contained. Do not add remote scripts, styles,
  fonts, images, analytics, or runtime network requests.
- Keep book content sanitization and the Content Security Policy strict.
- Do not include DRM circumvention or code that uploads books or reading data.

## Development setup

Requirements: Python 3.10+ and Node.js 18+.

```sh
python src/build.py      # build dist/Waraq.html and the demo book
node scripts/check.mjs   # run the automated checks
python scripts/package.py
```

To preview the built reader:

```sh
python -m http.server 8000 --directory dist
```

Then open <http://localhost:8000/Waraq.html>.

## Pull requests

- Edit `src/index.html`, not `dist/Waraq.html`. Rebuild `dist/` before committing.
- Keep `dist/` in sync with the source; CI verifies that a fresh build produces
  no diff.
- Update `docs/README.txt`, `docs/TESTED.txt`, and `CHANGELOG.md` when behavior
  changes. Keep the English section first and the Arabic section below it.
- Bump `VERSION` for a release and rebuild the portable ZIP.
- Describe what you tested, including the browser and any manual checks.

## Reporting problems

Open a GitHub issue with the Waraq version, browser, operating system, and steps
to reproduce. Do not attach copyrighted books; use the bundled demo book or a
small original sample instead. For security-sensitive reports, use the
repository's private security advisory flow rather than a public issue.
