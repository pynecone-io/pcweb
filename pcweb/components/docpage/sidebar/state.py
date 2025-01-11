"""The state of the sidebar component."""

from __future__ import annotations

import reflex as rx
from reflex.base import Base


class SideBarBase(Base):
    """Base class for the Side bar."""

    # The name to display in the sidebar.
    names: str = ""

    alt_name_for_next_prev: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SideBarItem] = []

    # Whether the item is a category. Occurs if a single item is at the top level of the sidebar for aesthetics.
    outer = False


class SideBarItem(SideBarBase):
    """A single item in the sidebar."""

    ...


class SideBarSection(SideBarBase):
    """A section in the sidebar."""

    ...


class SidebarState(rx.State):
    _sidebar_index: int = -1

    def set_sidebar_index(self, num) -> int:
        self._sidebar_index = num

    @rx.var(cache=True, initial_value=-1)
    def sidebar_index(self) -> int:
        route = self.router.page.path
        if self._sidebar_index < 0:
            if "library" in route:
                return 1
            elif "hosting" in route:
                return 2
            elif "api-reference" in route:
                return 3
            else:
                return 0
        if "hosting" in route:
            return 2
        return self._sidebar_index