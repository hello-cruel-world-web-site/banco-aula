CREATE TABLE Pessoa(
	idpessoa int primary key,
    contato varchar(40),
    nome varchar(30),
    dataUltSolic date,
    matric integer,
    dtnascimento date
);

CREATE TABLE racas(
	idRacas int primary key,
    racas varchar(30)

);

CREATE TABLE especies(
	idEspecie int primary key,
    especie varchar(30)

);

CREATE TABLE animais(
	idAnimal int primary key,
    nome varchar(40),
    dataNascimento date,
    DtUltTrat date,
    idRaca int,
    idEspecie int,
    FOREIGN KEY(idRaca) REFERENCES racas(idRacas),
    FOREIGN KEY(idEspecie) REFERENCES especies(idEspecie)
);

CREATE TABLE servico(
	idServico int,
    valor decimal(10,2),
    descricao varchar(30),
    PRIMARY KEY(idServico)
    );

    
CREATE TABLE remediosProdutos(
	idRemedioProd int,
    tipo int,
    nome varchar(40),
    preco decimal(10,2),
    dtValidade date,
    qtdEstoque int,
    dtUltCompra date,
    dtUltVenda date,
    PRIMARY KEY(idRemedioProd)

);

CREATE TABLE veterinarios(
	idPessoa int,
    CRV int,
    dtAdmissao date,
    FOREIGN KEY(idPessoa) REFERENCES Pessoa(idPessoa)

);

CREATE TABLE consulta(
	idAnimal int,
    idPessoa int,
    idConsulta int,
    hora time,
    data date,
    obs text(300),
    PRIMARY KEY(idConsulta),
    FOREIGN KEY(idAnimal) REFERENCES animais(idAnimal),
    FOREIGN KEY(idPessoa) REFERENCES Pessoa(idPessoa)
    
);

CREATE TABLE tratamento(
	idConsulta int,
    idRemedioProd int,
    FOREIGN KEY(idConsulta) REFERENCES consulta(idConsulta),
    FOREIGN KEY(idRemedioProd) REFERENCES remediosprodutos(idRemedioProd)
);

CREATE TABLE solicita(
	dataSolicitacao date,
    hora time,
    valor decimal(10,2),
    idAnimal int,
    idServico int,
    idPessoa int,
    matric int,
    PRIMARY KEY(dataSolicitacao),
	FOREIGN KEY(matric) REFERENCES pessoa(idPessoa),
    FOREIGN KEY(idPessoa) REFERENCES pessoa(idPessoa),
	FOREIGN KEY(idAnimal) REFERENCES animais(idAnimal),
	FOREIGN KEY(idServico) REFERENCES servico(idServico)
    
);

CREATE TABLE possui(
	idAnimal int,
    idPessoa int,
    FOREIGN KEY(idAnimal) REFERENCES animais(idAnimal),
    FOREIGN KEY(idPessoa) REFERENCES pessoa(idPessoa)

);
CREATE TABLE fornecedor(
	idFornecedor int,
    razaoSocial varchar(40),
    PRIMARY KEY(idFornecedor)

);

CREATE TABLE NF(
	numNf int,
    data date,
    tipo int,
    atualizada int,
    idFornecedor int,
    idProp int,
    PRIMARY KEY(numNf),
    FOREIGN KEY(idFornecedor) REFERENCES fornecedor(idFornecedor),
    FOREIGN KEY(idProp) REFERENCES remediosProdutos(idRemedioProd)
    
);

CREATE TABLE itens(
	valor decimal(10,2),
    idItem int,
    qtd int,
    idRemedioProd int,
    numNf int,
    PRIMARY KEY(idItem),
    FOREIGN KEY(idRemedioProd) REFERENCES remediosProdutos(idRemedioProd),
    FOREIGN KEY(numNf) REFERENCES NF(numNf)

);

CREATE TABLE movFinanceira(
	idFinanceiro int,
    dataVenc date,
    valorPrev decimal(10,2),
    dataPagto date,
    valorPagto decimal(10,2),
    tipo int,
    numNf int,
    PRIMARY KEY(idFinanceiro),
    FOREIGN KEY(numNf) REFERENCES NF(numNf)
    
);

CREATE TABLE auditFinanceiro(
	idAuditFinanceiro int auto_increment,
    operacao char,
    usuario int,
    dtAudit timestamp,
    idFinanceira int,
    dataVenc date,
    valorPrev decimal(10,2),
    dataPagto date,
    valorPagto decimal(10,2),
    tipo int,
    numNf int,
    PRIMARY KEY(idAuditFinanceiro),
    FOREIGN KEY(idFinanceira) REFERENCES movFinanceira(idFinanceiro)
    
);

CREATE TABLE logSolicita(
	seq int auto_increment,
    dtLog timestamp,
    usuario varchar(50),
    operacao char,
    dataSolicitacao date,
    hora time,
    valor decimal(10,2),
    idAnimal int,
    idPessoa int,
    idServico int,
    matric int,
    PRIMARY KEY(seq)

);

CREATE TABLE logConsulta(
	seq int auto_increment,
    dtLog timestamp,
    usuario varchar(50),
    operacao char,
    data date,
    hora time,
    idConsulta int,
    PRIMARY KEY(seq),
    FOREIGN KEY(idConsulta) REFERENCES consulta(idConsulta)


);