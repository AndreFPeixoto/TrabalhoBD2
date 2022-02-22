-- USERS
-- Listar todos os utilizadores:
db.users.find();

-- Listar todos os administradores:
db.users.find({'is_admin': true});

-- Listar todos os utilizadores ordenados pela data de criação:
db.users.find().sort({'created_at': -1});

-- Listar os 3 primeiros utilizadores ordenados por ordem alfabética:
db.users.find().sort({'name': 1}).limit(3);

-- Listar os utilizadores ativos que subscreveram o grupo 2, ordenados pela data de criação:
db.users.find({$and: [{'subs': 2}, {'is_active': true}]}, {'name': 1, 'created_at': 1, 'is_active': 1, 'subs': 1, '_id': 0}).sort({'created_at': -1})

-- Listar todos os utilizadores com o nome “Krista Hawtin” e atualizar o nome para “Cristina Martins”:
db.users.findAndModify({query: {'name': 'Krista Hawtin'}, sort:{'id': 1}, update: {$set: {'name': 'Cristina Martins'}}});

-- Listar todos os administradores que não estão ativos e remover o status de administrador:
db.users.findAndModify({query: {$and: [{'is_admin': true}, {'is_active': {$ne: true}}]}, update: {$set: {'is_admin': false}}});

-- Listar todos os utilizadores com 3 ou mais subscrições:
db.users.find({$where: 'this.subs.length>=3'}, {'name': 1, 'subs': 1, '_id': 0});

-- Lista todos os utilizadores que efetuaram o seu registo no ano 2022:
db.users.find({'created_at': {$gte: ISODate("2022-01-01"), $lte: ISODate("2022-12-31")}});

-- Listar utilizadores que usaram a aplicação por 6 meses ou mais, isto é, a diferença entre a data de registo e o último login deverá ser maior ou igual a 6 meses:
db.users.aggregate([
	{$addFields: {months: {$dateDiff: {startDate: "$created_at", endDate: "$last_login", unit: "month"}}}},
	{$match: {"months": {$gte: 6}}},
	{$project: {last_login: "$last_login", created_at: "$created_at", months: "$months"}},
	{$sort: {"months": -1}}
]);

-- Listar utilizadores ativos que não efetuam login na aplicação a mais de 100 dias:
db.users.aggregate([
	{$addFields: {days: {$dateDiff: {startDate: "$last_login", endDate: "$$NOW", unit: "day"}}}},
	{$match: {$and: [{"days": {$gt: 100}}, {"is_active": true}]}},
	{$project: {last_login: "$last_login", is_active: "$is_active", days: "$days"}},
	{$sort: {"days": 1}}
]);

-- GROUPS
-- Lista todos os grupos:
db.groups.find();

-- Lista todos os grupos com “os” no nome:
db.groups.find({"name": /os/});

-- Conta quantos grupos começam com a letra “F” no nome:
db.groups.find({"name": /^F/}).count();

-- Lista todos os grupos ordenados pelo número de caracteres da sua respetiva descrição:
db.groups.aggregate([
	{$project: {"name": 1, "description": 1, "desc_length": {$strLenCP: "$description"}}},
	{$sort: {"desc_length": 1}}
]);

-- NOTICES
-- Listar todas as notícias:
db.notices.find();

-- Listar as notícias que não são publicas ordenadas pela data:
db.notices.find({"is_public": {$ne: true}}, {'title': 1, 'is_public': 1, '_id': 0}).sort({'last_modified': -1});

-- Contar o número de notícias do utilizador 15 ou dos grupos 4, 5, ou 8:
db.notices.find({$or: [{'user_id': 15}, {'group_id': {$in: [4, 5, 8]}}]}).count();

-- Listar as notícias que não possuem imagem nem descrição:
db.notices.find({$and: [{'image_url': null}, {'description': null}]}, {'id': 1, 'title': 1, 'image_url': 1, 'description': 1, '_id': 0});

-- Listar as notícias publicadas para os utilizadores:
db.notices.find({'group_id': null}).sort({'title': 1});

-- Mostrar os dados do utilizador em conjunto com a notícia 15:
db.notices.aggregate([
	{$match: {'id': 15}},
	{$lookup: {
		from: 'users',
		localField: 'user_id',
		foreignField: 'id',
		pipeline: [{$project: {name: 1, _id: 0, email: 1}}],
		as: 'Utilizador'
	}},
	{$project: {'id': 1, 'title': 1, 'user_id': 1, 'Utilizador': 1, _id:0}}
]);

-- Mostrar os dados do grupo em conjunto com a notícia 7:
db.notices.aggregate([
	{$match: {'id': 7}},
	{$lookup: {
		from: 'groups',
		localField: 'group_id',
		foreignField: 'id',
		pipeline: [{$project: {name: 1, _id: 0, created_at: 1}}],
		as: 'Grupo'
	}},
	{$project: {'id': 1, 'title': 1, 'group_id': 1, 'Grupo': 1, _id:0}}
]);