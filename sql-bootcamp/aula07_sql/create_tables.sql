CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS clients (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	limite INTEGER NOT NULL,
	saldo INTEGER NOT NULL,
	CHECK (saldo >= -limite),
	CHECK (limite > 0)
);

CREATE TABLE IF NOT EXISTS transactions (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	tipo CHAR(1) NOT NULL,
	descricao VARCHAR(10) NOT NULL,
	valor INTEGER NOT NULL,
	client_id UUID NOT NULL,
	realizada_em TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO clients (limite, saldo)
VALUES
	(10000, 0),
	(80000, 0),
	(1000000, 0),
	(10000000, 0),
	(500000, 0);