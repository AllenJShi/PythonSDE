import justpy as jp
import pandas
from datetime import datetime
from pytz import utc 
import matplotlib as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date 
day_average = data.groupby(['Day']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ''
    },
    subtitle: {
        text: 'Data provided by Udemy'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Course Review Analysis", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="The following graphs:")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Day"
    
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average["Rating"])
    return wp


jp.justpy(app)