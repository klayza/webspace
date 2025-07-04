# Awesome Plone [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
[<img align="right" src="logo.png" height="64">](https://plone.org)

> A community-curated list of _awesome_ Plone add-ons.

<!--lint ignore double-link-->
[Plone](https://plone.org) is a open source CMS written in Python with a focus on functionality, customizability and security out of the box.

There are over [3000 add-ons for Plone on pypi](https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Plone) and over 1500 repositories in the [collective](https://github.com/collective/). If you want to know if there is already a add-on for Plone that fits your needs, searching for it on GitHub or pypi can be hard. It's hard to understand which one could be a good solution or not.

This list is intended to fill that gap, and create a shared knowledge about common products and techniques.

For a filterable list of addons aggreating all Plone related packages from PyPi see https://pag.derico.tech.

This list only covers add-ons that work with the latest major versions of Plone (currently 5.2 and 6) and only those that support Python 3.

Plone 6 comes with a new default frontend called Volto, which is written in React and uses `plone.restapi` to communicate with Plone. Volto is very extendable in itself. Checkout the [awesome-volto list](https://github.com/collective/awesome-volto) for add-ons to Volto.


## Contents

* [Content and utilities for content](#content-and-utilities-for-content)
* [Searching and Categorizing](#searching-and-categorizing)
* [Layout](#layout)
* [Tiles](#tiles)
* [Events](#events)
* [Forms](#forms)
* [Multilingual](#multilingual)
* [Media](#media)
* [Security](#security)
* [SEO](#seo)
* [Authentication](#authentication)
* [Shop](#shop)
* [Export, Import and Migrations](#export-import-and-migrations)
* [Themes](#themes)
* [Develop](#develop)
* [Sysadmin](#sysadmin)
* [Finding more add-ons](#finding-more-add-ons)
* [Official resources](#official-resources)

---

## Content and utilities for content

_Add-ons that provide content-types or additional functionality for content_

* [collective.a11ycheck](https://github.com/collective/collective.a11ycheck) - Reports accessibility issues to your site editors when a page is saved.
* [collective.bbcodesnippets](https://github.com/collective/collective.bbcodesnippets) - Provides generic and extensible BBCode markup integration for Plone.
* [collective.consent](https://github.com/collective/collective.consent) - Ask users for consent to different topics, before they can continue.
* [collective.dexteritytextindexer](https://github.com/collective/collective.dexteritytextindexer) - Dynamic SearchableText index for dexterity content types. For Plone 6 this was merged into Plone core.
* [collective.documentgenerator](https://github.com/collective/collective.documentgenerator) - Generate Documents (.odt, .pdf, .doc) from content based on appy framework (https://appyframe.work/) and OpenOffice/LibreOffice.
* [collective.documentviewer](https://github.com/collective/collective.documentviewer) - Very nice document viewer that integrates DocumentCloud viewer and PDF processing into Plone.
* [collective.easyformplugin.createdx](https://github.com/collective/collective.easyformplugin.createdx) - Creates Plone content objects from EasyForm submissions.
* [collective.embeddedpage](https://github.com/collective/collective.embeddedpage) - A content type to embed remote HTML pages in Plone Classic and Volto.
* [collective.folderishtraverse](https://github.com/collective/collective.folderishtraverse) - Traverse to first item in folder.
* [collective.folderishtypes](https://github.com/collective/collective.folderishtypes) - Provides the types "Folderish Event", "Folderish News Item" and "Folderish Document" as replacements for default types. Those types are able to hold any other content, like a Folder.
* [collective.geolocationbehavior](https://github.com/collective/collective.geolocationbehavior) - Geotagging for Plone content using LeafletJS.
* [collective.glossary](https://github.com/collective/collective.glossary) - Content type to define a glossary and its terms.
* [collective.immediatecreate](https://github.com/collective/collective.immediatecreate) - Create content immediatly and skip the add form.
* [collective.lineage](https://github.com/collective/collective.lineage) - Subsites: Turns subfolders of a Plone site to appear as autonomous Plone sites. There is also a whole ecosystem off addons specific to subsites.
* [collective.mailchimp](https://github.com/collective/collective.mailchimp) - MailChimp newsletter integration for Plone.
* [collective.mirror](https://github.com/collective/collective.mirror) - A content type that mirrors the content of any other container.
* [collective.mustread](https://github.com/collective/collective.mustread) - Tracking user views on content that are marked as must-read.
* [collective.remoteproxy](https://github.com/collective/collective.remoteproxy) - Proxy for remote content. All remote URLs for which a local proxy was created are replaced in the resulting content.
* [collective.restrictportlets](https://github.com/collective/collective.restrictportlets) - Allows you to restrict the available portlets that non-Managers can add.
* [collective.richdescription](https://github.com/collective/collective.richdescription) - Formatable description field for Plone.
* [collective.workspace](https://github.com/collective/collective.workspace) - Easily manage 'membership' in specific areas of a Plone Site. It allows to grant people access to areas of content using a membership group rather than local roles for each user, and to delegate control over that group to people who don't have access to the site-wide user/group control panel.
* [dexterity.membrane](https://github.com/collective/dexterity.membrane) - Enables content to be used as users and groups in Plone sites.
* [plone.pdfexport](https://github.com/plone/plone.pdfexport) - Generic PDF export functionality for Plone content.
* [Products.EasyNewsletter](https://github.com/collective/Products.EasyNewsletter) - Powerful newsletter/mailing product for Plone.
* [zopyx.ipsumplone](https://github.com/zopyx/zopyx.ipsumplone) - Creates demo content and demo images for Plone.


## Searching and Categorizing

* [cioppino.twothumbs](https://github.com/collective/cioppino.twothumbs) - Rate content using up- and down-thumbs.
* [collective.bookmarks](https://github.com/collective/collective.bookmarks) - Bookmarks/ favorites/ wish-list for Plone.
* [collective.collectionfilter](https://github.com/collective/collective.collectionfilter) - Faceted navigation filter for collection or contentlisting tiles.
* [collective.elasticsearch](https://github.com/collective/collective.elasticsearch) - Use ElasticSearch as the search backend for Plone.
* [collective.elastic.plone](https://github.com/collective/collective.elastic.plone) - ElasticSearch Integration for Plone content.
* [collective.searchandreplace](https://github.com/collective/collective.searchandreplace) - Find and replace text in Plone content objects.
* [collective.solr](https://github.com/collective/collective.solr) - Solr search engine integration for Plone.
* [collective.taxonomy](https://github.com/collective/collective.taxonomy) - Create, edit and use hierarchical taxonomies to categorize content.
* [eea.facetednavigation](https://github.com/collective/eea.facetednavigation) - Very powerful interface to improve search without programming skills. Configuration is done through-the-web and lets you gradually select and explore different facets (metadata/properties) of the content and narrow down you search quickly and dynamically.
* [Products.PloneKeywordManager](https://github.com/collective/Products.PloneKeywordManager) - Change, merge and delete keywords/tags/subjects).
* [zopyx.typesense](https://github.com/zopyx/zopyx.typesense) - Plone integration with the external Typesense search server (open-source). This is an alternative to collective.solr or Elasticsearch.


## Layout

_Products and resources that help developers and users to create and manage site layouts._

* [plone.app.mosaic](https://github.com/plone/plone.app.mosaic) - Powerful and extendable editor that allows users to compose the content of a page with different tiles.
* [collective.cover](https://github.com/collective/collective.cover) - Cover allows the creation of elaborate covers built around a drag-and-drop interface. Uses the same blocks/tiles ecosystem as plone.app.mosaic but a different approach to editing.
* [collective.contentsections](https://github.com/collective/collective.contentsections) - Offers a block approach for Plone 6 Classic based entirely on Dexterity content types.


## Tiles

_Add-ons that extend the layout editor plone.app.mosaic._

* [plone.app.standardtiles](https://github.com/plone/plone.app.standardtiles) - A set of standard tiles used by Mosaic, but can be used from any other tile manager.
* [collective.tiles.carousel](https://github.com/collective/collective.tiles.carousel) - A slider tile for plone.app.mosaic based on the carousel component of Bootstrap 5.
* [collective.tiles.advancedstatic](https://github.com/collective/collective.tiles.advancedstatic) - A tile that shows html text (similar to the static text portlet), with some additional configuration like the possibility to add custom css classes.
* [collective.tiles.collection](https://github.com/collective/collective.tiles.collection) - A tile that shows a set of collection results with possibility to choose (and develop) custom layouts.


## Events

_Add-ons that handle events and calendars._

* [collective.easyformplugin.registration](https://github.com/collective/collective.easyformplugin.registration) - Add a behavior to collective.easyform to manage registration forms for events.
* [collective.fullcalendar](https://github.com/collective/collective.fullcalendar) - Display events in a nice calendar UI using https://fullcalendar.io.
* [collective.venue](https://github.com/collective/collective.venue) - Venue type with geolocation support for use with events or any other location specific content.


## Forms

_Add-ons that allow generating and using forms._

* [collective.easyform](https://github.com/collective/collective.easyform) - EasyForm provides a Plone form builder through-the-web using fields, widgets, actions and validators. Form input can be saved or emailed. A simple and user-friendly interface allows non-programmers to create custom forms.
* [collective.fieldedit](https://github.com/collective/collective.fieldedit) - A flexible form to edit selected fields of a content type.
* [collective.honeypot](https://github.com/collective/collective.honeypot) - Honeypot protection for forms.
* [collective.z3cform.datagridfield](https://github.com/collective/collective.z3cform.datagridfield) - A field with a datagrid (table), where each row is a sub form.
* [collective.z3cform.norobots](https://github.com/collective/collective.z3cform.norobots) - A "human" captcha widget based on a list of questions/answers.
* [plone.formwidgets.hcaptcha](https://github.com/plone/plone.formwidget.hcaptcha) - HCaptcha widget to protect Plone from bots, spam, and other forms of automated abuse.
* [yafowil.plone](https://github.com/bluedynamics/yafowil.plone) - Yafowil is a form library for Python. This is its Plone Integration package.


## Multilingual

_Add-ons to help manage multilingual sites._

* [collective.linguatags](https://github.com/collective/collective.linguatags) - Multilingual Tags for Plone.
* [plone.app.multilingualindexes](https://github.com/plone/plone.app.multilingualindexes) - Indexes optimized to query multilingual content made with plone.app.multilingual.


## Media

_Add-ons that handle image, video and audio content._

* [collective.autoscaling](https://github.com/collective/collective.autoscaling) - Automatic scaling of large images. Useful to reduce your database size when editors upload too large images.
* [collective.behavior.banner](https://github.com/collective/collective.behavior.banner) - A behavior to create banners and sliders from banners.
* [collective.behavior.relatedmedia](https://github.com/collective/collective.behavior.relatedmedia) - A behavior to create/upload/manage media relations (Image, File) for content types.
* [collective.lazysizes](https://github.com/collective/collective.lazysizes) - Integration of lazysizes, a lightweight lazy loader, into Plone.
* [collective.wavesurfer](https://github.com/collective/collective.wavesurfer) - Implementation of https://wavesurfer-js.org audio player for Plone.
* [plone.app.imagecropping](https://github.com/collective/plone.app.imagecropping) - Crops Images in Plone manually using cropper JS library.
* [plone.gallery](https://github.com/plone/plone.gallery) - Photo gallery view for Plone.
* [redturtle.gallery](https://github.com/RedTurtle/redturtle.gallery) - Adds a gallery view with a carousel made with slick.
* [wildcard.media](https://github.com/collective/wildcard.media) - Provides audio and video content types and behaviors.


## Security

* [collective.explicitacquisition](https://github.com/collective/collective.explicitacquisition) - Disallow access to acquired content outside the current path.
* [collective.geotransform](https://github.com/collective/collective.geotransform) - Graceful E-mail Obfuscation for Plone.
* [collective.contactformprotection](https://github.com/collective/collective.contactformprotection) - Disables the default `contact-info` form or protect it with `plone.formwidget.[h|re]captcha`.

## SEO

_Add-ons for search engine optimization._

* [bda.plone.gtm](https://github.com/bluedynamics/bda.plone.gtm) - Google Tag Manager Integration.
* [collective.behavior.seo](https://github.com/collective/collective.behavior.seo) - Adds extra fields used for SEO optimisation.
* [collective.splitsitemap](https://github.com/collective/collective.splitsitemap) - Provides a cached split sitemap on big public sites.

## Authentication

_A list of authentication plugins, to integrate Plone with external user , Importsources and Migrations.import_

* [pas.plugins.ldap](https://github.com/collective/pas.plugins.ldap) - Provides users and groups from a LDAP directory.
* [pas.plugins.authomatic](https://github.com/collective/pas.plugins.authomatic) - Authomatic OAuth1/OAuth2/OpenID Login Integration with Plone.
* [iw.rejectanonymous](https://github.com/collective/iw.rejectanonymous) - Reject unconditionnally anonymous users from a Plone site, without any change in your security policy matrix or workflows. The basic use case is an extranet, where all visitors must be authenticated.
* [pas.plugins.headers](https://github.com/collective/pas.plugins.headers) - Reads request headers and uses them for authentication. Think SAML headers that are set by a front web server like Apache or nginx.
* [dm.zope.saml2](https://pypi.org/project/dm.zope.saml2/) - Supports SAML2 based Single Sign-On.
* [collective.impersonate](https://github.com/collective/collective.impersonate) - Allow administrators to impersonate another user. Useful for verifying workflow/permission set up on real content.
* [collective.pwexpiry](https://github.com/collective/collective.pwexpiry) - Provideds methods for stronger user passwords in Plone and password attack protection.


## Shop

* [bda.plone.productshop](https://github.com/bluedynamics/bda.plone.productshop) - Flexible and modular e-commerce solution for Plone.


## Export, Import and Migrations

* [collective.exportimport](https://github.com/collective/collective.exportimport/) - Export and import content and a lot of other data from and to Plone. The main solution for all kinds of migrations based on plone.restapi.
* [collective.migrationhelpers](https://github.com/collective/collective.migrationhelpers/) - Helpers and examples to use during migrations.
* [collective.jsonify](https://github.com/collective/collective.jsonify) - Export Plone content to JSON.
* [collective.transmogrifier](https://github.com/collective/collective.transmogrifier) - A configurable pipeline, aimed at transforming content for import and export.


## Themes

* [plonetheme.tokyo](https://github.com/collective/plonetheme.tokyo) - Tokyo Theme for Plone implements Bootstrap 4 into Plone, with an emphasis on keeping things as close to "default" as possible.
* [plonetheme.grueezibuesi](https://github.com/collective/plonetheme.grueezibuesi) - A kitten inspired theme for Plone 6.
* [collective.sidebar](https://github.com/collective/collective.sidebar) - A sidebar that consolidates toolbar and navigation.
* [collective.editablemenu](https://github.com/RedTurtle/collective.editablemenu) - A customizable navigation menu for Plone.


## Develop

_Add-ons that help developing Plone_

* [Products.PDBDebugMode](https://github.com/collective/Products.PDBDebugMode) - Post-mortem debugging: open a pdb session whenever an exception occurs so you you can find out what is going wrong. Plus: By adding /pdb to a url you end up you in a pdb session on the current context. A killer tool for developers.
* [plone.app.debugtoolbar](https://github.com/plone/plone.app.debugtoolbar) - A toolbar that shows a wealth of debug information about a running Plone site and the content you are inspecting. Also includes a interactive python-shell, a TALES-expression evaluator and and code-reload.
* [plone.reload](https://github.com/plone/plone.reload) - Code and configuration reload without server restarts.
* [Products.PrintingMailHost](https://github.com/collective/Products.PrintingMailHost) - Log mail messages instead of sending mail.
* [experimental.gracefulblobmissing](https://github.com/collective/experimental.gracefulblobmissing/) - Gracefully handle missing binary files in Plone.
* [collective.patchwatcher](https://github.com/collective/collective.patchwatcher) - A great companion for keeping track of patched or overridden files.
* [collective.relationhelpers](https://github.com/collective/collective.relationhelpers) - Helpers to manage, create, export and rebuild relations in Plone 5.x. For Plone 6 this was merged into Plone core.


## Sysadmin

_Add-ons that help admins deploying and maintaining Plone_

* [collective.catalogcleanup](https://github.com/collective/collective.catalogcleanup) - Removes data from the catalog that no longer belong to an actual object.
* [collective.fingerpointing](https://github.com/collective/collective.fingerpointing) - Keeps track of different events and write them down to an audit log.
* [collective.ifttt](https://github.com/collective/collective.ifttt) - Enables any Plone site to play in the IFTTT ecosystem. For example when a news item is published, then tweet about it or post it on Facebook.
* [collective.purgebyid](https://github.com/collective/collective.purgebyid) - Use tag-based cache invalidation in Plone (e.g. with Varnish's xkey module).
* [collective.recipe.backup](https://github.com/collective/collective.recipe.backup) - Powerful and flexible backup/restore solution for Plone.
* [collective.regenv](https://github.com/collective/collective.regenv) - Override registry settings using environment variables.
* [collective.revisionmanager](https://github.com/collective/collective.revisionmanager) - Manage Products.CMFEditions histories that can bloat your database.
* [collective.sentry](https://github.com/collective/collective.sentry) - Sentry integration to aggregate errors and help finding their causes.
* [dm.historical](https://pypi.org/project/dm.historical) - Access any historical state of your database. Can be useful to find out what happened to objects in the past and to restore accidentally deleted or modified objects.
* [haufe.requestmonitoring](https://github.com/collective/haufe.requestmonitoring) - Detailed request logging functionality on top of the publication events. Useful to find out what takes longer than it should.


## Finding more add-ons

It can be hard to find the right add-on for your requirements.
Here are some tips:

* Make a list of required features.
* Look in this list first.
* Search pypi: https://pypi.org/search/?c=Framework+%3A%3A+Plone
* Search the collective organization on github: https://github.com/collective
* Search the plone organization on github: https://github.com/plone
* Google for your requirements

Once you have a shortlist, test these add-ons. Here are the main issues you need to test before you install an add-on on a production site:

* Test all required features. Read but do not trust the documentation
* Check if the add-on runs on your required version
* Check if it is maintained
* Does it have i18n-support, i.e. is the user-interface translated to your language?
* Does it uninstall cleanly?
* Check for unwanted dependencies

Once you found an add-on you like, you can ask the community if you made a good choice or if you missed something:

* Message Board: https://community.plone.org

If you can't find something that fits your requirements 100% you can:

* Adapt your requirements to what is available.
* Invest the time & money to customize an existing add-ons to better fit your needs.
* Create a new add-on that does exactly what you need.

## Official resources

_Because Plone also has a lot of good official info resources_

<!--lint ignore double-link-->
* [plone.org](https://plone.org/) - Official website for developers and community.
* [community.plone.org](https://community.plone.org/) - Official community forum, the best place to get help.
* [Discord chat](https://discord.gg/zFY3EBbjaj) - Discord is the best way to chat with members of the Plone community.
* [Plone support](https://plone.org/support) - Where to find help.
* [docs.plone.org](https://docs.plone.org/) - Official documentation for developers/integrators.
* [Plone 6 Documentation](https://6.dev-docs.plone.org/) - Official documentation for the upcoming Plone 6 (work on progress).
* [training.plone.org](https://training.plone.org/) - Training classes for developers/integrators/users/designers.
* [plone.api](https://6.dev-docs.plone.org/plone.api/index.html) - Documentation for plone.api.


## Contributing

Contributions are welcome! Read the [contribution guidelines](contributing.md).
