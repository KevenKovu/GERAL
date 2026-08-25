drop database if exists DBOO; # Não rodar em Produção.
create database DBOO;
use DBOO;

create table Cliente (
	codigo int not null,
    nome varchar(30) not null,
    dataNasc date not null,
    constraint pk_Cliente primary key (codigo)
);

create table PessoaFisica (
	CPF varchar(14) not null,
    codigo int not null,
    constraint pk_PF primary key (CPF, codigo),
    constraint fk_CliPF foreign key (codigo) references Cliente(codigo) on delete cascade
);

create table PessoaJuridica (
	CNPJ varchar(18) not null,
    codigo int not null,
    sociedade varchar(20) null,
    constraint pk_CNPJ primary key (CNPJ, codigo),
    constraint fk_CliPJ foreign key (codigo) references Cliente(codigo) on delete cascade
);

insert into Cliente values (10, 'Moisés Pereira', str_to_date('13/05/1982', '%d/%m/%Y'));
insert into Cliente values (11, 'Luanda Lima', str_to_date('11/09/1982', '%d/%m/%Y'));
insert into Cliente values (20, 'Maria Luiza', str_to_date('01/01/2020', '%d/%m/%Y'));
insert into Cliente values (21, 'Heberton Correa', str_to_date('07/08/1981', '%d/%m/%Y'));
insert into Cliente values (22, 'David Franco', str_to_date('30/03/1990', '%d/%m/%Y'));
insert into Cliente values (37, 'Juliana Ventura', str_to_date('13/05/1982', '%d/%m/%Y'));

insert into PessoaFisica values ('013.999.888-33', 10);
insert into PessoaFisica values ('058.111.111-03', 11);
insert into PessoaJuridica values ('13.970.629/0001-06', 20, 'Limitada');
insert into PessoaJuridica values ('25.986.183/0001-97', 21, 'Anônima');
insert into PessoaFisica values ('370.037.703-07', 22);
insert into PessoaFisica values ('222.222.222-22', 37);

select  c.codigo as 'Codigo',
 c.nome'Nome',
 f.CPF'CPF/CNPJ', null as 'Tipo Sociedade (se PJ)'
from Cliente c, PessoaFisica f
where c.codigo = f.codigo
union
select	c.codigo, c.nome, J.CNPJ, j.sociedade
from	Cliente c, PessoaJuridica j
where c.codigo = j.codigo;

select *
from	Cliente c, PessoaJuridica j
where	c.codigo = j.codigo and
		c.dataNasc >= '2019-01-01';

select * from Cliente c;