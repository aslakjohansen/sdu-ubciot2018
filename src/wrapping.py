from rdflib import Graph, Namespace, URIRef, Literal
import rdflib
import json
import requests

RDF        = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS       = Namespace('http://www.w3.org/2000/01/rdf-schema#')
OWL        = Namespace('http://www.w3.org/2002/07/owl#')
BRICK      = Namespace('http://buildsys.org/ontologies/Brick#')
BRICKFRAME = Namespace('http://buildsys.org/ontologies/BrickFrame#')
BRICKTAG   = Namespace('http://buildsys.org/ontologies/BrickTag#')

N = Namespace('http://cfei.mmmi.sdk.dk/junk/example#')

def model ():
    g = Graph()
    
    brickpath = lambda filename: '../var/'+filename
    g.parse(brickpath('../var/Brick.ttl'), format='turtle')
    g.parse(brickpath('../var/BrickFrame.ttl'), format='turtle')
    g.parse(brickpath('../var/BrickTag.ttl'), format='turtle')
    
    g.bind('rdf'  , RDF)
    g.bind('rdfs' , RDFS)
    g.bind('owl'  , OWL)
    g.bind('brick', BRICK)
    g.bind('bf'   , BRICKFRAME)
    g.bind('btag' , BRICKTAG)
    g.bind('n'    , N)
    
    return g

def query (g, q):
    r = g.query(q)
    return list(map(lambda row: list(row), r))

def pprint (structure):
    pretty = json.dumps(structure, sort_keys=True, indent=4, separators=(',', ': '))
    print(pretty)

