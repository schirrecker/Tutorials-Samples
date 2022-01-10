import wikipedia

#print(wikipedia.summary("google"))

#complete_content = wikipedia.page("facebook")
#print(complete_content.content)

#print(wikipedia.search("Curie"))

# wikipedia.summary("Mercury")


ny = wikipedia.page("Quanzhou")
print(ny.title)
print(ny.url)
print(ny.sections)
print(ny.content)
print(ny.images[0])
print(ny.links[0])


#print(wikipedia.suggest("New York"))
