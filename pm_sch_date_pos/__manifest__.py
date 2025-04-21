{
    'name': 'Spa Appointment and Salon POS',
    'Version': '17.0',
    "category": 'Point of Sale',
    'summary':'SPA - POS Appointment Booking is a custom Odoo 17.0 integration that enables  appointment'
              ' scheduling directly from the Point of Sale (POS) interface. It enhances customer experience by'
              ' linking service-based products with real-time appointment booking, calendar integration, and '
              'automated notifications.',
    'description':'This module allows POS users to book appointments in real-time using a custom popup for '
                  'selecting date, time, employee, and resource. Appointment details are saved in the POS order, '
                  'auto-confirmed via email, and synced with the Odoo Calendar. Customers can also view their '
                  'bookings in their profile section. Ideal for salons, spas,and other service-driven businesses.',
    'category': 'Extra Tools',
    'depends': ['point_of_sale','web','hr','appointment'],
    'data': [

        'views/pos_order_line.xml',
        'views/appointment_view.xml',
        'views/appointment_portal.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pm_sch_date_pos/static/src/**/*',

            ],
    },
    'author':'Prime Minds Consulting Pvt ltd',
    'company':'Prime Minds Consulting Pvt ltd',
    'maintainer':'Prime Minds Consulting Pvt ltd',
    'website':'https://www.primeminds.co',
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images':['static/description/banner.png'],
    'price':125.0,
    'currency': 'USD',
}
