---
components:
    - rx.radix.text
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Text

```python demo
text("The quick brown fox jumps over the lazy dog.")
```

## As another element

Use the `as_` prop to render text as a `p`, `label`, `div` or `span`. This prop is purely semantic and does not alter visual appearance.

```python demo
flex(
    text("This is a ", strong("paragraph"), " element.", as_="p"),
    text("This is a ", strong("label"), " element.", as_="label"),
    text("This is a ", strong("div"), " element.", as_="div"),
    text("This is a ", strong("span"), " element.", as_="span"),
    direction="column",
    gap="3",
)             
```

## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.


```python demo
flex(
    text("The quick brown fox jumps over the lazy dog.", size="1"),
    text("The quick brown fox jumps over the lazy dog.", size="2"),
    text("The quick brown fox jumps over the lazy dog.", size="3"),
    text("The quick brown fox jumps over the lazy dog.", size="4"),
    text("The quick brown fox jumps over the lazy dog.", size="5"),
    text("The quick brown fox jumps over the lazy dog.", size="6"),
    text("The quick brown fox jumps over the lazy dog.", size="7"),
    text("The quick brown fox jumps over the lazy dog.", size="8"),
    text("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    gap="3",
)
```

Sizes 2–4 are designed to work well for long-form content. Sizes 1–3 are designed to work well for UI labels.


## Weight

Use the `weight` prop to set the text weight.

```python demo
flex(
    text("The quick brown fox jumps over the lazy dog.", weight="light", as_="div"),
    text("The quick brown fox jumps over the lazy dog.", weight="regular", as_="div"),
    text("The quick brown fox jumps over the lazy dog.", weight="medium", as_="div"),
    text("The quick brown fox jumps over the lazy dog.", weight="bold", as_="div"),
    direction="column",
    gap="3",
)
```


## Align

Use the `align` prop to set text alignment.


```python demo
flex(
    text("Left-aligned", align="left", as_="div"),
    text("Center-aligned", align="center", as_="div"),
    text("Right-aligned", align="right", as_="div"),
    direction="column",
    gap="3",
    width="100%",
)
```


## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text box.


```python demo
flex(
    text("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    text("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    gap="3",
)
```


Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.


```python demo
flex(
    box(
        heading("Without trim", margin_bottom="4px", size="3",),
        text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    box(
        heading("With trim", margin_bottom="4px", size="3", trim="start"),
        text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    direction="column",
    gap="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    text("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    text("The quick brown fox jumps over the lazy dog.", color_scheme="indigo", high_contrast=True),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="cyan", high_contrast=True),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="crimson", high_contrast=True),
    text("The quick brown fox jumps over the lazy dog.", color_scheme="orange", high_contrast=True),
    direction="column",
)
```


## With formatting

Compose `Text` with formatting components to add emphasis and structure to content.

```python demo
text(
    "Look, such a helpful ",
    link("link", href="#"),
    ", an ",
    em("italic emphasis"),
    " a piece of computer ",
    code("code"),
    ", and even a hotkey combination ",
    kbd("⇧⌘A"),
    " within the text.",
    size="5",
)
```


## With form controls

Composing `text` with a form control like `checkbox`, `radiogroup`, or `switch` automatically centers the control with the first line of text, even when the text is multi-line.


```python demo
box(
    text(
        flex(
            checkbox(default_checked=True),
            "I understand that these documents are confidential and cannot be shared with a third party.",
        ),
        as_="label",
        size="3",
    ),
    style={"max_width": 300},
)
```