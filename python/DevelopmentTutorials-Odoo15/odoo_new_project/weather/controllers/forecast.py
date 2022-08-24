from crypt import methods
import json
import werkzeug
from odoo import http
from odoo.http import request
import requests


class WeatherForecastController(http.Controller):


    @http.route('/weather_forecast_json',auth='public',type='http')
    def weather_forecast_json(self,**kwargs):
        address = kwargs["address"]
        _url = 'https://api.weatherapi.com/v1/current.json?key=ea5cec8b4a60443684f83726220808&q=%s'% str(address)
        data = requests.get(_url)
        data = data.json()
        return  json.dumps(data)


    ''' render ra templates'''
    @http.route('/weather_forecast',auth='public',type='http')
    def weather_forecast(self):
        response = request.render('weather.input_location')
        return response
    @http.route('/weather_forecast_location',auth='public',type='http')
    def weather_forecast_location(self,**kwargs):
        location = kwargs["name"]
        _url = 'https://api.weatherapi.com/v1/current.json?key=ea5cec8b4a60443684f83726220808&q=%s'% str(location)
        data = requests.get(_url)
        data = data.json()
        # location
        name = data["location"]["name"]
        temp_c = str(data["current"]["temp_c"])
        # wind_degree = "xyz"
        wind_degree = str(data["current"]["wind_degree"])
        template = ''' <h1>Weather Forecast</h1>
                        <p>location %s temp %s wind %s </p>'''%(name,temp_c,wind_degree)
        return template


    @http.route('/weather_forecast_show',auth='user',type='http')
    def weather_forecast_show(self):
        qcontext = {
                'name': 'Minh',
                'temp_c': "60",
                'wind_degree':0 
        }
        response = request.render('weather.show_weather_forecast',qcontext)
        return response





    @http.route('/weather', type='http', auth='public')
    def get_weather(self, *kw):
        return "<h1>helo ae</h1>"

    # @http.route('/christjobs/thankyou', type='http', auth="public", website=True)
    # def test_method(self, **kw):    
    #     # from here you can call    
    #     sale_rec = request.env['sale.order'].search([('id', '=', 1)]).method_name()    
    #     request.render('template_page')



    ''' truyen 1 bien vao bang url  '''
    # @http.route('/weather_forecast/<int:id>',auth='public', type='http')
    # def weather_forecast(self,id):
    #     return "Hello day la du bao thoi tiet %s" %str(id)

    ''' truyen den 1 trang web khac '''
    # @http.route('/weather_forecast',auth='public',type='http')
    # def weather_forecast(self):
    #     return werkzeug.utils.redirect('https://www.google.com')


    ''' return ve json '''
    # @http.route('/weather_forecast',auth='public',type='http')
    # def weather_forecast(self):
    #     return json.dumps({
    #         "name": "Minh",
    #         "day_of_birth":"19/10/2000"
    #         })

    ''' xu ly voi database '''
    # @http.route('/weather_forecast',auth='public',type='http')
    # def weather_forecast(self):
    #     partner = request.env['res.partner'].sudo().create({
    #         'name': 'Test'
    #     })
    #     return json.dumps({
    #         "status": 200,
    #         "message":"successful create !"
    #         })