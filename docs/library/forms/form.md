```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo
from pcweb.pages.docs.component_lib.forms.form import FormState


form_state = """
class FormState(State):

    form_data: dict = {}
    def handle_submit(self, form_data: dict):
        \"""Handle the form submit.\"""
        self.form_data = form_data
"""

form_example = """rx.vstack(
    rx.form(
        rx.vstack(
            rx.input(placeholder="First Name", id="first_name"),
            rx.input(placeholder="Last Name", id="last_name"),
            rx.hstack(
                rx.checkbox("Checked", id="check"),
                rx.switch("Switched", id="switch"),
            ),
            rx.button("Submit", type_="submit"),
        ),
        on_submit=FormState.handle_submit,
    ),
    rx.divider(),
    rx.heading("Results"),
    rx.text(FormState.form_data.to_string()),
)"""

```

Forms are used to collect user input. The `rx.form` component is used to group inputs and submit them together.


The form component's children can be form controls such as `rx.input`, `rx.checkbox`, or `rx.switch`. The controls should have an `id` attribute that is used to identify the control in the form data. The `on_submit` event trigger submits the form data as a dictionary to the `handle_submit` event handler.

The form is submitted when the user clicks the submit button or presses enter on the form controls.


```python eval
docdemo(form_example,
        state=form_state,
        comp=eval(form_example),
        context=True,
)
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.alert_title(
        "When using the form you must include a button or input with ",
        rx.code("type_='submit'"),
        ".",
    ),
    status="warning",
)
```
