```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages import docs
from pcweb.styles.styles import get_code_style, cell_style


regions = {
    "ams": "Amsterdam, Netherlands",
    "arn": "Stockholm, Sweden",
    "alt": "Atlanta, Georgia (US)",
    "bog": "Bogotá, Colombia",
    "bom": "Mumbai, India",
    "bos": "Boston, Massachusetts (US)",
    "cdg": "Paris, France",
    "den": "Denver, Colorado (US)",
    "dfw": "Dallas, Texas (US)",
    "ewr": "Secaucus, NJ (US)",
    "eze": "Ezeiza, Argentina",
    "fra": "Frankfurt, Germany",
    "gdl": "Guadalajara, Mexico",
    "gig": "Rio de Janeiro, Brazil",
    "gru": "Sao Paulo, Brazil",
    "hkg": "Hong Kong, Hong Kong",
    "iad": "Ashburn, Virginia (US)",
    "jnb": "Johannesburg, South Africa",
    "lax": "Los Angeles, California (US)",
    "lhr": "London, United Kingdom",
    "mad": "Madrid, Spain",
    "mia": "Miami, Florida (US)",
    "nrt": "Tokyo, Japan",
    "ord": "Chicago, Illinois (US)",
    "otp": "Bucharest, Romania",
    "phx": "Phoenix, Arizona (US)",
    "qro": "Querétaro, Mexico",
    "scl": "Santiago, Chile",
    "sea": "Seattle, Washington (US)",
    "sin": "Singapore, Singapore",
    "sjc": "San Jose, California (US)",
    "syd": "Sydney, Australia",
    "waw": "Warsaw, Poland",
    "yul": "Montreal, Canada",
    "yyz": "Toronto, Canada"
}

vmtypes = [
    {"id": "c1m.5", "name": "Single CPU Small", "cpu_cores": 1, "ram_gb": 0.512},
    {"id": "c1m1", "name": "Single CPU Medium", "cpu_cores": 1, "ram_gb": 1.024},
    {"id": "c1m2", "name": "Single CPU Large", "cpu_cores": 1, "ram_gb": 2.048},
    {"id": "c2m.5", "name": "Double CPU Micro", "cpu_cores": 2, "ram_gb": 0.512},
    {"id": "c2m1", "name": "Double CPU Small", "cpu_cores": 2, "ram_gb": 1.024},
    {"id": "c2m2", "name": "Double CPU Medium", "cpu_cores": 2, "ram_gb": 2.048},
    {"id": "c2m4", "name": "Double CPU Large", "cpu_cores": 2, "ram_gb": 4.096},
    {"id": "c4m1", "name": "Quad CPU Micro", "cpu_cores": 4, "ram_gb": 1.024},
    {"id": "c4m2", "name": "Quad CPU Small", "cpu_cores": 4, "ram_gb": 2.048},
    {"id": "c4m4", "name": "Quad CPU Medium", "cpu_cores": 4, "ram_gb": 4.096},
    {"id": "c4m8", "name": "Quad CPU Large", "cpu_cores": 4, "ram_gb": 8.192}
]

```


# Reflex Cloud - Additional Concepts

To go back, i.e. from an app to a project or from a project to your list of projects you just click the `REFLEX logo` in the top left corner of the page.

```md alert info
# All flag values are saved between runs
All your flag values, i.e. environment variables or regions or tokens, are saved between runs. This means that if you run a command and you pass a flag value, the next time you run the same command the flag value will be the same as the last time you ran it. This means you should only set the flag values again if you want to change them.
```


## Adding Team Members

If you are a User you have the ability to create, deploy and delete apps, but you do not have the power to add or delete users from that project. You must be an Admin for that.

As an Admin you will see the an `Add user` button in the top right of the screen, as shown in the image below. Clicking on this will allow you to add a user to the project. You will need to enter the email address of the user you wish to add.

```python eval
image_zoom(rx.image(src="/hosting_adding_team_members.png", alt="Adding team members to Reflex Cloud"))
```

```python eval
rx.box(height="20px")
```

```md alert warning
# Currently a User must already have logged in once before they can be added to a project. 
At this time a User must be logged in to be added to a project. In future there will be automatic email invites sent to add new users who have never logged in before.
```



## Tokens

A token gives someone else all the permissions you have as a User or an Admin. They can run any Reflex Cloud command from the CLI as if they are you using the `--token` flag. A good use case would be for GitHub actions (you store this token in the secrets).

Tokens are found on the Project List page. If you cannot find it click the Reflex Logo in the top left side of the page until it appears as in the image below.

```python eval
image_zoom(rx.image(src="/hosting_tokens.png", alt="Adding tokens to Reflex Cloud"))
```


## VMTypes

To get all the possible VMTypes you can run the following command:

```bash
reflex apps vmtypes
```

To set which VMType to use when deploying your app you can pass the `--vmtype` flag with the id of the VMType. For example:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --vmtype c2m4
```

This will deploy your app with the `c2m4` VMType, giving your app 2 cpu cores and 4 gb of ram.

Below is a table of all the possible VMTypes:

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("id"),
            rx.table.column_header_cell("name"),
            rx.table.column_header_cell("cpu (cores)"),
            rx.table.column_header_cell("ram (gb)"),
        ),
    ),
    rx.table.body(
        *[
            rx.table.row(
                rx.table.cell(rx.code(vmtype["id"], style=get_code_style("violet"))),
                rx.table.cell(vmtype["name"], style=cell_style),
                rx.table.cell(vmtype["cpu_cores"], style=cell_style),
                rx.table.cell(vmtype["ram_gb"], style=cell_style),
            )
            for vmtype in vmtypes
        ]
    ),
    variant="surface",
)
```

## Regions

Below is an example of how to deploy your app in several regions:

```bash
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag (`-r` also works) with the region code. Check out all the regions that we can deploy to below:


```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Region Code"),
            rx.table.column_header_cell("Region"),
        ),
    ),
    rx.table.body(
        *[
            rx.table.row(
                rx.table.cell(rx.code(region_code, style=get_code_style("violet"))),
                rx.table.cell(region_name, style=cell_style),
            )
            for region_code, region_name in regions.items()
        ]
    ),
    variant="surface",
)
```