"""UI and logic inkeep chat component."""

from typing import Set
import reflex as rx
from reflex.vars import ImportVar, Var

class Search(rx.Component):
    tag = "SearchBar"

    special_props: Set[Var] = {Var.create_safe("{...searchBarProps}")}

    is_open: Var[bool] = False

    def _get_imports(self):
        return rx.utils.imports.merge_imports(
            super()._get_imports(),
            {
              "next/dynamic": {ImportVar(tag="dynamic", is_default=True)},
              "react": {ImportVar(tag="useContext")},
              "/utils/context": {ImportVar(tag="ColorModeContext")},
            },
        )

    def get_triggers(self) -> Set[str]:
        """Get the event triggers for the component.

        Returns:
            The event triggers.
        """
        return super().get_triggers() | {"on_close", "on_shortcutKey_pressed"}

    def _get_all_hooks(self) -> dict[str, None]:
        """Get the React hooks for this component and its children.

        Returns:
            The code that should appear just before returning the rendered component.
        """
        # Add the hook code for this component.
        code = {
            "const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)": None,
            """const SearchBar = dynamic(
  () => import('@inkeep/widgets').then((mod) => mod.InkeepSearchBar),
  {
    ssr: false,
  },
);

const searchBarProps = {
  stylesheetUrls: ['/inkeepstyle-docs.css'],
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#5646ED',
    breadcrumbRules: {
      urlToBreadcrumbMapper: [
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/blog',
          },
          breadcrumbName: 'Blogs',
        }, 
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs',
          },
          breadcrumbName: 'Docs',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/api-reference',
          },
          replaceLeading: true,
          breadcrumbName: 'API Reference',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/library',
          },
          replaceLeading: true,
          breadcrumbName: 'Components',
        },
      ],
    },
    colorMode: {
      forcedColorMode: colorMode, // options: 'light' or dark'
    },
    theme: {
      components: {
        SearchBarTrigger: {
          defaultProps: {
            variant: 'emphasized', // 'emphasized' 'subtle'
          },
        },
      }
    }
  },
  searchSettings: { // optional InkeepSearchSettings
    tabSettings: {
      isAllTabEnabled: true,
      useAllRootBreadcrumbsAsTabs: true,
      rootBreadcrumbsToUseAsTabs: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
      tabOrderByLabel: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
    },
    placeholder: 'Search...',
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    quickQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
  },
};""": None,
        }
        # Add the hook code for the children.
        for child in self.children:
            code = {**code, **child._get_all_hooks()}

        return code

    def _get_custom_code(self) -> str:
        return """const SearchBar = dynamic(
  () => import('@inkeep/widgets').then((mod) => mod.InkeepSearchBar),
  {
    ssr: false,
  },
);"""


inkeep = Search.create
