from pcweb.flexdown import component_map
import flexdown


def render_editor():
    return flexdown.render_file(
        "docs/library/chakra/forms/editor.md", component_map=component_map
    )
