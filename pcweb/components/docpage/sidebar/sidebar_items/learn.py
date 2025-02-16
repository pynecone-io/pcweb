from pcweb.pages.docs import cloud_cliref
from .item import create_item


def get_sidebar_items_learn():
    from pcweb.pages.docs import (
        getting_started,
        advanced_onboarding,
    )

    items = [
        create_item(
            "Getting Started",
            children=[
                getting_started.introduction,
                getting_started.installation,
                getting_started.basics,
                getting_started.project_structure,
                getting_started.dashboard_tutorial,
                getting_started.chatapp_tutorial,
            ],
        ),
        create_item(
            "Advanced Onboarding",
            children=[
                advanced_onboarding.how_reflex_works,
                advanced_onboarding.configuration,
                advanced_onboarding.code_structure,
            ],
        ),
    ]
    return items


def get_sidebar_items_frontend():
    from pcweb.pages.docs import (
        assets,
        components,
        library_,
        pages,
        styling,
        ui,
        wrapping_react,
        custom_components,
    )
    from pcweb.components.docpage.sidebar.state import SideBarSection

    items = [
        SideBarSection(
            names="User Interface Overview",
            alt_name_for_next_prev="",
            link=ui.overview.path
        ),
        create_item(
            "Components",
            children=[
                components.props,
                components.conditional_rendering,
                components.rendering_iterables,
                components.html_to_reflex,
                library_,
            ],
        ),
        create_item(
            "Pages",
            children=[
                pages.overview,
                pages.dynamic_routing,
            ],
        ),
        create_item(
            "Styling",
            children=[
                styling.overview,
                styling.theming,
                styling.responsive,
                styling.custom_stylesheets,
                styling.layout,
                styling.common_props,
            ],
        ),
        create_item(
            "Assets",
            children=[
                assets.overview,
                assets.upload_and_download_files,
            ],
        ),
        create_item(
            "Wrapping React",
            children=[
                wrapping_react.overview,
                wrapping_react.guide,
                wrapping_react.example,
                wrapping_react.more_wrapping_examples,
            ],
        ),
        create_item(
            "Custom Components",
            children=[
                custom_components.overview,
                custom_components.prerequisites_for_publishing,
                custom_components.command_reference,
            ],
        ),
    ]
    return items


def get_sidebar_items_backend():
    from pcweb.pages.docs import (
        api_routes,
        authentication,
        client_storage,
        database,
        events,
        state,
        substates,
        utility_methods,
        vars,
    )
    from pcweb.components.docpage.sidebar.state import SideBarSection

    items = [
        SideBarSection(
            names="State Overview",
            alt_name_for_next_prev="",
            link=state.overview.path
        ),
        create_item(
            "Vars",
            children=[
                vars.base_vars,
                vars.computed_vars,
                vars.var_operations,
                vars.custom_vars,
            ],
        ),
        create_item(
            "Events",
            children=[
                events.events_overview,
                events.event_arguments,
                events.setters,
                events.yield_events,
                events.chaining_events,
                events.special_events,
                events.page_load_events,
                events.background_events,
                events.event_actions,
            ],
        ),
        create_item(
            "Substates",
            children=[
                substates.overview,
                substates.component_state,
            ],
        ),
        create_item(
            "API Routes",
            children=[
                api_routes.overview,
            ],
        ),
        create_item(
            "Client Storage",
            children=[
                client_storage.overview,
            ],
        ),
        create_item(
            "Database",
            children=[
                database.overview,
                database.tables,
                database.queries,
                database.relationships,
                database.model_editor,
            ],
        ),
        create_item(
            "Authentication",
            children=[
                authentication.authentication_overview,
            ],
        ),
        create_item(
            "Utility Methods",
            children=[
                utility_methods.router_attributes,
                utility_methods.lifespan_tasks,
                utility_methods.other_methods,
            ],
        ),
    ]
    return items


def get_sidebar_items_hosting():
    from pcweb.pages.docs import hosting

    items = [
        create_item(
            "Deploy Quick Start",
            children=[
                hosting.deploy_quick_start,
            ],
        ),
        create_item(
            "Project",
            children=[
                hosting.adding_members,
            ],
        ),  
        create_item(
            "App",
            children=[
                hosting.app_management,
                hosting.machine_types,
                hosting.regions, 
                hosting.logs,
                hosting.secrets_environment_vars,
                hosting.custom_domains,
                hosting.config_file,
                hosting.tokens,
                hosting.deploy_with_github_actions,
            ],
        ),  
        create_item(
            "Usage", 
            children=[   
                hosting.billing,
                hosting.compute,   
            ]
        ),
        create_item(
            "CLI Reference",
            children=cloud_cliref.pages
        ),
        create_item(
            "Self Hosting",
            children=[hosting.self_hosting],
        ),
    ]
    return items


learn = get_sidebar_items_learn()
frontend = get_sidebar_items_frontend()
backend = get_sidebar_items_backend()
hosting = get_sidebar_items_hosting()
