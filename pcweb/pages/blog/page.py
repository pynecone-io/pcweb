import reflex as rx
from pcweb.components.icons import get_icon
from pcweb.components.webpage.comps import h1_title
from pcweb.flexdown import xd2 as xd
from .paths import blog_data


def back(title, url):
    def create_linkedin_share_url(path):
        """Create a LinkedIn share URL."""
        encoded_url = "https://reflex.dev" + (
            path if path.startswith("/") else "/" + path
        )
        encoded_url = encoded_url.replace(":", "%3A").replace("/", "%2F") + (
            "" if encoded_url.endswith("%2F") else "%2F"
        )
        return f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"

    return rx.flex(
        rx.link(
            "<- Back to Blog",
            color="var(--c-slate-9)",
            margin_bottom="2em",
            underline="hover",
            href="/blog",
        ),
        rx.link(
            rx.image(src="/companies/dark/twitter.svg", height="2em"),
            href=f"https://twitter.com/intent/tweet?text={title}&url=https://reflex.dev{url}&via=getreflex",
        ),
        rx.link(
            rx.image(src="/companies/dark/linkedin.svg", height="2em"),
            href=create_linkedin_share_url(url),
            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/yc.svg", height="2em"),
            href=f"https://news.ycombinator.com/submitlink?u=https://reflex.dev{url}&t={title}",
            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/reddit.svg", height="2em"),
            href=f"https://www.reddit.com/submit?url=https://reflex.dev{url}&title={title}",
            is_external=True,
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
        spacing="2",
        direction="column",
        z_index=1,
        position="fixed",
        top="300px",
        left="15px",
        margin=0,
        width="auto",
    )


def more_posts(current_post: dict) -> rx.Component:
    from .blog import card_content

    posts = []
    blog_items = list(blog_data.items())
    current_index = next(
        (
            i
            for i, (path, document) in enumerate(blog_items)
            if document.metadata.get("title") == current_post.get("title")
        ),
        None,
    )

    if current_index is None:
        # If current post is not found, default to first 3 posts
        selected_posts = blog_items[:3]
    elif current_index == 0:
        # If it's the first post, get the next 3
        selected_posts = blog_items[1:4]
    elif current_index == len(blog_items) - 1:
        # If it's the last post, get the previous 3
        selected_posts = blog_items[-4:-1]
    else:
        # Get previous 1 and next 2, excluding current post
        selected_posts = (
            blog_items[max(0, current_index - 1) : current_index]
            + blog_items[current_index + 1 : current_index + 3]
        )

    for path, document in selected_posts:
        meta = document.metadata
        posts.append(card_content(meta=meta, path=path.replace("blog/", "")))
    return rx.el.section(
        rx.el.h2(
            "More Posts",
            class_name="font-x-large gradient-heading",
        ),
        rx.box(
            *posts,
            class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full mb-4 blog-grid",
        ),
        class_name="flex flex-col gap-10 mt-20",
    )


def page(document, route) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.el.section(
        rx.el.article(
            rx.link(
                rx.box(
                    get_icon("arrow_right", class_name="rotate-180"),
                    "Back to Blog",
                    class_name="box-border flex justify-center items-center gap-2 border-slate-5 bg-slate-1 hover:bg-slate-3 -mb-4 px-3 py-0.5 border rounded-full font-small text-slate-9 transition-bg cursor-pointer",
                ),
                underline="none",
                href="/blog",
            ),
            rx.el.header(
                h1_title(title=meta["title"]),
                rx.el.h2(
                    str(meta["description"]),
                    class_name="font-md text-balance text-slate-10",
                ),
                rx.box(
                    rx.text(
                        meta["author"],
                    ),
                    rx.text(
                        "·",
                    ),
                    rx.moment(
                        str(meta["date"]),
                        format="MMM DD, YYYY",
                    ),
                    class_name="flex items-center gap-2 !font-normal font-small text-nowrap text-slate-9",
                ),
                class_name="section-header",
            ),
            rx.image(
                src=f"{meta['image']}",
                alt=f"Image for blog post: {meta['title']}",
                loading="lazy",
                class_name="rounded-[1.125rem] w-auto object-cover max-w-full max-h-[25rem] aspect-[1500/938]",
            ),
            rx.box(
                xd.render(document, "blog.md"),
                class_name="flex flex-col gap-4 w-full max-w-2xl",
            ),
            more_posts(meta),
            class_name="flex flex-col justify-center items-center gap-12 max-w-full",
        ),
        class_name="section-content",
    )
