from pcweb.styles.tailwind_radix_map import radix_colors_dict, custom_colors_dict

tw_config = {
    "plugins": ["@tailwindcss/typography", "tailwindcss-radix"],
    "darkMode": "class",
    "theme": {
        "fontFamily": {
            "code": ["JetBrains Mono", "monospace"],
        },
        "fontSize": {
            "xs": [
                "0.75rem",
                {
                    "lineHeight": "1rem",
                    "letterSpacing": "-0.00375rem",
                },
            ],
            "sm": [
                "0.875rem",
                {
                    "lineHeight": "1.25rem",
                    "letterSpacing": "-0.01rem",
                },
            ],
            "base": [
                "1rem",
                {
                    "lineHeight": "1.5rem",
                    "letterSpacing": "-0.015rem",
                },
            ],
            "lg": [
                "1.125rem",
                {
                    "lineHeight": "1.625rem",
                    "letterSpacing": "-0.01625rem",
                },
            ],
            "xl": [
                "1.25rem",
                {
                    "lineHeight": "1.75rem",
                    "letterSpacing": "-0.028125rem",
                },
            ],
            "2xl": [
                "1.5rem",
                {
                    "lineHeight": "2rem",
                    "letterSpacing": "-0.0375rem",
                },
            ],
            "3xl": [
                "2rem",
                {
                    "lineHeight": "2.5rem",
                    "letterSpacing": "-0.07rem",
                },
            ],
            "4xl": [
                "2.5rem",
                {
                    "lineHeight": "3rem",
                    "letterSpacing": "-0.125rem",
                },
            ],
            "5xl": [
                "3rem",
                {
                    "lineHeight": "3.5rem",
                    "letterSpacing": "-0.1575rem",
                },
            ],
            "6xl": [
                "3.5rem",
                {
                    "lineHeight": "4rem",
                    "letterSpacing": "-0.1925rem",
                },
            ],
        },
        "colors": {
            **radix_colors_dict,
            **custom_colors_dict,
            "transparent": "transparent",
        },
        "boxShadow": {
            "none": "none",
            "small": "0px 2px 5px 0px light-dark(rgba(28, 32, 36, 0.03), rgba(0, 0, 0, 0.00))",
            "medium": "0px 4px 8px 0px light-dark(rgba(28, 32, 36, 0.04), rgba(0, 0, 0, 0.00))",
            "large": "0px 24px 12px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 8px 8px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 2px 6px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00))",
        },
    },
}
