from app import create_app, db
from app.user.models import User
from app.chat.models import Chats, Messages, Notification
from app.feedback.models import Feedback
from app.health_record.models import HealthRecord
from app.consultation.models import Consultation
from app.clinical_note.models import ClinicalNote
from app.medical_cert.models import MedicalCert
from app.prescription.models import Prescription
from app.company.models import Company
from app.currency.models import Currency
from app.product.models import Product
from app.cart.models import Cart, CartItem
from app.order.models import Order, IncomingOrder
from app.delivery.models import Delivery

app = create_app()

#
# def cents_to_dollars(cents):
#
#
#     '''
#     Convert Cents to Dollars
#
#     :params cents: Amount in cents
#     :type cents: int
#     :return: float
#
#     100.0 is a float, 2 is the number of decimal place
#     operation in integer and float returns a float value
#     '''
#     return round(int(cents) / 100.0, 2)
#
#
# def dollars_to_cents(dollars):
#
#
#     '''
#     Convert Dollars to Cents
#
#     :params dollars: Amount in dollars
#     :type dollars: float
#     :return: int
#     '''
#     return int(dollars * 100)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Chats': Chats,
        'Messages': Messages,
        'Notification': Notification,
        'Feedback': Feedback,
        'HealthRecord': HealthRecord,
        'Consultation': Consultation,
        'ClinicalNote': ClinicalNote,
        'Prescription': Prescription,
        'MedicalCert': MedicalCert,
        'Company': Company,
        'Currency': Currency,
        'Product': Product,
        'Cart': Cart,
        'CartItem': CartItem,
        'Order': Order,
        'IncomingOrder': IncomingOrder,
        'Delivery': Delivery}


if __name__ == '__main__':
    app.run(debug=True)
