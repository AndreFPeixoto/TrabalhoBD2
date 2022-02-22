-- USERS
-- Listar todos os dados dos utilizadores:
function functionEncontraUsers() { return db.VistaUtilizadores.find(); }
functionEncontraUsers()

-- Filtrar dados dos utilizadores:
function findFiltrarUsers(atributo, valor) {
	var filtro = {};
	filtro[atributo] = valor;
	return db.users.find(filtro, {'id': 1, 'name': 1, 'is_admin': 1, 'last_login': 1, '_id': 0}); 
}
findFiltrarUsers("is_admin", false)
findFiltrarUsers("last_login", null)
findFiltrarUsers("name", /Aron/)

-- Contar quantos utilizadores subscreveram um grupo:
function countTotalSubs(group_id) {
	var filtro = {};
	filtro['subs'] = group_id;
	return db.users.find(filtro).count();
}
countTotalSubs(1)

-- Subscrever um grupo:
function subscribeGroup(user, group) {
	db.users.updateOne({'id': user}, {$push: {subs: group}});
}
subscribeGroup(5, 2)

-- Cancelar subscrição de um grupo:
function unsubscribeGroup(user, group) {
	db.users.updateOne({'id': user}, {$pull: {subs: group}});
}
unsubscribeGroup(5, 2)

-- GROUPS
-- Listar todos os dados dos grupos:
function functionFindGroups() { return db.VistaGrupos.find(); }
functionFindGroups();

-- Filtrar dados dos grupos:
function findFiltrarGroups(atributo,valor) {
	var filtro = {};
	filtro[atributo] = valor;
	return db.groups.find(filtro).sort({'name': 1}); 
}
findFiltrarGroups("description", /Aliquam sit/)
findFiltrarGroups("created_at", ISODate("2021-06-05T12:47:07Z"))

-- Atualizar um grupo:
function updateGroup(group_id, name, description) {
	db.groups.updateOne({"id": group_id},{$set:{"name": name, "description": description}});
}
updateGroup(7, "Literatura", "Novo grupo de literatura")

-- NOTICES
-- Listar noticias de um utilizador:
function listNoticiasUser(user_id) {
	var filtro = {};
	filtro['user_id'] = user_id;
	return db.notices.find(filtro);
}
listNoticiasUser(1)

-- Remover uma notícia:
function deleteNotice(id) {
	db.notices.deleteOne({"id": id});
}
deleteNotice(19)

-- Atualizar um campo de uma notícia:
function updateNotice(id, atributo, valor) {
	var filtro = {};
	filtro[atributo] = valor;
	db.notices.updateOne({"id": id},{$set: filtro});
}
updateNotice(11, 'title', 'Novo titulo')
updateNotice(11, 'description', 'Nova Descrição')