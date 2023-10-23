# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from collections import defaultdict
from lxml import etree
from odoo import fields, models, tools, _, api
from odoo.exceptions import UserError


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    # for pass sequence on payment creation
    def _create_payments(self):
        payments = super(
            AccountPaymentRegister, self)._create_payments()

        context = self.env.context

        if context and context.get('payment_seq'):

            payments.write({
                'name': self.env.context.get('payment_seq')
            })
        return payments
