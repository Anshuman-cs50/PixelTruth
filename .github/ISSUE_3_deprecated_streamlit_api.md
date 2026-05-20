## Description

Streamlit has deprecated `use_column_width` in favour of `use_container_width`. The codebase still uses the deprecated parameter in several `st.image()` calls, producing deprecation warnings in the console.

## Problems

All `st.image(..., use_column_width=True)` calls should be migrated to `st.image(..., use_container_width=True)`.

## Type of Change

- [x] Bug fix

## Affected Files

- `app.py`

## Checklist

- [x] I have tested my changes locally
- [x] My code follows the project guidelines
