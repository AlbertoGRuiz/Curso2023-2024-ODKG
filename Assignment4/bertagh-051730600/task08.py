# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YraQ9cYYnFkUFouoTxfdOkVSuGry30vH

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

ns = Namespace("http://data.org#")

from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS

#With this query we find out which of the required properties are missing for each individual.

q1 = prepareQuery('''
   SELECT ?Subject ?Property WHERE {
    ?Subject ?Property ?value.
    ?Subject RDF:type ns:Person.
    }
  ''',
  initNs = {"RDF": RDF,
            "ns":ns}
)
#Visualize the results

for r in g1.query(q1):
  print(r.Subject, r.Property)

#By listing everything in g2 we're able to see the values of the missing data in g1
for s, p, o in g2:
  print(s,p,o)

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

#We add the missing values to g1
g1.add((ns.JohnDoe, VCARD.Given, Literal("John")))
g1.add((ns.SaraJones, VCARD.Given, Literal("Sara")))
g1.add((ns.SaraJones, VCARD.Family, Literal("Jones")))
g1.add((ns.SaraJones, VCARD.EMAIL, Literal("sara.jones@data.org")))
g1.add((ns.JohnSmith, VCARD.Family, Literal("Smith")))
g1.add((ns.HarryPotter, VCARD.EMAIL, Literal("hpotter@hogwarts.org")))

from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS

#We check g1 again to see that now we have every property we needed.

q1 = prepareQuery('''
   SELECT ?Subject ?Property WHERE {
    ?Subject ?Property ?value.
    ?Subject RDF:type ns:Person.
    }
  ''',
  initNs = {"RDF": RDF,
            "ns":ns}
)
#Visualize the results

for r in g1.query(q1):
  print(r.Subject, r.Property)