# -*- coding: utf-8 -*-
__author__ = 'Iryna Ilina'

from model.contact import Contact

def test_contact_info(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


def test_home_contact_info_vs_db(app, db):
    home_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(map(app.contact.contact_like_on_home_page, db.get_contact_list()), key=Contact.id_or_max)
    assert home_contacts == db_contacts


