odoo.define('pos_example', function (require) {
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var rpc = require('web.rpc');

    var _super_Order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function (attributes, options) {
            _super_Order.initialize.apply(this, arguments);
            if (this.pos.config.pos_auto_invoice) {
                this.to_invoice = true;
            }
        },
        init_from_JSON: function (json) {
            var res = _super_Order.init_from_JSON.apply(this, arguments);
            if (json.to_invoice) {
                this.to_invoice = json.to_invoice;
            }
        }
    });
    var _super_PosModel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function (session, attributes) {
            var partner_model = _.find(this.models, function (model) {
                return model.model === 'res.partner';
            });
            partner_model.fields.push('vat');
            _super_PosModel.initialize.apply(this, arguments);
        },
        push_and_invoice_order: function () {
            var self = this;
            return _super_PosModel.push_and_invoice_order.apply(this, arguments).then(function () {
                var order = self.get_order();
                self.order = order;
                if (order.is_to_invoice() && self.config.receipt_invoice_number) {
                    return rpc.query({
                        model: 'pos.order',
                        method: 'search_read',
                        domain: [['name', '=', order['name']]],
                        fields: ['invoice_id'],
                    }).then(function (orders) {
                        if (orders.length >= 1) {
                            var invoice = orders[0]['invoice_id']
                            return rpc.query({
                                model: 'account.invoice',
                                method: 'search_read',
                                domain: [['id', '=', invoice[0]]],
                                fields: ['number'],
                            }).then(function (invoices) {
                                if (invoices.length >= 1) {
                                    self.order.invoice_number = invoices[0]['number']
                                }
                            }).fail(function (error) {
                            })
                        }
                    }).fail(function (error) {
                    })
                }
            });
        }
    })
});
