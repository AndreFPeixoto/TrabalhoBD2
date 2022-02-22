-- USERS
-- Remove os utilizadores não ativos que nunca fizeram login na aplicação:
db.users.remove({$and: [{'last_login': null}, {'is_active': false}]});

-- Remove o utilizador 6:
db.users.deleteOne({"id":6});

-- GROUPS
-- Remove o grupo com nome “Filmes”:
db.groups.deleteOne({"name" : "Filmes"});

-- NOTICES
-- Remove as notícias do grupo 8:
db.notices.remove({"group_id": 8});

-- Remove a primeira publicação do utilizador 1:
db.notices.deleteOne({"user_id": 1});