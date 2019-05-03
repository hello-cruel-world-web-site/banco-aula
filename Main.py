from gerar_pessoa import gerar_nome, gerar_data, gerar_matricula, gerar_telefone

if __name__ == '__main__':
    arquivo = open('inserir-pessoa.sql', 'w')
    for i in range(0, 2000):
        sql = f"""
insert into pessoa(nome, contato, dataUltimaSolicitacao, matricula, dataNascimento)
    values ('{gerar_nome()}','{gerar_telefone()}', null, {gerar_matricula()}, '{gerar_data()}');
    """
        
        arquivo.write(sql)
    
