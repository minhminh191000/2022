# import json
# import werkzeug
from odoo import http
from odoo.http import request

from odoo.addons.weather.controllers.forecast import WeatherForecastController

class WeatherForecastController(WeatherForecastController):

    @http.route('/weather_forecast')
    def weather_forecast(self):
        super(WeatherForecastController,self).weather_forecast()
        # https://api.weatherapi.com/v1/current.json?key=ea5cec8b4a60443684f83726220808&q=VietNam
        return "hello toi da ke thua "
from zeep import Client, Settings, xsd
import datetime
from odoo import http
from lxml.etree import tostring

# class WaseelCrm(http.Controller):
#    @http.route('/test/zeep', type='http', methods=['POST'], auth="public", website=True, csrf=False)
#    def test_zeep(self, **kw):
#        settings = Settings(strict=False, xml_huge_tree=True)
#        client = Client('odoo/custom_modules/zeep_test/static/src/uhud/Uhud.wsdl', settings=settings)
#        factory = client.type_factory('ns0')
#        transaction = factory.TransactionCT('1.1', 'NEW', None, None, 'REQUEST')
#        user = factory.UserCT('ahmed', kw['username'], kw['password'])
#        interaction = factory.InteractionCT(None, 102, 2260, 101)
#        timestamp = datetime.datetime.combine(datetime.datetime.now(), datetime.time(10, 23))
#        cmh = factory.MessageHeaderCT(transaction, interaction, user, timestamp)
#        member = factory.MemberCT('002069310841001', '2069310841', '15884942')
#        visitInfo = factory.visitInfoCT(timestamp, 7, 'NEW')
#        eligibilityRequest = factory.EligibilitySubmissionRequestCT(member, visitInfo)
#        with client.settings(raw_response=True):
#            response = client.service.submitSchema(CommonMessageHeader=cmh,
#                                                   EligibilitySubmissionRequest=eligibilityRequest)

#        if response.content:
#         print(response.content)
    


