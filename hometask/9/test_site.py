def test_main_contacts(main_page):
    (main_page.open()
        .go_to_contact_us_page()
        .check_phone()
        .check_email())



