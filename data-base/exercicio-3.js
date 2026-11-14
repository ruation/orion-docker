db.createCollection("posts")

db.posts.insertOne({
 titulo: "Orion Bootcamp",
 autor: "Yago",
 conteudo: "New Rizon"
})

db.posts.insertOne({
 titulo: "Orion Bootcamp 2",
 autor: "Cinthia",
 conteudo: "New Rizon 2",
 tags: ["nosql", "flexivel"]
})

db.posts.find()