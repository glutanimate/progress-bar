# Changelog

All notable changes to Progress Bar will be documented here. You can click on each release number to be directed to a detailed log of all code commits for that particular release. The download links will direct you to the GitHub release page, allowing you to manually install a release if you want.

If you enjoy Progress Bar, please consider supporting my work on Patreon, or by buying me a cup of coffee :coffee::

<p align="center">
<a href="https://www.patreon.com/glutanimate" rel="nofollow" title="Support me on Patreon 😄"><img src="https://glutanimate.com/logos/patreon_button.svg"></a>      <a href="https://ko-fi.com/X8X0L4YV" rel="nofollow" title="Buy me a coffee 😊"><img src="https://glutanimate.com/logos/kofi_button.svg"></a>
</p>

:heart: My heartfelt thanks goes out to everyone who has supported this add-on through their tips, contributions, or any other means (you know who you are!). All of this would not have been possible without you. Thank you for being awesome!

## [Unreleased]

### Added

- Support for Anki 2.1.28+ (thanks to liuzikai)
- Display overall progress in deck browser (thanks to liuzikai)
- Progress is now remembered when switching back/forth between decks (thanks to liuzikai)

### Changed

- Largely refactor progress calculation (thanks to liuzikai)
- Use a robuster method to get due counts (thanks to liuzikai)
- Smoothen progress by introducing customizable weights for new cards, reviews, and cards in learning (thanks to liuzikai)
- Introduce type hints to many parts of the codebase (thanks to liuzikai)
- Rework project structure and move the add-on to a new repo in order to make it easier to publish updates, and reduce the barrier of entry for new contributors

## [1.3.0] - 2017-08-23

### Added

- Anki 2.1 compatibility
- New setting that shows remaining count (thanks to Sebastien Guillemot)

### Changed

- Limit to daily review limits by default (thanks to Sebastien Guillemot)

### Fixed

- Many bug fixes and smaller improvements (thanks to Sebastien Guillemot)

## 1.2.0 - 2017-08-06

Rework configuration section, add options for width and new/review queue

## 1.1.0 - 2017-08-06

Re-upload by me after the original add-on was deleted / the author went missing.

## 1.0.0 - 2017

Original release of Progress Bar by nest0r/Ja-Dark.


[Unreleased]: https://github.com/glutanimate/progress-bar/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/glutanimate/progress-bar/releases/tag/v1.3.0


-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).