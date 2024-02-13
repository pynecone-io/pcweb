```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Theming

As of Reflex 'v0.4.0', you can now theme your Reflex applications. The core of our theming system is directly based on the [Radix Themes](https://radix-ui.com/docs/themes) library. This allows you to easily change the theme of your application along with providding a default light and dark theme.


## Theme

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rdxt.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
```

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the (Theme docs)[/docs/library/radix/theming/theme-panel/].

## Colors


### Color Scheme

ON a high level components `color_scheme` inherits from the color specified in the the theme. This means that if you change the theme, the color of the component will also change.

You can also specifiy the `color_scheme` prop.

```python demo
rdxt.flex(
    rdxt.button(
        "Hello World",
        color_scheme="tomato",
    ),
    rdxt.button(
        "Hello World",
        color_scheme="teal",
    ),
    spacing="2"
)
```

### Specific Shades of Palettes

To access a specific shade of color from the theme, you can use the `rx.color'. When switching to light and dark themes, the color will automatically change.

Shades can be accessed by using the color name and the shade number. The shade number ranges from 1 to 12. Additionally, they can have their alpha value set by using the `True` parameter it defaults to `False`.


```python demo
rdxt.flex(
    rdxt.button(
        "Hello World",
        color=rx.color("grass", 1),
        background_color=rx.color("grass", 12),
        border_color=f"1px solid {rx.color('grass', 1)}",
    ),
    rdxt.button(
        "Hello World",
        color=rx.color("grass", 1, True),
        background_color=rx.color("grass", 12, True),
        border_color=f"1px solid {rx.color('grass', 1, True)}",
    ),
    spacing="2"
)
```

### Regular Colors

You can also use standard hex, rgb, and rgba colors.

```python demo
rdxt.flex(
    rdxt.button(
        "Hello World",
        color="white",
        background_color="blue",
        border_color="1px solid red",
    ),
    rdxt.button(
        "Hello World",
        color="#ff0000",
        background_color="rgba(0, 0, 255, 0.5)",
        border_color="1px solid #ff0000",
    ),
    spacing="2"
)
```