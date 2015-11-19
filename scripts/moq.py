from frontend.models import Tree
tree = Tree(
    name = "holla",
    latitude = 45.5088400,
    longitude = -73.5878100,
    memory = "A memory"
)
tree.save()