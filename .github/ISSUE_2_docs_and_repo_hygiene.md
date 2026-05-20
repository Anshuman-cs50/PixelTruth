## Description

Several documentation files have formatting errors, the MIT LICENSE file referenced in README is missing, `.DS_Store` is committed to the repo, and the test file is misnamed.

## Problems

1. **Missing `LICENSE` file** — README references `LICENSE` but no such file exists.
2. **CONTRIBUTING.md broken markdown** — Line 35 opens a code fence that is never closed before a new `## How to Contribute` heading begins on line 38, breaking rendering.
3. **README.md stray code fence** — A closing `` ``` `` on line 210 wraps the footer HTML in a code block.
4. **`.DS_Store` committed** — macOS metadata file should be in `.gitignore`.
5. **Test file misnamed** — `ptest.py` documents itself as `test_pipeline.py` (line 5) but the filename doesn't match.

## Type of Change

- [x] Documentation update
- [x] Bug fix

## Affected Files

- `LICENSE` (new)
- `CONTRIBUTING.md`
- `README.md`
- `.gitignore`
- `ptest.py` → `test_pipeline.py`

## Checklist

- [x] I have tested my changes locally
- [x] My code follows the project guidelines
