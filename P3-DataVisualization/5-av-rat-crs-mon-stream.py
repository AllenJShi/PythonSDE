import justpy as jp
import pandas
from datetime import datetime
from pytz import utc 
import matplotlib as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()

chart_def = """
{
    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },
    title: {
        floating: true,
        align: 'left',
        text: 'Winter Olympic Medal Wins'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Course Launched'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Python Popular!'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Course Review Analysis", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="The following graphs:")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_average_crs.index)
    hc_data = [{"name":v1,"data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    hc.options.series = hc_data
    hc.options.legend.floating = False
        
    return wp

jp.justpy(app)