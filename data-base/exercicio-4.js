db.posts.updateOne(
  { autor: "Yago" },
  {
    $set: {
      comentarios: [
        { usuario: "Cinthia", texto: "o Bootcamp é incrível!" },
        { usuario: "Ruan", texto: "o Orion Bootcamp é inspirador!" }
      ]
    }
  }
)

db.posts.find({ tags : "nosql" })

db.posts.find({ autor : "Yago" })