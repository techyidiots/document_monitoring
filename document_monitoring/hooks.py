# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "document_monitoring"
app_title = "Document Monitoring"
app_publisher = "Syed Abdul Qadeer"
app_description = "Monitoring the document with status"
app_icon = "octicon octicon-file-directory"
app_color = "#7578f6"
app_email = "sdqadeer44@gmail.com"
app_license = "Proprietary"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/document_monitoring/css/document_monitoring.css"
# app_include_js = "/assets/document_monitoring/js/document_monitoring.js"

# include js, css files in header of web template
# web_include_css = "/assets/document_monitoring/css/document_monitoring.css"
# web_include_js = "/assets/document_monitoring/js/document_monitoring.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "document_monitoring.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "document_monitoring.install.before_install"
# after_install = "document_monitoring.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "document_monitoring.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"document_monitoring.tasks.all"
# 	],
# 	"daily": [
# 		"document_monitoring.tasks.daily"
# 	],
# 	"hourly": [
# 		"document_monitoring.tasks.hourly"
# 	],
# 	"weekly": [
# 		"document_monitoring.tasks.weekly"
# 	]
# 	"monthly": [
# 		"document_monitoring.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "document_monitoring.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "document_monitoring.event.get_events"
# }

