# Model Editor

The [`reflex-ag-grid`](https://github.com/reflex-dev/reflex-ag-grid) package
provides a `model_wrapper` component that is intended to display and edit model
data for an admin interface. It is intended for use in prototyping and
development and does not use any kind of authentication by default, so it should
not be used in production without additional security measures.

## Installation

To install the package, run:

```bash
pip install reflex-ag-grid
```

## Usage

A `model_wrapper` component displays a table of data for a given model class. In
the simple case, it is used like a normal component.

```python
import reflex as rx

from reflex_ag_grid import model_wrapper


class User(rx.Model, table=True):
    username: str
    email: str
    password: str


def user_table():
    return rx.box(
        model_wrapper(model_class=User, row_selection="multiple"),
        width="100%",
        height="50vh",
    )
```

The `model_wrapper` passes additional keyword arguments to the `ag_grid`
component, in this case `row_selection="multiple"` allows more than one row to
be selected.

By default, the table will display all rows in the database for all columns
defined in the model. Filtering and sorting are enabled based on the column
types and editing of all cells (except `id`) is allowed.

The `model_wrapper` component uses AG Grid infinite row model to efficiently
load and display large datasets. It fetches data from the backend in chunks as
the user scrolls through the table.

## Customizing Behavior

The `ModelWrapper` is implemented as a `ComponentState` with various hooks
exposed for customizing its behavior. To create a custom wrapper, subclass
`ModelWrapper` and override the desired methods.

To extend functionality of existing behavior, remember to call `super()` in the
overridden method.

```python
from reflex_ag_grid import ModelWrapper


class CustomWrapper(ModelWrapper):
    # See examples of overriding methods below
    ...


def custom_user_table():
    return rx.box(
        CustomWrapper.create(model_class=User, row_selection="multiple"),
        width="100%",
        height="50vh",
    )
```

### Row selection callback

The `on_selection_changed` method is called when a row is selected. By default, it
updates the `_selected_items` backend variable with model instances associated
with the selected rows.

To also display a toast with the selected row IDs, the method can be overridden:

```python
class CustomWrapper(ModelWrapper):
    def on_selection_changed(self, rows, source, type):
        super().on_selection_changed(rows, source, type)
        selected_ids = [row.id for row in self._selected_items]
        return rx.toast.info(f"Selected rows: \{selected_ids}")
```

### Displayed Columns and Behavior

The `_get_column_defs` method is called to get the AG Grid column definitions.
By default, it creates a ColumnDef for all model fields that allows editing.
Overriding this method allows you to disable editing, sorting, or filtering for
certain fields, or change the way values are displayed.

It is recommended to get the default columns by calling
`super()._get_column_defs()` and modifying, reordering, or removing them as
needed.

```python
class CustomWrapper(ModelWrapper):
    def _get_column_defs(self):
        new_columns = []
        for cdef in super()._get_column_defs():
            if cdef.field == "password":
                continue  # skip the password field
            if cdef.field == "email":
                cdef.editable = False  # Disable editing for the email field
            new_columns.append(cdef)

        # Swap the second and third column
        new_columns[1], new_columns[2] = new_columns[2], new_columns[1]
        return new_columns
```

### Handle Authorization

Each operation against the database calls the `_is_authorized` async method.

```python
async def _is_authorized(
    self,
    action: ModelWrapperActionType,
    action_data: list[M] | dict[str, Any] | None,
) -> bool: ...
```

If this method returns `False`, the operation will not be performed. By default,
this method always returns `True`.

`action` may be one of `ModelWrapperActionType` values.

```python
class ModelWrapperActionType(enum.Enum):
    """ModelWrapper action types."""

    SELECT = "select"
    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
```

`action_data` will differ based on the action type.

* For `SELECT`, `action_data` is None.
* For `INSERT`, `action_data` is a dictionary of the new row data.
* For `UPDATE`, `action data` is a dictionary of updated row data.
* For `DELETE`, `action data` is a list of model objects to delete.

Typically this method will use `self.get_state` to fetch a state containing the
current user and perform some check to ensure that user can perform the desired
action.

### Adding Data

There are 3 methods that influence the creation of new data:

* `_add_dialog` - classmethod that returns a component which will be rendered
  above the table. This component should display a form for creating a new row.
  The default implementation uses an `rx.dialog` with a form that has fields for
  each column in the model.
* `_add_dialog_field` - classmethod called by the default `_add_dialog` that
  returns a component to be rendered in the `_add_dialog` component. The
  returned component should be a form field for the new row. Since the default
  `_add_dialog` uses an `rx.table`, the default implementation of this method
  returns an `rx.table.row` with the field name, control, and field data type.
* `on_add` - event handler called when the user submits the form in the
  `_add_dialog`. The default implementation creates a new row in the database
  with the submitted data.

The following example renders an `rx.switch` for boolean fields, instead of the
default `rx.checkbox`:

```python
class CustomWrapper(ModelWrapper):
    @classmethod
    def _add_dialog_field(cls, field_name: str, field_type: type) -> rx.Component:
        if field_type == bool:
            return rx.table.row(
                rx.table.cell(rx.text(field_name)),
                rx.table.cell(rx.switch(id=field_name)),
            )
        return super()._add_dialog_field(field_name, field_type)
```

### Deleting Data

TBD