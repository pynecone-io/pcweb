```python exec
from pcweb.pages.docs import hosting
from pcweb.pages.pricing.pricing import pricing_path
```

# Reflex Branding

Remove Reflex branding from your exported or deployed sites. 

By default, Reflex branding, such as the "Made in Reflex" badge, will appear on all your published sites.


## How to remove the Reflex branding from your app

You can turn off the Reflex branding, when deploying to Reflex Cloud, by adding the `--badge` flag to the `reflex deploy` command. 

In order for this to work a user hosting with Reflex Cloud must be logged in and on a [paid plan]({pricing_path}) (at least pro tier). 


```md alert info
# A paid plan is required to remove the Reflex branding.
```

If you are self-hosting check out these instructions on [how to remove the Reflex branding from your self-hosted app]({hosting.self_hosting.path}#remove-reflex-branding-from-your-self-hosted-app).
