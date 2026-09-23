# sentinel-sre-playground

A playground repo for [Sentinel SRE](https://github.com/bakiizese/autonomous-ai-sre-platform). It contains a few small, intentionally broken Python modules under `demo/`, and Sentinel's "inject a bug" demo opens issues against them.

The bugs are on purpose. Don't use this code for anything.

| File | Bug |
|------|-----|
| `demo/off_by_one.py` | `calculate_running_total` skips the last item |
| `demo/null_deref.py` | `get_user_display_name` crashes when `nickname` is `None` |
| `demo/bare_except.py` | `parse_config_value` swallows every exception and returns `None` |
| `demo/type_coercion.py` | `apply_discount` raises `TypeError` when the percentage is a string |

Fixes show up here as pull requests, each waiting for a human to merge.
