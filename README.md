This is a plugin for Tutor Open edX, and can be used for marketing and other educational purposes.
It's easy to install and customize like WordPress. Because plugins based of Wagtail and CodeRed CMS. Thanks a lot to the Vince Salvino :) https://github.com/coderedcorp/coderedcms 

### Installation:

`pip3 install  tutor-contrib-frontpage`

`tutor plugins list`

`tutor plugins enable frontpage`

`tutor config save`

`tutor images build frontpage`

`tutor local quickstart`


## Customization:

First of all you must add an A record to the your DNS management. Bacause Frontpage runs as a subdomain of your LMS_HOST. For example: if your domain is https://myedx.com so your marketing site will be https://frontpage.myedx.com 
