import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Course Review Analysis", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="The following graphs:")
    
    return wp


jp.justpy(app)