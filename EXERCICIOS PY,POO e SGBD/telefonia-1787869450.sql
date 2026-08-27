-- Dimensão de clientes da operadora.
CREATE TABLE IF NOT EXISTS `cliente` (
	`id_cliente` int NOT NULL COMMENT 'Primary Key',
	`nome` varchar(255) NOT NULL,
	`endereco` varchar(255) NOT NULL,
	`cidade` varchar(255) NOT NULL,
	PRIMARY KEY (`id_cliente`)
) COMMENT='Dimensão de clientes da operadora.';
-- Dimensão de planos tarifários.
CREATE TABLE IF NOT EXISTS `plano` (
	`id_plano` int NOT NULL COMMENT 'Primary Key',
	`nome_plano` varchar(255) NOT NULL,
	`descricao_plano` varchar(255) NOT NULL,
	PRIMARY KEY (`id_plano`)
) COMMENT='Dimensão de planos tarifários.';
-- Dimensão de datas (calendário).
CREATE TABLE IF NOT EXISTS `tempo` (
	`id_tempo` int NOT NULL COMMENT 'Primary Key',
	`dia` int NOT NULL,
	`mes` int NOT NULL,
	`ano` int NOT NULL,
	PRIMARY KEY (`id_tempo`)
) COMMENT='Dimensão de datas (calendário).';
-- Tabela fato de consumo telefônico (chave composta por cliente, plano e tempo).
CREATE TABLE IF NOT EXISTS `fato_consumo` (
	`id_cliente` int NOT NULL COMMENT 'FK -> Cliente.id_cliente',
	`id_plano` int NOT NULL COMMENT 'FK -> Plano.id_plano',
	`id_tempo` int NOT NULL COMMENT 'FK -> Tempo.id_tempo',
	`valor_conta` decimal(10,2) COMMENT 'Métrica: valor da conta',
	`qtd_minutos` int COMMENT 'Métrica: quantidade de minutos',
	`media_msg` int COMMENT 'Métrica: média de mensagens',
	`minutos_roaming` int COMMENT 'Métrica: minutos em roaming',
	PRIMARY KEY (`id_cliente`, `id_plano`, `id_tempo`)
) COMMENT='Tabela fato de consumo telefônico (chave composta por cliente, plano e tempo).';
ALTER TABLE `fato_consumo` ADD CONSTRAINT `fato_consumo_fk0` FOREIGN KEY (`id_cliente`) REFERENCES `cliente`(`id_cliente`);
ALTER TABLE `fato_consumo` ADD CONSTRAINT `fato_consumo_fk1` FOREIGN KEY (`id_plano`) REFERENCES `plano`(`id_plano`);
ALTER TABLE `fato_consumo` ADD CONSTRAINT `fato_consumo_fk2` FOREIGN KEY (`id_tempo`) REFERENCES `tempo`(`id_tempo`);