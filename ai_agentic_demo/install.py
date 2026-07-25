import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

# Frappe has no equivalent of Odoo's view inheritance: you extend a stock DocType
# by shipping a Custom Field. Creating it in after_install (rather than exporting
# a fixture from a live site) keeps the definition in this repo and makes a fresh
# `bench install-app` reproducible.
CUSTOM_FIELDS = {
	"Customer": [
		{
			"fieldname": "ai_readiness_score",
			"label": "AI Readiness Score (/100)",
			"fieldtype": "Int",
			"insert_after": "customer_group",
			"description": (
				"Scratch field from the ai_agentic_demo app. Its presence on the "
				"Customer form confirms the app is being loaded from its own repo."
			),
		}
	]
}


def after_install():
	create_custom_fields(CUSTOM_FIELDS)


def before_uninstall():
	for doctype, fields in CUSTOM_FIELDS.items():
		for field in fields:
			frappe.delete_doc_if_exists("Custom Field", f"{doctype}-{field['fieldname']}")
