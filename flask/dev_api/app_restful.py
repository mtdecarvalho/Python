from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Lista_Habilidades, Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Theus',
        'habilidades': ['Python', 'Django', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Matheus',
        'habilidades': ['Python', 'Django', 'Flask']
    }
]


# devolve um desenvolvedor pelo id, tambem altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError as e:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception as e:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}


# lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class Lista_Desenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')
api.add_resource(Lista_Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
