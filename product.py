from openerp.osv import osv, fields

class product_template(osv.osv):
    _inherit = "product.template"

    def _compute_bom_stock(self, cr, uid, product, context=None):
        bom_obj = self.pool.get('mrp.bom')
        uom_obj = self.pool.get('product.uom')

        bom_id = bom_obj._bom_find(cr, uid, product.id, product.uom_id.id, properties=[])
        prod_min_quantities = []
        if bom_id:

            bom = bom_obj.browse(cr, uid, bom_id, context=context)

            if bom.bom_line_ids:
                stop_compute_bom = False
                for line in bom.bom_line_ids:
                    bom_qty = line.product_id["virtual_available"]
                    line_product_qty = line.product_qty

                    if bom_qty >= line_product_qty:
                        prod_min_quantity = bom_qty / line.product_qty
                        prod_min_quantities.append(prod_min_quantity)
                    else:
                        stop_compute_bom = True

                    if stop_compute_bom:
                        break

            if not prod_min_quantities:
                return -1
            else:
                return min(prod_min_quantities) * bom.product_qty
        else:
            return -1


    def _get_bom_quantity(self, cr, uid, ids, name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        for product_tpl in self.browse(cr, uid, ids, context=context):
            res[product_tpl.id] = self._compute_bom_stock(cr, uid, product_tpl, context=context)

        return res

    _columns = {
        'bom_quantity': fields.function(_get_bom_quantity, type='integer', string="BOM Quantity"),
    }