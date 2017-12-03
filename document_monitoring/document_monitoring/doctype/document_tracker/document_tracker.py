# -*- coding: utf-8 -*-
# Copyright (c) 2017, Syed Abdul Qadeer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.user import get_system_managers
from frappe.translate import get_user_lang
from frappe import _

class DocumentTracker(Document):
	def before_insert(self):
		self.flags.in_insert = True

	def on_update(self):
		users = get_system_managers(True)

		if self.flags.in_insert:

			if users:
				for user in users:
					user_lang = get_user_lang(user)
					email_subject = _("A New Document Tracker Request : %(name)s is created", user_lang)%{
				"name": self.name,
				"status": self.status
			}
					email_content = _(""" 
					A new Document Tracker Request is created
					""", user_lang)%{
				"name": self.name,
				"status": self.status
			}

					frappe.sendmail(recipients=user, subject=email_subject, content=email_content)

			if self.user:
				email_subject = _("We have received your Document Tracker Request : " + self.name)
				email_content = _("""
					Your Document Tracker Request was received!
				""") % {
					"name": self.name,
					"status": self.status
				}

				frappe.sendmail(recipients=self.user, subject=email_subject, content=email_content)

			return


		if users:
			for user in users:
				user_lang = get_user_lang(user)
				email_subject = _("Document Tracker Request " +  self.name + " have new updates", user_lang)
				email_content = _(""" 
				Document Tracker Request %(name)s status was changed to : %(status)s
				""", user_lang)%{
				"name": self.name,
				"status": self.status
			}

				frappe.sendmail(recipients=user, subject=email_subject, content=email_content)

		if self.user:
			email_subject = _("Document Tracker Request " + self.name + " have new updates")
			email_content = _("""
				Document Tracker Request %(name)s status was changed to : %(status)s
			""")%{
				"name": self.name,
				"status": self.status
			}

			frappe.sendmail(recipients=self.user, subject=email_subject, content=email_content)

		return

