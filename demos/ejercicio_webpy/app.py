import web
import os

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout'
)

app = web.application(urls, globals())

if not os.path.exists('sessions'):
    os.makedirs('sessions')
session_store = web.session.DiskStore('sessions')

session = web.session.Session(app, session_store, initializer={'usuario': None, 'conectado': False})

render = web.template.render('views')

class Index:
    def GET(self):
        if session.conectado == False:
            raise web.seeother('/login')
        
        return render.index(session.usuario)

class Login:
    def GET(self):
        return render.login("")

    def POST(self):
        datos = web.input()
        usuario_ingresado = datos.username
        contrasena_ingresada = datos.password

        if usuario_ingresado == "admin" and contrasena_ingresada == "1234":
            session.usuario = usuario_ingresado
            session.conectado = True
            raise web.seeother('/')
        else:
            return render.login("Usuario o contraseña incorrectos. Intenta de nuevo.")

class Logout:
    def GET(self):
        session.kill()
        return render.logout()

if __name__ == "__main__":
    app.run()