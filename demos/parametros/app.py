import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals()) 
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Parametros:
    def GET(self):
        titulo = "Título desde Python"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit curae blandit praesent id arcu fames turpis, nunc lectus sodales vulputate senectus torquent per curabitur fringilla commodo pharetra tristique dictumst. Blandit libero suscipit dignissim tellus mattis pellentesque luctus gravida, interdum facilisis est eros fringilla dis dapibus cubilia, semper odio eu erat platea orci lectus. Purus vel suscipit imperdiet neque blandit sem eleifend nullam class, penatibus vitae arcu tincidunt laoreet platea facilisi porta, hendrerit turpis pellentesque egestas nibh tellus senectus nam. Dictum arcu platea at justo accumsan scelerisque mi ad ultricies, et sociis egestas lobortis elementum augue ante blandit, nec viverra magna nunc sapien habitant leo varius. Porta tempus tristique ultricies nec imperdiet et aliquet interdum, montes lectus pellentesque himenaeos eu tortor convallis magna, habitasse accumsan class massa justo posuere pharetra. Dictum commodo tempor pulvinar ac aliquet ultricies varius lectus feugiat class, risus vivamus malesuada sapien nam sollicitudin inceptos ridiculus nostra, hendrerit hac convallis magnis eros ornare lobortis fusce aptent."""
        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()
