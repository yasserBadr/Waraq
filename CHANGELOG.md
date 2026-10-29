# Changelog

All notable changes to Waraq are documented here. The project follows a
single-file, offline-first release model; `VERSION` is the source of truth for
the app footer and the portable ZIP name.

## [1.3] — 2026-10-29

### Added

- Continuous scroll reading with the chapter filling the available reading area.
- A4 portrait and screen-sized page layouts alongside scroll mode.
- Fit-page button, always-available sidebar toggle, and keyboard focus for the
  reading area.
- English-first documentation, a project screenshot, and a changelog.
- GitHub Actions CI and GitHub Pages deployment.
- Deterministic builds with fixed ZIP timestamps, so the EPUB, HTML, and release
  ZIP are reproducible.
- Automated checks for the page title, inline favicon, version substitution,
  and the absence of remote stylesheets.

### Changed

- The default reading layout is scroll mode; A4 and screen layouts remain
  available in Settings.
- The page `<title>` is now English-first (`Waraq — Portable EPUB Reader`) and
  the version is injected from `VERSION` at build time.
- The portable guide and test summary are now English-first with an Arabic
  section.

### Fixed

- Prevented horizontal scrolling in scroll mode and kept the reading sheet
  inside the visual viewport on short windows.
- Restored the welcome page document title after closing a book.
- Removed a stale byte count from the build output and unused imports.

## [1.2] — 2026-10-29

### Added

- Fit-page control and a sidebar toggle at every window size.

### Fixed

- Tied the app height to the actual visual viewport and recalculated on resize.
- Prevented book content from expanding the view area.
- Kept the A4 sheet fully visible in short and narrow windows.

## [1.1] — 2026-10-29

### Added

- A4 page layout with the correct 210:297 ratio, scaled to fit the screen.

### Changed

- Page layout can be switched between A4 and screen-sized pages.

## [1.0] — 2026-10-29

### Added

- Initial single-file EPUB 2/3 reader with Arabic-first RTL support.
- Table of contents, full-text search, bookmarks, and resume.
- Light, sepia, and dark themes; font size, family, and line-height controls.
- Focus mode, fullscreen, drag and drop, and keyboard shortcuts.
- Local reading data with JSON export/import.
- Optional last-book cache and a bundled Arabic demo book.
