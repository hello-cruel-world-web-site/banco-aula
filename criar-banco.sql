create database petshop;
use petshop;


create table pessoa(
    id serial primary key, 
    nome varchar(100) not null, 
    contato varchar(40) null,
    dataUltimaSolicitacao date null,
    matricula integer not null,
    dataNascimento date not null
);



