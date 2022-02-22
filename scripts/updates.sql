-- USERS
-- Atualiza o campo “is_active” dos utilizadores cujo email termina em “.com”:
db.users.updateMany({"email":/.com$/},{$set:{"is_active":true}});

-- Atualiza o campo “is_admin” do utilizador com id 6:
db.users.updateOne({"id":6},{$set:{"is_admin":true}});

-- GROUPS
-- Atualiza o campo “created_at” do grupo “Desporto”:
db.groups.updateOne({"name":"Desporto"},{$set:{"created_at":ISODate("2004-10-19T06:36:15.000Z")}});

-- Atualiza o campo “description” do grupo 2:
db.groups.updateOne({"id":2},{$set:{"description":"Descrição do grupo"}});

-- NOTICES
-- Atualiza o campo “is_public” das publicações do utilizador 4:
db.notices.updateMany({"user_id":4},{$set:{"is_public":false}});

-- Atualiza o campo “last_modified” das publicações do grupo 5 ou do utilizador 16:
db.notices.updateMany({$or: [{"group_id": 5}, {"user_id": 16}]}, {$set:{"last_modified":ISODate("2001-04-19T06:36:15.000Z")}});

-- Atualiza o campo “image_url” das notícias publicas que não possuem imagem:
db.notices.updateMany({$and: [{'image_url': null}, {'is_public': true}]}, {$set: {'image_url': 'https://voh-ny.com/wp-content/uploads/2020/01/201412547de803cbef5-1.jpg'}});