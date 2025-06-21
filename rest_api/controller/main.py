from odoo import http
from odoo.http import request, Response
import json


class PublicPartnerAPI(http.Controller):

    @http.route('/partner/create', type='http', auth='public', methods=['POST'], csrf=False)
    def create_partner(self, **kwargs):
        vals = json.loads(request.httprequest.data)
        partner = request.env['res.partner'].sudo().create(vals)
        return Response(
            json.dumps({"id": partner.id, "name": partner.name}),

        )

    @http.route('/partner/update/<int:partner_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_partner(self, partner_id, **kwargs):
        vals = json.loads(request.httprequest.data)
        partner = request.env['res.partner'].sudo().browse(partner_id)
        if not partner.exists():
            return Response("Partner not found", status=404)
        partner.write(vals)
        return {"status": "success", "id": partner.id}

    @http.route('/partner/delete/<int:partner_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_partner(self, partner_id, **kwargs):
        partner = request.env['res.partner'].sudo().browse(partner_id)
        if not partner.exists():
            return Response("Partner not found", status=404)
        partner.unlink()
        return {"status": "deleted", "id": partner_id}

    @http.route('/partner/<int:partner_id>', type='json', auth='public', methods=['GET'], csrf=False)
    def get_partner_by_id(self, partner_id, **kwargs):
        partner = request.env['res.partner'].sudo().browse(partner_id)
        if not partner.exists():
            return Response("Partner not found", status=404)
        return {
            "id": partner.id,
            "name": partner.name,
            "email": partner.email,
            "phone": partner.phone,
        }

    @http.route('/partner/all', type='json', auth='public', methods=['GET'], csrf=False)
    def get_all_partners(self, **kwargs):
        partners = request.env['res.partner'].sudo().search([],limit=20)
        data = []
        for partner in partners:
            data.append({
                "id": partner.id,
                "name": partner.name,
                "email": partner.email,
                "phone": partner.phone,
            })
        return data
