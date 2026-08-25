create database mercenaria;
use mercenaria;

create table Cliente(
	Cpf varchar(14) not null primary key,
    nome varchar(30) not null,
    endereco text not null,
    
    constraint pk_Cliente primary key (Cpf)
);

create table Produto(
	codigo int not null,
    marca varchar(10) not null,
    estoque int not null,
    preco double not null,
    
    constraint pk_Produto primary key (codigo)
);

create table Compra(
	CpfCliente varchar(14) not null,
    codigoProduto int not null,
    quantidade int not null,
    
    constraint pk_Compra primary key(CpfCliente, codigoProduto, quantidade),
    constraint fk_Cliente foreign key(CpfCliente)
		references Cliente(Cpf) on delete restrict,
	constraint fk_Produto foreign key
);

create view NotaFiscal as
	select c.Cpf, c.nome, sum(co.quantidade * p.preco)
    from	Cliente c, Compra co, Produto p
    where	c.Cpf = co.CpfCliente and
			co.codigoProduto = p.codigo
	group by c.Cpf, c.nome;
    
delimiter $$
create trigger AtualizaEstoque after insert on Compra for each row
begin
	if(new.quantidade > 0) then
		update Produto set estoque = estoque - new.quantidade
        where codigo = new.CodigoProduto;
	end if;
end $$
delimiter ;