# -*- coding: utf-8 -*-

import openerp.addons.decimal_precision as dp
from openerp import fields, models


class buy_order_detail(models.TransientModel):
    _name = 'buy.order.detail'
    _description = u'采购明细表'

    date = fields.Date(u'采购日期')
    order_name = fields.Char(u'采购单据号')
    type = fields.Char(u'业务类型')
    partner_id = fields.Many2one('partner', u'供应商')
    goods_code = fields.Char(u'商品编码')
    goods_id = fields.Many2one('goods', u'商品名称')
    attribute = fields.Char(u'属性')
    uom = fields.Char(u'单位')
    warehouse_dest = fields.Char(u'仓库')
    qty = fields.Float(u'数量', digits_compute=dp.get_precision('Quantity'))
    price = fields.Float(u'单价', digits_compute=dp.get_precision('Amount'))
    amount = fields.Float(u'采购金额', digits_compute=dp.get_precision('Amount'))  # 商品的购货金额
    tax_amount = fields.Float(u'税额', digits_compute=dp.get_precision('Amount'))
    subtotal = fields.Float(u'价税合计', digits_compute=dp.get_precision('Amount'))
    note = fields.Char(u'备注')
