-- USERS
-- Listar todos os utilizadores:
db.createView("VistaUtilizadores","users",[]);
db.VistaUtilizadores.find()

-- Listar todos os utilizadores ordenados pelo campo “last_login”:
db.runCommand({create:"VistaOrdenarLastLogin", viewOn:"users", pipeline:[{$sort: {"last_login":1}}]})
db.VistaOrdenarLastLogin.find()

-- Listar campos específicos pela data de criação da conta:
db.runCommand({create:"VistaOrdenarUsers", viewOn:"users", pipeline:[{$sort: {"created_at":1}}, {$project:{"name":1,"last_login":1,"created_at":1}}]})
db.VistaOrdenarUsers.find()

-- Alterar vista para ordem decrescente:
db.runCommand({collMod:"VistaOrdenarUsers", viewOn:"users", pipeline:[{$sort: {"created_at":-1}}, {$project:{"name":1,"last_login":1,"created_at":1}}]})
db.VistaOrdenarUsers.find()

-- GROUPS
-- Listar todos os grupos:
db.createView("VistaGrupos","groups",[]);
db.VistaGrupos.find()

-- Listar os grupos criados após 2021-12-01:
db.createView("VistaGruposPorData", "groups", [{$match: {"created_at": {$gt: ISODate("2021-12-01")}}}]);
db.ViewGrupsdata.find();

-- Listar os últimos 3 grupos criados:
db.createView("VistaNovosGrupos","groups",[{$sort:{"created_at":1}},{$limit:3}]);
db.NovosGruops.find();

-- Apagar uma vista:
db.VistaNovosGrupos.drop();

-- NOTICES
-- Listar 10 noticias ordenadas por id:
db.runCommand({create:"VistaListar10Notices", viewOn:"notices", pipeline:[{$limit:10}, {$sort:{"id_user":1}}]});
db.VistaListar10Notices.find();

-- Listar todas as notícias do grupo 4:
db.createView("VistaNoticesPorGrupo", "notices", [{$match:{"group_id":4}}]);
db.VistaNoticesPorGrupo.find();

-- Listar campos específicos das notícias do utilizador 5:
db.createView("VistaNoticesPorID", "notices",[{$match:{"user_id":5}}, {$project:{"title":1,"content":1}}]);
db.VistaNoticesPorID.find();

-- Alterar noticia:
db.createView("VistaAlterarNoticia", "notices",[{$match:{"id":5}}, {$set: {"title": "Titulo", "description": "Descrição"}}]);
db.VistaAlterarNoticia.find();