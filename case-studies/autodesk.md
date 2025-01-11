---
company: Autodesk
description: "Streamlining Complex Workflows: Why Autodesk Chose Reflex Over Streamlit for Scalable, Python-Based Solutions"
domain: "https://autodesk.com"
founded: "San Francisco, 1982"
investors: "NASDAQ"
stats: [
    {
        "metric": "Company projects completed with Reflex",
        "value": "4"
    },
    {
        "metric": "Time saved on each project with Reflex",
        "value": "25%"
    },
    {
        "metric": "Cost saved as 1 person can do the job of 2 with Reflex",
        "value": "50%"
    }
]
meta: [
  {
    "name": "keywords",
    "content": "
      autodesk web app,
      python web app for construction,
      reflex vs streamlit,
      python react for data management,
      reflex autodesk case study,
      python data visibility,
      python workflow automation,
      python and react components,
      autodesk consulting tools,
      python web apps for enterprise,
      scalable python web apps,
      self-hosted python web apps,
      python web apps,
      react with python,
      web app framework python,
      web app python,
    "
  }
]
---

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import library
```

<!-- ```python eval
rx.vstack(
    image_zoom(rx.image(src="/case_studies/bayesline_app.png", border_radius="10px", alt="Bayesline App")),
    rx.text("Bayesline App built with Reflex"),
    width="100%",
)
``` -->


Meet Autodesk a globally recognized leader in design and engineering software, known for its innovative solutions that empower professionals across industries to bring their creative visions to life. Autodesk has established itself as a trusted partner for millions of users worldwide, helping them achieve greater efficiency, precision, and creativity in their projects.

In addition to its flagship offerings like AutoCAD, Revit, Maya, and Fusion 360, Autodesk serves a wide range of industries, including architecture, manufacturing, construction, and media.



## Struggling with Data Visibility and Manual Workflows

Autodesk Consulting provides support to customers to enable data-centric workflows, and integrating systems with custom app development leveraging Autodesk Platform Services.

Autodesk consults for a wide variety of companies that need a better way to move data and manage their digital project delivery in a way that is easily visible for all stakeholders to see the progress. Up until now, many relied on legacy, disconnected workflows using spreadsheets or other 3rd party systems, disjoint from where the live project data is stored.

These companies hired Autodesk Consulting to help them move their data more efficiently and visibly to create insights. The main parts that they needed help with were:

- **Document Management**: This feature helps construction teams organize, store, and share important documents (e.g., blueprints, contracts, plans, [3D designs and 2D drawings data](https://tutorials.autodesk.io/tutorials/simple-viewer/)) efficiently in a Common Data Environment.
- **RFI (Request for Information)**: RFIs are formal requests used during construction to clarify aspects of a project. Autodesk Build allows users to manage and track these RFIs within the platform.

Autodesk was looking to build an app for its clients to exchange information between design and construction. These companies wanted automated workflows to migrate RFI submissions and handle the repetitive, time-consuming and error prone actions like document uploads, data entry, attachments and comment logs for collaboration.

Paolo Serra, a Principal Implementation Consultant at Autodesk, was tasked with this project. Paolo is a Python developer and was looking for a web based solution. He didn’t want to use React and Javascript, but still wanted to build a production grade web app.

```md quote
- name: Paolo
- role: Principal Implementation Consultant
It normally requires multiple people to get an app up and there was a lack of resources available in the time frame we needed.
```

The solution had to be cloud based, to connect to existing systems and they only had 60 days to deliver it all. 

Failure to deliver the value and results, due to contract obligations, could lead to court litigations, financial losses, damaged reputation and losing the customer. And as Consulting services are available for high-end customers in the context of Enterprise Business Agreements, there was a lot at stake.



## Why Existing Solutions Fell Short for Autodesk’s Needs

Paolo explored other Python web app frameworks like Mesop and FastUI, but neither supported React—a requirement for all Autodesk products to ensure consistent styling with Autodesk certified React components. Company policy mandates building on Weave, a local company fork of the Material UI React library.

He explored Streamlit, Taipy and Dash, but didn’t like the way they looked and again did not have an easy way to use the required React components. He wanted to focus on business logic not low level implementation details.

```md quote
- name: Paolo
- role: Principal Implementation Consultant
Reflex gave us the freedom to create a product that could meet our business needs compared to streamlit to name one.
```

## Enabling Rapid Development with Reflex and Custom Components

Reflex’s React wrapping feature allowed Paolo to integrate the Weave React component library—a company requirement—directly into his app.

```md quote
- name: Paolo
- role: Principal Implementation Consultant
Wrapping the React component in Reflex allowed us to catch and prevent common issues, enforce standardization and raise more descriptive errors. The result is that instead of days it takes hours to be productive with the same design system.
```

Their team was able to leverage reusable high level components to build out UI with clean code including:

- A custom wrapped Treeview component to show the file directory
- A wrapped ModelViewer React component to view and collaborate on 2D drawings and 3D models via Autodesks Platform Services Viewer
- A table component to show and filter the data

The team was able to:

- Connect to different data sources using Python code they already had available
- Hook the app up with Autodesk auth
- Self-host their reflex app with their internal infrastructure, deploying to Azure


```md quote
- name: Paolo
- role: Principal Implementation Consultant
I am able to wear all the caps at once: Solution Architecture, UI/UX, front-end and back-end.
```




## Why Autodesk chose Reflex


Paolo and his team chose Reflex to develop a production-ready web app fully in Python. Reflex offered several key advantages, including:

* Allowing Autodesk to achieve more with fewer resources, significantly reducing overall costs

```md quote
- name: Paolo
- role: Principal Implementation Consultant
One person the can do the job of two with Reflex, so it cut our cost in half.
```

* Rapid prototyping, ensuring faster, more collaborative development

```md quote
- name: Paolo
- role: Principal Implementation Consultant
The time from ideation to prototype is shorter than traditional web dev, which is a massive win when you need to get to shared understanding of the product you are building.
```

* Saving Autodesk 25% on project timelines, delivering results faster and impressing clients.

```md quote
- name: Paolo
- role: Principal Implementation Consultant
A couple of weeks of work can be skimmed off the estimate for an average 60 day project by using Reflex meaning we were able to focus on exceeding customer expectations.
```

* The ability to wrap their local react library, which was a company requirement, and create reusable high-level components

* Future proofing their code by writing it in Python



### From One Project to Four

Paolo and his team have now worked on three other projects for different customers with Reflex:

1. A content management service to entirely redesign the way in which their consulting is delivered, from an in person experience to an online digital platform for consulting
2. An information registry project with digital delivery of artifacts
3. An analysis component dashboard which understands insights into what is happening in a companies local data, draws conclusions, and link to all the relevant Autodesk services


```md quote
- name: Paolo
- role: Principal Implementation Consultant
Everything I was able to accomplish was because of the framework and unparalleled support and promptness of the Reflex team.
```
