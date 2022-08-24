from odoo import models, fields

class WeatherForecastLayout(models.TransientModel):
    '''
        Tùy chỉnh bố cục home
    '''
    _name = "weather.forecast.layout"

    location = fields.Char()
    name = fields.Char()
    region = fields.Char()
    country = fields.Char()
    localtime = fields.Char()
    weather_conditions = fields.Char()
    weather_conditions_icon = fields.Char()
    wind_degree = fields.Char()
    humidity = fields.Char()
    pressure_mb = fields.Char()
    temp_c = fields.Char()


