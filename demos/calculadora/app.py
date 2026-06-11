import web 

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)
app = web.application(urls, globals()) 
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Calculadora:
    def GET(self):
        numero_1 = 0.0
        numero_2 = 0.0
        resultado = 0.0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero_1 = float(formulario['prinum'])
        numero_2 = float(formulario['segnum'])
        operacion = formulario.get('operacion')
        match operacion:
            case "suma": resultado = numero_1 + numero_2 
            case "resta": resultado = numero_1 - numero_2
            case "multiplica": resultado = numero_1 * numero_2
            case "divide": resultado = numero_1 / numero_2
            case "modulo": resultado = numero_1 % numero_2
            case "potencia": resultado = numero_1 ** numero_2
            case "raiz": resultado = numero_1 ** 0.5

        return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
