---
components:
    - rx.radix.separator
---

```python exec
import reflex as rx
```

# Separator

Visually or semantically separates content.

## Basic Example

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.separator(),
    rx.card("Section 2"),
    gap="4",
    direction="column",
    align="center",
)
```

## Size

The `size` prop controls how long the separator is. Using `size="4"` will make
the separator fill the parent container. Setting CSS `width` or `height` prop to `"100%"`
can also achieve this effect, but `size` works the same regardless of the orientation.

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.separator(size="4"),
    rx.card("Section 2"),
    gap="4",
    direction="column",
)
```

## Orientation

Setting the orientation prop to `vertical` will make the separator appear vertically.

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.separator(orientation="vertical", size="4"),
    rx.card("Section 2"),
    gap="4",
    width="100%",
    height="10vh",
)
```