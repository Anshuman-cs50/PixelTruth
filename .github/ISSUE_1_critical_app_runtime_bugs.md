## Description

Multiple critical runtime bugs exist in `app.py` due to merge conflicts and code duplication introduced across recent PRs. These prevent Grad-CAM from working and cause training figures to render twice.

## Problems

1. **Missing `find_last_conv_layer()` definition** — The function was added in commit `f2f2003` but its definition was lost during the merge in `a0f9bda`. It is still called at `app.py:322`, causing a `NameError` at runtime. Grad-CAM visualization is silently broken.

2. **Duplicate `preprocess_image` definitions** — The function is defined twice (lines 146–148 and 157–169). The second definition silently shadows the first.

3. **Duplicate `preprocess_uploaded_image` definitions** — Same issue: defined at lines 150–155 and again at 172–179, with duplicate `cache_clear`/`cache_info` assignments.

4. **Duplicate `st.image` calls for training figures** — `Figure_2.png` and `Figure_1.png` are each rendered twice (once with deprecated `use_column_width`, once with `use_container_width`).

## Type of Change

- [x] Bug fix

## Affected Files

- `app.py`

## Steps to Reproduce

1. Run `streamlit run app.py`
2. Upload any image
3. Observe: Grad-CAM warning appears ("could not be generated: name 'find_last_conv_layer' is not defined")
4. Scroll to Training Performance section — each figure appears twice

## Expected Behavior

- Grad-CAM heatmap renders correctly alongside the original image
- Training figures appear exactly once each

## Checklist

- [x] I have tested my changes locally
- [x] My code follows the project guidelines
