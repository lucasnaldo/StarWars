import json
import requests 
import unicodedata

from .utils import cores_olhos, sexo, to_date_swagger

class Process:
    
    def personagem(nome):
        nome = nome.replace(" ", "-")
        base_url = 'https://swapi.co/api/people/'
        search = '?search='
        URL = ((base_url + search) + nome)
        resposta = requests.get(URL)
        personagem = resposta.text
        json_retorno = json.loads(personagem)
        retorno = json_retorno['results'][0]
        output = {}
        if 'name' in retorno and retorno['name']:
            output['nome'] = retorno['name']
        if 'height' in retorno and retorno['height']:
            output['altura'] = retorno['height'] + 'cm'
        if 'mass' in retorno and retorno['mass']:
            output['peso'] = retorno['mass'] + 'Kg'
        if 'hair_color' in retorno and retorno['hair_color']:
            output['cor_do_cabelo'] = retorno['hair_color']
        if 'skin_color' in retorno and retorno['skin_color']:
            output['cor_da_pele'] = retorno['skin_color']
        if 'eye_color' in retorno and retorno['eye_color']:
            olhos = retorno['eye_color']
            olhos = cores_olhos(olhos)
            output['cor_do_olho'] = olhos
        if 'birth_year' in retorno and retorno['birth_year']:
            output['data_de_nascimento'] = retorno['birth_year']
        if 'gender' in retorno and retorno['gender']:
            sex = retorno['gender']
            sex = sexo(sex)
            output['sexo'] = sex

        if 'films' in retorno and retorno['films']:
            filminhos = []
            for obj in retorno['films']:
                _film_obj = {}
                film_search = obj + search
                resposta_filme = requests.get(film_search)
                filme = resposta_filme.text
                json_filme = json.loads(filme)
                _film_obj['Episodio'] = json_filme['episode_id']
                _film_obj['Filme'] = json_filme['title']
                datadata = json_filme['release_date']
                datadata = to_date_swagger(datadata)
                _film_obj['Data de lançamento'] = datadata
                _film_obj['Diretor'] = json_filme['director']
                filminhos.append(_film_obj)
            filminhos_ordenados = sorted(filminhos, key=lambda i: i['Episodio'])
            output['Filmes'] = filminhos_ordenados

        if 'species' in retorno and retorno['species']:
            especies = []
            for obj in retorno['species']:
                _spec_obj = {}
                resposta_espec = requests.get(obj)
                espec = resposta_espec.text
                json_espec = json.loads(espec)
                _spec_obj['Nome'] = json_espec['name']
                _spec_obj['Lingua'] = json_espec['language']
                especies.append(_spec_obj)
            output['Especie'] = especies

        if 'vehicles' in retorno and retorno['vehicles']:
            veiculos = []
            for obj in retorno['vehicles']:
                _veic_obj = {}
                resposta_veic = requests.get(obj)
                veic = resposta_veic.text
                json_veic = json.loads(veic)
                _veic_obj['Nome'] = json_veic['name']
                _veic_obj['Modelo'] = json_veic['model']
                veiculos.append(_veic_obj)
            output['Veiculos'] = veiculos
        
        if 'starships' in retorno and retorno['starships']:
            naves = []
            for obj in retorno['starships']:
                _nave_obj = {}
                resposta_nave = requests.get(obj)
                nave = resposta_nave.text
                json_nave = json.loads(nave)
                _nave_obj['Nome'] = json_nave['name']
                _nave_obj['Modelo'] = json_nave['model']
                naves.append(_nave_obj)
            output['Naves'] = naves

        return output
