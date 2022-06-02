import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    compress=True
)

server = app.server

app.title = 'feffery-leaflet-components在线文档'
