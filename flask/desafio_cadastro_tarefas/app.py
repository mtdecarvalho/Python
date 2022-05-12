from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Matheus',
        'tarefa': 'Lavar a louça',
        'status': 'pendente'
    },
    {
        'id': 1,
        'responsavel': 'Juliana',
        'tarefa': 'Fazer a janta',
        'status': 'concluido'
    }
]


@app.route('/tarefas/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError as e:
            mensagem = f'A tarefa de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception as e:
            print(e.message)
            mensagem = 'Erro desconhecido, entre em contato com o admnisitrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        try:
            response = json.loads(request.data)
            tarefas[id]['status'] = response['status']
        except IndexError as e:
            mensagem = f'A tarefa de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception as e:
            mensagem = 'Erro desconhecido, entre em contato com o admnisitrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify({'status': 'sucesso', 'mensagem': 'Status alterado para {}'.format(response['status'])})

    elif request.method == 'DELETE':
        try:
            tarefas.pop(id)
            mensagem = f'Tarefa de ID {id} excluída com sucesso!'
            response = {'status': 'sucesso', 'mensagem': mensagem}
        except IndexError as e:
            mensagem = f'Tarefa de ID {id} não existe!'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception as e:
            mensagem = 'Erro desconhecido, entre em contato com o admnisitrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)


@app.route('/tarefas/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(dados)

    elif request.method == 'GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)
